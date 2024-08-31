# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_central_transformador.ui'
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
        NewBook.resize(946, 576)
        NewBook.setMinimumSize(QSize(946, 576))
        NewBook.setMaximumSize(QSize(946, 576))
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
        self.label.setGeometry(QRect(20, 10, 911, 41))
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
        self.inputCodigo.setGeometry(QRect(20, 95, 141, 31))
        font1 = QFont()
        font1.setPointSize(12)
        self.inputCodigo.setFont(font1)
        self.inputCodigo.setMaxLength(15)
        self.inputCentral = QLineEdit(NewBook)
        self.inputCentral.setObjectName(u"inputCentral")
        self.inputCentral.setGeometry(QRect(170, 95, 241, 31))
        self.inputCentral.setFont(font1)
        self.addButton = QPushButton(NewBook)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setGeometry(QRect(170, 520, 291, 41))
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
        self.cancelButton.setGeometry(QRect(490, 520, 271, 41))
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
        self.label_aquienVisita.setGeometry(QRect(170, 70, 191, 25))
        self.label_area = QLabel(NewBook)
        self.label_area.setObjectName(u"label_area")
        self.label_area.setGeometry(QRect(660, 70, 191, 25))
        self.label_horaSalida = QLabel(NewBook)
        self.label_horaSalida.setObjectName(u"label_horaSalida")
        self.label_horaSalida.setGeometry(QRect(410, 310, 81, 25))
        self.label_motivoVisita = QLabel(NewBook)
        self.label_motivoVisita.setObjectName(u"label_motivoVisita")
        self.label_motivoVisita.setGeometry(QRect(540, 310, 131, 25))
        self.label_nota_obligatoria = QLabel(NewBook)
        self.label_nota_obligatoria.setObjectName(u"label_nota_obligatoria")
        self.label_nota_obligatoria.setGeometry(QRect(20, 500, 281, 21))
        self.ast_aquienvisita = QLabel(NewBook)
        self.ast_aquienvisita.setObjectName(u"ast_aquienvisita")
        self.ast_aquienvisita.setGeometry(QRect(70, 70, 21, 25))
        self.label_advertencia_dni = QLabel(NewBook)
        self.label_advertencia_dni.setObjectName(u"label_advertencia_dni")
        self.label_advertencia_dni.setGeometry(QRect(20, 500, 251, 21))
        self.cbEstado = QComboBox(NewBook)
        self.cbEstado.setObjectName(u"cbEstado")
        self.cbEstado.setGeometry(QRect(410, 335, 121, 31))
        self.cbEstado.setFont(font1)
        self.cbEstado.setEditable(False)
        self.inputFecha = QDateEdit(NewBook)
        self.inputFecha.setObjectName(u"inputFecha")
        self.inputFecha.setGeometry(QRect(540, 335, 131, 31))
        font3 = QFont()
        font3.setPointSize(11)
        font3.setBold(False)
        font3.setWeight(50)
        self.inputFecha.setFont(font3)
        self.cbTipo = QComboBox(NewBook)
        self.cbTipo.setObjectName(u"cbTipo")
        self.cbTipo.setGeometry(QRect(420, 95, 231, 31))
        self.cbTipo.setFont(font1)
        self.cbTipo.setEditable(False)
        self.label_area_3 = QLabel(NewBook)
        self.label_area_3.setObjectName(u"label_area_3")
        self.label_area_3.setGeometry(QRect(420, 70, 141, 25))
        self.inputMarca = QLineEdit(NewBook)
        self.inputMarca.setObjectName(u"inputMarca")
        self.inputMarca.setGeometry(QRect(530, 215, 121, 31))
        self.inputMarca.setFont(font1)
        self.inputMarca.setMaxLength(50)
        self.label_autoriza_2 = QLabel(NewBook)
        self.label_autoriza_2.setObjectName(u"label_autoriza_2")
        self.label_autoriza_2.setGeometry(QRect(530, 190, 101, 25))
        self.inputAnio = QLineEdit(NewBook)
        self.inputAnio.setObjectName(u"inputAnio")
        self.inputAnio.setGeometry(QRect(660, 215, 91, 31))
        self.inputAnio.setFont(font1)
        self.inputAnio.setMaxLength(4)
        self.label_autoriza_3 = QLabel(NewBook)
        self.label_autoriza_3.setObjectName(u"label_autoriza_3")
        self.label_autoriza_3.setGeometry(QRect(660, 190, 101, 25))
        self.inputTipoInstalacion = QComboBox(NewBook)
        self.inputTipoInstalacion.setObjectName(u"inputTipoInstalacion")
        self.inputTipoInstalacion.setGeometry(QRect(660, 95, 271, 31))
        self.inputTipoInstalacion.setFont(font1)
        self.inputTipoInstalacion.setEditable(False)
        self.label_autoriza_4 = QLabel(NewBook)
        self.label_autoriza_4.setObjectName(u"label_autoriza_4")
        self.label_autoriza_4.setGeometry(QRect(430, 130, 151, 25))
        self.inputTension = QLineEdit(NewBook)
        self.inputTension.setObjectName(u"inputTension")
        self.inputTension.setGeometry(QRect(430, 155, 161, 31))
        self.inputTension.setFont(font1)
        self.inputTension.setMaxLength(8)
        self.inputConexion = QLineEdit(NewBook)
        self.inputConexion.setObjectName(u"inputConexion")
        self.inputConexion.setGeometry(QRect(20, 155, 211, 31))
        self.inputConexion.setFont(font1)
        self.inputConexion.setMaxLength(12)
        self.label_autoriza_5 = QLabel(NewBook)
        self.label_autoriza_5.setObjectName(u"label_autoriza_5")
        self.label_autoriza_5.setGeometry(QRect(20, 130, 151, 25))
        self.inputSerie = QLineEdit(NewBook)
        self.inputSerie.setObjectName(u"inputSerie")
        self.inputSerie.setGeometry(QRect(240, 155, 181, 31))
        self.inputSerie.setFont(font1)
        self.inputSerie.setMaxLength(30)
        self.label_autoriza_6 = QLabel(NewBook)
        self.label_autoriza_6.setObjectName(u"label_autoriza_6")
        self.label_autoriza_6.setGeometry(QRect(240, 130, 151, 25))
        self.inputTension2 = QLineEdit(NewBook)
        self.inputTension2.setObjectName(u"inputTension2")
        self.inputTension2.setGeometry(QRect(600, 155, 161, 31))
        self.inputTension2.setFont(font1)
        self.inputTension2.setMaxLength(8)
        self.label_autoriza_7 = QLabel(NewBook)
        self.label_autoriza_7.setObjectName(u"label_autoriza_7")
        self.label_autoriza_7.setGeometry(QRect(600, 130, 151, 25))
        self.label_autoriza_8 = QLabel(NewBook)
        self.label_autoriza_8.setObjectName(u"label_autoriza_8")
        self.label_autoriza_8.setGeometry(QRect(770, 130, 151, 25))
        self.inputTension3 = QLineEdit(NewBook)
        self.inputTension3.setObjectName(u"inputTension3")
        self.inputTension3.setGeometry(QRect(770, 155, 161, 31))
        self.inputTension3.setFont(font1)
        self.inputTension3.setMaxLength(8)
        self.label_autoriza_9 = QLabel(NewBook)
        self.label_autoriza_9.setObjectName(u"label_autoriza_9")
        self.label_autoriza_9.setGeometry(QRect(190, 190, 151, 25))
        self.inputPotenciaLado = QLineEdit(NewBook)
        self.inputPotenciaLado.setObjectName(u"inputPotenciaLado")
        self.inputPotenciaLado.setGeometry(QRect(20, 215, 161, 31))
        self.inputPotenciaLado.setFont(font1)
        self.inputPotenciaLado.setMaxLength(8)
        self.label_autoriza_10 = QLabel(NewBook)
        self.label_autoriza_10.setObjectName(u"label_autoriza_10")
        self.label_autoriza_10.setGeometry(QRect(20, 190, 151, 25))
        self.label_autoriza_11 = QLabel(NewBook)
        self.label_autoriza_11.setObjectName(u"label_autoriza_11")
        self.label_autoriza_11.setGeometry(QRect(360, 190, 151, 25))
        self.inputPotenciaLado3 = QLineEdit(NewBook)
        self.inputPotenciaLado3.setObjectName(u"inputPotenciaLado3")
        self.inputPotenciaLado3.setGeometry(QRect(360, 215, 161, 31))
        self.inputPotenciaLado3.setFont(font1)
        self.inputPotenciaLado3.setMaxLength(8)
        self.inputPotenciaLado2 = QLineEdit(NewBook)
        self.inputPotenciaLado2.setObjectName(u"inputPotenciaLado2")
        self.inputPotenciaLado2.setGeometry(QRect(190, 215, 161, 31))
        self.inputPotenciaLado2.setFont(font1)
        self.inputPotenciaLado2.setMaxLength(8)
        self.cbDisponibilidad = QComboBox(NewBook)
        self.cbDisponibilidad.setObjectName(u"cbDisponibilidad")
        self.cbDisponibilidad.setGeometry(QRect(760, 215, 171, 31))
        self.cbDisponibilidad.setFont(font1)
        self.cbDisponibilidad.setEditable(False)
        self.label_autoriza_12 = QLabel(NewBook)
        self.label_autoriza_12.setObjectName(u"label_autoriza_12")
        self.label_autoriza_12.setGeometry(QRect(760, 190, 131, 25))
        self.label_autoriza_13 = QLabel(NewBook)
        self.label_autoriza_13.setObjectName(u"label_autoriza_13")
        self.label_autoriza_13.setGeometry(QRect(20, 250, 111, 25))
        self.label_autoriza_14 = QLabel(NewBook)
        self.label_autoriza_14.setObjectName(u"label_autoriza_14")
        self.label_autoriza_14.setGeometry(QRect(380, 250, 171, 25))
        self.inputPotenciaBase = QLineEdit(NewBook)
        self.inputPotenciaBase.setObjectName(u"inputPotenciaBase")
        self.inputPotenciaBase.setGeometry(QRect(380, 275, 161, 31))
        self.inputPotenciaBase.setFont(font1)
        self.inputPotenciaBase.setMaxLength(8)
        self.label_autoriza_15 = QLabel(NewBook)
        self.label_autoriza_15.setObjectName(u"label_autoriza_15")
        self.label_autoriza_15.setGeometry(QRect(140, 250, 151, 25))
        self.inputVCC3 = QLineEdit(NewBook)
        self.inputVCC3.setObjectName(u"inputVCC3")
        self.inputVCC3.setGeometry(QRect(260, 275, 111, 31))
        self.inputVCC3.setFont(font1)
        self.inputVCC3.setMaxLength(8)
        self.inputVCC = QLineEdit(NewBook)
        self.inputVCC.setObjectName(u"inputVCC")
        self.inputVCC.setGeometry(QRect(20, 275, 111, 31))
        self.inputVCC.setFont(font1)
        self.inputVCC.setMaxLength(8)
        self.label_autoriza_16 = QLabel(NewBook)
        self.label_autoriza_16.setObjectName(u"label_autoriza_16")
        self.label_autoriza_16.setGeometry(QRect(260, 250, 151, 25))
        self.inputVCC2 = QLineEdit(NewBook)
        self.inputVCC2.setObjectName(u"inputVCC2")
        self.inputVCC2.setGeometry(QRect(140, 275, 111, 31))
        self.inputVCC2.setFont(font1)
        self.inputVCC2.setMaxLength(8)
        self.label_autoriza_17 = QLabel(NewBook)
        self.label_autoriza_17.setObjectName(u"label_autoriza_17")
        self.label_autoriza_17.setGeometry(QRect(810, 250, 151, 25))
        self.label_autoriza_18 = QLabel(NewBook)
        self.label_autoriza_18.setObjectName(u"label_autoriza_18")
        self.label_autoriza_18.setGeometry(QRect(680, 250, 151, 25))
        self.inputPerdidaCu2 = QLineEdit(NewBook)
        self.inputPerdidaCu2.setObjectName(u"inputPerdidaCu2")
        self.inputPerdidaCu2.setGeometry(QRect(680, 275, 121, 31))
        self.inputPerdidaCu2.setFont(font1)
        self.inputPerdidaCu2.setMaxLength(8)
        self.label_autoriza_19 = QLabel(NewBook)
        self.label_autoriza_19.setObjectName(u"label_autoriza_19")
        self.label_autoriza_19.setGeometry(QRect(550, 250, 151, 25))
        self.inputPerdidaCu = QLineEdit(NewBook)
        self.inputPerdidaCu.setObjectName(u"inputPerdidaCu")
        self.inputPerdidaCu.setGeometry(QRect(550, 275, 121, 31))
        self.inputPerdidaCu.setFont(font1)
        self.inputPerdidaCu.setMaxLength(8)
        self.inputPerdidaCu3 = QLineEdit(NewBook)
        self.inputPerdidaCu3.setObjectName(u"inputPerdidaCu3")
        self.inputPerdidaCu3.setGeometry(QRect(810, 275, 121, 31))
        self.inputPerdidaCu3.setFont(font1)
        self.inputPerdidaCu3.setMaxLength(8)
        self.inputPerdidaFe = QLineEdit(NewBook)
        self.inputPerdidaFe.setObjectName(u"inputPerdidaFe")
        self.inputPerdidaFe.setGeometry(QRect(20, 335, 121, 31))
        self.inputPerdidaFe.setFont(font1)
        self.inputPerdidaFe.setMaxLength(8)
        self.inputPerdidaFe2 = QLineEdit(NewBook)
        self.inputPerdidaFe2.setObjectName(u"inputPerdidaFe2")
        self.inputPerdidaFe2.setGeometry(QRect(150, 335, 121, 31))
        self.inputPerdidaFe2.setFont(font1)
        self.inputPerdidaFe2.setMaxLength(8)
        self.inputPerdidaFe3 = QLineEdit(NewBook)
        self.inputPerdidaFe3.setObjectName(u"inputPerdidaFe3")
        self.inputPerdidaFe3.setGeometry(QRect(280, 335, 121, 31))
        self.inputPerdidaFe3.setFont(font1)
        self.inputPerdidaFe3.setMaxLength(8)
        self.label_autoriza_20 = QLabel(NewBook)
        self.label_autoriza_20.setObjectName(u"label_autoriza_20")
        self.label_autoriza_20.setGeometry(QRect(150, 310, 151, 25))
        self.label_autoriza_21 = QLabel(NewBook)
        self.label_autoriza_21.setObjectName(u"label_autoriza_21")
        self.label_autoriza_21.setGeometry(QRect(20, 310, 151, 25))
        self.label_autoriza_22 = QLabel(NewBook)
        self.label_autoriza_22.setObjectName(u"label_autoriza_22")
        self.label_autoriza_22.setGeometry(QRect(280, 310, 151, 25))
        self.groupBox_2 = QGroupBox(NewBook)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(500, 390, 331, 101))
        font4 = QFont()
        font4.setPointSize(11)
        font4.setBold(True)
        font4.setWeight(75)
        self.groupBox_2.setFont(font4)
        self.groupBox_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_motivoVisita_3 = QLabel(self.groupBox_2)
        self.label_motivoVisita_3.setObjectName(u"label_motivoVisita_3")
        self.label_motivoVisita_3.setGeometry(QRect(210, 30, 121, 25))
        self.label_horaSalida_3 = QLabel(self.groupBox_2)
        self.label_horaSalida_3.setObjectName(u"label_horaSalida_3")
        self.label_horaSalida_3.setGeometry(QRect(110, 30, 81, 25))
        self.inputX_2 = QLineEdit(self.groupBox_2)
        self.inputX_2.setObjectName(u"inputX_2")
        self.inputX_2.setGeometry(QRect(10, 55, 91, 31))
        self.inputX_2.setFont(font1)
        self.inputX_2.setMaxLength(9)
        self.inputY_2 = QLineEdit(self.groupBox_2)
        self.inputY_2.setObjectName(u"inputY_2")
        self.inputY_2.setGeometry(QRect(110, 55, 91, 31))
        self.inputY_2.setFont(font1)
        self.inputY_2.setMaxLength(9)
        self.inputANG_2 = QLineEdit(self.groupBox_2)
        self.inputANG_2.setObjectName(u"inputANG_2")
        self.inputANG_2.setGeometry(QRect(210, 55, 91, 31))
        self.inputANG_2.setFont(font1)
        self.inputANG_2.setMaxLength(11)
        self.label_horaIngreso_3 = QLabel(self.groupBox_2)
        self.label_horaIngreso_3.setObjectName(u"label_horaIngreso_3")
        self.label_horaIngreso_3.setGeometry(QRect(10, 30, 71, 25))
        self.groupBox = QGroupBox(NewBook)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 390, 431, 101))
        self.groupBox.setFont(font4)
        self.groupBox.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_motivoVisita_2 = QLabel(self.groupBox)
        self.label_motivoVisita_2.setObjectName(u"label_motivoVisita_2")
        self.label_motivoVisita_2.setGeometry(QRect(210, 30, 131, 25))
        self.label_horaSalida_2 = QLabel(self.groupBox)
        self.label_horaSalida_2.setObjectName(u"label_horaSalida_2")
        self.label_horaSalida_2.setGeometry(QRect(110, 30, 81, 25))
        self.inputX = QLineEdit(self.groupBox)
        self.inputX.setObjectName(u"inputX")
        self.inputX.setGeometry(QRect(10, 55, 91, 31))
        self.inputX.setFont(font1)
        self.inputX.setMaxLength(14)
        self.inputY = QLineEdit(self.groupBox)
        self.inputY.setObjectName(u"inputY")
        self.inputY.setGeometry(QRect(110, 55, 91, 31))
        self.inputY.setFont(font1)
        self.inputY.setMaxLength(14)
        self.inputZ = QLineEdit(self.groupBox)
        self.inputZ.setObjectName(u"inputZ")
        self.inputZ.setGeometry(QRect(210, 55, 91, 31))
        self.inputZ.setFont(font1)
        self.inputZ.setMaxLength(14)
        self.label_horaIngreso_2 = QLabel(self.groupBox)
        self.label_horaIngreso_2.setObjectName(u"label_horaIngreso_2")
        self.label_horaIngreso_2.setGeometry(QRect(10, 30, 71, 25))
        self.label_horaIngreso_4 = QLabel(self.groupBox)
        self.label_horaIngreso_4.setObjectName(u"label_horaIngreso_4")
        self.label_horaIngreso_4.setGeometry(QRect(310, 30, 71, 25))
        self.inputANG = QLineEdit(self.groupBox)
        self.inputANG.setObjectName(u"inputANG")
        self.inputANG.setGeometry(QRect(310, 55, 111, 31))
        self.inputANG.setFont(font1)
        self.inputANG.setMaxLength(11)
        self.inputCodEmpresa = QLineEdit(NewBook)
        self.inputCodEmpresa.setObjectName(u"inputCodEmpresa")
        self.inputCodEmpresa.setGeometry(QRect(680, 335, 121, 31))
        self.inputCodEmpresa.setFont(font1)
        self.inputCodEmpresa.setMaxLength(5)
        self.label_empresa = QLabel(NewBook)
        self.label_empresa.setObjectName(u"label_empresa")
        self.label_empresa.setGeometry(QRect(680, 310, 111, 21))
        self.label_empresa.setScaledContents(True)
        QWidget.setTabOrder(self.inputCodigo, self.inputCentral)
        QWidget.setTabOrder(self.inputCentral, self.addButton)
        QWidget.setTabOrder(self.addButton, self.cancelButton)

        self.retranslateUi(NewBook)

        self.addButton.setDefault(True)
        self.cancelButton.setDefault(True)


        QMetaObject.connectSlotsByName(NewBook)
    # setupUi

    def retranslateUi(self, NewBook):
        NewBook.setWindowTitle(QCoreApplication.translate("NewBook", u"Nuevo Registro", None))
        self.label.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">TRANSFORMADOR</span></p></body></html>", None))
        self.label_autoriza.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Codigo:</span></p></body></html>", None))
        self.addButton.setText(QCoreApplication.translate("NewBook", u"AGREGAR", None))
        self.cancelButton.setText(QCoreApplication.translate("NewBook", u"CANCELAR", None))
        self.label_aquienVisita.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Central:</span></p></body></html>", None))
        self.label_area.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Tipo Instalaci\u00f3n:</span></p></body></html>", None))
        self.label_horaSalida.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Estado:</span></p></body></html>", None))
        self.label_motivoVisita.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Fecha de Alta:</span></p></body></html>", None))
        self.label_nota_obligatoria.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; font-style:italic; color:#ff0000;\">(*) El c\u00f3digo es obligatorio</span></p></body></html>", None))
        self.ast_aquienvisita.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ff0000;\">*</span></p></body></html>", None))
        self.label_advertencia_dni.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; font-style:italic; color:#ff0000;\">(*) El c\u00f3digo es obligatorio</span></p></body></html>", None))
        self.label_area_3.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Tipo:</span></p></body></html>", None))
        self.label_autoriza_2.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Marca:</span></p></body></html>", None))
        self.label_autoriza_3.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">A\u00f1o:</span></p></body></html>", None))
        self.label_autoriza_4.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Tensi\u00f3n Nom. 1\u00b0:</span></p></body></html>", None))
        self.label_autoriza_5.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Conexi\u00f3n:</span></p></body></html>", None))
        self.label_autoriza_6.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">N\u00b0 Serie:</span></p></body></html>", None))
        self.label_autoriza_7.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Tensi\u00f3n Nom. 2\u00b0:</span></p></body></html>", None))
        self.label_autoriza_8.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Tensi\u00f3n Nom. 3\u00b0:</span></p></body></html>", None))
        self.label_autoriza_9.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Potencia Lado 2\u00b0:</span></p></body></html>", None))
        self.label_autoriza_10.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Potencia Lado 1\u00b0:</span></p></body></html>", None))
        self.label_autoriza_11.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Potencia Lado 3\u00b0:</span></p></body></html>", None))
        self.label_autoriza_12.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Disponibilidad:</span></p></body></html>", None))
        self.label_autoriza_13.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">VCC Lado 1\u00b0:</span></p></body></html>", None))
        self.label_autoriza_14.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Potencia Base Ref.:</span></p></body></html>", None))
        self.label_autoriza_15.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">VCC Lado 2\u00b0:</span></p></body></html>", None))
        self.label_autoriza_16.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">VCC Lado 3\u00b0:</span></p></body></html>", None))
        self.label_autoriza_17.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Perdida Cu 3\u00b0:</span></p></body></html>", None))
        self.label_autoriza_18.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Perdida Cu 2\u00b0:</span></p></body></html>", None))
        self.label_autoriza_19.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Perdida Cu 1\u00b0:</span></p></body></html>", None))
        self.label_autoriza_20.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Perdida Fe 2\u00b0:</span></p></body></html>", None))
        self.label_autoriza_21.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Perdida Fe 1\u00b0:</span></p></body></html>", None))
        self.label_autoriza_22.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Perdida Fe 3\u00b0:</span></p></body></html>", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("NewBook", u"Ubicaci\u00f3n Esquema:", None))
        self.label_motivoVisita_3.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">ANG:</span></p></body></html>", None))
        self.label_horaSalida_3.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Y:</span></p></body></html>", None))
        self.label_horaIngreso_3.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">X:</span></p></body></html>", None))
        self.groupBox.setTitle(QCoreApplication.translate("NewBook", u"Ubicaci\u00f3n dentro del Plano Planta:", None))
        self.label_motivoVisita_2.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Z:</span></p></body></html>", None))
        self.label_horaSalida_2.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Y:</span></p></body></html>", None))
        self.label_horaIngreso_2.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">X:</span></p></body></html>", None))
        self.label_horaIngreso_4.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">ANG:</span></p></body></html>", None))
        self.label_empresa.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Empresa:</span></p></body></html>", None))
    # retranslateUi

