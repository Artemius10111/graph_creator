# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\artem\Desktop\graph\.venv\pyqt\design\UI\graph4_1.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1202, 900)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.StackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.StackedWidget.setStyleSheet("QStackedWidget {\n"
"    background-color: rgb(134, 134, 134)\n"
"}")
        self.StackedWidget.setObjectName("StackedWidget")
        self.First_Page = QtWidgets.QWidget()
        self.First_Page.setObjectName("First_Page")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.First_Page)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.FP_VerticalLayout1 = QtWidgets.QVBoxLayout()
        self.FP_VerticalLayout1.setObjectName("FP_VerticalLayout1")
        self.FP_VL1_PushButton = QtWidgets.QPushButton(self.First_Page)
        self.FP_VL1_PushButton.setObjectName("FP_VL1_PushButton")
        self.FP_VerticalLayout1.addWidget(self.FP_VL1_PushButton)
        self.gridLayout_3.addLayout(self.FP_VerticalLayout1, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.FP_VP3_CheckGraphBtn = QtWidgets.QPushButton(self.First_Page)
        self.FP_VP3_CheckGraphBtn.setObjectName("FP_VP3_CheckGraphBtn")
        self.horizontalLayout_2.addWidget(self.FP_VP3_CheckGraphBtn)
        self.FP_VP3_GreatGraphExampleBtn = QtWidgets.QPushButton(self.First_Page)
        self.FP_VP3_GreatGraphExampleBtn.setObjectName("FP_VP3_GreatGraphExampleBtn")
        self.horizontalLayout_2.addWidget(self.FP_VP3_GreatGraphExampleBtn)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 0, 1, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.First_Page)
        self.label.setEnabled(True)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.pushButton_2 = QtWidgets.QPushButton(self.First_Page)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.First_Page)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.gridLayout_3.addLayout(self.verticalLayout_2, 1, 1, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.First_Page)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_3.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.First_Page)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_3.addWidget(self.pushButton_4)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.FP_VP2_LineEdit = QtWidgets.QLineEdit(self.First_Page)
        self.FP_VP2_LineEdit.setText("")
        self.FP_VP2_LineEdit.setClearButtonEnabled(True)
        self.FP_VP2_LineEdit.setObjectName("FP_VP2_LineEdit")
        self.verticalLayout_4.addWidget(self.FP_VP2_LineEdit)
        self.FP_VP2_PushButton = QtWidgets.QPushButton(self.First_Page)
        self.FP_VP2_PushButton.setObjectName("FP_VP2_PushButton")
        self.verticalLayout_4.addWidget(self.FP_VP2_PushButton)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.gridLayout_3.addLayout(self.horizontalLayout_3, 2, 1, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.First_Page)
        self.groupBox.setObjectName("groupBox")
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_6.setGeometry(QtCore.QRect(10, 10, 301, 23))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_7.setGeometry(QtCore.QRect(210, 70, 75, 23))
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_3.addWidget(self.groupBox, 3, 0, 1, 2)
        self.verticalLayout_3.addLayout(self.gridLayout_3)
        self.StackedWidget.addWidget(self.First_Page)
        self.Second_Page = QtWidgets.QWidget()
        self.Second_Page.setObjectName("Second_Page")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.Second_Page)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.SP_HL_VL_VL_PushButton = QtWidgets.QPushButton(self.Second_Page)
        self.SP_HL_VL_VL_PushButton.setEnabled(True)
        self.SP_HL_VL_VL_PushButton.setObjectName("SP_HL_VL_VL_PushButton")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.SP_HL_VL_VL_PushButton)
        self.SP_HL_VL_VL2_PushButton = QtWidgets.QPushButton(self.Second_Page)
        self.SP_HL_VL_VL2_PushButton.setObjectName("SP_HL_VL_VL2_PushButton")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.SP_HL_VL_VL2_PushButton)
        self.formLayout_2.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.formLayout)
        self.SP_HL_HorizontalLayout = QtWidgets.QHBoxLayout()
        self.SP_HL_HorizontalLayout.setObjectName("SP_HL_HorizontalLayout")
        self.SP_HL_HL_VerticalLayout = QtWidgets.QVBoxLayout()
        self.SP_HL_HL_VerticalLayout.setObjectName("SP_HL_HL_VerticalLayout")
        self.SP_HL_HL_VL1_Label = QtWidgets.QLabel(self.Second_Page)
        self.SP_HL_HL_VL1_Label.setObjectName("SP_HL_HL_VL1_Label")
        self.SP_HL_HL_VerticalLayout.addWidget(self.SP_HL_HL_VL1_Label)
        self.SP_HL_HL_VL1_ListWidget = QtWidgets.QListWidget(self.Second_Page)
        self.SP_HL_HL_VL1_ListWidget.setObjectName("SP_HL_HL_VL1_ListWidget")
        item = QtWidgets.QListWidgetItem()
        self.SP_HL_HL_VL1_ListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.SP_HL_HL_VL1_ListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.SP_HL_HL_VL1_ListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.SP_HL_HL_VL1_ListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.SP_HL_HL_VL1_ListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.SP_HL_HL_VL1_ListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.SP_HL_HL_VL1_ListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.SP_HL_HL_VL1_ListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.SP_HL_HL_VL1_ListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.SP_HL_HL_VL1_ListWidget.addItem(item)
        self.SP_HL_HL_VerticalLayout.addWidget(self.SP_HL_HL_VL1_ListWidget)
        self.SP_HL_HL_VL1_ChangeColorBtn = QtWidgets.QPushButton(self.Second_Page)
        self.SP_HL_HL_VL1_ChangeColorBtn.setObjectName("SP_HL_HL_VL1_ChangeColorBtn")
        self.SP_HL_HL_VerticalLayout.addWidget(self.SP_HL_HL_VL1_ChangeColorBtn)
        self.SP_HL_HorizontalLayout.addLayout(self.SP_HL_HL_VerticalLayout)
        self.SP_HL_HL_VerticalLayout3 = QtWidgets.QVBoxLayout()
        self.SP_HL_HL_VerticalLayout3.setObjectName("SP_HL_HL_VerticalLayout3")
        self.SP_HL_HL_VL3_Label = QtWidgets.QLabel(self.Second_Page)
        self.SP_HL_HL_VL3_Label.setObjectName("SP_HL_HL_VL3_Label")
        self.SP_HL_HL_VerticalLayout3.addWidget(self.SP_HL_HL_VL3_Label)
        self.SP_HL_HL_VL3_ListWidget = QtWidgets.QListWidget(self.Second_Page)
        self.SP_HL_HL_VL3_ListWidget.setObjectName("SP_HL_HL_VL3_ListWidget")
        self.SP_HL_HL_VerticalLayout3.addWidget(self.SP_HL_HL_VL3_ListWidget)
        self.SP_HL_HorizontalLayout.addLayout(self.SP_HL_HL_VerticalLayout3)
        self.SP_HL_HL_VerticalLayout_2 = QtWidgets.QVBoxLayout()
        self.SP_HL_HL_VerticalLayout_2.setObjectName("SP_HL_HL_VerticalLayout_2")
        self.SP_HL_HL_VL2_Label = QtWidgets.QLabel(self.Second_Page)
        self.SP_HL_HL_VL2_Label.setObjectName("SP_HL_HL_VL2_Label")
        self.SP_HL_HL_VerticalLayout_2.addWidget(self.SP_HL_HL_VL2_Label)
        self.SP_HL_HL_VL2_ListWidget = QtWidgets.QListWidget(self.Second_Page)
        self.SP_HL_HL_VL2_ListWidget.setObjectName("SP_HL_HL_VL2_ListWidget")
        self.SP_HL_HL_VerticalLayout_2.addWidget(self.SP_HL_HL_VL2_ListWidget)
        self.SP_HL_HorizontalLayout.addLayout(self.SP_HL_HL_VerticalLayout_2)
        self.formLayout_2.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.SP_HL_HorizontalLayout)
        self.verticalLayout.addLayout(self.formLayout_2)
        self.StackedWidget.addWidget(self.Second_Page)
        self.horizontalLayout.addWidget(self.StackedWidget)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout.setObjectName("gridLayout")
        self.VP_Label = QtWidgets.QLabel(self.centralwidget)
        self.VP_Label.setObjectName("VP_Label")
        self.gridLayout.addWidget(self.VP_Label, 1, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 2, 0, 1, 1)
        self.VP_UploadGraphButton = QtWidgets.QPushButton(self.centralwidget)
        self.VP_UploadGraphButton.setObjectName("VP_UploadGraphButton")
        self.gridLayout.addWidget(self.VP_UploadGraphButton, 3, 0, 1, 1)
        self.VP_PushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.VP_PushButton1.setObjectName("VP_PushButton1")
        self.gridLayout.addWidget(self.VP_PushButton1, 4, 0, 1, 1)
        self.Info = QtWidgets.QPushButton(self.centralwidget)
        self.Info.setEnabled(True)
        self.Info.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Info.setObjectName("Info")
        self.gridLayout.addWidget(self.Info, 0, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1202, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.StackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.FP_VL1_PushButton.setText(_translate("MainWindow", "<<< Алгоритмизация графов"))
        self.FP_VP3_CheckGraphBtn.setText(_translate("MainWindow", "Проверить граф"))
        self.FP_VP3_GreatGraphExampleBtn.setText(_translate("MainWindow", "Пример правильного графа"))
        self.label.setText(_translate("MainWindow", "Масштаб элемента графа"))
        self.pushButton_2.setText(_translate("MainWindow", "+"))
        self.pushButton.setText(_translate("MainWindow", "-"))
        self.pushButton_3.setText(_translate("MainWindow", "Очистить карту графов"))
        self.pushButton_4.setText(_translate("MainWindow", "Удалить элемент графа"))
        self.FP_VP2_LineEdit.setPlaceholderText(_translate("MainWindow", "Название элемента графа"))
        self.FP_VP2_PushButton.setText(_translate("MainWindow", "Создать элемент графа"))
        self.groupBox.setTitle(_translate("MainWindow", "Арена"))
        self.pushButton_6.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_7.setText(_translate("MainWindow", "PushButton"))
        self.SP_HL_VL_VL_PushButton.setText(_translate("MainWindow", "<<< Редактор графов"))
        self.SP_HL_VL_VL2_PushButton.setText(_translate("MainWindow", "Обойти граф"))
        self.SP_HL_HL_VL1_Label.setText(_translate("MainWindow", "Выбрать цвет стрелки:"))
        __sortingEnabled = self.SP_HL_HL_VL1_ListWidget.isSortingEnabled()
        self.SP_HL_HL_VL1_ListWidget.setSortingEnabled(False)
        item = self.SP_HL_HL_VL1_ListWidget.item(0)
        item.setText(_translate("MainWindow", "Красный"))
        item = self.SP_HL_HL_VL1_ListWidget.item(1)
        item.setText(_translate("MainWindow", "Синий"))
        item = self.SP_HL_HL_VL1_ListWidget.item(2)
        item.setText(_translate("MainWindow", "Зеленый"))
        item = self.SP_HL_HL_VL1_ListWidget.item(3)
        item.setText(_translate("MainWindow", "Желтый "))
        item = self.SP_HL_HL_VL1_ListWidget.item(4)
        item.setText(_translate("MainWindow", "Розовый"))
        item = self.SP_HL_HL_VL1_ListWidget.item(5)
        item.setText(_translate("MainWindow", "Фиолетовый"))
        item = self.SP_HL_HL_VL1_ListWidget.item(6)
        item.setText(_translate("MainWindow", "Голубой"))
        item = self.SP_HL_HL_VL1_ListWidget.item(7)
        item.setText(_translate("MainWindow", "Пурпурный"))
        item = self.SP_HL_HL_VL1_ListWidget.item(8)
        item.setText(_translate("MainWindow", "Салатовый"))
        item = self.SP_HL_HL_VL1_ListWidget.item(9)
        item.setText(_translate("MainWindow", "Коричневый"))
        self.SP_HL_HL_VL1_ListWidget.setSortingEnabled(__sortingEnabled)
        self.SP_HL_HL_VL1_ChangeColorBtn.setText(_translate("MainWindow", "Выбрать свой цвет"))
        self.SP_HL_HL_VL3_Label.setText(_translate("MainWindow", "Выбрать тип обхода дерева:"))
        self.SP_HL_HL_VL2_Label.setText(_translate("MainWindow", "Выбрать тип перемещения стрелок:"))
        self.VP_Label.setText(_translate("MainWindow", "Актуальный граф: graph.json"))
        self.pushButton_5.setText(_translate("MainWindow", "Сохранить граф"))
        self.VP_UploadGraphButton.setText(_translate("MainWindow", "Загрузить граф (.json)"))
        self.VP_PushButton1.setText(_translate("MainWindow", "Ваши графы"))
        self.Info.setText(_translate("MainWindow", "Справка"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
