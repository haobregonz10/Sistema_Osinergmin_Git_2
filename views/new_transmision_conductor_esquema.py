# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_transmision_conductor_esquema.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_NewBook(object):
    def setupUi(self, NewBook):
        if not NewBook.objectName():
            NewBook.setObjectName(u"NewBook")
        NewBook.resize(657, 201)
        NewBook.setStyleSheet(u"QPushButton\n"
"{	\n"
"	height: 2em;\n"
" 	border-style: solid;\n"
"	border-width: 2px;\n"
" 	border-color: grey;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   	background-color:grey;\n"
"	color:white;\n"
"}")
        self.label = QLabel(NewBook)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 621, 41))
        font = QFont()
        font.setUnderline(False)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet(u"background-color: red;")
        self.label.setFrameShape(QFrame.Box)
        self.label_area_2 = QLabel(NewBook)
        self.label_area_2.setObjectName(u"label_area_2")
        self.label_area_2.setGeometry(QRect(140, 65, 171, 21))
        self.cancelButton = QPushButton(NewBook)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setGeometry(QRect(340, 140, 271, 41))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setWeight(75)
        self.cancelButton.setFont(font1)
        self.cancelButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.cancelButton.setStyleSheet(u"QPushButton\n"
"{	\n"
"	height: 2em;\n"
" 	border-style: solid;\n"
"	border-width: 2px;\n"
" 	border-color: grey;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   	background-color:grey;\n"
"	color:white;\n"
"}")
        icon = QIcon()
        icon.addFile(u"./assets/icons/cancel-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cancelButton.setIcon(icon)
        self.cancelButton.setIconSize(QSize(30, 30))
        self.cancelButton.setAutoDefault(True)
        self.cancelButton.setFlat(True)
        self.inputBarra = QLineEdit(NewBook)
        self.inputBarra.setObjectName(u"inputBarra")
        self.inputBarra.setGeometry(QRect(140, 90, 161, 31))
        font2 = QFont()
        font2.setPointSize(12)
        self.inputBarra.setFont(font2)
        self.label_autoriza = QLabel(NewBook)
        self.label_autoriza.setObjectName(u"label_autoriza")
        self.label_autoriza.setGeometry(QRect(20, 65, 101, 21))
        self.inputCodigo = QLineEdit(NewBook)
        self.inputCodigo.setObjectName(u"inputCodigo")
        self.inputCodigo.setGeometry(QRect(20, 90, 111, 31))
        self.inputCodigo.setFont(font2)
        self.label_horaSalida_3 = QLabel(NewBook)
        self.label_horaSalida_3.setObjectName(u"label_horaSalida_3")
        self.label_horaSalida_3.setGeometry(QRect(550, 65, 81, 25))
        self.inputY = QLineEdit(NewBook)
        self.inputY.setObjectName(u"inputY")
        self.inputY.setGeometry(QRect(550, 90, 91, 31))
        self.inputY.setFont(font2)
        self.inputY.setMaxLength(14)
        self.label_motivoVisita_3 = QLabel(NewBook)
        self.label_motivoVisita_3.setObjectName(u"label_motivoVisita_3")
        self.label_motivoVisita_3.setGeometry(QRect(310, 65, 101, 25))
        self.label_horaIngreso_3 = QLabel(NewBook)
        self.label_horaIngreso_3.setObjectName(u"label_horaIngreso_3")
        self.label_horaIngreso_3.setGeometry(QRect(450, 65, 71, 25))
        self.inputX = QLineEdit(NewBook)
        self.inputX.setObjectName(u"inputX")
        self.inputX.setGeometry(QRect(450, 90, 91, 31))
        self.inputX.setFont(font2)
        self.inputX.setMaxLength(14)
        self.inputSecuencia = QLineEdit(NewBook)
        self.inputSecuencia.setObjectName(u"inputSecuencia")
        self.inputSecuencia.setGeometry(QRect(310, 90, 131, 31))
        self.inputSecuencia.setFont(font2)
        self.addButton = QPushButton(NewBook)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setGeometry(QRect(40, 140, 291, 41))
        self.addButton.setFont(font1)
        self.addButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.addButton.setStyleSheet(u"QPushButton\n"
"{	\n"
"	height: 2em;\n"
" 	border-style: solid;\n"
"	border-width: 2px;\n"
" 	border-color: #0069c0;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   	background-color:#0069c0;\n"
"	color:white;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"./assets/icons/add-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.addButton.setIcon(icon1)
        self.addButton.setIconSize(QSize(30, 30))
        self.addButton.setAutoDefault(True)
        self.addButton.setFlat(True)

        self.retranslateUi(NewBook)

        self.cancelButton.setDefault(True)
        self.addButton.setDefault(True)


        QMetaObject.connectSlotsByName(NewBook)
    # setupUi

    def retranslateUi(self, NewBook):
        NewBook.setWindowTitle(QCoreApplication.translate("NewBook", u"Nuevo Registro", None))
        self.label.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">CONDUCTOR- UBICACI\u00d3N ESQUEMA</span></p></body></html>", None))
        self.label_area_2.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Conductor:</span></p></body></html>", None))
        self.cancelButton.setText(QCoreApplication.translate("NewBook", u"CANCELAR", None))
        self.label_autoriza.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Subestaci\u00f3n:</span></p></body></html>", None))
        self.label_horaSalida_3.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Y:</span></p></body></html>", None))
        self.label_motivoVisita_3.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Secuencia:</span></p></body></html>", None))
        self.label_horaIngreso_3.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">X:</span></p></body></html>", None))
        self.addButton.setText(QCoreApplication.translate("NewBook", u"AGREGAR", None))
    # retranslateUi

