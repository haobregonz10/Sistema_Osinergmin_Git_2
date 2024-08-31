# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_transmision_subestacion_plano.ui'
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
        NewBook.resize(643, 395)
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
        self.label_nota_obligatoria = QLabel(NewBook)
        self.label_nota_obligatoria.setObjectName(u"label_nota_obligatoria")
        self.label_nota_obligatoria.setGeometry(QRect(20, 320, 281, 21))
        self.label_dni_2 = QLabel(NewBook)
        self.label_dni_2.setObjectName(u"label_dni_2")
        self.label_dni_2.setGeometry(QRect(390, 60, 91, 21))
        self.ast_aquienvisita_3 = QLabel(NewBook)
        self.ast_aquienvisita_3.setObjectName(u"ast_aquienvisita_3")
        self.ast_aquienvisita_3.setGeometry(QRect(290, 60, 21, 21))
        self.label_aquienVisita = QLabel(NewBook)
        self.label_aquienVisita.setObjectName(u"label_aquienVisita")
        self.label_aquienVisita.setGeometry(QRect(20, 60, 191, 21))
        self.label_area_2 = QLabel(NewBook)
        self.label_area_2.setObjectName(u"label_area_2")
        self.label_area_2.setGeometry(QRect(160, 60, 101, 21))
        self.tablePlano = QTableWidget(NewBook)
        self.tablePlano.setObjectName(u"tablePlano")
        self.tablePlano.setGeometry(QRect(20, 150, 601, 171))
        self.tablePlano.setAutoFillBackground(True)
        self.tablePlano.setLineWidth(5)
        self.tablePlano.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tablePlano.setTextElideMode(Qt.ElideLeft)
        self.tablePlano.horizontalHeader().setMinimumSectionSize(10)
        self.ast_aquienvisita = QLabel(NewBook)
        self.ast_aquienvisita.setObjectName(u"ast_aquienvisita")
        self.ast_aquienvisita.setGeometry(QRect(120, 60, 21, 21))
        self.btnAddPlano = QPushButton(NewBook)
        self.btnAddPlano.setObjectName(u"btnAddPlano")
        self.btnAddPlano.setGeometry(QRect(560, 120, 24, 30))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.btnAddPlano.setFont(font1)
        self.btnAddPlano.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnAddPlano.setStyleSheet(u"QPushButton\n"
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
        icon.addFile(u"./assets/icons/add-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnAddPlano.setIcon(icon)
        self.btnAddPlano.setIconSize(QSize(25, 25))
        self.btnAddPlano.setAutoDefault(True)
        self.btnAddPlano.setFlat(True)
        self.ast_aquienvisita_2 = QLabel(NewBook)
        self.ast_aquienvisita_2.setObjectName(u"ast_aquienvisita_2")
        self.ast_aquienvisita_2.setGeometry(QRect(230, 60, 21, 21))
        self.label_advertencia_dni = QLabel(NewBook)
        self.label_advertencia_dni.setObjectName(u"label_advertencia_dni")
        self.label_advertencia_dni.setGeometry(QRect(20, 320, 251, 21))
        self.btnDeletePlano = QPushButton(NewBook)
        self.btnDeletePlano.setObjectName(u"btnDeletePlano")
        self.btnDeletePlano.setGeometry(QRect(590, 120, 24, 30))
        self.btnDeletePlano.setFont(font1)
        self.btnDeletePlano.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnDeletePlano.setStyleSheet(u"QPushButton\n"
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
        icon1.addFile(u"./assets/icons/deletesquare.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnDeletePlano.setIcon(icon1)
        self.btnDeletePlano.setIconSize(QSize(25, 25))
        self.btnDeletePlano.setAutoDefault(True)
        self.btnDeletePlano.setFlat(True)
        self.label_fecha_2 = QLabel(NewBook)
        self.label_fecha_2.setObjectName(u"label_fecha_2")
        self.label_fecha_2.setGeometry(QRect(270, 60, 101, 16))
        self.label_visitante_2 = QLabel(NewBook)
        self.label_visitante_2.setObjectName(u"label_visitante_2")
        self.label_visitante_2.setGeometry(QRect(510, 60, 121, 21))
        self.inputCodigoCentral = QLineEdit(NewBook)
        self.inputCodigoCentral.setObjectName(u"inputCodigoCentral")
        self.inputCodigoCentral.setGeometry(QRect(20, 80, 131, 31))
        font2 = QFont()
        font2.setPointSize(12)
        self.inputCodigoCentral.setFont(font2)
        self.label_4 = QLabel(NewBook)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 120, 311, 30))
        self.label_4.setScaledContents(True)
        self.inputX = QLineEdit(NewBook)
        self.inputX.setObjectName(u"inputX")
        self.inputX.setGeometry(QRect(270, 80, 111, 31))
        self.inputX.setFont(font2)
        self.inputX.setInputMethodHints(Qt.ImhDigitsOnly)
        self.inputSecuencia = QLineEdit(NewBook)
        self.inputSecuencia.setObjectName(u"inputSecuencia")
        self.inputSecuencia.setGeometry(QRect(160, 80, 101, 31))
        self.inputSecuencia.setFont(font2)
        self.inputZ = QLineEdit(NewBook)
        self.inputZ.setObjectName(u"inputZ")
        self.inputZ.setGeometry(QRect(510, 80, 111, 31))
        self.inputZ.setFont(font2)
        self.ast_aquienvisita_5 = QLabel(NewBook)
        self.ast_aquienvisita_5.setObjectName(u"ast_aquienvisita_5")
        self.ast_aquienvisita_5.setGeometry(QRect(530, 60, 21, 21))
        self.ast_aquienvisita_4 = QLabel(NewBook)
        self.ast_aquienvisita_4.setObjectName(u"ast_aquienvisita_4")
        self.ast_aquienvisita_4.setGeometry(QRect(410, 60, 21, 21))
        self.inputY = QLineEdit(NewBook)
        self.inputY.setObjectName(u"inputY")
        self.inputY.setGeometry(QRect(390, 80, 111, 31))
        self.inputY.setFont(font2)
        self.inputY.setInputMethodHints(Qt.ImhDigitsOnly)
        self.cancelButton = QPushButton(NewBook)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setGeometry(QRect(180, 340, 271, 41))
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

        self.btnAddPlano.setDefault(True)
        self.btnDeletePlano.setDefault(True)
        self.cancelButton.setDefault(True)


        QMetaObject.connectSlotsByName(NewBook)
    # setupUi

    def retranslateUi(self, NewBook):
        NewBook.setWindowTitle(QCoreApplication.translate("NewBook", u"Nuevo Registro", None))
        self.label.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">SUBESTACI\u00d3N - V\u00c9RTICE PLANO DE PLANTA</span></p></body></html>", None))
        self.label_nota_obligatoria.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; font-style:italic; color:#ff0000;\">(*) Campos Obligatorios</span></p></body></html>", None))
        self.label_dni_2.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Y:</span></p></body></html>", None))
        self.ast_aquienvisita_3.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ff0000;\">*</span></p></body></html>", None))
        self.label_aquienVisita.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Subestaci\u00f3n:</span></p></body></html>", None))
        self.label_area_2.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Secuencia:</span></p></body></html>", None))
        self.ast_aquienvisita.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ff0000;\">*</span></p></body></html>", None))
        self.btnAddPlano.setText("")
        self.ast_aquienvisita_2.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ff0000;\">*</span></p></body></html>", None))
        self.label_advertencia_dni.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; font-style:italic; color:#ff0000;\">(*) Campos Obligatorios</span></p></body></html>", None))
        self.btnDeletePlano.setText("")
        self.label_fecha_2.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">X:</span></p></body></html>", None))
        self.label_visitante_2.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Z:</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Ubicaci\u00f3n dentro del Plano Planta:</span></p></body></html>", None))
        self.ast_aquienvisita_5.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ff0000;\">*</span></p></body></html>", None))
        self.ast_aquienvisita_4.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ff0000;\">*</span></p></body></html>", None))
        self.cancelButton.setText(QCoreApplication.translate("NewBook", u"Listo", None))
    # retranslateUi

