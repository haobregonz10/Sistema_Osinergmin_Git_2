# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_transmision_subestacion.ui'
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
        NewBook.resize(1373, 621)
        NewBook.setMinimumSize(QSize(1235, 621))
        NewBook.setMaximumSize(QSize(3000, 621))
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
        self.label.setGeometry(QRect(20, 10, 1341, 41))
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
        self.inputCodigo.setMaxLength(20)
        self.inputNombre = QLineEdit(NewBook)
        self.inputNombre.setObjectName(u"inputNombre")
        self.inputNombre.setGeometry(QRect(140, 95, 221, 31))
        self.inputNombre.setFont(font1)
        self.inputNombre.setMaxLength(50)
        self.addButton = QPushButton(NewBook)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setGeometry(QRect(300, 560, 291, 41))
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
        self.cancelButton.setGeometry(QRect(660, 560, 271, 41))
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
        self.label_fecha = QLabel(NewBook)
        self.label_fecha.setObjectName(u"label_fecha")
        self.label_fecha.setGeometry(QRect(1230, 70, 101, 25))
        self.label_visitante = QLabel(NewBook)
        self.label_visitante.setObjectName(u"label_visitante")
        self.label_visitante.setGeometry(QRect(150, 140, 141, 25))
        self.label_entidad = QLabel(NewBook)
        self.label_entidad.setObjectName(u"label_entidad")
        self.label_entidad.setGeometry(QRect(310, 140, 151, 25))
        self.label_horaIngreso = QLabel(NewBook)
        self.label_horaIngreso.setObjectName(u"label_horaIngreso")
        self.label_horaIngreso.setGeometry(QRect(920, 140, 91, 25))
        self.label_horaSalida = QLabel(NewBook)
        self.label_horaSalida.setObjectName(u"label_horaSalida")
        self.label_horaSalida.setGeometry(QRect(640, 210, 81, 25))
        self.label_motivoVisita = QLabel(NewBook)
        self.label_motivoVisita.setObjectName(u"label_motivoVisita")
        self.label_motivoVisita.setGeometry(QRect(790, 210, 131, 25))
        self.inputAltitud = QLineEdit(NewBook)
        self.inputAltitud.setObjectName(u"inputAltitud")
        self.inputAltitud.setGeometry(QRect(20, 165, 121, 31))
        self.inputAltitud.setFont(font1)
        self.inputAltitud.setInputMethodHints(Qt.ImhDigitsOnly)
        self.inputAltitud.setMaxLength(4)
        self.label_dni = QLabel(NewBook)
        self.label_dni.setObjectName(u"label_dni")
        self.label_dni.setGeometry(QRect(20, 140, 91, 25))
        self.inputTelefono = QLineEdit(NewBook)
        self.inputTelefono.setObjectName(u"inputTelefono")
        self.inputTelefono.setGeometry(QRect(920, 165, 101, 31))
        self.inputTelefono.setFont(font1)
        self.inputTelefono.setMaxLength(15)
        self.inputDatum = QLineEdit(NewBook)
        self.inputDatum.setObjectName(u"inputDatum")
        self.inputDatum.setGeometry(QRect(930, 235, 151, 31))
        self.inputDatum.setFont(font1)
        self.inputDatum.setMaxLength(10)
        self.label_nota_obligatoria = QLabel(NewBook)
        self.label_nota_obligatoria.setObjectName(u"label_nota_obligatoria")
        self.label_nota_obligatoria.setGeometry(QRect(20, 540, 281, 21))
        self.ast_aquienvisita = QLabel(NewBook)
        self.ast_aquienvisita.setObjectName(u"ast_aquienvisita")
        self.ast_aquienvisita.setGeometry(QRect(70, 70, 21, 25))
        self.label_advertencia_dni = QLabel(NewBook)
        self.label_advertencia_dni.setObjectName(u"label_advertencia_dni")
        self.label_advertencia_dni.setGeometry(QRect(20, 540, 251, 21))
        self.cbCalificacion = QComboBox(NewBook)
        self.cbCalificacion.setObjectName(u"cbCalificacion")
        self.cbCalificacion.setGeometry(QRect(370, 95, 191, 31))
        self.cbCalificacion.setFont(font1)
        self.cbCalificacion.setEditable(False)
        self.label_area_2 = QLabel(NewBook)
        self.label_area_2.setObjectName(u"label_area_2")
        self.label_area_2.setGeometry(QRect(370, 70, 131, 25))
        self.cbTipoSistema = QComboBox(NewBook)
        self.cbTipoSistema.setObjectName(u"cbTipoSistema")
        self.cbTipoSistema.setGeometry(QRect(570, 95, 131, 31))
        self.cbTipoSistema.setFont(font1)
        self.cbTipoSistema.setEditable(False)
        self.label_area_3 = QLabel(NewBook)
        self.label_area_3.setObjectName(u"label_area_3")
        self.label_area_3.setGeometry(QRect(570, 70, 121, 25))
        self.label_area_4 = QLabel(NewBook)
        self.label_area_4.setObjectName(u"label_area_4")
        self.label_area_4.setGeometry(QRect(850, 70, 131, 25))
        self.cbAreaOperativa = QComboBox(NewBook)
        self.cbAreaOperativa.setObjectName(u"cbAreaOperativa")
        self.cbAreaOperativa.setGeometry(QRect(850, 95, 131, 31))
        self.cbAreaOperativa.setFont(font1)
        self.cbAreaOperativa.setEditable(False)
        self.cbRegion = QComboBox(NewBook)
        self.cbRegion.setObjectName(u"cbRegion")
        self.cbRegion.setGeometry(QRect(990, 95, 231, 31))
        self.cbRegion.setFont(font1)
        self.cbRegion.setEditable(False)
        self.label_area_5 = QLabel(NewBook)
        self.label_area_5.setObjectName(u"label_area_5")
        self.label_area_5.setGeometry(QRect(990, 70, 191, 25))
        self.cbZona = QComboBox(NewBook)
        self.cbZona.setObjectName(u"cbZona")
        self.cbZona.setGeometry(QRect(1230, 95, 131, 31))
        self.cbZona.setFont(font1)
        self.cbZona.setEditable(False)
        self.label_entidad_2 = QLabel(NewBook)
        self.label_entidad_2.setObjectName(u"label_entidad_2")
        self.label_entidad_2.setGeometry(QRect(490, 140, 121, 25))
        self.inputDireccion = QLineEdit(NewBook)
        self.inputDireccion.setObjectName(u"inputDireccion")
        self.inputDireccion.setGeometry(QRect(620, 165, 291, 31))
        self.inputDireccion.setFont(font1)
        self.inputDireccion.setMaxLength(150)
        self.label_entidad_3 = QLabel(NewBook)
        self.label_entidad_3.setObjectName(u"label_entidad_3")
        self.label_entidad_3.setGeometry(QRect(620, 140, 151, 25))
        self.inputZona = QLineEdit(NewBook)
        self.inputZona.setObjectName(u"inputZona")
        self.inputZona.setGeometry(QRect(1090, 235, 111, 31))
        self.inputZona.setFont(font1)
        self.inputZona.setMaxLength(5)
        self.cbEstado = QComboBox(NewBook)
        self.cbEstado.setObjectName(u"cbEstado")
        self.cbEstado.setGeometry(QRect(640, 235, 141, 31))
        self.cbEstado.setFont(font1)
        self.cbEstado.setEditable(False)
        self.inputFecha = QDateEdit(NewBook)
        self.inputFecha.setObjectName(u"inputFecha")
        self.inputFecha.setGeometry(QRect(790, 235, 131, 31))
        font3 = QFont()
        font3.setPointSize(11)
        font3.setBold(False)
        font3.setWeight(50)
        self.inputFecha.setFont(font3)
        self.label_motivoVisita_2 = QLabel(NewBook)
        self.label_motivoVisita_2.setObjectName(u"label_motivoVisita_2")
        self.label_motivoVisita_2.setGeometry(QRect(930, 210, 131, 25))
        self.label_motivoVisita_3 = QLabel(NewBook)
        self.label_motivoVisita_3.setObjectName(u"label_motivoVisita_3")
        self.label_motivoVisita_3.setGeometry(QRect(1090, 210, 131, 25))
        self.tableBarras = QTableWidget(NewBook)
        self.tableBarras.setObjectName(u"tableBarras")
        self.tableBarras.setGeometry(QRect(20, 360, 141, 181))
        self.tableBarras.setAutoFillBackground(True)
        self.tableBarras.setLineWidth(5)
        self.tableBarras.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableBarras.setTextElideMode(Qt.ElideLeft)
        self.tableBarras.horizontalHeader().setMinimumSectionSize(10)
        self.label_6 = QLabel(NewBook)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 340, 71, 21))
        self.label_7 = QLabel(NewBook)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(170, 340, 81, 21))
        self.tablePorticos = QTableWidget(NewBook)
        self.tablePorticos.setObjectName(u"tablePorticos")
        self.tablePorticos.setGeometry(QRect(170, 360, 141, 181))
        self.tablePorticos.setAutoFillBackground(True)
        self.tablePorticos.setLineWidth(5)
        self.tablePorticos.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tablePorticos.setTextElideMode(Qt.ElideLeft)
        self.tablePorticos.horizontalHeader().setMinimumSectionSize(10)
        self.tableTransformador = QTableWidget(NewBook)
        self.tableTransformador.setObjectName(u"tableTransformador")
        self.tableTransformador.setGeometry(QRect(470, 360, 141, 181))
        self.tableTransformador.setAutoFillBackground(True)
        self.tableTransformador.setLineWidth(5)
        self.tableTransformador.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableTransformador.setTextElideMode(Qt.ElideLeft)
        self.tableTransformador.horizontalHeader().setMinimumSectionSize(10)
        self.tableCeldas = QTableWidget(NewBook)
        self.tableCeldas.setObjectName(u"tableCeldas")
        self.tableCeldas.setGeometry(QRect(320, 360, 141, 181))
        self.tableCeldas.setAutoFillBackground(True)
        self.tableCeldas.setLineWidth(5)
        self.tableCeldas.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableCeldas.setTextElideMode(Qt.ElideLeft)
        self.tableCeldas.horizontalHeader().setMinimumSectionSize(10)
        self.tableBobina = QTableWidget(NewBook)
        self.tableBobina.setObjectName(u"tableBobina")
        self.tableBobina.setGeometry(QRect(920, 360, 141, 181))
        self.tableBobina.setAutoFillBackground(True)
        self.tableBobina.setLineWidth(5)
        self.tableBobina.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableBobina.setTextElideMode(Qt.ElideLeft)
        self.tableBobina.horizontalHeader().setMinimumSectionSize(10)
        self.tableConductor = QTableWidget(NewBook)
        self.tableConductor.setObjectName(u"tableConductor")
        self.tableConductor.setGeometry(QRect(1070, 360, 141, 181))
        self.tableConductor.setAutoFillBackground(True)
        self.tableConductor.setLineWidth(5)
        self.tableConductor.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableConductor.setTextElideMode(Qt.ElideLeft)
        self.tableConductor.horizontalHeader().setMinimumSectionSize(10)
        self.tablePararrayo = QTableWidget(NewBook)
        self.tablePararrayo.setObjectName(u"tablePararrayo")
        self.tablePararrayo.setGeometry(QRect(620, 360, 141, 181))
        self.tablePararrayo.setAutoFillBackground(True)
        self.tablePararrayo.setLineWidth(5)
        self.tablePararrayo.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tablePararrayo.setTextElideMode(Qt.ElideLeft)
        self.tablePararrayo.horizontalHeader().setMinimumSectionSize(10)
        self.tableMedicion = QTableWidget(NewBook)
        self.tableMedicion.setObjectName(u"tableMedicion")
        self.tableMedicion.setGeometry(QRect(770, 360, 141, 181))
        self.tableMedicion.setAutoFillBackground(True)
        self.tableMedicion.setLineWidth(5)
        self.tableMedicion.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableMedicion.setTextElideMode(Qt.ElideLeft)
        self.tableMedicion.horizontalHeader().setMinimumSectionSize(10)
        self.label_9 = QLabel(NewBook)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(320, 340, 101, 21))
        self.label_11 = QLabel(NewBook)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(470, 340, 111, 21))
        self.label_12 = QLabel(NewBook)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(620, 340, 111, 21))
        self.label_13 = QLabel(NewBook)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(770, 340, 111, 21))
        font4 = QFont()
        font4.setPointSize(7)
        self.label_13.setFont(font4)
        self.label_14 = QLabel(NewBook)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(1070, 340, 111, 21))
        font5 = QFont()
        font5.setPointSize(10)
        self.label_14.setFont(font5)
        self.cbAreaDemanda = QComboBox(NewBook)
        self.cbAreaDemanda.setObjectName(u"cbAreaDemanda")
        self.cbAreaDemanda.setGeometry(QRect(710, 95, 131, 31))
        self.cbAreaDemanda.setFont(font1)
        self.cbAreaDemanda.setEditable(False)
        self.label_area_6 = QLabel(NewBook)
        self.label_area_6.setObjectName(u"label_area_6")
        self.label_area_6.setGeometry(QRect(710, 70, 131, 25))
        self.inputServicios = QLineEdit(NewBook)
        self.inputServicios.setObjectName(u"inputServicios")
        self.inputServicios.setGeometry(QRect(1030, 165, 161, 31))
        self.inputServicios.setFont(font1)
        self.inputServicios.setMaxLength(30)
        self.inputObras = QLineEdit(NewBook)
        self.inputObras.setObjectName(u"inputObras")
        self.inputObras.setGeometry(QRect(1200, 165, 161, 31))
        self.inputObras.setFont(font1)
        self.inputObras.setMaxLength(30)
        self.inputEdificios = QLineEdit(NewBook)
        self.inputEdificios.setObjectName(u"inputEdificios")
        self.inputEdificios.setGeometry(QRect(20, 235, 191, 31))
        self.inputEdificios.setFont(font1)
        self.inputEdificios.setMaxLength(30)
        self.inputRed = QLineEdit(NewBook)
        self.inputRed.setObjectName(u"inputRed")
        self.inputRed.setGeometry(QRect(220, 235, 181, 31))
        self.inputRed.setFont(font1)
        self.inputRed.setMaxLength(30)
        self.inputInstalaciones = QLineEdit(NewBook)
        self.inputInstalaciones.setObjectName(u"inputInstalaciones")
        self.inputInstalaciones.setGeometry(QRect(410, 235, 221, 31))
        self.inputInstalaciones.setFont(font1)
        self.inputInstalaciones.setMaxLength(30)
        self.label_horaIngreso_2 = QLabel(NewBook)
        self.label_horaIngreso_2.setObjectName(u"label_horaIngreso_2")
        self.label_horaIngreso_2.setGeometry(QRect(1030, 140, 171, 25))
        self.label_horaIngreso_3 = QLabel(NewBook)
        self.label_horaIngreso_3.setObjectName(u"label_horaIngreso_3")
        self.label_horaIngreso_3.setGeometry(QRect(1200, 140, 171, 25))
        self.label_horaIngreso_4 = QLabel(NewBook)
        self.label_horaIngreso_4.setObjectName(u"label_horaIngreso_4")
        self.label_horaIngreso_4.setGeometry(QRect(20, 210, 171, 25))
        self.label_horaIngreso_5 = QLabel(NewBook)
        self.label_horaIngreso_5.setObjectName(u"label_horaIngreso_5")
        self.label_horaIngreso_5.setGeometry(QRect(220, 210, 171, 25))
        self.label_horaIngreso_6 = QLabel(NewBook)
        self.label_horaIngreso_6.setObjectName(u"label_horaIngreso_6")
        self.label_horaIngreso_6.setGeometry(QRect(410, 210, 221, 25))
        self.label_16 = QLabel(NewBook)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(920, 340, 111, 21))
        self.label_16.setFont(font5)
        self.btnAddBarras = QPushButton(NewBook)
        self.btnAddBarras.setObjectName(u"btnAddBarras")
        self.btnAddBarras.setGeometry(QRect(120, 340, 20, 20))
        font6 = QFont()
        font6.setPointSize(12)
        font6.setBold(True)
        font6.setWeight(75)
        self.btnAddBarras.setFont(font6)
        self.btnAddBarras.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnAddBarras.setStyleSheet(u"QPushButton\n"
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
        self.btnAddBarras.setIcon(icon)
        self.btnAddBarras.setAutoDefault(True)
        self.btnAddBarras.setFlat(True)
        self.btnDeleteBarras = QPushButton(NewBook)
        self.btnDeleteBarras.setObjectName(u"btnDeleteBarras")
        self.btnDeleteBarras.setGeometry(QRect(140, 340, 20, 20))
        self.btnDeleteBarras.setFont(font6)
        self.btnDeleteBarras.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnDeleteBarras.setStyleSheet(u"QPushButton\n"
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
        self.btnDeleteBarras.setIcon(icon2)
        self.btnDeleteBarras.setAutoDefault(True)
        self.btnDeleteBarras.setFlat(True)
        self.btnDeletePorticos = QPushButton(NewBook)
        self.btnDeletePorticos.setObjectName(u"btnDeletePorticos")
        self.btnDeletePorticos.setGeometry(QRect(290, 340, 20, 20))
        self.btnDeletePorticos.setFont(font6)
        self.btnDeletePorticos.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnDeletePorticos.setStyleSheet(u"QPushButton\n"
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
        self.btnDeletePorticos.setIcon(icon2)
        self.btnDeletePorticos.setAutoDefault(True)
        self.btnDeletePorticos.setFlat(True)
        self.btnAddPorticos = QPushButton(NewBook)
        self.btnAddPorticos.setObjectName(u"btnAddPorticos")
        self.btnAddPorticos.setGeometry(QRect(270, 340, 20, 20))
        self.btnAddPorticos.setFont(font6)
        self.btnAddPorticos.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnAddPorticos.setStyleSheet(u"QPushButton\n"
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
        self.btnAddPorticos.setIcon(icon)
        self.btnAddPorticos.setAutoDefault(True)
        self.btnAddPorticos.setFlat(True)
        self.btnAddCeldas = QPushButton(NewBook)
        self.btnAddCeldas.setObjectName(u"btnAddCeldas")
        self.btnAddCeldas.setGeometry(QRect(420, 340, 20, 20))
        self.btnAddCeldas.setFont(font6)
        self.btnAddCeldas.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnAddCeldas.setStyleSheet(u"QPushButton\n"
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
        self.btnAddCeldas.setIcon(icon)
        self.btnAddCeldas.setAutoDefault(True)
        self.btnAddCeldas.setFlat(True)
        self.btnDeleteCeldas = QPushButton(NewBook)
        self.btnDeleteCeldas.setObjectName(u"btnDeleteCeldas")
        self.btnDeleteCeldas.setGeometry(QRect(440, 340, 20, 20))
        self.btnDeleteCeldas.setFont(font6)
        self.btnDeleteCeldas.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnDeleteCeldas.setStyleSheet(u"QPushButton\n"
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
        self.btnDeleteCeldas.setIcon(icon2)
        self.btnDeleteCeldas.setAutoDefault(True)
        self.btnDeleteCeldas.setFlat(True)
        self.btnAddTransformadores = QPushButton(NewBook)
        self.btnAddTransformadores.setObjectName(u"btnAddTransformadores")
        self.btnAddTransformadores.setGeometry(QRect(570, 340, 20, 20))
        self.btnAddTransformadores.setFont(font6)
        self.btnAddTransformadores.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnAddTransformadores.setStyleSheet(u"QPushButton\n"
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
        self.btnAddTransformadores.setIcon(icon)
        self.btnAddTransformadores.setAutoDefault(True)
        self.btnAddTransformadores.setFlat(True)
        self.btnDeleteTransformador = QPushButton(NewBook)
        self.btnDeleteTransformador.setObjectName(u"btnDeleteTransformador")
        self.btnDeleteTransformador.setGeometry(QRect(590, 340, 20, 20))
        self.btnDeleteTransformador.setFont(font6)
        self.btnDeleteTransformador.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnDeleteTransformador.setStyleSheet(u"QPushButton\n"
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
        self.btnDeleteTransformador.setIcon(icon2)
        self.btnDeleteTransformador.setAutoDefault(True)
        self.btnDeleteTransformador.setFlat(True)
        self.btnAddPararrayo = QPushButton(NewBook)
        self.btnAddPararrayo.setObjectName(u"btnAddPararrayo")
        self.btnAddPararrayo.setGeometry(QRect(720, 340, 20, 20))
        self.btnAddPararrayo.setFont(font6)
        self.btnAddPararrayo.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnAddPararrayo.setStyleSheet(u"QPushButton\n"
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
        self.btnAddPararrayo.setIcon(icon)
        self.btnAddPararrayo.setAutoDefault(True)
        self.btnAddPararrayo.setFlat(True)
        self.btnDeletePararrayo = QPushButton(NewBook)
        self.btnDeletePararrayo.setObjectName(u"btnDeletePararrayo")
        self.btnDeletePararrayo.setGeometry(QRect(740, 340, 20, 20))
        self.btnDeletePararrayo.setFont(font6)
        self.btnDeletePararrayo.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnDeletePararrayo.setStyleSheet(u"QPushButton\n"
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
        self.btnDeletePararrayo.setIcon(icon2)
        self.btnDeletePararrayo.setAutoDefault(True)
        self.btnDeletePararrayo.setFlat(True)
        self.btnDeleteTransfMed = QPushButton(NewBook)
        self.btnDeleteTransfMed.setObjectName(u"btnDeleteTransfMed")
        self.btnDeleteTransfMed.setGeometry(QRect(890, 340, 20, 20))
        self.btnDeleteTransfMed.setFont(font6)
        self.btnDeleteTransfMed.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnDeleteTransfMed.setStyleSheet(u"QPushButton\n"
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
        self.btnDeleteTransfMed.setIcon(icon2)
        self.btnDeleteTransfMed.setAutoDefault(True)
        self.btnDeleteTransfMed.setFlat(True)
        self.btnAddTransfMed = QPushButton(NewBook)
        self.btnAddTransfMed.setObjectName(u"btnAddTransfMed")
        self.btnAddTransfMed.setGeometry(QRect(870, 340, 20, 20))
        self.btnAddTransfMed.setFont(font6)
        self.btnAddTransfMed.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnAddTransfMed.setStyleSheet(u"QPushButton\n"
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
        self.btnAddTransfMed.setIcon(icon)
        self.btnAddTransfMed.setAutoDefault(True)
        self.btnAddTransfMed.setFlat(True)
        self.btnDeleteConductor = QPushButton(NewBook)
        self.btnDeleteConductor.setObjectName(u"btnDeleteConductor")
        self.btnDeleteConductor.setGeometry(QRect(1190, 340, 20, 20))
        self.btnDeleteConductor.setFont(font6)
        self.btnDeleteConductor.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnDeleteConductor.setStyleSheet(u"QPushButton\n"
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
        self.btnDeleteConductor.setIcon(icon2)
        self.btnDeleteConductor.setAutoDefault(True)
        self.btnDeleteConductor.setFlat(True)
        self.btnAddConductores = QPushButton(NewBook)
        self.btnAddConductores.setObjectName(u"btnAddConductores")
        self.btnAddConductores.setGeometry(QRect(1170, 340, 20, 20))
        self.btnAddConductores.setFont(font6)
        self.btnAddConductores.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnAddConductores.setStyleSheet(u"QPushButton\n"
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
        self.btnAddConductores.setIcon(icon)
        self.btnAddConductores.setAutoDefault(True)
        self.btnAddConductores.setFlat(True)
        self.btnDeleteBobina = QPushButton(NewBook)
        self.btnDeleteBobina.setObjectName(u"btnDeleteBobina")
        self.btnDeleteBobina.setGeometry(QRect(1040, 330, 20, 20))
        self.btnDeleteBobina.setFont(font6)
        self.btnDeleteBobina.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnDeleteBobina.setStyleSheet(u"QPushButton\n"
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
        self.btnDeleteBobina.setIcon(icon2)
        self.btnDeleteBobina.setAutoDefault(True)
        self.btnDeleteBobina.setFlat(True)
        self.btnAddBobina = QPushButton(NewBook)
        self.btnAddBobina.setObjectName(u"btnAddBobina")
        self.btnAddBobina.setGeometry(QRect(1020, 330, 20, 20))
        self.btnAddBobina.setFont(font6)
        self.btnAddBobina.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnAddBobina.setStyleSheet(u"QPushButton\n"
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
        self.btnAddBobina.setIcon(icon)
        self.btnAddBobina.setAutoDefault(True)
        self.btnAddBobina.setFlat(True)
        self.tableCompensador = QTableWidget(NewBook)
        self.tableCompensador.setObjectName(u"tableCompensador")
        self.tableCompensador.setGeometry(QRect(1220, 360, 141, 181))
        self.tableCompensador.setAutoFillBackground(True)
        self.tableCompensador.setLineWidth(5)
        self.tableCompensador.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableCompensador.setTextElideMode(Qt.ElideLeft)
        self.tableCompensador.horizontalHeader().setMinimumSectionSize(10)
        self.label_15 = QLabel(NewBook)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(1220, 340, 111, 21))
        self.label_15.setFont(font5)
        self.btnAddCompensador = QPushButton(NewBook)
        self.btnAddCompensador.setObjectName(u"btnAddCompensador")
        self.btnAddCompensador.setGeometry(QRect(1320, 340, 20, 20))
        self.btnAddCompensador.setFont(font6)
        self.btnAddCompensador.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnAddCompensador.setStyleSheet(u"QPushButton\n"
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
        self.btnAddCompensador.setIcon(icon)
        self.btnAddCompensador.setAutoDefault(True)
        self.btnAddCompensador.setFlat(True)
        self.btnDeleteCompensador = QPushButton(NewBook)
        self.btnDeleteCompensador.setObjectName(u"btnDeleteCompensador")
        self.btnDeleteCompensador.setGeometry(QRect(1340, 340, 20, 20))
        self.btnDeleteCompensador.setFont(font6)
        self.btnDeleteCompensador.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnDeleteCompensador.setStyleSheet(u"QPushButton\n"
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
        self.btnDeleteCompensador.setIcon(icon2)
        self.btnDeleteCompensador.setAutoDefault(True)
        self.btnDeleteCompensador.setFlat(True)
        self.cbTecnologia = QComboBox(NewBook)
        self.cbTecnologia.setObjectName(u"cbTecnologia")
        self.cbTecnologia.setGeometry(QRect(150, 165, 151, 31))
        self.cbTecnologia.setFont(font1)
        self.cbTecnologia.setEditable(False)
        self.cbFuncion = QComboBox(NewBook)
        self.cbFuncion.setObjectName(u"cbFuncion")
        self.cbFuncion.setGeometry(QRect(310, 165, 171, 31))
        self.cbFuncion.setFont(font1)
        self.cbFuncion.setEditable(False)
        self.cbAtendida = QComboBox(NewBook)
        self.cbAtendida.setObjectName(u"cbAtendida")
        self.cbAtendida.setGeometry(QRect(490, 165, 121, 31))
        self.cbAtendida.setFont(font1)
        self.cbAtendida.setEditable(False)
        self.btnPlano = QPushButton(NewBook)
        self.btnPlano.setObjectName(u"btnPlano")
        self.btnPlano.setGeometry(QRect(950, 280, 411, 31))
        font7 = QFont()
        font7.setPointSize(11)
        font7.setBold(True)
        font7.setWeight(75)
        self.btnPlano.setFont(font7)
        self.btnPlano.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnPlano.setStyleSheet(u"QPushButton\n"
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
        self.btnPlano.setIcon(icon)
        self.btnPlano.setIconSize(QSize(25, 25))
        self.btnPlano.setAutoDefault(True)
        self.btnPlano.setFlat(True)
        self.btnCoordenadas = QPushButton(NewBook)
        self.btnCoordenadas.setObjectName(u"btnCoordenadas")
        self.btnCoordenadas.setGeometry(QRect(530, 280, 411, 31))
        self.btnCoordenadas.setFont(font7)
        self.btnCoordenadas.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnCoordenadas.setStyleSheet(u"QPushButton\n"
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
        self.btnCoordenadas.setIcon(icon)
        self.btnCoordenadas.setIconSize(QSize(25, 25))
        self.btnCoordenadas.setAutoDefault(True)
        self.btnCoordenadas.setFlat(True)
        self.inputCodEmpresa = QLineEdit(NewBook)
        self.inputCodEmpresa.setObjectName(u"inputCodEmpresa")
        self.inputCodEmpresa.setGeometry(QRect(20, 290, 121, 31))
        self.inputCodEmpresa.setFont(font1)
        self.inputCodEmpresa.setMaxLength(5)
        self.label_empresa = QLabel(NewBook)
        self.label_empresa.setObjectName(u"label_empresa")
        self.label_empresa.setGeometry(QRect(20, 270, 111, 21))
        self.label_empresa.setScaledContents(True)
        QWidget.setTabOrder(self.inputCodigo, self.inputNombre)
        QWidget.setTabOrder(self.inputNombre, self.inputAltitud)
        QWidget.setTabOrder(self.inputAltitud, self.inputTelefono)
        QWidget.setTabOrder(self.inputTelefono, self.inputDatum)
        QWidget.setTabOrder(self.inputDatum, self.addButton)
        QWidget.setTabOrder(self.addButton, self.cancelButton)

        self.retranslateUi(NewBook)

        self.addButton.setDefault(True)
        self.cancelButton.setDefault(True)
        self.btnAddBarras.setDefault(True)
        self.btnDeleteBarras.setDefault(True)
        self.btnDeletePorticos.setDefault(True)
        self.btnAddPorticos.setDefault(True)
        self.btnAddCeldas.setDefault(True)
        self.btnDeleteCeldas.setDefault(True)
        self.btnAddTransformadores.setDefault(True)
        self.btnDeleteTransformador.setDefault(True)
        self.btnAddPararrayo.setDefault(True)
        self.btnDeletePararrayo.setDefault(True)
        self.btnDeleteTransfMed.setDefault(True)
        self.btnAddTransfMed.setDefault(True)
        self.btnDeleteConductor.setDefault(True)
        self.btnAddConductores.setDefault(True)
        self.btnDeleteBobina.setDefault(True)
        self.btnAddBobina.setDefault(True)
        self.btnAddCompensador.setDefault(True)
        self.btnDeleteCompensador.setDefault(True)
        self.btnPlano.setDefault(True)
        self.btnCoordenadas.setDefault(True)


        QMetaObject.connectSlotsByName(NewBook)
    # setupUi

    def retranslateUi(self, NewBook):
        NewBook.setWindowTitle(QCoreApplication.translate("NewBook", u"Nuevo Registro", None))
        self.label.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">SUBESTACI\u00d3N</span></p></body></html>", None))
        self.label_autoriza.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Codigo:</span></p></body></html>", None))
        self.addButton.setText(QCoreApplication.translate("NewBook", u"AGREGAR", None))
        self.cancelButton.setText(QCoreApplication.translate("NewBook", u"CANCELAR", None))
        self.label_aquienVisita.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Nombre:</span></p></body></html>", None))
        self.label_fecha.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Zona:</span></p></body></html>", None))
        self.label_visitante.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Tecnolog\u00eda:</span></p></body></html>", None))
        self.label_entidad.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Funci\u00f3n:</span></p></body></html>", None))
        self.label_horaIngreso.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Tel\u00e9fono:</span></p></body></html>", None))
        self.label_horaSalida.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Estado:</span></p></body></html>", None))
        self.label_motivoVisita.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Fecha de Alta:</span></p></body></html>", None))
        self.label_dni.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Altitud:</span></p></body></html>", None))
        self.inputTelefono.setText("")
        self.label_nota_obligatoria.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; font-style:italic; color:#ff0000;\">(*) El c\u00f3digo es obligatorio</span></p></body></html>", None))
        self.ast_aquienvisita.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ff0000;\">*</span></p></body></html>", None))
        self.label_advertencia_dni.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; font-style:italic; color:#ff0000;\">(*) El c\u00f3digo es obligatorio</span></p></body></html>", None))
        self.label_area_2.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Calificaci\u00f3n:</span></p></body></html>", None))
        self.label_area_3.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Tipo Sistema:</span></p></body></html>", None))
        self.label_area_4.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">\u00c1rea Operativa:</span></p></body></html>", None))
        self.label_area_5.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Regi\u00f3n Geogr\u00e1fica:</span></p></body></html>", None))
        self.label_entidad_2.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Atendida:</span></p></body></html>", None))
        self.label_entidad_3.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Direcci\u00f3n:</span></p></body></html>", None))
        self.label_motivoVisita_2.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Datum UTM:</span></p></body></html>", None))
        self.label_motivoVisita_3.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Zona UTM:</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Barras:</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">P\u00f3rticos:</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Celdas:</span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Transf.Potencia:</span></p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Pararrayos:</span></p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Transf.Med.:</span></p></body></html>", None))
        self.label_14.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Conductores:</span></p></body></html>", None))
        self.label_area_6.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">\u00c1rea Demanda:</span></p></body></html>", None))
        self.label_horaIngreso_2.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Servicios Aux.:</span></p></body></html>", None))
        self.label_horaIngreso_3.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Obras Civiles:</span></p></body></html>", None))
        self.label_horaIngreso_4.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Edificios de Control:</span></p></body></html>", None))
        self.label_horaIngreso_5.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Red Tierra Profunda:</span></p></body></html>", None))
        self.label_horaIngreso_6.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Instalaciones Electr. Ext.:</span></p></body></html>", None))
        self.label_16.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Bob. Bloq:</span></p></body></html>", None))
        self.btnAddBarras.setText("")
        self.btnDeleteBarras.setText("")
        self.btnDeletePorticos.setText("")
        self.btnAddPorticos.setText("")
        self.btnAddCeldas.setText("")
        self.btnDeleteCeldas.setText("")
        self.btnAddTransformadores.setText("")
        self.btnDeleteTransformador.setText("")
        self.btnAddPararrayo.setText("")
        self.btnDeletePararrayo.setText("")
        self.btnDeleteTransfMed.setText("")
        self.btnAddTransfMed.setText("")
        self.btnDeleteConductor.setText("")
        self.btnAddConductores.setText("")
        self.btnDeleteBobina.setText("")
        self.btnAddBobina.setText("")
        self.label_15.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Compensador:</span></p></body></html>", None))
        self.btnAddCompensador.setText("")
        self.btnDeleteCompensador.setText("")
        self.btnPlano.setText(QCoreApplication.translate("NewBook", u"V\u00e9rtices Per\u00edmetro Plano Planta", None))
        self.btnCoordenadas.setText(QCoreApplication.translate("NewBook", u"V\u00e9rtice Per\u00edmetro Coordenadas Geograficas", None))
        self.label_empresa.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Empresa:</span></p></body></html>", None))
    # retranslateUi

