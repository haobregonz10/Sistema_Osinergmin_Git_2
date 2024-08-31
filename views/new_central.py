# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_central.ui'
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
        NewBook.resize(1368, 666)
        NewBook.setMinimumSize(QSize(1368, 666))
        NewBook.setMaximumSize(QSize(1368, 666))
        icon = QIcon()
        icon.addFile(u"./logo_feban.ico", QSize(), QIcon.Normal, QIcon.Off)
        NewBook.setWindowIcon(icon)
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
        self.label.setGeometry(QRect(10, 10, 1341, 41))
        font = QFont()
        font.setUnderline(False)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet(u"background-color: red;")
        self.label.setFrameShape(QFrame.Box)
        self.label_autoriza = QLabel(NewBook)
        self.label_autoriza.setObjectName(u"label_autoriza")
        self.label_autoriza.setGeometry(QRect(20, 70, 111, 21))
        font1 = QFont()
        font1.setPointSize(10)
        self.label_autoriza.setFont(font1)
        self.label_autoriza.setScaledContents(True)
        self.inputCodigo = QLineEdit(NewBook)
        self.inputCodigo.setObjectName(u"inputCodigo")
        self.inputCodigo.setGeometry(QRect(20, 90, 111, 31))
        font2 = QFont()
        font2.setPointSize(12)
        self.inputCodigo.setFont(font2)
        self.inputCodigo.setMaxLength(20)
        self.inputNombre = QLineEdit(NewBook)
        self.inputNombre.setObjectName(u"inputNombre")
        self.inputNombre.setGeometry(QRect(140, 90, 221, 31))
        self.inputNombre.setFont(font2)
        self.inputNombre.setMaxLength(50)
        self.addButton = QPushButton(NewBook)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setGeometry(QRect(300, 610, 291, 41))
        font3 = QFont()
        font3.setPointSize(14)
        font3.setBold(True)
        font3.setWeight(75)
        self.addButton.setFont(font3)
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
        self.cancelButton = QPushButton(NewBook)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setGeometry(QRect(630, 610, 271, 41))
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
        icon2.addFile(u"./assets/icons/cancel-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cancelButton.setIcon(icon2)
        self.cancelButton.setIconSize(QSize(30, 30))
        self.cancelButton.setAutoDefault(True)
        self.cancelButton.setFlat(True)
        self.label_aquienVisita = QLabel(NewBook)
        self.label_aquienVisita.setObjectName(u"label_aquienVisita")
        self.label_aquienVisita.setGeometry(QRect(140, 70, 221, 21))
        font4 = QFont()
        font4.setPointSize(5)
        self.label_aquienVisita.setFont(font4)
        self.label_aquienVisita.setScaledContents(True)
        self.label_area = QLabel(NewBook)
        self.label_area.setObjectName(u"label_area")
        self.label_area.setGeometry(QRect(500, 70, 201, 21))
        self.label_area.setScaledContents(True)
        self.inputCaudalDisenio = QLineEdit(NewBook)
        self.inputCaudalDisenio.setObjectName(u"inputCaudalDisenio")
        self.inputCaudalDisenio.setGeometry(QRect(160, 160, 141, 31))
        self.inputCaudalDisenio.setFont(font2)
        self.inputCaudalDisenio.setMaxLength(10)
        self.label_fecha = QLabel(NewBook)
        self.label_fecha.setObjectName(u"label_fecha")
        self.label_fecha.setGeometry(QRect(1220, 70, 131, 16))
        self.label_fecha.setScaledContents(True)
        self.label_visitante = QLabel(NewBook)
        self.label_visitante.setObjectName(u"label_visitante")
        self.label_visitante.setGeometry(QRect(160, 140, 141, 21))
        self.label_visitante.setScaledContents(True)
        self.inputCoefProduccion = QLineEdit(NewBook)
        self.inputCoefProduccion.setObjectName(u"inputCoefProduccion")
        self.inputCoefProduccion.setGeometry(QRect(310, 160, 151, 31))
        self.inputCoefProduccion.setFont(font2)
        self.inputCoefProduccion.setMaxLength(10)
        self.label_entidad = QLabel(NewBook)
        self.label_entidad.setObjectName(u"label_entidad")
        self.label_entidad.setGeometry(QRect(310, 140, 151, 21))
        self.label_entidad.setScaledContents(True)
        self.label_horaIngreso = QLabel(NewBook)
        self.label_horaIngreso.setObjectName(u"label_horaIngreso")
        self.label_horaIngreso.setGeometry(QRect(1070, 140, 141, 16))
        self.label_horaSalida = QLabel(NewBook)
        self.label_horaSalida.setObjectName(u"label_horaSalida")
        self.label_horaSalida.setGeometry(QRect(1220, 140, 131, 16))
        self.label_horaSalida.setScaledContents(True)
        self.label_motivoVisita = QLabel(NewBook)
        self.label_motivoVisita.setObjectName(u"label_motivoVisita")
        self.label_motivoVisita.setGeometry(QRect(20, 210, 131, 21))
        self.label_motivoVisita.setScaledContents(True)
        self.inputAltitud = QLineEdit(NewBook)
        self.inputAltitud.setObjectName(u"inputAltitud")
        self.inputAltitud.setGeometry(QRect(20, 160, 131, 31))
        self.inputAltitud.setFont(font2)
        self.inputAltitud.setInputMethodHints(Qt.ImhDigitsOnly)
        self.inputAltitud.setMaxLength(4)
        self.label_dni = QLabel(NewBook)
        self.label_dni.setObjectName(u"label_dni")
        self.label_dni.setGeometry(QRect(20, 140, 91, 21))
        self.label_dni.setScaledContents(True)
        self.inputTelefono = QLineEdit(NewBook)
        self.inputTelefono.setObjectName(u"inputTelefono")
        self.inputTelefono.setGeometry(QRect(1070, 160, 141, 31))
        self.inputTelefono.setFont(font2)
        self.inputTelefono.setMaxLength(15)
        self.inputDatum = QLineEdit(NewBook)
        self.inputDatum.setObjectName(u"inputDatum")
        self.inputDatum.setGeometry(QRect(160, 230, 101, 31))
        self.inputDatum.setFont(font2)
        self.inputDatum.setMaxLength(10)
        self.label_nota_obligatoria = QLabel(NewBook)
        self.label_nota_obligatoria.setObjectName(u"label_nota_obligatoria")
        self.label_nota_obligatoria.setGeometry(QRect(20, 590, 281, 21))
        self.ast_aquienvisita = QLabel(NewBook)
        self.ast_aquienvisita.setObjectName(u"ast_aquienvisita")
        self.ast_aquienvisita.setGeometry(QRect(70, 70, 21, 21))
        self.ast_area = QLabel(NewBook)
        self.ast_area.setObjectName(u"ast_area")
        self.ast_area.setGeometry(QRect(70, 70, 21, 21))
        self.ast_entidadempresa = QLabel(NewBook)
        self.ast_entidadempresa.setObjectName(u"ast_entidadempresa")
        self.ast_entidadempresa.setGeometry(QRect(70, 70, 21, 21))
        self.ast_motivo = QLabel(NewBook)
        self.ast_motivo.setObjectName(u"ast_motivo")
        self.ast_motivo.setGeometry(QRect(70, 70, 21, 21))
        self.ast_dni = QLabel(NewBook)
        self.ast_dni.setObjectName(u"ast_dni")
        self.ast_dni.setGeometry(QRect(70, 70, 21, 21))
        self.ast_horaingreso = QLabel(NewBook)
        self.ast_horaingreso.setObjectName(u"ast_horaingreso")
        self.ast_horaingreso.setGeometry(QRect(70, 70, 21, 21))
        self.ast_fecha = QLabel(NewBook)
        self.ast_fecha.setObjectName(u"ast_fecha")
        self.ast_fecha.setGeometry(QRect(70, 70, 21, 21))
        self.ast_visitante = QLabel(NewBook)
        self.ast_visitante.setObjectName(u"ast_visitante")
        self.ast_visitante.setGeometry(QRect(70, 70, 21, 21))
        self.inputConsumoPropio = QLineEdit(NewBook)
        self.inputConsumoPropio.setObjectName(u"inputConsumoPropio")
        self.inputConsumoPropio.setGeometry(QRect(470, 160, 151, 31))
        self.inputConsumoPropio.setFont(font2)
        self.inputConsumoPropio.setMaxLength(10)
        self.label_advertencia_dni = QLabel(NewBook)
        self.label_advertencia_dni.setObjectName(u"label_advertencia_dni")
        self.label_advertencia_dni.setGeometry(QRect(20, 590, 251, 21))
        self.cbTipo = QComboBox(NewBook)
        self.cbTipo.setObjectName(u"cbTipo")
        self.cbTipo.setGeometry(QRect(370, 90, 121, 31))
        self.cbTipo.setFont(font2)
        self.cbTipo.setEditable(False)
        self.label_area_2 = QLabel(NewBook)
        self.label_area_2.setObjectName(u"label_area_2")
        self.label_area_2.setGeometry(QRect(370, 70, 121, 21))
        self.label_area_2.setScaledContents(True)
        self.cbDemanda = QComboBox(NewBook)
        self.cbDemanda.setObjectName(u"cbDemanda")
        self.cbDemanda.setGeometry(QRect(500, 90, 201, 31))
        self.cbDemanda.setFont(font2)
        self.cbDemanda.setEditable(False)
        self.cbTipoSistema = QComboBox(NewBook)
        self.cbTipoSistema.setObjectName(u"cbTipoSistema")
        self.cbTipoSistema.setGeometry(QRect(710, 90, 131, 31))
        self.cbTipoSistema.setFont(font2)
        self.cbTipoSistema.setEditable(False)
        self.label_area_3 = QLabel(NewBook)
        self.label_area_3.setObjectName(u"label_area_3")
        self.label_area_3.setGeometry(QRect(710, 70, 131, 21))
        self.label_area_3.setScaledContents(True)
        self.label_area_4 = QLabel(NewBook)
        self.label_area_4.setObjectName(u"label_area_4")
        self.label_area_4.setGeometry(QRect(850, 70, 131, 21))
        self.label_area_4.setScaledContents(True)
        self.cbAreaOperativa = QComboBox(NewBook)
        self.cbAreaOperativa.setObjectName(u"cbAreaOperativa")
        self.cbAreaOperativa.setGeometry(QRect(850, 90, 131, 31))
        self.cbAreaOperativa.setFont(font2)
        self.cbAreaOperativa.setEditable(False)
        self.cbRegion = QComboBox(NewBook)
        self.cbRegion.setObjectName(u"cbRegion")
        self.cbRegion.setGeometry(QRect(990, 90, 221, 31))
        self.cbRegion.setFont(font2)
        self.cbRegion.setEditable(False)
        self.label_area_5 = QLabel(NewBook)
        self.label_area_5.setObjectName(u"label_area_5")
        self.label_area_5.setGeometry(QRect(990, 70, 221, 21))
        self.label_area_5.setScaledContents(True)
        self.cbZona = QComboBox(NewBook)
        self.cbZona.setObjectName(u"cbZona")
        self.cbZona.setGeometry(QRect(1220, 90, 131, 31))
        self.cbZona.setFont(font2)
        self.cbZona.setEditable(False)
        self.label_entidad_2 = QLabel(NewBook)
        self.label_entidad_2.setObjectName(u"label_entidad_2")
        self.label_entidad_2.setGeometry(QRect(470, 140, 151, 21))
        self.label_entidad_2.setScaledContents(True)
        self.inputDireccion = QLineEdit(NewBook)
        self.inputDireccion.setObjectName(u"inputDireccion")
        self.inputDireccion.setGeometry(QRect(630, 160, 431, 31))
        self.inputDireccion.setFont(font2)
        self.inputDireccion.setMaxLength(150)
        self.label_entidad_3 = QLabel(NewBook)
        self.label_entidad_3.setObjectName(u"label_entidad_3")
        self.label_entidad_3.setGeometry(QRect(630, 140, 431, 21))
        self.label_entidad_3.setScaledContents(True)
        self.inputZonaUTM = QLineEdit(NewBook)
        self.inputZonaUTM.setObjectName(u"inputZonaUTM")
        self.inputZonaUTM.setGeometry(QRect(270, 230, 111, 31))
        self.inputZonaUTM.setFont(font2)
        self.inputZonaUTM.setMaxLength(5)
        self.cbEstado = QComboBox(NewBook)
        self.cbEstado.setObjectName(u"cbEstado")
        self.cbEstado.setGeometry(QRect(1220, 160, 131, 31))
        self.cbEstado.setFont(font2)
        self.cbEstado.setEditable(False)
        self.inputFechaAlta = QDateEdit(NewBook)
        self.inputFechaAlta.setObjectName(u"inputFechaAlta")
        self.inputFechaAlta.setGeometry(QRect(20, 230, 131, 31))
        font5 = QFont()
        font5.setPointSize(11)
        font5.setBold(False)
        font5.setWeight(50)
        self.inputFechaAlta.setFont(font5)
        self.label_motivoVisita_2 = QLabel(NewBook)
        self.label_motivoVisita_2.setObjectName(u"label_motivoVisita_2")
        self.label_motivoVisita_2.setGeometry(QRect(160, 210, 111, 21))
        self.label_motivoVisita_2.setScaledContents(True)
        self.label_motivoVisita_3 = QLabel(NewBook)
        self.label_motivoVisita_3.setObjectName(u"label_motivoVisita_3")
        self.label_motivoVisita_3.setGeometry(QRect(270, 210, 111, 21))
        self.label_motivoVisita_3.setScaledContents(True)
        self.label_4 = QLabel(NewBook)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 320, 80, 30))
        self.label_4.setScaledContents(True)
        self.btnDeleteGenerador = QPushButton(NewBook)
        self.btnDeleteGenerador.setObjectName(u"btnDeleteGenerador")
        self.btnDeleteGenerador.setGeometry(QRect(150, 320, 24, 30))
        font6 = QFont()
        font6.setPointSize(12)
        font6.setBold(True)
        font6.setWeight(75)
        self.btnDeleteGenerador.setFont(font6)
        self.btnDeleteGenerador.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnDeleteGenerador.setStyleSheet(u"QPushButton\n"
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
        icon3 = QIcon()
        icon3.addFile(u"./assets/icons/deletesquare.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnDeleteGenerador.setIcon(icon3)
        self.btnDeleteGenerador.setIconSize(QSize(25, 25))
        self.btnDeleteGenerador.setAutoDefault(True)
        self.btnDeleteGenerador.setFlat(True)
        self.btnAddGeneradores = QPushButton(NewBook)
        self.btnAddGeneradores.setObjectName(u"btnAddGeneradores")
        self.btnAddGeneradores.setGeometry(QRect(120, 320, 24, 30))
        self.btnAddGeneradores.setFont(font6)
        self.btnAddGeneradores.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnAddGeneradores.setStyleSheet(u"QPushButton\n"
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
        self.btnAddGeneradores.setIcon(icon1)
        self.btnAddGeneradores.setIconSize(QSize(25, 25))
        self.btnAddGeneradores.setAutoDefault(True)
        self.btnAddGeneradores.setFlat(True)
        self.btnAddCeldas = QPushButton(NewBook)
        self.btnAddCeldas.setObjectName(u"btnAddCeldas")
        self.btnAddCeldas.setGeometry(QRect(290, 320, 24, 30))
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
        self.btnAddCeldas.setIcon(icon1)
        self.btnAddCeldas.setIconSize(QSize(25, 25))
        self.btnAddCeldas.setAutoDefault(True)
        self.btnAddCeldas.setFlat(True)
        self.btnDeleteCeldas = QPushButton(NewBook)
        self.btnDeleteCeldas.setObjectName(u"btnDeleteCeldas")
        self.btnDeleteCeldas.setGeometry(QRect(320, 320, 24, 30))
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
        self.btnDeleteCeldas.setIcon(icon3)
        self.btnDeleteCeldas.setIconSize(QSize(25, 25))
        self.btnDeleteCeldas.setAutoDefault(True)
        self.btnDeleteCeldas.setFlat(True)
        self.label_5 = QLabel(NewBook)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(190, 320, 43, 30))
        self.label_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_5.setMargin(0)
        self.label_6 = QLabel(NewBook)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(360, 320, 42, 30))
        self.btnDeleteBarras = QPushButton(NewBook)
        self.btnDeleteBarras.setObjectName(u"btnDeleteBarras")
        self.btnDeleteBarras.setGeometry(QRect(490, 320, 24, 30))
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
        self.btnDeleteBarras.setIcon(icon3)
        self.btnDeleteBarras.setIconSize(QSize(25, 25))
        self.btnDeleteBarras.setAutoDefault(True)
        self.btnDeleteBarras.setFlat(True)
        self.btnAddBarras = QPushButton(NewBook)
        self.btnAddBarras.setObjectName(u"btnAddBarras")
        self.btnAddBarras.setGeometry(QRect(460, 320, 24, 30))
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
        self.btnAddBarras.setIcon(icon1)
        self.btnAddBarras.setIconSize(QSize(25, 25))
        self.btnAddBarras.setAutoDefault(True)
        self.btnAddBarras.setFlat(True)
        self.btnDeletePorticos = QPushButton(NewBook)
        self.btnDeletePorticos.setObjectName(u"btnDeletePorticos")
        self.btnDeletePorticos.setGeometry(QRect(650, 320, 24, 30))
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
        self.btnDeletePorticos.setIcon(icon3)
        self.btnDeletePorticos.setIconSize(QSize(25, 25))
        self.btnDeletePorticos.setAutoDefault(True)
        self.btnDeletePorticos.setFlat(True)
        self.btnAddPorticos = QPushButton(NewBook)
        self.btnAddPorticos.setObjectName(u"btnAddPorticos")
        self.btnAddPorticos.setGeometry(QRect(620, 320, 24, 30))
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
        self.btnAddPorticos.setIcon(icon1)
        self.btnAddPorticos.setIconSize(QSize(25, 25))
        self.btnAddPorticos.setAutoDefault(True)
        self.btnAddPorticos.setFlat(True)
        self.label_7 = QLabel(NewBook)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(530, 320, 54, 30))
        self.label_7.setScaledContents(True)
        self.tableGeneradores = QTableWidget(NewBook)
        self.tableGeneradores.setObjectName(u"tableGeneradores")
        self.tableGeneradores.setGeometry(QRect(20, 350, 155, 233))
        self.tableGeneradores.setAutoFillBackground(True)
        self.tableGeneradores.setLineWidth(5)
        self.tableGeneradores.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableGeneradores.setTextElideMode(Qt.ElideLeft)
        self.tableGeneradores.horizontalHeader().setMinimumSectionSize(10)
        self.tableCeldas = QTableWidget(NewBook)
        self.tableCeldas.setObjectName(u"tableCeldas")
        self.tableCeldas.setGeometry(QRect(190, 350, 155, 233))
        self.tableCeldas.setAutoFillBackground(True)
        self.tableCeldas.setLineWidth(5)
        self.tableCeldas.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableCeldas.setTextElideMode(Qt.ElideLeft)
        self.tableCeldas.horizontalHeader().setMinimumSectionSize(10)
        self.tableBarras = QTableWidget(NewBook)
        self.tableBarras.setObjectName(u"tableBarras")
        self.tableBarras.setGeometry(QRect(360, 350, 155, 233))
        self.tableBarras.setAutoFillBackground(True)
        self.tableBarras.setLineWidth(5)
        self.tableBarras.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableBarras.setTextElideMode(Qt.ElideLeft)
        self.tableBarras.horizontalHeader().setMinimumSectionSize(10)
        self.tablePorticos = QTableWidget(NewBook)
        self.tablePorticos.setObjectName(u"tablePorticos")
        self.tablePorticos.setGeometry(QRect(530, 350, 150, 233))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tablePorticos.sizePolicy().hasHeightForWidth())
        self.tablePorticos.setSizePolicy(sizePolicy)
        self.tablePorticos.setAutoFillBackground(True)
        self.tablePorticos.setLineWidth(5)
        self.tablePorticos.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tablePorticos.setTextElideMode(Qt.ElideLeft)
        self.tablePorticos.horizontalHeader().setMinimumSectionSize(10)
        self.btnDeletePararrayo = QPushButton(NewBook)
        self.btnDeletePararrayo.setObjectName(u"btnDeletePararrayo")
        self.btnDeletePararrayo.setGeometry(QRect(990, 320, 24, 30))
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
        self.btnDeletePararrayo.setIcon(icon3)
        self.btnDeletePararrayo.setIconSize(QSize(25, 25))
        self.btnDeletePararrayo.setAutoDefault(True)
        self.btnDeletePararrayo.setFlat(True)
        self.btnAddTransformadores = QPushButton(NewBook)
        self.btnAddTransformadores.setObjectName(u"btnAddTransformadores")
        self.btnAddTransformadores.setGeometry(QRect(790, 320, 24, 30))
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
        self.btnAddTransformadores.setIcon(icon1)
        self.btnAddTransformadores.setIconSize(QSize(25, 25))
        self.btnAddTransformadores.setAutoDefault(True)
        self.btnAddTransformadores.setFlat(True)
        self.btnDeleteTransformador = QPushButton(NewBook)
        self.btnDeleteTransformador.setObjectName(u"btnDeleteTransformador")
        self.btnDeleteTransformador.setGeometry(QRect(820, 320, 24, 30))
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
        self.btnDeleteTransformador.setIcon(icon3)
        self.btnDeleteTransformador.setIconSize(QSize(25, 25))
        self.btnDeleteTransformador.setAutoDefault(True)
        self.btnDeleteTransformador.setFlat(True)
        self.btnAddPararrayo = QPushButton(NewBook)
        self.btnAddPararrayo.setObjectName(u"btnAddPararrayo")
        self.btnAddPararrayo.setGeometry(QRect(960, 320, 24, 30))
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
        self.btnAddPararrayo.setIcon(icon1)
        self.btnAddPararrayo.setIconSize(QSize(25, 25))
        self.btnAddPararrayo.setAutoDefault(True)
        self.btnAddPararrayo.setFlat(True)
        self.label_11 = QLabel(NewBook)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(690, 330, 107, 16))
        self.label_12 = QLabel(NewBook)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(860, 330, 63, 16))
        self.btnDeleteConductor = QPushButton(NewBook)
        self.btnDeleteConductor.setObjectName(u"btnDeleteConductor")
        self.btnDeleteConductor.setGeometry(QRect(1330, 320, 24, 30))
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
        self.btnDeleteConductor.setIcon(icon3)
        self.btnDeleteConductor.setIconSize(QSize(25, 25))
        self.btnDeleteConductor.setAutoDefault(True)
        self.btnDeleteConductor.setFlat(True)
        self.label_14 = QLabel(NewBook)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(1200, 330, 82, 16))
        self.label_14.setFont(font1)
        self.label_13 = QLabel(NewBook)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(1030, 330, 111, 16))
        font7 = QFont()
        font7.setPointSize(7)
        self.label_13.setFont(font7)
        self.btnDeleteTransfMed = QPushButton(NewBook)
        self.btnDeleteTransfMed.setObjectName(u"btnDeleteTransfMed")
        self.btnDeleteTransfMed.setGeometry(QRect(1160, 320, 24, 30))
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
        self.btnDeleteTransfMed.setIcon(icon3)
        self.btnDeleteTransfMed.setIconSize(QSize(25, 25))
        self.btnDeleteTransfMed.setAutoDefault(True)
        self.btnDeleteTransfMed.setFlat(True)
        self.btnAddConductores = QPushButton(NewBook)
        self.btnAddConductores.setObjectName(u"btnAddConductores")
        self.btnAddConductores.setGeometry(QRect(1300, 320, 24, 30))
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
        self.btnAddConductores.setIcon(icon1)
        self.btnAddConductores.setIconSize(QSize(25, 25))
        self.btnAddConductores.setAutoDefault(True)
        self.btnAddConductores.setFlat(True)
        self.btnAddTransfMed = QPushButton(NewBook)
        self.btnAddTransfMed.setObjectName(u"btnAddTransfMed")
        self.btnAddTransfMed.setGeometry(QRect(1130, 320, 24, 30))
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
        self.btnAddTransfMed.setIcon(icon1)
        self.btnAddTransfMed.setIconSize(QSize(25, 25))
        self.btnAddTransfMed.setAutoDefault(True)
        self.btnAddTransfMed.setFlat(True)
        self.tablePararrayo = QTableWidget(NewBook)
        self.tablePararrayo.setObjectName(u"tablePararrayo")
        self.tablePararrayo.setGeometry(QRect(860, 350, 155, 232))
        sizePolicy.setHeightForWidth(self.tablePararrayo.sizePolicy().hasHeightForWidth())
        self.tablePararrayo.setSizePolicy(sizePolicy)
        self.tablePararrayo.setAutoFillBackground(True)
        self.tablePararrayo.setLineWidth(5)
        self.tablePararrayo.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tablePararrayo.setTextElideMode(Qt.ElideLeft)
        self.tablePararrayo.horizontalHeader().setMinimumSectionSize(10)
        self.tableConductor = QTableWidget(NewBook)
        self.tableConductor.setObjectName(u"tableConductor")
        self.tableConductor.setGeometry(QRect(1200, 350, 155, 232))
        self.tableConductor.setAutoFillBackground(True)
        self.tableConductor.setLineWidth(5)
        self.tableConductor.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableConductor.setTextElideMode(Qt.ElideLeft)
        self.tableConductor.horizontalHeader().setMinimumSectionSize(10)
        self.tableMedicion = QTableWidget(NewBook)
        self.tableMedicion.setObjectName(u"tableMedicion")
        self.tableMedicion.setGeometry(QRect(1030, 350, 155, 232))
        self.tableMedicion.setAutoFillBackground(True)
        self.tableMedicion.setLineWidth(5)
        self.tableMedicion.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableMedicion.setTextElideMode(Qt.ElideLeft)
        self.tableMedicion.horizontalHeader().setMinimumSectionSize(10)
        self.tableTransformador = QTableWidget(NewBook)
        self.tableTransformador.setObjectName(u"tableTransformador")
        self.tableTransformador.setGeometry(QRect(690, 350, 155, 232))
        self.tableTransformador.setAutoFillBackground(True)
        self.tableTransformador.setLineWidth(5)
        self.tableTransformador.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableTransformador.setTextElideMode(Qt.ElideLeft)
        self.tableTransformador.horizontalHeader().setMinimumSectionSize(10)
        self.btnCoordenadas = QPushButton(NewBook)
        self.btnCoordenadas.setObjectName(u"btnCoordenadas")
        self.btnCoordenadas.setGeometry(QRect(520, 230, 411, 31))
        font8 = QFont()
        font8.setPointSize(11)
        font8.setBold(True)
        font8.setWeight(75)
        self.btnCoordenadas.setFont(font8)
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
        self.btnCoordenadas.setIcon(icon1)
        self.btnCoordenadas.setIconSize(QSize(25, 25))
        self.btnCoordenadas.setAutoDefault(True)
        self.btnCoordenadas.setFlat(True)
        self.btnPlano = QPushButton(NewBook)
        self.btnPlano.setObjectName(u"btnPlano")
        self.btnPlano.setGeometry(QRect(940, 230, 411, 31))
        self.btnPlano.setFont(font8)
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
        self.btnPlano.setIcon(icon1)
        self.btnPlano.setIconSize(QSize(25, 25))
        self.btnPlano.setAutoDefault(True)
        self.btnPlano.setFlat(True)
        self.label_empresa = QLabel(NewBook)
        self.label_empresa.setObjectName(u"label_empresa")
        self.label_empresa.setGeometry(QRect(390, 210, 111, 21))
        self.label_empresa.setScaledContents(True)
        self.inputCodEmpresa = QLineEdit(NewBook)
        self.inputCodEmpresa.setObjectName(u"inputCodEmpresa")
        self.inputCodEmpresa.setGeometry(QRect(390, 230, 121, 31))
        self.inputCodEmpresa.setFont(font2)
        self.inputCodEmpresa.setMaxLength(5)
        QWidget.setTabOrder(self.inputCodigo, self.inputNombre)
        QWidget.setTabOrder(self.inputNombre, self.inputAltitud)
        QWidget.setTabOrder(self.inputAltitud, self.inputCaudalDisenio)
        QWidget.setTabOrder(self.inputCaudalDisenio, self.inputCoefProduccion)
        QWidget.setTabOrder(self.inputCoefProduccion, self.inputTelefono)
        QWidget.setTabOrder(self.inputTelefono, self.inputDatum)
        QWidget.setTabOrder(self.inputDatum, self.inputConsumoPropio)
        QWidget.setTabOrder(self.inputConsumoPropio, self.addButton)
        QWidget.setTabOrder(self.addButton, self.cancelButton)

        self.retranslateUi(NewBook)

        self.addButton.setDefault(True)
        self.cancelButton.setDefault(True)
        self.btnDeleteGenerador.setDefault(True)
        self.btnAddGeneradores.setDefault(True)
        self.btnAddCeldas.setDefault(True)
        self.btnDeleteCeldas.setDefault(True)
        self.btnDeleteBarras.setDefault(True)
        self.btnAddBarras.setDefault(True)
        self.btnDeletePorticos.setDefault(True)
        self.btnAddPorticos.setDefault(True)
        self.btnDeletePararrayo.setDefault(True)
        self.btnAddTransformadores.setDefault(True)
        self.btnDeleteTransformador.setDefault(True)
        self.btnAddPararrayo.setDefault(True)
        self.btnDeleteConductor.setDefault(True)
        self.btnDeleteTransfMed.setDefault(True)
        self.btnAddConductores.setDefault(True)
        self.btnAddTransfMed.setDefault(True)
        self.btnCoordenadas.setDefault(True)
        self.btnPlano.setDefault(True)


        QMetaObject.connectSlotsByName(NewBook)
    # setupUi

    def retranslateUi(self, NewBook):
        NewBook.setWindowTitle(QCoreApplication.translate("NewBook", u"Nuevo Registro", None))
        self.label.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">CENTRALES DE GENERACION</span></p></body></html>", None))
        self.label_autoriza.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Codigo:</span></p></body></html>", None))
        self.addButton.setText(QCoreApplication.translate("NewBook", u"AGREGAR", None))
        self.cancelButton.setText(QCoreApplication.translate("NewBook", u"CANCELAR", None))
        self.label_aquienVisita.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Nombre:</span></p></body></html>", None))
        self.label_area.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">\u00c1rea de Demanda:</span></p></body></html>", None))
        self.label_fecha.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Zona:</span></p></body></html>", None))
        self.label_visitante.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Caudal Dise\u00f1o:</span></p></body></html>", None))
        self.label_entidad.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Coef. Producci\u00f3n:</span></p></body></html>", None))
        self.label_horaIngreso.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Tel\u00e9fono:</span></p></body></html>", None))
        self.label_horaSalida.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Estado:</span></p></body></html>", None))
        self.label_motivoVisita.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Fecha de Alta:</span></p></body></html>", None))
        self.label_dni.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Altitud:</span></p></body></html>", None))
        self.label_nota_obligatoria.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; font-style:italic; color:#ff0000;\">(*) El c\u00f3digo es obligatorio</span></p></body></html>", None))
        self.ast_aquienvisita.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ff0000;\">*</span></p></body></html>", None))
        self.ast_area.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ff0000;\">*</span></p></body></html>", None))
        self.ast_entidadempresa.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ff0000;\">*</span></p></body></html>", None))
        self.ast_motivo.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ff0000;\">*</span></p></body></html>", None))
        self.ast_dni.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ff0000;\">*</span></p></body></html>", None))
        self.ast_horaingreso.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ff0000;\">*</span></p></body></html>", None))
        self.ast_fecha.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ff0000;\">*</span></p></body></html>", None))
        self.ast_visitante.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ff0000;\">*</span></p></body></html>", None))
        self.label_advertencia_dni.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; font-style:italic; color:#ff0000;\">(*) El c\u00f3digo es obligatorio</span></p></body></html>", None))
        self.label_area_2.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Tipo:</span></p></body></html>", None))
        self.label_area_3.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Tipo Sistema:</span></p></body></html>", None))
        self.label_area_4.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">\u00c1rea Operativa:</span></p></body></html>", None))
        self.label_area_5.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Regi\u00f3n Geogr\u00e1fica:</span></p></body></html>", None))
        self.label_entidad_2.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Consumo Propio:</span></p></body></html>", None))
        self.label_entidad_3.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Direcci\u00f3n:</span></p></body></html>", None))
        self.label_motivoVisita_2.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Datum UTM:</span></p></body></html>", None))
        self.label_motivoVisita_3.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Zona UTM:</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Generadores:</span></p></body></html>", None))
        self.btnDeleteGenerador.setText("")
        self.btnAddGeneradores.setText("")
        self.btnAddCeldas.setText("")
        self.btnDeleteCeldas.setText("")
        self.label_5.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Celdas:</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Barras:</span></p></body></html>", None))
        self.btnDeleteBarras.setText("")
        self.btnAddBarras.setText("")
        self.btnDeletePorticos.setText("")
        self.btnAddPorticos.setText("")
        self.label_7.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">P\u00f3rticos:</span></p></body></html>", None))
        self.btnDeletePararrayo.setText("")
        self.btnAddTransformadores.setText("")
        self.btnDeleteTransformador.setText("")
        self.btnAddPararrayo.setText("")
        self.label_11.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Transformador:</span></p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Pararrayo:</span></p></body></html>", None))
        self.btnDeleteConductor.setText("")
        self.label_14.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Conductores:</span></p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Transf.Med.:</span></p></body></html>", None))
        self.btnDeleteTransfMed.setText("")
        self.btnAddConductores.setText("")
        self.btnAddTransfMed.setText("")
        self.btnCoordenadas.setText(QCoreApplication.translate("NewBook", u"V\u00e9rtice Per\u00edmetro Coordenadas Geograficas", None))
        self.btnPlano.setText(QCoreApplication.translate("NewBook", u"V\u00e9rtices Per\u00edmetro Plano Planta", None))
        self.label_empresa.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Empresa:</span></p></body></html>", None))
    # retranslateUi

