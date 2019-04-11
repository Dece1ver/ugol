# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ugol.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(810, 581)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 9, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_frame.sizePolicy().hasHeightForWidth())
        self.label_frame.setSizePolicy(sizePolicy)
        self.label_frame.setMinimumSize(QtCore.QSize(0, 60))
        self.label_frame.setMaximumSize(QtCore.QSize(16777215, 60))
        self.label_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_frame.setObjectName("label_frame")
        self.label = QtWidgets.QLabel(self.label_frame)
        self.label.setGeometry(QtCore.QRect(6, 0, 791, 60))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 60))
        self.label.setMaximumSize(QtCore.QSize(16777215, 60))
        self.label.setStyleSheet("font: 8pt \"Century Gothic\";")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label_frame, 0, 0, 1, 2)
        self.data_frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.data_frame.sizePolicy().hasHeightForWidth())
        self.data_frame.setSizePolicy(sizePolicy)
        self.data_frame.setMaximumSize(QtCore.QSize(210, 16777215))
        self.data_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.data_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.data_frame.setObjectName("data_frame")
        self.data_box = QtWidgets.QGroupBox(self.data_frame)
        self.data_box.setGeometry(QtCore.QRect(10, 0, 191, 181))
        self.data_box.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.data_box.setFlat(False)
        self.data_box.setCheckable(False)
        self.data_box.setObjectName("data_box")
        self.diameter_label = QtWidgets.QLabel(self.data_box)
        self.diameter_label.setGeometry(QtCore.QRect(6, 30, 181, 31))
        self.diameter_label.setStyleSheet("font: 14pt \"Century Gothic\";")
        self.diameter_label.setObjectName("diameter_label")
        self.diameter_input = QtWidgets.QLineEdit(self.data_box)
        self.diameter_input.setGeometry(QtCore.QRect(10, 60, 51, 31))
        self.diameter_input.setStyleSheet("font: 14pt \"Century Gothic\";")
        self.diameter_input.setText("")
        self.diameter_input.setObjectName("diameter_input")
        self.diameter_label_2 = QtWidgets.QLabel(self.data_box)
        self.diameter_label_2.setGeometry(QtCore.QRect(60, 60, 41, 31))
        self.diameter_label_2.setStyleSheet("font: 14pt \"Century Gothic\";")
        self.diameter_label_2.setObjectName("diameter_label_2")
        self.step_input = QtWidgets.QLineEdit(self.data_box)
        self.step_input.setGeometry(QtCore.QRect(10, 130, 51, 31))
        self.step_input.setStyleSheet("font: 14pt \"Century Gothic\";")
        self.step_input.setText("")
        self.step_input.setObjectName("step_input")
        self.step_label_2 = QtWidgets.QLabel(self.data_box)
        self.step_label_2.setGeometry(QtCore.QRect(60, 130, 41, 31))
        self.step_label_2.setStyleSheet("font: 14pt \"Century Gothic\";")
        self.step_label_2.setObjectName("step_label_2")
        self.step_label = QtWidgets.QLabel(self.data_box)
        self.step_label.setGeometry(QtCore.QRect(6, 100, 171, 31))
        self.step_label.setStyleSheet("font: 14pt \"Century Gothic\";")
        self.step_label.setObjectName("step_label")
        self.data_box_2 = QtWidgets.QGroupBox(self.data_frame)
        self.data_box_2.setGeometry(QtCore.QRect(10, 190, 191, 181))
        self.data_box_2.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.data_box_2.setObjectName("data_box_2")
        self.diameter_label_3 = QtWidgets.QLabel(self.data_box_2)
        self.diameter_label_3.setGeometry(QtCore.QRect(6, 30, 181, 31))
        self.diameter_label_3.setStyleSheet("font: 14pt \"Century Gothic\";")
        self.diameter_label_3.setObjectName("diameter_label_3")
        self.diameter_input_2 = QtWidgets.QLineEdit(self.data_box_2)
        self.diameter_input_2.setEnabled(False)
        self.diameter_input_2.setGeometry(QtCore.QRect(10, 60, 51, 31))
        self.diameter_input_2.setStyleSheet("font: 14pt \"Century Gothic\";")
        self.diameter_input_2.setText("")
        self.diameter_input_2.setObjectName("diameter_input_2")
        self.diameter_label_4 = QtWidgets.QLabel(self.data_box_2)
        self.diameter_label_4.setGeometry(QtCore.QRect(65, 60, 31, 31))
        self.diameter_label_4.setStyleSheet("font: 14pt \"Century Gothic\";")
        self.diameter_label_4.setObjectName("diameter_label_4")
        self.step_input_2 = QtWidgets.QLineEdit(self.data_box_2)
        self.step_input_2.setEnabled(False)
        self.step_input_2.setGeometry(QtCore.QRect(10, 130, 51, 31))
        self.step_input_2.setStyleSheet("font: 14pt \"Century Gothic\";")
        self.step_input_2.setText("")
        self.step_input_2.setObjectName("step_input_2")
        self.step_label_3 = QtWidgets.QLabel(self.data_box_2)
        self.step_label_3.setGeometry(QtCore.QRect(65, 130, 41, 31))
        self.step_label_3.setStyleSheet("font: 14pt \"Century Gothic\";")
        self.step_label_3.setObjectName("step_label_3")
        self.step_label_4 = QtWidgets.QLabel(self.data_box_2)
        self.step_label_4.setGeometry(QtCore.QRect(6, 100, 171, 31))
        self.step_label_4.setStyleSheet("font: 14pt \"Century Gothic\";")
        self.step_label_4.setObjectName("step_label_4")
        self.gridLayout.addWidget(self.data_frame, 1, 0, 1, 1)
        self.widget_frame = QtWidgets.QFrame(self.centralwidget)
        self.widget_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.widget_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.widget_frame.setLineWidth(1)
        self.widget_frame.setMidLineWidth(0)
        self.widget_frame.setObjectName("widget_frame")
        self.widget = QtWidgets.QWidget(self.widget_frame)
        self.widget.setGeometry(QtCore.QRect(-1, -1, 591, 441))
        self.widget.setObjectName("widget")
        self.gridLayout.addWidget(self.widget_frame, 1, 1, 1, 1)
        self.button_frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_frame.sizePolicy().hasHeightForWidth())
        self.button_frame.setSizePolicy(sizePolicy)
        self.button_frame.setMinimumSize(QtCore.QSize(0, 60))
        self.button_frame.setMaximumSize(QtCore.QSize(16777215, 60))
        self.button_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.button_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.button_frame.setObjectName("button_frame")
        self.pushButton = QtWidgets.QPushButton(self.button_frame)
        self.pushButton.setGeometry(QtCore.QRect(290, 10, 221, 41))
        self.pushButton.setStyleSheet("font: 14pt \"Century Gothic\";")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.button_frame, 2, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt;\">Выбор опорной пластины</span></p></body></html>"))
        self.data_box.setTitle(_translate("MainWindow", "Параметры"))
        self.diameter_label.setText(_translate("MainWindow", "<html><head/><body><p>Диаметр резьбы:</p></body></html>"))
        self.diameter_label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">мм</p></body></html>"))
        self.step_label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">мм</p></body></html>"))
        self.step_label.setText(_translate("MainWindow", "<html><head/><body><p>Шаг резьбы:</p></body></html>"))
        self.data_box_2.setTitle(_translate("MainWindow", "Расчеты"))
        self.diameter_label_3.setText(_translate("MainWindow", "<html><head/><body><p>Угол подъема:</p></body></html>"))
        self.diameter_label_4.setText(_translate("MainWindow", "<html><head/><body><p>°</p></body></html>"))
        self.step_label_3.setText(_translate("MainWindow", "<html><head/><body><p>°</p></body></html>"))
        self.step_label_4.setText(_translate("MainWindow", "<html><head/><body><p>Пластина:</p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Рассчитать"))
