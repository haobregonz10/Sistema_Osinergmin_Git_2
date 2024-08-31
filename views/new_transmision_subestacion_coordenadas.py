# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_transmision_subestacion_coordenadas.ui'
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
        NewBook.resize(647, 409)
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
        self.label.setGeometry(QRect(20, 10, 601, 41))
        font = QFont()
        font.setUnderline(False)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet(u"background-color: red;")
        self.label.setFrameShape(QFrame.Box)
        self.label_dni_2 = QLabel(NewBook)
        self.label_dni_2.setObjectName(u"label_dni_2")
        self.label_dni_2.setGeometry(QRect(390, 60, 91, 21))
        self.label_advertencia_dni = QLabel(NewBook)
        self.label_advertencia_dni.setObjectName(u"label_advertencia_dni")
        self.label_advertencia_dni.setGeometry(QRect(20, 320, 251, 21))
        self.btnDeleteEsquema = QPushButton(NewBook)
        self.btnDeleteEsquema.setObjectName(u"btnDeleteEsquema")
        self.btnDeleteEsquema.setGeometry(QRect(590, 120, 24, 30))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.btnDeleteEsquema.setFont(font1)
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
        self.btnAddEsquema = QPushButton(NewBook)
        self.btnAddEsquema.setObjectName(u"btnAddEsquema")
        self.btnAddEsquema.setGeometry(QRect(560, 120, 24, 30))
        self.btnAddEsquema.setFont(font1)
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
        self.ast_aquienvisita_2 = QLabel(NewBook)
        self.ast_aquienvisita_2.setObjectName(u"ast_aquienvisita_2")
        self.ast_aquienvisita_2.setGeometry(QRect(230, 60, 21, 21))
        self.inputX = QLineEdit(NewBook)
        self.inputX.setObjectName(u"inputX")
        self.inputX.setGeometry(QRect(270, 80, 111, 31))
        font2 = QFont()
        font2.setPointSize(12)
        self.inputX.setFont(font2)
        self.inputX.setInputMethodHints(Qt.ImhDigitsOnly)
        self.label_visitante_2 = QLabel(NewBook)
        self.label_visitante_2.setObjectName(u"label_visitante_2")
        self.label_visitante_2.setGeometry(QRect(510, 60, 121, 21))
        self.tableEsquema = QTableWidget(NewBook)
        self.tableEsquema.setObjectName(u"tableEsquema")
        self.tableEsquema.setGeometry(QRect(20, 150, 601, 171))
        self.tableEsquema.setAutoFillBackground(True)
        self.tableEsquema.setLineWidth(5)
        self.tableEsquema.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableEsquema.setTextElideMode(Qt.ElideLeft)
        self.tableEsquema.horizontalHeader().setMinimumSectionSize(10)
        self.label_fecha_2 = QLabel(NewBook)
        self.label_fecha_2.setObjectName(u"label_fecha_2")
        self.label_fecha_2.setGeometry(QRect(270, 60, 101, 16))
        self.inputSecuencia = QLineEdit(NewBook)
        self.inputSecuencia.setObjectName(u"inputSecuencia")
        self.inputSecuencia.setGeometry(QRect(160, 80, 101, 31))
        self.inputSecuencia.setFont(font2)
        self.ast_aquienvisita_4 = QLabel(NewBook)
        self.ast_aquienvisita_4.setObjectName(u"ast_aquienvisita_4")
        self.ast_aquienvisita_4.setGeometry(QRect(410, 60, 21, 21))
        self.ast_aquienvisita_3 = QLabel(NewBook)
        self.ast_aquienvisita_3.setObjectName(u"ast_aquienvisita_3")
        self.ast_aquienvisita_3.setGeometry(QRect(290, 60, 21, 21))
        self.label_4 = QLabel(NewBook)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 120, 311, 30))
        self.label_4.setScaledContents(True)
        self.ast_aquienvisita_5 = QLabel(NewBook)
        self.ast_aquienvisita_5.setObjectName(u"ast_aquienvisita_5")
        self.ast_aquienvisita_5.setGeometry(QRect(530, 60, 21, 21))
        self.label_nota_obligatoria = QLabel(NewBook)
        self.label_nota_obligatoria.setObjectName(u"label_nota_obligatoria")
        self.label_nota_obligatoria.setGeometry(QRect(20, 320, 281, 21))
        self.ast_aquienvisita = QLabel(NewBook)
        self.ast_aquienvisita.setObjectName(u"ast_aquienvisita")
        self.ast_aquienvisita.setGeometry(QRect(120, 60, 21, 21))
        self.label_area_2 = QLabel(NewBook)
        self.label_area_2.setObjectName(u"label_area_2")
        self.label_area_2.setGeometry(QRect(160, 60, 101, 21))
        self.inputCodigoCentral = QLineEdit(NewBook)
        self.inputCodigoCentral.setObjectName(u"inputCodigoCentral")
        self.inputCodigoCentral.setGeometry(QRect(20, 80, 131, 31))
        self.inputCodigoCentral.setFont(font2)
        self.inputY = QLineEdit(NewBook)
        self.inputY.setObjectName(u"inputY")
        self.inputY.setGeometry(QRect(390, 80, 111, 31))
        self.inputY.setFont(font2)
        self.inputY.setInputMethodHints(Qt.ImhDigitsOnly)
        self.label_aquienVisita = QLabel(NewBook)
        self.label_aquienVisita.setObjectName(u"label_aquienVisita")
        self.label_aquienVisita.setGeometry(QRect(20, 60, 131, 21))
        self.inputZ = QLineEdit(NewBook)
        self.inputZ.setObjectName(u"inputZ")
        self.inputZ.setGeometry(QRect(510, 80, 111, 31))
        self.inputZ.setFont(font2)
        self.cancelButton = QPushButton(NewBook)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setGeometry(QRect(190, 350, 271, 41))
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
        self.label.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">SUBESTACI\u00d3N - V\u00c9RTICE COORDENADAS GEOGR\u00c1FICAS</span></p></body></html>", None))
        self.label_dni_2.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Y:</span></p></body></html>", None))
        self.label_advertencia_dni.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; font-style:italic; color:#ff0000;\">(*) Campos Obligatorios</span></p></body></html>", None))
        self.btnDeleteEsquema.setText("")
        self.btnAddEsquema.setText("")
        self.ast_aquienvisita_2.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ff0000;\">*</span></p></body></html>", None))
        self.label_visitante_2.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Z:</span></p></body></html>", None))
        self.label_fecha_2.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">X:</span></p></body></html>", None))
        self.ast_aquienvisita_4.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ff0000;\">*</span></p></body></html>", None))
        self.ast_aquienvisita_3.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ff0000;\">*</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Ubicaci\u00f3n Coordenadas Geogr\u00e1ficas:</span></p></body></html>", None))
        self.ast_aquienvisita_5.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ff0000;\">*</span></p></body></html>", None))
        self.label_nota_obligatoria.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; font-style:italic; color:#ff0000;\">(*) Campos Obligatorios</span></p></body></html>", None))
        self.ast_aquienvisita.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ff0000;\">*</span></p></body></html>", None))
        self.label_area_2.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Secuencia:</span></p></body></html>", None))
        self.label_aquienVisita.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Subestaci\u00f3n:</span></p></body></html>", None))
        self.cancelButton.setText(QCoreApplication.translate("NewBook", u"Listo", None))
    # retranslateUi

