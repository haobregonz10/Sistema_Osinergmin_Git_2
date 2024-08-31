# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_transmision_barra.ui'
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
        NewBook.resize(860, 556)
        NewBook.setMinimumSize(QSize(860, 556))
        NewBook.setMaximumSize(QSize(860, 556))
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
        self.label.setGeometry(QRect(20, 10, 821, 41))
        self.label.setMinimumSize(QSize(821, 0))
        self.label.setMaximumSize(QSize(821, 16777215))
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
        self.inputNombre = QLineEdit(NewBook)
        self.inputNombre.setObjectName(u"inputNombre")
        self.inputNombre.setGeometry(QRect(140, 95, 221, 31))
        self.inputNombre.setFont(font1)
        self.addButton = QPushButton(NewBook)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setGeometry(QRect(120, 510, 291, 41))
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
        self.cancelButton.setGeometry(QRect(450, 510, 271, 41))
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
        self.label_area = QLabel(NewBook)
        self.label_area.setObjectName(u"label_area")
        self.label_area.setGeometry(QRect(20, 140, 141, 25))
        self.label_horaIngreso = QLabel(NewBook)
        self.label_horaIngreso.setObjectName(u"label_horaIngreso")
        self.label_horaIngreso.setGeometry(QRect(170, 140, 111, 25))
        self.label_horaSalida = QLabel(NewBook)
        self.label_horaSalida.setObjectName(u"label_horaSalida")
        self.label_horaSalida.setGeometry(QRect(410, 140, 81, 25))
        self.label_motivoVisita = QLabel(NewBook)
        self.label_motivoVisita.setObjectName(u"label_motivoVisita")
        self.label_motivoVisita.setGeometry(QRect(540, 140, 131, 25))
        self.label_nota_obligatoria = QLabel(NewBook)
        self.label_nota_obligatoria.setObjectName(u"label_nota_obligatoria")
        self.label_nota_obligatoria.setGeometry(QRect(20, 480, 281, 21))
        self.label_advertencia_dni = QLabel(NewBook)
        self.label_advertencia_dni.setObjectName(u"label_advertencia_dni")
        self.label_advertencia_dni.setGeometry(QRect(20, 480, 251, 21))
        self.label_area_2 = QLabel(NewBook)
        self.label_area_2.setObjectName(u"label_area_2")
        self.label_area_2.setGeometry(QRect(520, 70, 141, 25))
        self.cbEstado = QComboBox(NewBook)
        self.cbEstado.setObjectName(u"cbEstado")
        self.cbEstado.setGeometry(QRect(410, 165, 121, 31))
        self.cbEstado.setFont(font1)
        self.cbEstado.setEditable(False)
        self.inputFecha = QDateEdit(NewBook)
        self.inputFecha.setObjectName(u"inputFecha")
        self.inputFecha.setGeometry(QRect(540, 165, 131, 31))
        font3 = QFont()
        font3.setPointSize(11)
        font3.setBold(False)
        font3.setWeight(50)
        self.inputFecha.setFont(font3)
        self.inputArreglo = QComboBox(NewBook)
        self.inputArreglo.setObjectName(u"inputArreglo")
        self.inputArreglo.setGeometry(QRect(680, 95, 161, 31))
        self.inputArreglo.setFont(font1)
        self.inputArreglo.setEditable(False)
        self.inputInstalacion = QComboBox(NewBook)
        self.inputInstalacion.setObjectName(u"inputInstalacion")
        self.inputInstalacion.setGeometry(QRect(20, 165, 141, 31))
        self.inputInstalacion.setFont(font1)
        self.inputInstalacion.setEditable(False)
        self.inputTension = QLineEdit(NewBook)
        self.inputTension.setObjectName(u"inputTension")
        self.inputTension.setGeometry(QRect(170, 165, 111, 31))
        self.inputTension.setFont(font1)
        self.inputTension.setMaxLength(8)
        self.label_horaIngreso_4 = QLabel(NewBook)
        self.label_horaIngreso_4.setObjectName(u"label_horaIngreso_4")
        self.label_horaIngreso_4.setGeometry(QRect(290, 140, 111, 25))
        self.cbBarra = QComboBox(NewBook)
        self.cbBarra.setObjectName(u"cbBarra")
        self.cbBarra.setGeometry(QRect(290, 165, 111, 31))
        self.cbBarra.setFont(font1)
        self.cbBarra.setEditable(False)
        self.inputTipo = QComboBox(NewBook)
        self.inputTipo.setObjectName(u"inputTipo")
        self.inputTipo.setGeometry(QRect(520, 95, 151, 31))
        self.inputTipo.setFont(font1)
        self.inputTipo.setEditable(False)
        self.label_area_3 = QLabel(NewBook)
        self.label_area_3.setObjectName(u"label_area_3")
        self.label_area_3.setGeometry(QRect(680, 70, 141, 25))
        self.inputCalificacion = QComboBox(NewBook)
        self.inputCalificacion.setObjectName(u"inputCalificacion")
        self.inputCalificacion.setGeometry(QRect(370, 95, 141, 31))
        self.inputCalificacion.setFont(font1)
        self.inputCalificacion.setEditable(False)
        self.label_area_4 = QLabel(NewBook)
        self.label_area_4.setObjectName(u"label_area_4")
        self.label_area_4.setGeometry(QRect(370, 70, 141, 25))
        self.label_advertencia_dni_2 = QLabel(NewBook)
        self.label_advertencia_dni_2.setObjectName(u"label_advertencia_dni_2")
        self.label_advertencia_dni_2.setGeometry(QRect(60, 70, 21, 21))
        self.label_nota_obligatoria_2 = QLabel(NewBook)
        self.label_nota_obligatoria_2.setObjectName(u"label_nota_obligatoria_2")
        self.label_nota_obligatoria_2.setGeometry(QRect(20, 480, 281, 21))
        self.tablePlano = QTableWidget(NewBook)
        self.tablePlano.setObjectName(u"tablePlano")
        self.tablePlano.setGeometry(QRect(20, 240, 401, 233))
        self.tablePlano.setAutoFillBackground(True)
        self.tablePlano.setLineWidth(5)
        self.tablePlano.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tablePlano.setTextElideMode(Qt.ElideLeft)
        self.tablePlano.horizontalHeader().setMinimumSectionSize(10)
        self.label_5 = QLabel(NewBook)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(440, 210, 261, 30))
        self.label_5.setScaledContents(True)
        self.btnDeletePlano = QPushButton(NewBook)
        self.btnDeletePlano.setObjectName(u"btnDeletePlano")
        self.btnDeletePlano.setGeometry(QRect(390, 210, 24, 30))
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
        self.btnAddPlano.setGeometry(QRect(360, 210, 24, 30))
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
        self.label_advertencia_dni_3 = QLabel(NewBook)
        self.label_advertencia_dni_3.setObjectName(u"label_advertencia_dni_3")
        self.label_advertencia_dni_3.setGeometry(QRect(20, 480, 251, 21))
        self.btnAddEsquema = QPushButton(NewBook)
        self.btnAddEsquema.setObjectName(u"btnAddEsquema")
        self.btnAddEsquema.setGeometry(QRect(770, 210, 24, 30))
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
        self.label_4.setGeometry(QRect(20, 210, 311, 30))
        self.label_4.setScaledContents(True)
        self.btnDeleteEsquema = QPushButton(NewBook)
        self.btnDeleteEsquema.setObjectName(u"btnDeleteEsquema")
        self.btnDeleteEsquema.setGeometry(QRect(800, 210, 24, 30))
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
        self.tableEsquema.setGeometry(QRect(440, 240, 391, 233))
        self.tableEsquema.setAutoFillBackground(True)
        self.tableEsquema.setLineWidth(5)
        self.tableEsquema.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableEsquema.setTextElideMode(Qt.ElideLeft)
        self.tableEsquema.horizontalHeader().setMinimumSectionSize(10)
        self.inputCodEmpresa = QLineEdit(NewBook)
        self.inputCodEmpresa.setObjectName(u"inputCodEmpresa")
        self.inputCodEmpresa.setGeometry(QRect(680, 165, 161, 31))
        self.inputCodEmpresa.setFont(font1)
        self.inputCodEmpresa.setMaxLength(5)
        self.label_empresa = QLabel(NewBook)
        self.label_empresa.setObjectName(u"label_empresa")
        self.label_empresa.setGeometry(QRect(680, 140, 111, 21))
        self.label_empresa.setScaledContents(True)
        QWidget.setTabOrder(self.inputCodigo, self.inputNombre)
        QWidget.setTabOrder(self.inputNombre, self.addButton)
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
        self.label.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">BARRA</span></p></body></html>", None))
        self.label_autoriza.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Codigo:</span></p></body></html>", None))
        self.addButton.setText(QCoreApplication.translate("NewBook", u"AGREGAR", None))
        self.cancelButton.setText(QCoreApplication.translate("NewBook", u"CANCELAR", None))
        self.label_aquienVisita.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Subestaci\u00f3n:</span></p></body></html>", None))
        self.label_area.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Tipo Instalaci\u00f3n:</span></p></body></html>", None))
        self.label_horaIngreso.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Tensi\u00f3n:</span></p></body></html>", None))
        self.label_horaSalida.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Estado:</span></p></body></html>", None))
        self.label_motivoVisita.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Fecha de Alta:</span></p></body></html>", None))
        self.label_nota_obligatoria.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; font-style:italic; color:#ff0000;\">(*) El c\u00f3digo es obligatorio</span></p></body></html>", None))
        self.label_advertencia_dni.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; font-style:italic; color:#ff0000;\">(*) El c\u00f3digo es obligatorio</span></p></body></html>", None))
        self.label_area_2.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Tipo:</span></p></body></html>", None))
        self.label_horaIngreso_4.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Barra Ref.:</span></p></body></html>", None))
        self.label_area_3.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Tipo Arreglo:</span></p></body></html>", None))
        self.label_area_4.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Calificaci\u00f3n:</span></p></body></html>", None))
        self.label_advertencia_dni_2.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; font-style:italic; color:#ff0000;\">*</span></p></body></html>", None))
        self.label_nota_obligatoria_2.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; font-style:italic; color:#ff0000;\">(*) El c\u00f3digo es obligatorio</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Ubicaci\u00f3n Esquema:</span></p></body></html>", None))
        self.btnDeletePlano.setText("")
        self.btnAddPlano.setText("")
        self.label_advertencia_dni_3.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; font-style:italic; color:#ff0000;\">(*) El c\u00f3digo es obligatorio</span></p></body></html>", None))
        self.btnAddEsquema.setText("")
        self.label_4.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Ubicaci\u00f3n dentro del Plano Planta:</span></p></body></html>", None))
        self.btnDeleteEsquema.setText("")
        self.label_empresa.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Empresa:</span></p></body></html>", None))
    # retranslateUi

