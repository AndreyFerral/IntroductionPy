# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lab8.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 215)
        font = QtGui.QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        MainWindow.setAccessibleName("")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 180, 30))
        self.label_2.setObjectName("label_2")
        self.second_input = QtWidgets.QLineEdit(self.centralwidget)
        self.second_input.setGeometry(QtCore.QRect(190, 50, 400, 30))
        self.second_input.setObjectName("second_input")
        self.first_input = QtWidgets.QLineEdit(self.centralwidget)
        self.first_input.setGeometry(QtCore.QRect(190, 10, 400, 30))
        self.first_input.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.first_input.setObjectName("first_input")
        self.button = QtWidgets.QPushButton(self.centralwidget)
        self.button.setGeometry(QtCore.QRect(390, 90, 200, 30))
        self.button.setObjectName("button")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 180, 30))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 130, 180, 30))
        self.label_3.setObjectName("label_3")
        self.output = QtWidgets.QLineEdit(self.centralwidget)
        self.output.setGeometry(QtCore.QRect(190, 130, 400, 30))
        self.output.setReadOnly(True)
        self.output.setObjectName("output")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 27))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Лабораторная работа 8 - Снова анаграммы"))
        self.label_2.setText(_translate("MainWindow", "Второе предложение"))
        self.button.setText(_translate("MainWindow", "Проверить на анаграмму"))
        self.label.setText(_translate("MainWindow", "Первое предложение"))
        self.label_3.setText(_translate("MainWindow", "Результат"))
