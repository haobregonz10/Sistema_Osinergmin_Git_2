# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_central_generador.ui'
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
        NewBook.resize(789, 391)
        NewBook.setMinimumSize(QSize(789, 391))
        NewBook.setMaximumSize(QSize(789, 391))
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
        self.label.setGeometry(QRect(20, 10, 751, 41))
        font = QFont()
        font.setUnderline(False)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet(u"background-color: red;")
        self.label.setFrameShape(QFrame.Box)
        self.label_autoriza = QLabel(NewBook)
        self.label_autoriza.setObjectName(u"label_autoriza")
        self.label_autoriza.setGeometry(QRect(20, 70, 101, 21))
        font1 = QFont()
        font1.setPointSize(10)
        self.label_autoriza.setFont(font1)
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
        self.inputNombre.setMaxLength(20)
        self.addButton = QPushButton(NewBook)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setGeometry(QRect(90, 330, 291, 41))
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
        icon = QIcon()
        icon.addFile(u"./assets/icons/add-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.addButton.setIcon(icon)
        self.addButton.setIconSize(QSize(30, 30))
        self.addButton.setAutoDefault(True)
        self.addButton.setFlat(True)
        self.cancelButton = QPushButton(NewBook)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setGeometry(QRect(410, 330, 271, 41))
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
        icon1 = QIcon()
        icon1.addFile(u"./assets/icons/cancel-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cancelButton.setIcon(icon1)
        self.cancelButton.setIconSize(QSize(30, 30))
        self.cancelButton.setAutoDefault(True)
        self.cancelButton.setFlat(True)
        self.label_aquienVisita = QLabel(NewBook)
        self.label_aquienVisita.setObjectName(u"label_aquienVisita")
        self.label_aquienVisita.setGeometry(QRect(140, 70, 191, 21))
        self.label_aquienVisita.setFont(font1)
        self.label_area = QLabel(NewBook)
        self.label_area.setObjectName(u"label_area")
        self.label_area.setGeometry(QRect(570, 70, 191, 21))
        self.label_area.setFont(font1)
        self.label_horaIngreso = QLabel(NewBook)
        self.label_horaIngreso.setObjectName(u"label_horaIngreso")
        self.label_horaIngreso.setGeometry(QRect(20, 140, 171, 16))
        self.label_horaIngreso.setFont(font1)
        self.label_horaSalida = QLabel(NewBook)
        self.label_horaSalida.setObjectName(u"label_horaSalida")
        self.label_horaSalida.setGeometry(QRect(190, 140, 81, 16))
        self.label_horaSalida.setFont(font1)
        self.label_motivoVisita = QLabel(NewBook)
        self.label_motivoVisita.setObjectName(u"label_motivoVisita")
        self.label_motivoVisita.setGeometry(QRect(320, 140, 131, 21))
        self.label_motivoVisita.setFont(font1)
        self.label_nota_obligatoria = QLabel(NewBook)
        self.label_nota_obligatoria.setObjectName(u"label_nota_obligatoria")
        self.label_nota_obligatoria.setGeometry(QRect(20, 300, 281, 21))
        self.label_advertencia_dni = QLabel(NewBook)
        self.label_advertencia_dni.setObjectName(u"label_advertencia_dni")
        self.label_advertencia_dni.setGeometry(QRect(20, 300, 251, 21))
        self.label_area_2 = QLabel(NewBook)
        self.label_area_2.setObjectName(u"label_area_2")
        self.label_area_2.setGeometry(QRect(370, 70, 171, 21))
        self.label_area_2.setFont(font1)
        self.cbTurbina = QComboBox(NewBook)
        self.cbTurbina.setObjectName(u"cbTurbina")
        self.cbTurbina.setGeometry(QRect(20, 160, 161, 31))
        self.cbTurbina.setFont(font2)
        self.cbTurbina.setEditable(False)
        self.cbEstado = QComboBox(NewBook)
        self.cbEstado.setObjectName(u"cbEstado")
        self.cbEstado.setGeometry(QRect(190, 160, 121, 31))
        self.cbEstado.setFont(font2)
        self.cbEstado.setEditable(False)
        self.inputFecha = QDateEdit(NewBook)
        self.inputFecha.setObjectName(u"inputFecha")
        self.inputFecha.setGeometry(QRect(320, 160, 131, 31))
        font4 = QFont()
        font4.setPointSize(11)
        font4.setBold(False)
        font4.setWeight(50)
        self.inputFecha.setFont(font4)
        self.inputPotencia = QLineEdit(NewBook)
        self.inputPotencia.setObjectName(u"inputPotencia")
        self.inputPotencia.setGeometry(QRect(370, 90, 191, 31))
        self.inputPotencia.setFont(font2)
        self.inputPotencia.setMaxLength(8)
        self.inputTension = QLineEdit(NewBook)
        self.inputTension.setObjectName(u"inputTension")
        self.inputTension.setGeometry(QRect(570, 90, 141, 31))
        self.inputTension.setFont(font2)
        self.inputTension.setMaxLength(6)
        self.label_nota_obligatoria_2 = QLabel(NewBook)
        self.label_nota_obligatoria_2.setObjectName(u"label_nota_obligatoria_2")
        self.label_nota_obligatoria_2.setGeometry(QRect(70, 70, 41, 21))
        self.label_empresa = QLabel(NewBook)
        self.label_empresa.setObjectName(u"label_empresa")
        self.label_empresa.setGeometry(QRect(460, 135, 111, 21))
        self.label_empresa.setScaledContents(True)
        self.inputCodEmpresa = QLineEdit(NewBook)
        self.inputCodEmpresa.setObjectName(u"inputCodEmpresa")
        self.inputCodEmpresa.setGeometry(QRect(460, 160, 121, 31))
        self.inputCodEmpresa.setFont(font2)
        self.inputCodEmpresa.setMaxLength(5)
        self.groupBox = QGroupBox(NewBook)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 200, 431, 101))
        font5 = QFont()
        font5.setPointSize(11)
        font5.setBold(True)
        font5.setWeight(75)
        self.groupBox.setFont(font5)
        self.groupBox.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_motivoVisita_2 = QLabel(self.groupBox)
        self.label_motivoVisita_2.setObjectName(u"label_motivoVisita_2")
        self.label_motivoVisita_2.setGeometry(QRect(210, 30, 91, 25))
        self.label_horaSalida_2 = QLabel(self.groupBox)
        self.label_horaSalida_2.setObjectName(u"label_horaSalida_2")
        self.label_horaSalida_2.setGeometry(QRect(110, 30, 81, 25))
        self.inputX = QLineEdit(self.groupBox)
        self.inputX.setObjectName(u"inputX")
        self.inputX.setGeometry(QRect(10, 55, 91, 31))
        self.inputX.setFont(font2)
        self.inputX.setMaxLength(14)
        self.inputY = QLineEdit(self.groupBox)
        self.inputY.setObjectName(u"inputY")
        self.inputY.setGeometry(QRect(110, 55, 91, 31))
        self.inputY.setFont(font2)
        self.inputY.setMaxLength(14)
        self.inputZ = QLineEdit(self.groupBox)
        self.inputZ.setObjectName(u"inputZ")
        self.inputZ.setGeometry(QRect(210, 55, 91, 31))
        self.inputZ.setFont(font2)
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
        self.inputANG.setFont(font2)
        self.inputANG.setMaxLength(11)
        self.groupBox_2 = QGroupBox(NewBook)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(460, 200, 311, 101))
        self.groupBox_2.setFont(font5)
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
        self.inputX_2.setFont(font2)
        self.inputX_2.setMaxLength(9)
        self.inputY_2 = QLineEdit(self.groupBox_2)
        self.inputY_2.setObjectName(u"inputY_2")
        self.inputY_2.setGeometry(QRect(110, 55, 91, 31))
        self.inputY_2.setFont(font2)
        self.inputY_2.setMaxLength(9)
        self.inputANG_2 = QLineEdit(self.groupBox_2)
        self.inputANG_2.setObjectName(u"inputANG_2")
        self.inputANG_2.setGeometry(QRect(210, 55, 91, 31))
        self.inputANG_2.setFont(font2)
        self.inputANG_2.setMaxLength(11)
        self.label_horaIngreso_3 = QLabel(self.groupBox_2)
        self.label_horaIngreso_3.setObjectName(u"label_horaIngreso_3")
        self.label_horaIngreso_3.setGeometry(QRect(10, 30, 71, 25))
        QWidget.setTabOrder(self.inputCodigo, self.inputNombre)
        QWidget.setTabOrder(self.inputNombre, self.addButton)
        QWidget.setTabOrder(self.addButton, self.cancelButton)

        self.retranslateUi(NewBook)

        self.addButton.setDefault(True)
        self.cancelButton.setDefault(True)


        QMetaObject.connectSlotsByName(NewBook)
    # setupUi

    def retranslateUi(self, NewBook):
        NewBook.setWindowTitle(QCoreApplication.translate("NewBook", u"Nuevo Registro", None))
        self.label.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">GENERADOR</span></p></body></html>", None))
        self.label_autoriza.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-weight:600;\">Codigo:</span></p></body></html>", None))
        self.addButton.setText(QCoreApplication.translate("NewBook", u"AGREGAR", None))
        self.cancelButton.setText(QCoreApplication.translate("NewBook", u"CANCELAR", None))
        self.label_aquienVisita.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-weight:600;\">Central:</span></p></body></html>", None))
        self.label_area.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-weight:600;\">Tensi\u00f3n Nominal:</span></p></body></html>", None))
        self.label_horaIngreso.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-weight:600;\">Tipo Turbina:</span></p></body></html>", None))
        self.label_horaSalida.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-weight:600;\">Estado:</span></p></body></html>", None))
        self.label_motivoVisita.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-weight:600;\">Fecha de Alta:</span></p></body></html>", None))
        self.label_nota_obligatoria.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; font-style:italic; color:#ff0000;\">(*) El c\u00f3digo es obligatorio</span></p></body></html>", None))
        self.label_advertencia_dni.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; font-style:italic; color:#ff0000;\">(*) El c\u00f3digo es obligatorio</span></p></body></html>", None))
        self.label_area_2.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-weight:600;\">Potencia Nominal:</span></p></body></html>", None))
        self.label_nota_obligatoria_2.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ff0000;\">*</span></p></body></html>", None))
        self.label_empresa.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Empresa:</span></p></body></html>", None))
        self.groupBox.setTitle(QCoreApplication.translate("NewBook", u"Ubicaci\u00f3n dentro del Plano Planta:", None))
        self.label_motivoVisita_2.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Z:</span></p></body></html>", None))
        self.label_horaSalida_2.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Y:</span></p></body></html>", None))
        self.label_horaIngreso_2.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">X:</span></p></body></html>", None))
        self.label_horaIngreso_4.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">ANG:</span></p></body></html>", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("NewBook", u"Ubicaci\u00f3n Esquema:", None))
        self.label_motivoVisita_3.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">ANG:</span></p></body></html>", None))
        self.label_horaSalida_3.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Y:</span></p></body></html>", None))
        self.label_horaIngreso_3.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">X:</span></p></body></html>", None))
    # retranslateUi

