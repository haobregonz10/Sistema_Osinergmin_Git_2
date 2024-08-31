# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_central_celda_ubicacion_esquema.ui'
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
        NewBook.resize(652, 402)
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
        self.label.setGeometry(QRect(20, 10, 611, 41))
        font = QFont()
        font.setUnderline(False)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet(u"background-color: red;")
        self.label.setFrameShape(QFrame.Box)
        self.inputX = QLineEdit(NewBook)
        self.inputX.setObjectName(u"inputX")
        self.inputX.setGeometry(QRect(440, 90, 91, 31))
        font1 = QFont()
        font1.setPointSize(12)
        self.inputX.setFont(font1)
        self.inputX.setMaxLength(14)
        self.inputCodigo = QLineEdit(NewBook)
        self.inputCodigo.setObjectName(u"inputCodigo")
        self.inputCodigo.setGeometry(QRect(20, 90, 131, 31))
        self.inputCodigo.setFont(font1)
        self.label_area_2 = QLabel(NewBook)
        self.label_area_2.setObjectName(u"label_area_2")
        self.label_area_2.setGeometry(QRect(160, 70, 151, 21))
        self.label_autoriza = QLabel(NewBook)
        self.label_autoriza.setObjectName(u"label_autoriza")
        self.label_autoriza.setGeometry(QRect(20, 70, 101, 21))
        self.inputY = QLineEdit(NewBook)
        self.inputY.setObjectName(u"inputY")
        self.inputY.setGeometry(QRect(540, 90, 91, 31))
        self.inputY.setFont(font1)
        self.inputY.setMaxLength(14)
        self.inputCelda = QLineEdit(NewBook)
        self.inputCelda.setObjectName(u"inputCelda")
        self.inputCelda.setGeometry(QRect(160, 90, 151, 31))
        self.inputCelda.setFont(font1)
        self.label_motivoVisita_4 = QLabel(NewBook)
        self.label_motivoVisita_4.setObjectName(u"label_motivoVisita_4")
        self.label_motivoVisita_4.setGeometry(QRect(320, 70, 111, 25))
        self.label_horaIngreso_3 = QLabel(NewBook)
        self.label_horaIngreso_3.setObjectName(u"label_horaIngreso_3")
        self.label_horaIngreso_3.setGeometry(QRect(440, 70, 71, 25))
        self.inputSecuencia = QLineEdit(NewBook)
        self.inputSecuencia.setObjectName(u"inputSecuencia")
        self.inputSecuencia.setGeometry(QRect(320, 90, 111, 31))
        self.inputSecuencia.setFont(font1)
        self.label_horaSalida_3 = QLabel(NewBook)
        self.label_horaSalida_3.setObjectName(u"label_horaSalida_3")
        self.label_horaSalida_3.setGeometry(QRect(540, 70, 81, 25))
        self.tableEsquema = QTableWidget(NewBook)
        self.tableEsquema.setObjectName(u"tableEsquema")
        self.tableEsquema.setGeometry(QRect(20, 160, 611, 171))
        self.tableEsquema.setAutoFillBackground(True)
        self.tableEsquema.setLineWidth(5)
        self.tableEsquema.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableEsquema.setTextElideMode(Qt.ElideLeft)
        self.tableEsquema.horizontalHeader().setMinimumSectionSize(10)
        self.btnDeleteEsquema = QPushButton(NewBook)
        self.btnDeleteEsquema.setObjectName(u"btnDeleteEsquema")
        self.btnDeleteEsquema.setGeometry(QRect(600, 130, 24, 30))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setWeight(75)
        self.btnDeleteEsquema.setFont(font2)
        self.btnDeleteEsquema.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnDeleteEsquema.setStyleSheet(u"QPushButton\n"
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
        icon = QIcon()
        icon.addFile(u"./assets/icons/deletesquare.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnDeleteEsquema.setIcon(icon)
        self.btnDeleteEsquema.setIconSize(QSize(25, 25))
        self.btnDeleteEsquema.setAutoDefault(True)
        self.btnDeleteEsquema.setFlat(True)
        self.label_4 = QLabel(NewBook)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 130, 311, 30))
        self.label_4.setScaledContents(True)
        self.btnAddEsquema = QPushButton(NewBook)
        self.btnAddEsquema.setObjectName(u"btnAddEsquema")
        self.btnAddEsquema.setGeometry(QRect(570, 130, 24, 30))
        self.btnAddEsquema.setFont(font2)
        self.btnAddEsquema.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnAddEsquema.setStyleSheet(u"QPushButton\n"
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
        self.btnAddEsquema.setIcon(icon1)
        self.btnAddEsquema.setIconSize(QSize(25, 25))
        self.btnAddEsquema.setAutoDefault(True)
        self.btnAddEsquema.setFlat(True)
        self.cancelButton = QPushButton(NewBook)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setGeometry(QRect(190, 340, 271, 41))
        font3 = QFont()
        font3.setPointSize(14)
        font3.setBold(True)
        font3.setWeight(75)
        self.cancelButton.setFont(font3)
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
        icon2 = QIcon()
        icon2.addFile(u"./assets/icons/exitoso.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cancelButton.setIcon(icon2)
        self.cancelButton.setIconSize(QSize(30, 30))
        self.cancelButton.setAutoDefault(True)
        self.cancelButton.setFlat(True)

        self.retranslateUi(NewBook)

        self.btnDeleteEsquema.setDefault(True)
        self.btnAddEsquema.setDefault(True)
        self.cancelButton.setDefault(True)


        QMetaObject.connectSlotsByName(NewBook)
    # setupUi

    def retranslateUi(self, NewBook):
        NewBook.setWindowTitle(QCoreApplication.translate("NewBook", u"Nuevo Registro", None))
        self.label.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">CELDA UBICACI\u00d3N ESQUEMA</span></p></body></html>", None))
        self.label_area_2.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Celda:</span></p></body></html>", None))
        self.label_autoriza.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Central:</span></p></body></html>", None))
        self.label_motivoVisita_4.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Secuencia:</span></p></body></html>", None))
        self.label_horaIngreso_3.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">X:</span></p></body></html>", None))
        self.label_horaSalida_3.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Y:</span></p></body></html>", None))
        self.btnDeleteEsquema.setText("")
        self.label_4.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Ubicaci\u00f3n Esquema:</span></p></body></html>", None))
        self.btnAddEsquema.setText("")
        self.cancelButton.setText(QCoreApplication.translate("NewBook", u"Listo", None))
    # retranslateUi

