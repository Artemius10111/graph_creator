# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\artem\Desktop\graph\.venv\pyqt\design\UI\graph4.ui'
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
        self.StackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.StackedWidget.setGeometry(QtCore.QRect(-10, 0, 901, 861))
        self.StackedWidget.setStyleSheet("QStackedWidget {\n"
"    background-color: rgb(134, 134, 134)\n"
"}")
        self.StackedWidget.setObjectName("StackedWidget")
        self.First_Page = QtWidgets.QWidget()
        self.First_Page.setObjectName("First_Page")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.First_Page)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 0, 891, 211))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.FP_HorizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.FP_HorizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.FP_HorizontalLayout.setObjectName("FP_HorizontalLayout")
        self.FP_VerticalLayout1 = QtWidgets.QVBoxLayout()
        self.FP_VerticalLayout1.setObjectName("FP_VerticalLayout1")
        self.FP_VL1_PushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.FP_VL1_PushButton.setObjectName("FP_VL1_PushButton")
        self.FP_VerticalLayout1.addWidget(self.FP_VL1_PushButton)
        self.FP_HorizontalLayout.addLayout(self.FP_VerticalLayout1)
        self.FP_VerticalLayout3 = QtWidgets.QVBoxLayout()
        self.FP_VerticalLayout3.setObjectName("FP_VerticalLayout3")
        self.FP_VP3_GreatGraphExampleBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.FP_VP3_GreatGraphExampleBtn.setObjectName("FP_VP3_GreatGraphExampleBtn")
        self.FP_VerticalLayout3.addWidget(self.FP_VP3_GreatGraphExampleBtn)
        self.FP_VP3_CheckGraphBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.FP_VP3_CheckGraphBtn.setObjectName("FP_VP3_CheckGraphBtn")
        self.FP_VerticalLayout3.addWidget(self.FP_VP3_CheckGraphBtn)
        self.FP_HorizontalLayout.addLayout(self.FP_VerticalLayout3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label.setEnabled(True)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.FP_HorizontalLayout.addLayout(self.verticalLayout_2)
        self.FP_VerticalLayout2 = QtWidgets.QVBoxLayout()
        self.FP_VerticalLayout2.setObjectName("FP_VerticalLayout2")
        self.FP_VP2_LineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.FP_VP2_LineEdit.setText("")
        self.FP_VP2_LineEdit.setClearButtonEnabled(True)
        self.FP_VP2_LineEdit.setObjectName("FP_VP2_LineEdit")
        self.FP_VerticalLayout2.addWidget(self.FP_VP2_LineEdit)
        self.FP_VP2_PushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.FP_VP2_PushButton.setObjectName("FP_VP2_PushButton")
        self.FP_VerticalLayout2.addWidget(self.FP_VP2_PushButton)
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.FP_VerticalLayout2.addWidget(self.pushButton_4)
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.FP_VerticalLayout2.addWidget(self.pushButton_3)
        self.FP_HorizontalLayout.addLayout(self.FP_VerticalLayout2)
        self.ScrollAreaWidgets_3 = QtWidgets.QScrollArea(self.First_Page)
        self.ScrollAreaWidgets_3.setGeometry(QtCore.QRect(10, 210, 891, 731))
        self.ScrollAreaWidgets_3.setWidgetResizable(True)
        self.ScrollAreaWidgets_3.setObjectName("ScrollAreaWidgets_3")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 889, 729))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.ScrollAreaWidgets_3.setWidget(self.scrollAreaWidgetContents_4)
        self.StackedWidget.addWidget(self.First_Page)
        self.Second_Page = QtWidgets.QWidget()
        self.Second_Page.setObjectName("Second_Page")
        self.ScrollAreaWidgets_2 = QtWidgets.QScrollArea(self.Second_Page)
        self.ScrollAreaWidgets_2.setGeometry(QtCore.QRect(10, 130, 891, 731))
        self.ScrollAreaWidgets_2.setWidgetResizable(True)
        self.ScrollAreaWidgets_2.setObjectName("ScrollAreaWidgets_2")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 889, 729))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.ScrollAreaWidgets_2.setWidget(self.scrollAreaWidgetContents_3)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.Second_Page)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 891, 131))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.SP_HorizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.SP_HorizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.SP_HorizontalLayout.setObjectName("SP_HorizontalLayout")
        self.SP_HL_VL_VertIcaLayout1 = QtWidgets.QVBoxLayout()
        self.SP_HL_VL_VertIcaLayout1.setObjectName("SP_HL_VL_VertIcaLayout1")
        self.SP_HL_VL_VL_PushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.SP_HL_VL_VL_PushButton.setEnabled(True)
        self.SP_HL_VL_VL_PushButton.setObjectName("SP_HL_VL_VL_PushButton")
        self.SP_HL_VL_VertIcaLayout1.addWidget(self.SP_HL_VL_VL_PushButton)
        self.SP_HorizontalLayout.addLayout(self.SP_HL_VL_VertIcaLayout1)
        self.SP_HL_HorizontalLayout = QtWidgets.QHBoxLayout()
        self.SP_HL_HorizontalLayout.setObjectName("SP_HL_HorizontalLayout")
        self.SP_HL_HL_VerticalLayout = QtWidgets.QVBoxLayout()
        self.SP_HL_HL_VerticalLayout.setObjectName("SP_HL_HL_VerticalLayout")
        self.SP_HL_HL_VL1_Label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.SP_HL_HL_VL1_Label.setObjectName("SP_HL_HL_VL1_Label")
        self.SP_HL_HL_VerticalLayout.addWidget(self.SP_HL_HL_VL1_Label)
        self.SP_HL_HL_VL1_ListWidget = QtWidgets.QListWidget(self.horizontalLayoutWidget)
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
        self.SP_HL_HL_VL1_ChangeColorBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.SP_HL_HL_VL1_ChangeColorBtn.setObjectName("SP_HL_HL_VL1_ChangeColorBtn")
        self.SP_HL_HL_VerticalLayout.addWidget(self.SP_HL_HL_VL1_ChangeColorBtn)
        self.SP_HL_HorizontalLayout.addLayout(self.SP_HL_HL_VerticalLayout)
        self.SP_HL_HL_VerticalLayout3 = QtWidgets.QVBoxLayout()
        self.SP_HL_HL_VerticalLayout3.setObjectName("SP_HL_HL_VerticalLayout3")
        self.SP_HL_HL_VL3_Label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.SP_HL_HL_VL3_Label.setObjectName("SP_HL_HL_VL3_Label")
        self.SP_HL_HL_VerticalLayout3.addWidget(self.SP_HL_HL_VL3_Label)
        self.SP_HL_HL_VL3_ListWidget = QtWidgets.QListWidget(self.horizontalLayoutWidget)
        self.SP_HL_HL_VL3_ListWidget.setObjectName("SP_HL_HL_VL3_ListWidget")
        self.SP_HL_HL_VerticalLayout3.addWidget(self.SP_HL_HL_VL3_ListWidget)
        self.SP_HL_HorizontalLayout.addLayout(self.SP_HL_HL_VerticalLayout3)
        self.SP_HL_HL_VerticalLayout_2 = QtWidgets.QVBoxLayout()
        self.SP_HL_HL_VerticalLayout_2.setObjectName("SP_HL_HL_VerticalLayout_2")
        self.SP_HL_HL_VL2_Label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.SP_HL_HL_VL2_Label.setObjectName("SP_HL_HL_VL2_Label")
        self.SP_HL_HL_VerticalLayout_2.addWidget(self.SP_HL_HL_VL2_Label)
        self.SP_HL_HL_VL2_ListWidget = QtWidgets.QListWidget(self.horizontalLayoutWidget)
        self.SP_HL_HL_VL2_ListWidget.setObjectName("SP_HL_HL_VL2_ListWidget")
        self.SP_HL_HL_VerticalLayout_2.addWidget(self.SP_HL_HL_VL2_ListWidget)
        self.SP_HL_HorizontalLayout.addLayout(self.SP_HL_HL_VerticalLayout_2)
        self.SP_HorizontalLayout.addLayout(self.SP_HL_HorizontalLayout)
        self.SP_HL_VL_VerticalLayout2 = QtWidgets.QVBoxLayout()
        self.SP_HL_VL_VerticalLayout2.setObjectName("SP_HL_VL_VerticalLayout2")
        self.SP_HL_VL_VL2_PushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.SP_HL_VL_VL2_PushButton.setObjectName("SP_HL_VL_VL2_PushButton")
        self.SP_HL_VL_VerticalLayout2.addWidget(self.SP_HL_VL_VL2_PushButton)
        self.SP_HorizontalLayout.addLayout(self.SP_HL_VL_VerticalLayout2)
        self.StackedWidget.addWidget(self.Second_Page)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(890, 0, 311, 211))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.VerticalLayout1 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.VerticalLayout1.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.VerticalLayout1.setContentsMargins(0, 0, 0, 0)
        self.VerticalLayout1.setObjectName("VerticalLayout1")
        self.Info = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.Info.setEnabled(True)
        self.Info.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Info.setObjectName("Info")
        self.VerticalLayout1.addWidget(self.Info)
        self.VP_Label = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.VP_Label.setObjectName("VP_Label")
        self.VerticalLayout1.addWidget(self.VP_Label)
        self.pushButton_5 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setObjectName("pushButton_5")
        self.VerticalLayout1.addWidget(self.pushButton_5)
        self.VP_UploadGraphButton = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.VP_UploadGraphButton.setObjectName("VP_UploadGraphButton")
        self.VerticalLayout1.addWidget(self.VP_UploadGraphButton)
        self.VP_PushButton1 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.VP_PushButton1.setObjectName("VP_PushButton1")
        self.VerticalLayout1.addWidget(self.VP_PushButton1)
        self.VerticalLayout1.setStretch(0, 1)
        self.VerticalLayout1.setStretch(1, 1)
        self.VerticalLayout1.setStretch(2, 1)
        self.VerticalLayout1.setStretch(3, 1)
        self.verticalLayoutWidget_8 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_8.setGeometry(QtCore.QRect(890, 210, 311, 651))
        self.verticalLayoutWidget_8.setObjectName("verticalLayoutWidget_8")
        self.VerticalLayout2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_8)
        self.VerticalLayout2.setContentsMargins(0, 0, 0, 0)
        self.VerticalLayout2.setObjectName("VerticalLayout2")
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
        self.FP_VP3_GreatGraphExampleBtn.setText(_translate("MainWindow", "Пример правильного графа"))
        self.FP_VP3_CheckGraphBtn.setText(_translate("MainWindow", "Проверить граф"))
        self.label.setText(_translate("MainWindow", "Масштаб элемента графа"))
        self.pushButton_2.setText(_translate("MainWindow", "+"))
        self.pushButton.setText(_translate("MainWindow", "-"))
        self.FP_VP2_LineEdit.setPlaceholderText(_translate("MainWindow", "Название элемента графа"))
        self.FP_VP2_PushButton.setText(_translate("MainWindow", "Создать элемент графа"))
        self.pushButton_4.setText(_translate("MainWindow", "Удалить элемент графа"))
        self.pushButton_3.setText(_translate("MainWindow", "Очистить карту графов"))
        self.SP_HL_VL_VL_PushButton.setText(_translate("MainWindow", "<<< Редактор графов"))
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
        self.SP_HL_VL_VL2_PushButton.setText(_translate("MainWindow", "Обойти граф"))
        self.Info.setText(_translate("MainWindow", "Справка"))
        self.pushButton_5.setText(_translate("MainWindow", "Сохранить граф"))
        self.VP_UploadGraphButton.setText(_translate("MainWindow", "Загрузить граф (.json)"))
        self.VP_PushButton1.setText(_translate("MainWindow", "Ваши графы"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
