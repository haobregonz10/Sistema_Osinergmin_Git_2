# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_transmision_linea.ui'
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
        NewBook.resize(897, 498)
        NewBook.setMinimumSize(QSize(897, 498))
        NewBook.setMaximumSize(QSize(897, 498))
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
        self.label.setGeometry(QRect(20, 10, 861, 41))
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
        self.inputCodigo.setGeometry(QRect(20, 95, 91, 31))
        font1 = QFont()
        font1.setPointSize(12)
        self.inputCodigo.setFont(font1)
        self.inputCodigo.setMaxLength(10)
        self.inputNombre = QLineEdit(NewBook)
        self.inputNombre.setObjectName(u"inputNombre")
        self.inputNombre.setGeometry(QRect(120, 95, 291, 31))
        self.inputNombre.setFont(font1)
        self.inputNombre.setMaxLength(60)
        self.addButton = QPushButton(NewBook)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setGeometry(QRect(150, 440, 291, 41))
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
        self.cancelButton.setGeometry(QRect(460, 440, 271, 41))
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
        self.label_aquienVisita.setGeometry(QRect(120, 70, 191, 25))
        self.label_4 = QLabel(NewBook)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 220, 191, 21))
        self.label_nota_obligatoria = QLabel(NewBook)
        self.label_nota_obligatoria.setObjectName(u"label_nota_obligatoria")
        self.label_nota_obligatoria.setGeometry(QRect(20, 420, 281, 21))
        self.ast_aquienvisita = QLabel(NewBook)
        self.ast_aquienvisita.setObjectName(u"ast_aquienvisita")
        self.ast_aquienvisita.setGeometry(QRect(70, 70, 21, 25))
        self.label_advertencia_dni = QLabel(NewBook)
        self.label_advertencia_dni.setObjectName(u"label_advertencia_dni")
        self.label_advertencia_dni.setGeometry(QRect(20, 420, 251, 21))
        self.cbTipo = QComboBox(NewBook)
        self.cbTipo.setObjectName(u"cbTipo")
        self.cbTipo.setGeometry(QRect(420, 95, 121, 31))
        self.cbTipo.setFont(font1)
        self.cbTipo.setEditable(False)
        self.label_area_2 = QLabel(NewBook)
        self.label_area_2.setObjectName(u"label_area_2")
        self.label_area_2.setGeometry(QRect(420, 70, 61, 25))
        self.label_area_3 = QLabel(NewBook)
        self.label_area_3.setObjectName(u"label_area_3")
        self.label_area_3.setGeometry(QRect(550, 70, 151, 25))
        self.tableInterruptores = QTableWidget(NewBook)
        self.tableInterruptores.setObjectName(u"tableInterruptores")
        self.tableInterruptores.setGeometry(QRect(20, 240, 421, 181))
        self.tableInterruptores.setAutoFillBackground(True)
        self.tableInterruptores.setLineWidth(5)
        self.tableInterruptores.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableInterruptores.setTextElideMode(Qt.ElideLeft)
        self.tableInterruptores.horizontalHeader().setMinimumSectionSize(10)
        self.label_5 = QLabel(NewBook)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(460, 220, 111, 21))
        self.inputTension = QLineEdit(NewBook)
        self.inputTension.setObjectName(u"inputTension")
        self.inputTension.setGeometry(QRect(550, 95, 171, 31))
        self.inputTension.setFont(font1)
        self.inputTension.setMaxLength(8)
        self.tableSeccionadores = QTableWidget(NewBook)
        self.tableSeccionadores.setObjectName(u"tableSeccionadores")
        self.tableSeccionadores.setGeometry(QRect(460, 240, 421, 181))
        self.tableSeccionadores.setAutoFillBackground(True)
        self.tableSeccionadores.setLineWidth(5)
        self.tableSeccionadores.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableSeccionadores.setTextElideMode(Qt.ElideLeft)
        self.tableSeccionadores.horizontalHeader().setMinimumSectionSize(10)
        self.btnDeleteInterruptor = QPushButton(NewBook)
        self.btnDeleteInterruptor.setObjectName(u"btnDeleteInterruptor")
        self.btnDeleteInterruptor.setGeometry(QRect(410, 210, 31, 31))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setWeight(75)
        self.btnDeleteInterruptor.setFont(font3)
        self.btnDeleteInterruptor.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnDeleteInterruptor.setStyleSheet(u"QPushButton\n"
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
        icon2.addFile(u"./assets/icons/db_negative.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnDeleteInterruptor.setIcon(icon2)
        self.btnDeleteInterruptor.setIconSize(QSize(30, 30))
        self.btnDeleteInterruptor.setAutoDefault(True)
        self.btnDeleteInterruptor.setFlat(True)
        self.btnDeleteSeccionador = QPushButton(NewBook)
        self.btnDeleteSeccionador.setObjectName(u"btnDeleteSeccionador")
        self.btnDeleteSeccionador.setGeometry(QRect(850, 210, 31, 31))
        self.btnDeleteSeccionador.setFont(font3)
        self.btnDeleteSeccionador.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnDeleteSeccionador.setStyleSheet(u"QPushButton\n"
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
        self.btnDeleteSeccionador.setIcon(icon2)
        self.btnDeleteSeccionador.setIconSize(QSize(30, 30))
        self.btnDeleteSeccionador.setAutoDefault(True)
        self.btnDeleteSeccionador.setFlat(True)
        self.btnAddInterruptor = QPushButton(NewBook)
        self.btnAddInterruptor.setObjectName(u"btnAddInterruptor")
        self.btnAddInterruptor.setGeometry(QRect(370, 210, 31, 31))
        self.btnAddInterruptor.setFont(font3)
        self.btnAddInterruptor.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnAddInterruptor.setStyleSheet(u"QPushButton\n"
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
        self.btnAddInterruptor.setIcon(icon)
        self.btnAddInterruptor.setIconSize(QSize(30, 30))
        self.btnAddInterruptor.setAutoDefault(True)
        self.btnAddInterruptor.setFlat(True)
        self.addButton_7 = QPushButton(NewBook)
        self.addButton_7.setObjectName(u"addButton_7")
        self.addButton_7.setGeometry(QRect(810, 210, 31, 31))
        self.addButton_7.setFont(font3)
        self.addButton_7.setCursor(QCursor(Qt.PointingHandCursor))
        self.addButton_7.setStyleSheet(u"QPushButton\n"
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
        self.addButton_7.setIcon(icon)
        self.addButton_7.setIconSize(QSize(30, 30))
        self.addButton_7.setAutoDefault(True)
        self.addButton_7.setFlat(True)
        self.label_area_4 = QLabel(NewBook)
        self.label_area_4.setObjectName(u"label_area_4")
        self.label_area_4.setGeometry(QRect(730, 70, 151, 25))
        self.inputNodoSalida = QLineEdit(NewBook)
        self.inputNodoSalida.setObjectName(u"inputNodoSalida")
        self.inputNodoSalida.setGeometry(QRect(730, 95, 151, 31))
        self.inputNodoSalida.setFont(font1)
        self.inputNodoSalida.setMaxLength(25)
        self.label_area_5 = QLabel(NewBook)
        self.label_area_5.setObjectName(u"label_area_5")
        self.label_area_5.setGeometry(QRect(20, 140, 151, 25))
        self.inputNodoLlegada = QLineEdit(NewBook)
        self.inputNodoLlegada.setObjectName(u"inputNodoLlegada")
        self.inputNodoLlegada.setGeometry(QRect(20, 165, 151, 31))
        self.inputNodoLlegada.setFont(font1)
        self.inputNodoLlegada.setMaxLength(25)
        self.label_area_6 = QLabel(NewBook)
        self.label_area_6.setObjectName(u"label_area_6")
        self.label_area_6.setGeometry(QRect(180, 140, 151, 25))
        self.inputCeldaSalida = QLineEdit(NewBook)
        self.inputCeldaSalida.setObjectName(u"inputCeldaSalida")
        self.inputCeldaSalida.setGeometry(QRect(180, 165, 151, 31))
        self.inputCeldaSalida.setFont(font1)
        self.inputCeldaSalida.setMaxLength(10)
        self.label_area_7 = QLabel(NewBook)
        self.label_area_7.setObjectName(u"label_area_7")
        self.label_area_7.setGeometry(QRect(340, 140, 151, 25))
        self.inputCeldaLlegada = QLineEdit(NewBook)
        self.inputCeldaLlegada.setObjectName(u"inputCeldaLlegada")
        self.inputCeldaLlegada.setGeometry(QRect(340, 165, 151, 31))
        self.inputCeldaLlegada.setFont(font1)
        self.inputCeldaLlegada.setMaxLength(10)
        self.label_empresa = QLabel(NewBook)
        self.label_empresa.setObjectName(u"label_empresa")
        self.label_empresa.setGeometry(QRect(500, 145, 111, 21))
        self.label_empresa.setScaledContents(True)
        self.inputCodEmpresa = QLineEdit(NewBook)
        self.inputCodEmpresa.setObjectName(u"inputCodEmpresa")
        self.inputCodEmpresa.setGeometry(QRect(500, 165, 121, 31))
        self.inputCodEmpresa.setFont(font1)
        self.inputCodEmpresa.setMaxLength(5)
        QWidget.setTabOrder(self.inputCodigo, self.inputNombre)
        QWidget.setTabOrder(self.inputNombre, self.addButton)
        QWidget.setTabOrder(self.addButton, self.cancelButton)

        self.retranslateUi(NewBook)

        self.addButton.setDefault(True)
        self.cancelButton.setDefault(True)
        self.btnDeleteInterruptor.setDefault(True)
        self.btnDeleteSeccionador.setDefault(True)
        self.btnAddInterruptor.setDefault(True)
        self.addButton_7.setDefault(True)


        QMetaObject.connectSlotsByName(NewBook)
    # setupUi

    def retranslateUi(self, NewBook):
        NewBook.setWindowTitle(QCoreApplication.translate("NewBook", u"Nuevo Registro", None))
        self.label.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">L\u00cdNEA DE TRANSMISI\u00d3N</span></p></body></html>", None))
        self.label_autoriza.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Codigo:</span></p></body></html>", None))
        self.addButton.setText(QCoreApplication.translate("NewBook", u"AGREGAR", None))
        self.cancelButton.setText(QCoreApplication.translate("NewBook", u"CANCELAR", None))
        self.label_aquienVisita.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Nombre:</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Tramo de L\u00ednea:</span></p></body></html>", None))
        self.label_nota_obligatoria.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; font-style:italic; color:#ff0000;\">(*) El c\u00f3digo es obligatorio</span></p></body></html>", None))
        self.ast_aquienvisita.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ff0000;\">*</span></p></body></html>", None))
        self.label_advertencia_dni.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; font-style:italic; color:#ff0000;\">(*) El c\u00f3digo es obligatorio</span></p></body></html>", None))
        self.label_area_2.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Tipo:</span></p></body></html>", None))
        self.label_area_3.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Tensi\u00f3n Nominal:</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Estructura:</span></p></body></html>", None))
        self.btnDeleteInterruptor.setText("")
        self.btnDeleteSeccionador.setText("")
        self.btnAddInterruptor.setText("")
        self.addButton_7.setText("")
        self.label_area_4.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Nodo Salida:</span></p></body></html>", None))
        self.label_area_5.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Nodo Llegada:</span></p></body></html>", None))
        self.label_area_6.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Celda Salida:</span></p></body></html>", None))
        self.label_area_7.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Celda Llegada:</span></p></body></html>", None))
        self.label_empresa.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Empresa:</span></p></body></html>", None))
    # retranslateUi

