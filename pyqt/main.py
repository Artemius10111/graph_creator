# -*- coding: utf8 -*-
import PyQt5
from PyQt5.QtWidgets import QGraphicsView, QPushButton, QButtonGroup, QMdiSubWindow, QGridLayout, QWidget, QTabWidget, QApplication
from PyQt5 import QtWidgets, QtCore, QtGui
import sys
import os
from PyQt5 import Qt
import json

from pip import main
from design.py.graph5 import Ui_MainWindow # Основное окно
from design.py.hello_window import Ui_mainWindow as HelloMainWindow # Приветственное окно с информацией
import itertools

def suppress_qt_warnings():
    """
    Метод, который убирает предупреждения pyqt.
    Предупреждения связаны с импортированием pyqt6, ни о чем не говорят
    """
    os.environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    os.environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    os.environ["QT_SCALE_FACTOR"] = "1"

suppress_qt_warnings()
app = QtWidgets.QApplication(sys.argv)

class GraphButton(QPushButton):
    """
    Собственный класс кнопки,написанный для расширения ее функционала.
    Аргумент able_to_move определяет способность кнопки менять ее положение с помощью прааой кнопки мыши
    id_name - айдишник, переопределен и добавлен.
    btn_text- обязательный аргумент класса QPusbButton.
    """

    def __init__(self, btn_text, id_name, able_to_move, *args, **kwargs):
        super().__init__(btn_text, able_to_move, *args, **kwargs)
        self.able_to_move = able_to_move
        self.id_name = id_name

    def mousePressEvent(self, event):
        """
        Реакиция на правый щелчок мыщи по кнопке в зависимости от аргумента able_to_move
        """
        if self.able_to_move:
            if event.buttons() == QtCore.Qt.RightButton:
                mimeData = QtCore.QMimeData()
                drag = QtGui.QDrag(self)
                drag.setMimeData(mimeData)
                drag.exec_(QtCore.Qt.MoveAction)
        return Qt.QPushButton.mousePressEvent(self, event)


class Hello_Window(QtWidgets.QMainWindow):
    """
    Приветственное окно. Смотреть файл hello_window.py
    """
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.u_translate = QtCore.QCoreApplication.translate
        self.ui=HelloMainWindow()
        self.ui.setupUi(self)
            

class Main(QtWidgets.QMainWindow):
    """
    Основное окно. Смотреть файл graph(*).py, остальняе файлы нужны для отката к ранним версиям интерфейса.
    """
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.u_translate = QtCore.QCoreApplication.translate
        self.ui=Ui_MainWindow() #Устанавливаем основное окно модуля  graph(*).py как дочернее
        self.ui.setupUi(self)
        self.setWindowTitle('Редактор Графов')
        self.ui.StackedWidget.setCurrentWidget(self.ui.Second_Page)
        self.setAcceptDrops(True)
        self.graph_num = 1      # Атрибут, который отвечает за последнюю цифру в названии элемента графа. 
        self.active_graph = None # Один из самых главных атрибутов класса, который позволяет удалять, уменьшать, увеличивать, создавать соединения
                                # Является как таковой ссылкой на объект кнопки
        self.active_line = None # Немало важный атрибут класса, который отвечает за построения линий, является первой точкой для создания линии. 
                                # Вторым же атрибутом, который относится к этому атрибуту является self.last_active_line, который копирует значения
                                # Этого атрибута, позволяя ему уже быть другим объектом кнопки
        self.DrawTime = False   # Атрибут, который отвечает за рисование линий между вершинами графа, так же немало важен
        self.for_test = False   # Атрибут, который разделяет обычное построение между вершинами графа и построение линий для того случай, 
                                # Пользователь сдался и решил посмореть, как выглядит решение

        self.graph_elements_set = set() # Атрибут, который отсылается на множество, в котором находятся объекты кнопок, позволяет не добавлять дубликаты кнопок


        ### Экран и его максимальные размеры
        screen = app.primaryScreen()
        # self.setFixedHeight(size.height()-50)
        # size = screen.size()
        # self.setFixedHeight(size.height()-50)
        # self.setFixedWidth(size.width()-50)
        # self.showMaximized()
        ##########


        ####################################################################################################
        self.ui.SP_HL_HL_VL1_ChangeColorBtn.clicked.connect(self.change_color_on_click)
        # Выбрать цвет соединения
        ####################################################################################################

        ####################################################################################################
        self.ui.SP_HL_VL_VL_PushButton.clicked.connect(lambda: self.ui.StackedWidget.setCurrentWidget(self.ui.First_Page))
        # Редактор графов
        ####################################################################################################

        ####################################################################################################
        self.ui.SP_HL_VL_VL_PushButton.clicked.connect(self.clear_graph_map)
        # Очистить карту графов
        ####################################################################################################

        ####################################################################################################
        self.ui.FP_VL1_PushButton.clicked.connect(self.clear_graph_map)

        ####################################################################################################

        ####################################################################################################
        self.ui.FP_VL1_PushButton.clicked.connect(lambda: self.ui.StackedWidget.setCurrentWidget(self.ui.Second_Page))
        
        ####################################################################################################

        ####################################################################################################    
        self.ui.pushButton_6.clicked.connect(self.check_result)

        ####################################################################################################

        ####################################################################################################
        self.ui.pushButton_7.clicked.connect(self.gave_up)

        ####################################################################################################

        ####################################################################################################
        self.ui.VP_UploadGraphButton.clicked.connect(self.upload_json_map)
        
        ####################################################################################################

        ####################################################################################################
        self.ui.Info.clicked.connect(self.show_info)

        ####################################################################################################

        ####################################################################################################
        self.ui.FP_VP2_PushButton.clicked.connect(self.add_graph_button)

        ####################################################################################################

        ####################################################################################################
        self.ui.pushButton_3.clicked.connect(self.clear_graph_map)

        ####################################################################################################

        ####################################################################################################
        self.ui.pushButton_4.clicked.connect(self.delete_graph)

        ####################################################################################################

        ####################################################################################################
        self.ui.pushButton_2.clicked.connect(self.make_graph_bigger)

        ####################################################################################################

        ####################################################################################################
        self.ui.pushButton.clicked.connect(self.make_graph_less)

        ####################################################################################################

        ####################################################################################################
        self.ui.pushButton_5.clicked.connect(self.getSaveFileName)

        ####################################################################################################


        # Атрибуты класса, которые используются для методов
        self.last_active_graph = None
        self.last_active_line = None
        self.widget = QWidget()
        self.main = QtWidgets.QMainWindow()
        self.json_dict = dict() # Json словарь, который необходим для методов загрузки json файла, его сохранения
        self.json_list = list() # Json список, который необходим для методов загрузки json файла, его сохранения
        self.line_button_1_x = None # X первой вершины графа для построения линии
        self.line_button_1_y = None # Y первой вершины графа для построения линии
        self.line_button_2_x = None # X второй вершины графа для построения линии
        self.line_button_2_y = None # Y второй вершины графа для построения линии

        self.line_list = []
        self.line_dict = {}
        self.add_colors() # Читаем config/colors.json для добавления цветов
        self.graph_subset  = set()
        self.graph_list = []
        self.graph_list_2 = []
        self.graph_list_3 = []
        self.test_set = set()
        self.for_test = False
        self.json_ = None
        self.DrawTime = False
        self.for_test = None
        self.deleted_list = list() 
        #

        # Устанавливает прозрачность для виджета - зоны, где находятся элементы графа
        op_1=QtWidgets.QGraphicsOpacityEffect(self)
        op_1.setOpacity(0)
        self.ui.widget.setGraphicsEffect(op_1)

        op_2=QtWidgets.QGraphicsOpacityEffect(self)
        op_2.setOpacity(0)
        self.ui.widget_2.setGraphicsEffect(op_2)
        self.num_list = []
        #

    @QtCore.pyqtSlot()
    def setResult(self, state: bool):
            """
            Устанавливает надпись в зависимости от булевого аргумента state
            """
            if state:
                self.ui.label_3.setText('Результат: Пройдено!')
            else:
                self.ui.label_3.setText('Результат: Провалено!')

    @QtCore.pyqtSlot()
    def check_result(self):
        """
        Проверяет результаты построения графа пользователем.При любой ошибке тест проваливается.
        Граф изменить можно, но надпись даже при последующем построении будет такой же,как и при первой проверке.
        Два вида проверок:
        1. По длине правильного списка графа с длиной списка элементов гиафа, соединенных пользователем
        2. Методом пеоебора одной пары в целом списке

        """
        if self.json_:

            def compaire(pair: list, list_: list):
                """
                Проверяет наличие хотя бы одной последовательности переданного аргумента pair в виде списка в аргументе list_
                """
                for pair_2 in list_:
                    if len(set(pair+pair_2)) == len(pair_2):
                        return True
                return False

            self.list_example = []
            True_list = []
            for set_ in self.graph_list:
                self.list_example.append([graph.text() for graph in set_])
            if len(self.list_example) != len(self.graph_list_3):
                self.setResult(state=False)
            else:
                for pair in self.list_example:
                    if compaire(pair=pair, list_=self.graph_list_3):
                        True_list.append(True)
                    else:
                        True_list.append(False)
                if False in True_list:
                    self.setResult(state=False)
                else:
                    self.setResult(state=True)


    @QtCore.pyqtSlot()
    def gave_up(self):
        """
        Строет правильный граф, если пользователь сдается. Попытка построения графа считается провальной
        """
        if self.json_:
            self.clear_graph_map()
            self.setResult(False)
            for key, value in self.json_.items():
                if 'Graph_pair' in key:
                    list_ = []
                    for index in value:
                        graph_x = (list(index.items())[0][1].get('graph_x')) + 20 
                        graph_y = (list(index.items())[0][1].get('graph_y')) + 20
                        list_.append(graph_x)
                        list_.append(graph_y)

                    self.line_list.append(list_)
                    self.DrawTime = True
                    self.for_test = True                    
                        # print(index.items()[1].get('graph_y'))
                    for index in value:
                        graph_pair_list = list()
                        for data in value:
                            name = (list(data.keys())[0])
                            graph_pair_list.append(name)
                        self.graph_list_2.append(graph_pair_list)
                        for pair in self.graph_list_2:
                            while self.graph_list_2.count(pair) != 1:
                                self.graph_list_2.pop(self.graph_list_2.index(pair))
                        self.graph_list_3 = self.graph_list_2
                        for name, data in index.items():
                            id = name
                            graph_text = data.get('graph_text')
                            graph_id_name = data.get('graph_id_name')
                            graph_x = data.get('graph_x')
                            graph_y = data.get('graph_y')
                            graph_width = data.get('graph_width')
                            graph_height = data.get('graph_height')
                            self.add_graph_button(graph_text=graph_text, graph_id_name=graph_id_name)
                            self.ui.widget.button.move(graph_x, graph_y)
                            self.ui.widget.button.setDisabled(True)
                            self.update()


    @QtCore.pyqtSlot()
    def add_colors(self):
        """
        Читает файл пути config/colors.json, добавляет цвета в список
        """
        with open('config/colors.json', 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            colors= (data['colors'])
            for color in colors:
                self.ui.SP_HL_HL_VL1_ListWidget.addItem(list(color.values())[0])

    @QtCore.pyqtSlot()
    def delete_graph(self):
        """
        Удаляет элемент графа, добавляет элемент в список, если удаленный элемент не является последним.
        """
        if not self.active_graph is None:
            try:
                self.graph_elements_set.remove(self.active_graph)
            except KeyError:
                return None
            for key in list(self.line_dict):
                if self.active_graph in key:
                    del self.line_dict[key]
            if list(self.graph_elements_set)[-1] != self.active_graph:
                self.deleted_list.append(self.active_graph.text())
                try:
                    self.num_list.pop(self.num_list.pop(self.num_list.index(int(self.active_graph.text()[-1]))))
                except IndexError:
                    pass
            self.active_graph.deleteLater()
            self.active_graph = None 
            self.graph_num -= 1
            self.active_line = None
            self.last_active_graph = None
            self.last_active_line = None

    def clear_graph_map(self):
        """
        Полностью очищает страницу от графа, сбрасывает все переменные к исходным знв
        """
        for graph in self.graph_elements_set:
            graph.deleteLater()
        self.graph_elements_set = set()
        self.graph_num = 1
        self.json_dict = dict()
        self.json_list = list()
        self.graph_subset  = set()
        self.graph_list = []
        self.graph_list_2 = []
        self.active_line = None
        self.last_active_graph = None
        self.last_active_line = None
        self.DrawTime = False
        self.line_list = []
        self.line_dict = {}
        self.test_set = set()
        self.ui.label_3.setText('Результат:')
        self.last_active_num = None
        self.for_test = False
        self.num_list = []

        # self.graph_list_2 = []

    @QtCore.pyqtSlot()
    def make_graph_bigger(self):
        """
        Делает элемент графа больше
        """
        if not self.active_graph is None:
            width = self.active_graph.width()
            height = self.active_graph.height()
            if all([width<125, height<105]):
                width += 50 
                height += 15
                self.active_graph.resize(width, height)

    @QtCore.pyqtSlot()
    def make_graph_less(self):
        """
        Делает элемент графа меньше
        """
        if not self.active_graph is None:
            width = self.active_graph.width()
            height = self.active_graph.height()
            if all([width>50, height>15]):
                width -= 50 
                height -= 15
                self.active_graph.resize(width, height)

    @QtCore.pyqtSlot()
    def getSaveFileName(self):
        """
        Сохраняет файл в json формате
        """
        file_filter = '(*.json)'
        response = QtWidgets.QFileDialog.getSaveFileName(
            parent=self,
            caption='Select a data file',
            filter=file_filter,
            initialFilter='(*.json)'
        )
        if response[0] != "":
            with open(response[0], 'w', encoding='utf-8') as file:
                num = 1
                graph_list = []
                self.json_dict['elements'] = [graph.text() for graph in self.graph_elements_set]
                for graph_set in self.graph_list:
                    for graph in graph_set:
                        graph_id_name = graph.id_name
                        graph_text = graph.text()
                        graph_x = graph.x()
                        graph_y = graph.y()
                        graph_width = graph.width()
                        graph_height = graph.height()
                        graph_dict = {graph_text: {
                            'graph_text': graph_text,
                            'graph_id_name': graph_id_name, 
                            'graph_x': graph_x,
                            'graph_y': graph_y,
                            'graph_width': graph_width,
                            'graph_height': graph_height,
                            }
                        }
                        self.json_list.append(graph_dict)
                        # self.elements_list.append(graph_id_name)
                    self.json_dict[f'Graph_pair{num}'] = self.json_list
                    if self.ui.plainTextEdit_2.toPlainText() != "":
                        self.json_dict['task'] = self.ui.plainTextEdit_2.toPlainText()
                    num += 1
                    self.json_list = []
                file.seek(0)
                json.dump(self.json_dict, fp=file, indent=4)
                file.truncate()

    def show_info(self, error=False, text=None, info_text=None, title=None):
        """
        Показывает выскакивающую табличку для пользователя, если он что то сделал не так. 
        Аргумент error является главным, позволяет вместо информационного окошка показывать окошко с ошибкой
        """
        msg = QtWidgets.QMessageBox()
        if error:
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText(f"{text}")
            msg.setInformativeText(f"{info_text}")
            msg.setWindowTitle(f"{title}")
            msg.exec_()
        else:
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("Информация!")
            msg.setInformativeText('Комбинации кнопок и клавиш:\nВыбор элемента графа - Щелчок левой кнопкой мыши\nПеретаскивание графа - Щелчок правой кнопкой мыши по выбранному элементу графа\nОбъединение вершин графа - Ctrl + Щелчок левой кнопкой мыши\nУдаление связи между элементами - Shift + Ctrl\n\nИнструкция:\n\nЕсли в учитель и хотите создать новое задание:\nПерейдите в окно "Редактор графов", щелкнув по кнопке "Редактор графов".\nВ строке под словом "Задание:" опишите само задание.\nСоздать элемент графа: впечатайте имя элемента в строку "Название элемента графа" и нажмите на кнопку "Создать элемент графа". Создайте связи между элементами при помощи комбинаций, упомянутых выше. Изменить размер элемента: выберите нужный элемент и нажмите на кнопку "+" или "-", в разделе "Масштаб элемента графа". Удалить элемент: выберите нужный элемент и нажмите на кнопку "Удалить элемент графа". Удалить всё: нажмите на кнопку "Очистить карту графов".\nСохраните задание, нажав на кнопку "Сохранить граф".\n\nЕсли вы ученик и хотите выполнить задание:\nПерейдите в окно "Алгоритмизация графов"\nЗагрузите задание, нажав на кнопку "Загрузить граф". Прочитайте задание и растащите элементы графа по полю для наглядности.\nВыберите цвет стрелки, создайте нужные связи между элементами, постройте граф. По готовности нажмите на кнопку "Проверить правильность". Программа сравнит ваш граф с эталонным ответом и выведет результат. Посмотреть как выглядит ответ: нажмите на кнопку "Пример правильного ответа". На экране появится верный ответ к данному заданию. Результатом выполнения будет "Провалено!".')
            msg.setWindowTitle("Информация")
            msg.exec_()

    @QtCore.pyqtSlot()
    def change_color_on_click(self):
        """"
        Добавляет цвета в выпадающий список с помощью чтения конфига
        """
        color = QtWidgets.QColorDialog.getColor()
        if len(self.ui.SP_HL_HL_VL1_ListWidget) >= 15:
            self.ui.SP_HL_HL_VL1_ListWidget.takeItem(0)
        self.ui.SP_HL_HL_VL1_ListWidget.addItem(color.name())
        with open('config/colors.json', 'r+') as file:
            data = json.load(file)
            index = len(data['colors'])
            data['colors'].append({f'color{index+1}': color.name()})
            file.seek(0)
            json.dump(data, fp=file, indent=4)
            file.truncate()

    def add_graph_button(self, graph_text: str = None, graph_id_name: str = None):
        """
        Добавляет вершину графа. Зависим от названия графа, которое дано пользователем
        Иначе дастся вершине стандартное название - Граф
        """
        if graph_text and graph_id_name:
            graph_button = GraphButton(f"{graph_text}", f"{graph_id_name}",  self)
            graph_button.able_to_move = False
        else:
            if len(self.deleted_list) > 0:
                self.graph_num = int(self.deleted_list[0][-1])
                self.deleted_list.pop(0)
            if self.graph_num in self.num_list:
                self.graph_num += 1
            if self.ui.FP_VP2_LineEdit.text() == "":
                graph_button = GraphButton(f"Граф {self.graph_num}", f"Граф {self.graph_num}",  self)
                graph_button.able_to_move = False
            else:
                graph_button = GraphButton(f"{self.ui.FP_VP2_LineEdit.text()} {self.graph_num}", f"Граф {self.graph_num}", self)
                graph_button.able_to_move = False
        graph_button.setStyleSheet(
        ""
        "background-color: rgb(169, 170, 153)"
        ""
        )
        self.DrawTime = True
        self.ui.widget.button = graph_button
        self.ui.widget.button.show()
        self.ui.FP_VP2_LineEdit.clear()
        x = int(self.ui.widget.width()/2)
        self.num_list.append(self.graph_num)
        self.graph_num += 1 
        self.last_active_num = self.graph_num
        y = int(self.ui.widget.height()/2)
        self.ui.widget.button.move(x, y)
        self.graph_elements_set.add(graph_button)
        graph_button.clicked.connect(lambda: self.graph_on_click(button=graph_button))

    @QtCore.pyqtSlot()
    def graph_on_click(self, button):
        """
        Метод, который выполняет разные функции в зависимости от клавиши, которая была нажата вместей с ней.
        Ctrl - создает соединения и взаимосвязи между вершинами.
        Shift - удаляет соединения и взаимосвязи между вершинами.
        Обычный клик - выделяет граф и делает его активным.
        """
        modifiers = QApplication.keyboardModifiers()
        self.update()
        if modifiers == QtCore.Qt.ControlModifier:
            if not self.active_line is None:
                self.last_active_line = self.active_line
                self.active_line = button
                self.graph_subset.add(self.last_active_line)
                self.graph_subset.add(self.active_line)
                line_frozen_set = frozenset([self.last_active_line, self.active_line])
                list_line = []
                self.line_button_1_x = self.last_active_line.x() + 20
                self.line_button_1_y = self.last_active_line.y() + 20
                self.line_button_2_x = self.active_line.x() + 20
                self.line_button_2_y = self.active_line.y() + 20
                list_line.append(self.line_button_1_x)
                list_line.append(self.line_button_1_y)
                list_line.append(self.line_button_2_x)
                list_line.append(self.line_button_2_y)
                print(list_line)
                self.line_dict[line_frozen_set] = list_line
                self.active_graph = self.active_line
                self.graph_elements_set.remove(self.active_graph)
                for graph in self.graph_elements_set:
                    graph.setStyleSheet(
                        ""
                        "background-color: rgb(169, 170, 153)"
                        ""
                    )
                    graph.able_to_move = False
                self.active_graph.able_to_move = True
                self.graph_elements_set.add(self.active_graph)
                self.active_graph.setStyleSheet(
                    ""
                    "background-color: rgb(255, 120, 57)"
                    "")

                self.active_line.able_to_move = True
                for graph in self.graph_subset:
                    id_name = graph.id_name
                    text = graph.text()
                if self.graph_subset not in self.graph_list:
                    if len(self.graph_subset) == 2:
                        self.graph_list.append(self.graph_subset)
                self.active_line = None
                self.graph_subset = set()
                self.DrawTime = True
                self.update()
                return None
            else:
                self.active_line = button
                return self.active_line

        if modifiers == QtCore.Qt.ShiftModifier:
            for pair in list(self.line_dict):
                if button in pair:
                    del self.line_dict[pair]
                    print(self.graph_list)
            for pair in self.graph_list:
                if button in pair:
                    self.graph_list.remove(pair)
            self.DrawTime = True


        else:
            if self.active_line is None:
                self.active_graph = button
                self.graph_elements_set.remove(self.active_graph)
                for graph in self.graph_elements_set:
                    graph.setStyleSheet(
                        ""
                        "background-color: rgb(169, 170, 153)"
                        ""
                    )
                self.active_graph.able_to_move = True
                self.graph_elements_set.add(self.active_graph)
                self.active_graph.setStyleSheet(
                    ""
                    "background-color: rgb(255, 120, 57)"
                    "")

    @QtCore.pyqtSlot()
    def upload_json_map(self):
        """Сериализирует питоновские словари и массивы в json'овские. 
        Пример:
        {
    "Graph_pair1": [
        {
            "Кошки  1": {
                "graph_text": "Кошки 1",
                "graph_id_name": "\u0413\u0440\u0430\u0444 1",
                "graph_x": 466,
                "graph_y": 350,
                "graph_width": 100,
                "graph_height": 30
            }
        },
        {
            "\Собачки 2": {
                "graph_text": "Собачки 2",
                "graph_id_name": "\u0413\u0440\u0430\u0444 2",
                "graph_x": 627,
                "graph_y": 424,
                "graph_width": 100,
                "graph_height": 30
            }
        }
    ],
    "elements": [
        "Кошки  1",
        "Собачки 2"
    ]
}
        Так же метод реагирует на правильность созданного json'а, в ином случае бросает ошибку с подписью, что не так.
        """
        self.ui.StackedWidget.setCurrentWidget(self.ui.Second_Page)
        self.clear_graph_map()
        list_ = []
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        graph_list = []
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self ,"OpenFile", "Json Files (*.json)", options=options)
        if fileName:
            if fileName.endswith('.json'):
                try:
                    with open(fileName, 'r+') as json_file:
                        self.json_ = json.load(json_file)
                        self.ui.VP_Label.setText(self.u_translate("MainWindow", f"Актуальный граф: {fileName}"))
                        if not self.json_.get('task') is None:
                            task = self.json_.get('task')
                            self.ui.label_2.setText(f'Задание: {task}')
                        graph_list = self.json_.get('elements')
                        for key, value in self.json_.items():
                            if 'Graph_pair' in key:
                                for index in value:
                                    graph_pair_list = list()
                                    for data in value:
                                        name = (list(data.keys())[0])
                                        graph_pair_list.append(name)
                                    self.graph_list_2.append(graph_pair_list)
                                    for pair in self.graph_list_2:
                                        while self.graph_list_2.count(pair) != 1:
                                            self.graph_list_2.pop(self.graph_list_2.index(pair))
                                    self.graph_list_3 = self.graph_list_2
                                    for name, data in index.items():
                                        if name not in list_:
                                            list_.append(name)
                                            id = name
                                            graph_text = data.get('graph_text')
                                            graph_id_name = data.get('graph_id_name')
                                            graph_x = data.get('graph_x')
                                            graph_y = data.get('graph_y')
                                            graph_width = data.get('graph_width')
                                            graph_height = data.get('graph_height')
                                            self.add_graph_button(graph_text=graph_text, graph_id_name=graph_id_name)
                        self.num = 0
                        self.test_list = list(self.test_set)
                        graph_dict = {}
                        graph_elements_set = set()
                        for a in self.graph_list_2:
                            for b in a:
                                graph_elements_set.add(b)
                        
                        list_ = []
                        for a in graph_elements_set:
                            for b in self.graph_list_2:
                                for c in b:
                                    if a in b:
                                        if c!=a:
                                            list_.append(c)
                                graph_dict[a] = list_
                            list_ = []
                            graph_list = []
                except json.decoder.JSONDecodeError:
                    self.show_info(error=True, text='Ошибка в файле графа! Выберите другой файл!', info_text="json.decoder.JSONDecodeError", title="Ошибка в файле!")
            else:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setText("Ошибка! Файл не соответствует json формату!")
                msg.setInformativeText('Выберите файл с другим форматом!')
                msg.setWindowTitle("Ошибка!")
                msg.exec_()

    @QtCore.pyqtSlot()
    def show_json_graphs(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
    
    @QtCore.pyqtSlot()
    def dragEnterEvent(self, event):
        """
        Принимает перенос местоположения вершины графа с места на место.
        """
        event.accept()


    @QtCore.pyqtSlot()
    def dropEvent(self, event):
        """
        Регистрирует перемещения вершины графа, очень сильно привязан к невидимой арене, что бы пользователь не закинул вершину, куда не надо
        Так же реализованы активные перемещения линий при перемещении вершин.
        """
        position = event.pos()
        x = position.x() + 30
        y = position.y() + 30
        width = self.active_graph.width()
        y = position.y()
        widget_width = self.ui.widget_2.width()
        widget_height = self.ui.widget_2.height()
        widget_x = self.ui.widget_2.x()
        widget_y = self.ui.widget_2.y()
        if any([x<widget_x, width+x>widget_width+widget_x, y<widget_y, y>widget_y + widget_height]):
            return None
        else:
            if self.active_graph == self.active_line:
                return None
            self.active_graph.move(position)
            if self.active_graph != self.active_line:
                list_ = []
                for key in list(self.line_dict):
                    if self.active_graph in key:
                        for element in key:
                            if self.active_graph != element:
                                other_x = element.x() 
                                other_y = element.y()
                                list_.append(other_x)
                                list_.append(other_y)
                                list_.append(self.active_graph.x())
                                list_.append(self.active_graph.y())
                                while len(list_) != 4:
                                    list_.pop(0)
                                self.line_dict[key] = list_
                        list_ = []
            else:
                for key in list(self.line_dict):
                    if len(key) == 2:
                        if self.active_graph in key:
                            list_ = self.line_dict.get(key)
                            list_.pop(-1) ; list_.pop(-1)
                            list_.append(x)
                            list_.append(y)
                            if len(key) == 2:
                                self.line_dict[key] = list_
            self.DrawTime=True
            event.accept()



    def paintEvent(self, event):
        """
        Метод, который рисует линии. Зависит от аргумента for_test
        В первом случае строит линии сам пользователь
        В ином - сам
        """
        painter = QtGui.QPainter(self)
        painter.setPen(QtGui.QPen(QtCore.Qt.red, 3, QtCore.Qt.SolidLine))
        current_color = self.ui.SP_HL_HL_VL1_ListWidget.currentItem()
        try:
            print(current_color.text())
            if current_color.text() == "Красный":
                painter.setPen(QtGui.QPen(QtCore.Qt.red, 3, QtCore.Qt.SolidLine))
            if current_color.text() == "Синий":
                painter.setPen(QtGui.QPen(QtCore.Qt.blue, 3, QtCore.Qt.SolidLine))
            if current_color.text() == "Зеленый":
                painter.setPen(QtGui.QPen(QtCore.Qt.green, 3, QtCore.Qt.SolidLine))
            if current_color.text() == "Желтый":
                painter.setPen(QtGui.QPen(QtCore.Qt.yellow, 3, QtCore.Qt.SolidLine))
            if current_color.text() == "Розовый":
                painter.setPen(QtGui.QPen(QtCore.Qt.pink, 3, QtCore.Qt.SolidLine))

        except AttributeError:
            pass
        if self.for_test:
            if self.DrawTime:
                for line in self.line_list:
                    while self.line_list.count(line) != 1:
                        self.line_list.pop(self.line_list.index(line))
                for line in self.line_list:
                    painter.drawLine(*line)
        else:
            if self.DrawTime:
                for line in self.line_dict.values():
                    if not len(set(line)) == 2:
                        painter.drawLine(*line)
                        self.update()
                    else:
                        try:
                            del self.line_dict[line]
                        except TypeError:
                            pass

        self.update()
        
        

if __name__ == "__main__":
    """
    Определяем окна и запускаем наш код
    """
    main_app = Main()
    main_app.show()
    hello_window = Hello_Window()
    hello_window.show()
    sys.exit(app.exec_())
