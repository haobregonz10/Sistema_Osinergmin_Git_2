# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_central_conductor.ui'
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
        NewBook.resize(712, 551)
        NewBook.setMinimumSize(QSize(712, 551))
        NewBook.setMaximumSize(QSize(10000, 10000))
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
        self.label.setGeometry(QRect(20, 10, 671, 41))
        font = QFont()
        font.setUnderline(False)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet(u"background-color: red;")
        self.label.setFrameShape(QFrame.Box)
        self.label_autoriza = QLabel(NewBook)
        self.label_autoriza.setObjectName(u"label_autoriza")
        self.label_autoriza.setGeometry(QRect(20, 70, 101, 25))
        self.inputCodigo = QLineEdit(NewBook)
        self.inputCodigo.setObjectName(u"inputCodigo")
        self.inputCodigo.setGeometry(QRect(20, 95, 111, 31))
        font1 = QFont()
        font1.setPointSize(12)
        self.inputCodigo.setFont(font1)
        self.inputCodigo.setMaxLength(15)
        self.inputCentral = QLineEdit(NewBook)
        self.inputCentral.setObjectName(u"inputCentral")
        self.inputCentral.setGeometry(QRect(140, 95, 231, 31))
        self.inputCentral.setFont(font1)
        self.addButton = QPushButton(NewBook)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setGeometry(QRect(60, 490, 271, 41))
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setWeight(75)
        self.addButton.setFont(font2)
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
        icon = QIcon()
        icon.addFile(u"./assets/icons/add-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.addButton.setIcon(icon)
        self.addButton.setIconSize(QSize(30, 30))
        self.addButton.setAutoDefault(True)
        self.addButton.setFlat(True)
        self.cancelButton = QPushButton(NewBook)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setGeometry(QRect(370, 490, 271, 41))
        self.cancelButton.setFont(font2)
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
        icon1 = QIcon()
        icon1.addFile(u"./assets/icons/cancel-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cancelButton.setIcon(icon1)
        self.cancelButton.setIconSize(QSize(30, 30))
        self.cancelButton.setAutoDefault(True)
        self.cancelButton.setFlat(True)
        self.label_aquienVisita = QLabel(NewBook)
        self.label_aquienVisita.setObjectName(u"label_aquienVisita")
        self.label_aquienVisita.setGeometry(QRect(140, 70, 191, 25))
        self.label_horaSalida = QLabel(NewBook)
        self.label_horaSalida.setObjectName(u"label_horaSalida")
        self.label_horaSalida.setGeometry(QRect(550, 70, 81, 25))
        self.label_motivoVisita = QLabel(NewBook)
        self.label_motivoVisita.setObjectName(u"label_motivoVisita")
        self.label_motivoVisita.setGeometry(QRect(20, 135, 131, 25))
        self.label_nota_obligatoria = QLabel(NewBook)
        self.label_nota_obligatoria.setObjectName(u"label_nota_obligatoria")
        self.label_nota_obligatoria.setGeometry(QRect(20, 470, 281, 21))
        self.ast_aquienvisita = QLabel(NewBook)
        self.ast_aquienvisita.setObjectName(u"ast_aquienvisita")
        self.ast_aquienvisita.setGeometry(QRect(70, 70, 21, 25))
        self.label_advertencia_dni = QLabel(NewBook)
        self.label_advertencia_dni.setObjectName(u"label_advertencia_dni")
        self.label_advertencia_dni.setGeometry(QRect(20, 470, 251, 21))
        self.cbEstado = QComboBox(NewBook)
        self.cbEstado.setObjectName(u"cbEstado")
        self.cbEstado.setGeometry(QRect(550, 95, 151, 31))
        self.cbEstado.setFont(font1)
        self.cbEstado.setEditable(False)
        self.inputFecha = QDateEdit(NewBook)
        self.inputFecha.setObjectName(u"inputFecha")
        self.inputFecha.setGeometry(QRect(20, 160, 131, 31))
        font3 = QFont()
        font3.setPointSize(11)
        font3.setBold(False)
        font3.setWeight(50)
        self.inputFecha.setFont(font3)
        self.label_autoriza_4 = QLabel(NewBook)
        self.label_autoriza_4.setObjectName(u"label_autoriza_4")
        self.label_autoriza_4.setGeometry(QRect(380, 70, 151, 25))
        self.inputTension = QLineEdit(NewBook)
        self.inputTension.setObjectName(u"inputTension")
        self.inputTension.setGeometry(QRect(380, 95, 161, 31))
        self.inputTension.setFont(font1)
        self.inputTension.setMaxLength(8)
        self.label_nota_obligatoria_2 = QLabel(NewBook)
        self.label_nota_obligatoria_2.setObjectName(u"label_nota_obligatoria_2")
        self.label_nota_obligatoria_2.setGeometry(QRect(20, 470, 281, 21))
        self.tablePlano = QTableWidget(NewBook)
        self.tablePlano.setObjectName(u"tablePlano")
        self.tablePlano.setGeometry(QRect(20, 230, 325, 233))
        self.tablePlano.setAutoFillBackground(True)
        self.tablePlano.setLineWidth(5)
        self.tablePlano.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tablePlano.setTextElideMode(Qt.ElideLeft)
        self.tablePlano.horizontalHeader().setMinimumSectionSize(10)
        self.label_5 = QLabel(NewBook)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(370, 200, 261, 30))
        self.label_5.setScaledContents(True)
        self.btnDeletePlano = QPushButton(NewBook)
        self.btnDeletePlano.setObjectName(u"btnDeletePlano")
        self.btnDeletePlano.setGeometry(QRect(320, 200, 24, 30))
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(True)
        font4.setWeight(75)
        self.btnDeletePlano.setFont(font4)
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
        icon2 = QIcon()
        icon2.addFile(u"./assets/icons/deletesquare.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnDeletePlano.setIcon(icon2)
        self.btnDeletePlano.setIconSize(QSize(25, 25))
        self.btnDeletePlano.setAutoDefault(True)
        self.btnDeletePlano.setFlat(True)
        self.btnAddPlano = QPushButton(NewBook)
        self.btnAddPlano.setObjectName(u"btnAddPlano")
        self.btnAddPlano.setGeometry(QRect(290, 200, 24, 30))
        self.btnAddPlano.setFont(font4)
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
        self.btnAddPlano.setIcon(icon)
        self.btnAddPlano.setIconSize(QSize(25, 25))
        self.btnAddPlano.setAutoDefault(True)
        self.btnAddPlano.setFlat(True)
        self.label_advertencia_dni_2 = QLabel(NewBook)
        self.label_advertencia_dni_2.setObjectName(u"label_advertencia_dni_2")
        self.label_advertencia_dni_2.setGeometry(QRect(20, 470, 251, 21))
        self.btnAddEsquema = QPushButton(NewBook)
        self.btnAddEsquema.setObjectName(u"btnAddEsquema")
        self.btnAddEsquema.setGeometry(QRect(640, 200, 24, 30))
        self.btnAddEsquema.setFont(font4)
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
        self.btnAddEsquema.setIcon(icon)
        self.btnAddEsquema.setIconSize(QSize(25, 25))
        self.btnAddEsquema.setAutoDefault(True)
        self.btnAddEsquema.setFlat(True)
        self.label_4 = QLabel(NewBook)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 200, 231, 30))
        self.label_4.setScaledContents(True)
        self.btnDeleteEsquema = QPushButton(NewBook)
        self.btnDeleteEsquema.setObjectName(u"btnDeleteEsquema")
        self.btnDeleteEsquema.setGeometry(QRect(670, 200, 24, 30))
        self.btnDeleteEsquema.setFont(font4)
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
        self.btnDeleteEsquema.setIcon(icon2)
        self.btnDeleteEsquema.setIconSize(QSize(25, 25))
        self.btnDeleteEsquema.setAutoDefault(True)
        self.btnDeleteEsquema.setFlat(True)
        self.tableEsquema = QTableWidget(NewBook)
        self.tableEsquema.setObjectName(u"tableEsquema")
        self.tableEsquema.setGeometry(QRect(370, 230, 325, 233))
        self.tableEsquema.setAutoFillBackground(True)
        self.tableEsquema.setLineWidth(5)
        self.tableEsquema.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableEsquema.setTextElideMode(Qt.ElideLeft)
        self.tableEsquema.horizontalHeader().setMinimumSectionSize(10)
        self.inputCodEmpresa = QLineEdit(NewBook)
        self.inputCodEmpresa.setObjectName(u"inputCodEmpresa")
        self.inputCodEmpresa.setGeometry(QRect(160, 160, 121, 31))
        self.inputCodEmpresa.setFont(font1)
        self.inputCodEmpresa.setMaxLength(5)
        self.label_empresa = QLabel(NewBook)
        self.label_empresa.setObjectName(u"label_empresa")
        self.label_empresa.setGeometry(QRect(160, 135, 111, 21))
        self.label_empresa.setScaledContents(True)
        QWidget.setTabOrder(self.inputCodigo, self.inputCentral)
        QWidget.setTabOrder(self.inputCentral, self.addButton)
        QWidget.setTabOrder(self.addButton, self.cancelButton)

        self.retranslateUi(NewBook)

        self.addButton.setDefault(True)
        self.cancelButton.setDefault(True)
        self.btnDeletePlano.setDefault(True)
        self.btnAddPlano.setDefault(True)
        self.btnAddEsquema.setDefault(True)
        self.btnDeleteEsquema.setDefault(True)


        QMetaObject.connectSlotsByName(NewBook)
    # setupUi

    def retranslateUi(self, NewBook):
        NewBook.setWindowTitle(QCoreApplication.translate("NewBook", u"Nuevo Registro", None))
        self.label.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">CONDUCTOR</span></p></body></html>", None))
        self.label_autoriza.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Codigo:</span></p></body></html>", None))
        self.addButton.setText(QCoreApplication.translate("NewBook", u"AGREGAR", None))
        self.cancelButton.setText(QCoreApplication.translate("NewBook", u"CANCELAR", None))
        self.label_aquienVisita.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Central:</span></p></body></html>", None))
        self.label_horaSalida.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Estado:</span></p></body></html>", None))
        self.label_motivoVisita.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Fecha de Alta:</span></p></body></html>", None))
        self.label_nota_obligatoria.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; font-style:italic; color:#ff0000;\">(*) El c\u00f3digo es obligatorio</span></p></body></html>", None))
        self.ast_aquienvisita.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ff0000;\">*</span></p></body></html>", None))
        self.label_advertencia_dni.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; font-style:italic; color:#ff0000;\">(*) El c\u00f3digo es obligatorio</span></p></body></html>", None))
        self.label_autoriza_4.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Tensi\u00f3n Nominal:</span></p></body></html>", None))
        self.label_nota_obligatoria_2.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; font-style:italic; color:#ff0000;\">(*) El c\u00f3digo es obligatorio</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Ubicaci\u00f3n Esquema:</span></p></body></html>", None))
        self.btnDeletePlano.setText("")
        self.btnAddPlano.setText("")
        self.label_advertencia_dni_2.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; font-style:italic; color:#ff0000;\">(*) El c\u00f3digo es obligatorio</span></p></body></html>", None))
        self.btnAddEsquema.setText("")
        self.label_4.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Ubicaci\u00f3n dentro del Plano Planta::</span></p></body></html>", None))
        self.btnDeleteEsquema.setText("")
        self.label_empresa.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Empresa:</span></p></body></html>", None))
    # retranslateUi

