# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\artem\Desktop\graph\.venv\pyqt\design\UI\graph1.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(-30, 0, 911, 861))
        self.stackedWidget.setStyleSheet("QStackedWidget {\n"
"    background-color: rgb(134, 134, 134)\n"
"}")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.page)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(280, 0, 311, 111))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.page)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 281, 111))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_3.addWidget(self.pushButton_2)
        self.pushButton_5 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_3.addWidget(self.pushButton_5)
        self.pushButton_4 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_3.addWidget(self.pushButton_4)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.page)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(590, 0, 331, 111))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_3.setEnabled(True)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_4.addWidget(self.pushButton_3)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.page_2)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(30, 0, 321, 221))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        self.listView = QtWidgets.QListView(self.verticalLayoutWidget_4)
        self.listView.setObjectName("listView")
        self.verticalLayout_5.addWidget(self.listView)
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.page_2)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(350, 0, 321, 221))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_6.addWidget(self.label_2)
        self.listView_2 = QtWidgets.QListView(self.verticalLayoutWidget_5)
        self.listView_2.setObjectName("listView_2")
        self.verticalLayout_6.addWidget(self.listView_2)
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.page_2)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(670, 0, 211, 221))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.pushButton_7 = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout_7.addWidget(self.pushButton_7)
        self.pushButton_8 = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout_7.addWidget(self.pushButton_8)
        self.textEdit = QtWidgets.QTextEdit(self.verticalLayoutWidget_6)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_7.addWidget(self.textEdit)
        self.pushButton_6 = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
        self.pushButton_6.setEnabled(True)
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_7.addWidget(self.pushButton_6)
        self.stackedWidget.addWidget(self.page_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 911, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "???????????????? ???????????????? ??????????"))
        self.pushButton.setText(_translate("MainWindow", "?????????????? ?????????????? ??????????"))
        self.pushButton_2.setText(_translate("MainWindow", "?????????????????? ?????????? ??????????"))
        self.pushButton_5.setText(_translate("MainWindow", "?????????????????? ???????????????????????? ??????????"))
        self.pushButton_4.setText(_translate("MainWindow", "?????????????????? ???????????? ??????????"))
        self.pushButton_3.setText(_translate("MainWindow", "??????????????"))
        self.label.setText(_translate("MainWindow", "?????? ?????????????????????? ??????????????"))
        self.label_2.setText(_translate("MainWindow", "???????????? ???????????? ????????????"))
        self.pushButton_7.setText(_translate("MainWindow", "???????????? ????????????"))
        self.pushButton_8.setText(_translate("MainWindow", "?????????????? ???????? ??????????????"))
        self.pushButton_6.setText(_translate("MainWindow", "??????????????"))

