# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ex5.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(443, 509)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.CB_delete_word_less_than = QtWidgets.QCheckBox(self.centralwidget)
        self.CB_delete_word_less_than.setGeometry(QtCore.QRect(20, 70, 191, 41))
        self.CB_delete_word_less_than.setObjectName("CB_delete_word_less_than")
        self.CB_replace_nums_by_stars = QtWidgets.QCheckBox(self.centralwidget)
        self.CB_replace_nums_by_stars.setGeometry(QtCore.QRect(20, 110, 241, 41))
        self.CB_replace_nums_by_stars.setObjectName("CB_replace_nums_by_stars")
        self.CB_sort = QtWidgets.QCheckBox(self.centralwidget)
        self.CB_sort.setGeometry(QtCore.QRect(20, 190, 241, 41))
        self.CB_sort.setObjectName("CB_sort")
        self.CB_enter_spaces = QtWidgets.QCheckBox(self.centralwidget)
        self.CB_enter_spaces.setGeometry(QtCore.QRect(20, 150, 241, 41))
        self.CB_enter_spaces.setObjectName("CB_enter_spaces")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 390, 421, 31))
        self.label.setStyleSheet("color: #d6e810;\n"
"background-color: #242422;\n"
"border: none;")
        self.label.setObjectName("label")
        self.Button_Formate = QtWidgets.QPushButton(self.centralwidget)
        self.Button_Formate.setGeometry(QtCore.QRect(130, 300, 171, 41))
        self.Button_Formate.setObjectName("Button_Formate")
        self.RB_sort_size = QtWidgets.QRadioButton(self.centralwidget)
        self.RB_sort_size.setEnabled(False)
        self.RB_sort_size.setGeometry(QtCore.QRect(80, 230, 171, 21))
        self.RB_sort_size.setObjectName("RB_sort_size")
        self.RB_sort_lex = QtWidgets.QRadioButton(self.centralwidget)
        self.RB_sort_lex.setEnabled(False)
        self.RB_sort_lex.setGeometry(QtCore.QRect(80, 260, 171, 21))
        self.RB_sort_lex.setObjectName("RB_sort_lex")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(210, 80, 42, 22))
        self.spinBox.setMaximum(25)
        self.spinBox.setObjectName("spinBox")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(260, 80, 51, 21))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 29, 371, 21))
        self.lineEdit.setStyleSheet("color: #71d6e3;\n"
"background-color: #3b3d3d;\n"
"border: none;")
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 443, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "StringFormatter"))
        self.CB_delete_word_less_than.setText(_translate("MainWindow", "Удалить слова размером меньше "))
        self.CB_replace_nums_by_stars.setText(_translate("MainWindow", "Заменить все цифры на * (звёздочку)"))
        self.CB_sort.setText(_translate("MainWindow", "Сортировать слова в строке"))
        self.CB_enter_spaces.setText(_translate("MainWindow", "Вставить по пробелу между символами"))
        self.label.setText(_translate("MainWindow", "some text"))
        self.Button_Formate.setText(_translate("MainWindow", "ФОРМАТИРОВАТЬ"))
        self.RB_sort_size.setText(_translate("MainWindow", "По размеру"))
        self.RB_sort_lex.setText(_translate("MainWindow", "Лексикографически"))
        self.label_2.setText(_translate("MainWindow", "букв"))
