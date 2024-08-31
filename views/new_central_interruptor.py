# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_central_interruptor.ui'
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
        NewBook.resize(861, 383)
        NewBook.setMinimumSize(QSize(861, 383))
        NewBook.setMaximumSize(QSize(861, 383))
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
        self.label.setGeometry(QRect(20, 10, 831, 41))
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
        self.inputCentral.setGeometry(QRect(140, 95, 221, 31))
        self.inputCentral.setFont(font1)
        self.addButton = QPushButton(NewBook)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setGeometry(QRect(130, 330, 291, 41))
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
        self.cancelButton.setGeometry(QRect(460, 330, 271, 41))
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
        self.label_area.setGeometry(QRect(700, 70, 191, 25))
        self.label_horaSalida = QLabel(NewBook)
        self.label_horaSalida.setObjectName(u"label_horaSalida")
        self.label_horaSalida.setGeometry(QRect(260, 130, 81, 25))
        self.label_motivoVisita = QLabel(NewBook)
        self.label_motivoVisita.setObjectName(u"label_motivoVisita")
        self.label_motivoVisita.setGeometry(QRect(390, 130, 131, 25))
        self.label_nota_obligatoria = QLabel(NewBook)
        self.label_nota_obligatoria.setObjectName(u"label_nota_obligatoria")
        self.label_nota_obligatoria.setGeometry(QRect(20, 310, 281, 21))
        self.ast_aquienvisita = QLabel(NewBook)
        self.ast_aquienvisita.setObjectName(u"ast_aquienvisita")
        self.ast_aquienvisita.setGeometry(QRect(70, 70, 21, 25))
        self.label_advertencia_dni = QLabel(NewBook)
        self.label_advertencia_dni.setObjectName(u"label_advertencia_dni")
        self.label_advertencia_dni.setGeometry(QRect(20, 310, 251, 21))
        self.label_area_2 = QLabel(NewBook)
        self.label_area_2.setObjectName(u"label_area_2")
        self.label_area_2.setGeometry(QRect(370, 70, 61, 25))
        self.cbEstado = QComboBox(NewBook)
        self.cbEstado.setObjectName(u"cbEstado")
        self.cbEstado.setGeometry(QRect(260, 155, 121, 31))
        self.cbEstado.setFont(font1)
        self.cbEstado.setEditable(False)
        self.inputFecha = QDateEdit(NewBook)
        self.inputFecha.setObjectName(u"inputFecha")
        self.inputFecha.setGeometry(QRect(390, 155, 131, 31))
        font3 = QFont()
        font3.setPointSize(11)
        font3.setBold(False)
        font3.setWeight(50)
        self.inputFecha.setFont(font3)
        self.inputTension = QLineEdit(NewBook)
        self.inputTension.setObjectName(u"inputTension")
        self.inputTension.setGeometry(QRect(700, 95, 151, 31))
        self.inputTension.setFont(font1)
        self.inputTension.setMaxLength(8)
        self.inputCelda = QLineEdit(NewBook)
        self.inputCelda.setObjectName(u"inputCelda")
        self.inputCelda.setGeometry(QRect(370, 95, 151, 31))
        self.inputCelda.setFont(font1)
        self.cbTipo = QComboBox(NewBook)
        self.cbTipo.setObjectName(u"cbTipo")
        self.cbTipo.setGeometry(QRect(530, 95, 161, 31))
        self.cbTipo.setFont(font1)
        self.cbTipo.setEditable(False)
        self.label_area_3 = QLabel(NewBook)
        self.label_area_3.setObjectName(u"label_area_3")
        self.label_area_3.setGeometry(QRect(530, 70, 141, 25))
        self.inputMarca = QLineEdit(NewBook)
        self.inputMarca.setObjectName(u"inputMarca")
        self.inputMarca.setGeometry(QRect(20, 155, 111, 31))
        self.inputMarca.setFont(font1)
        self.inputMarca.setMaxLength(50)
        self.label_autoriza_2 = QLabel(NewBook)
        self.label_autoriza_2.setObjectName(u"label_autoriza_2")
        self.label_autoriza_2.setGeometry(QRect(20, 130, 101, 25))
        self.inputAnio = QLineEdit(NewBook)
        self.inputAnio.setObjectName(u"inputAnio")
        self.inputAnio.setGeometry(QRect(140, 155, 111, 31))
        self.inputAnio.setFont(font1)
        self.inputAnio.setMaxLength(4)
        self.label_autoriza_3 = QLabel(NewBook)
        self.label_autoriza_3.setObjectName(u"label_autoriza_3")
        self.label_autoriza_3.setGeometry(QRect(140, 130, 101, 25))
        self.groupBox_2 = QGroupBox(NewBook)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(510, 200, 331, 101))
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
        self.groupBox.setGeometry(QRect(20, 200, 431, 101))
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
        self.inputANG.setMaxLength(14)
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
        self.label.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">INTERRUPTOR</span></p></body></html>", None))
        self.label_autoriza.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Codigo:</span></p></body></html>", None))
        self.addButton.setText(QCoreApplication.translate("NewBook", u"AGREGAR", None))
        self.cancelButton.setText(QCoreApplication.translate("NewBook", u"CANCELAR", None))
        self.label_aquienVisita.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Central:</span></p></body></html>", None))
        self.label_area.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Tensi\u00f3n Nominal:</span></p></body></html>", None))
        self.label_horaSalida.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Estado:</span></p></body></html>", None))
        self.label_motivoVisita.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Fecha de Alta:</span></p></body></html>", None))
        self.label_nota_obligatoria.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; font-style:italic; color:#ff0000;\">(*) El c\u00f3digo es obligatorio</span></p></body></html>", None))
        self.ast_aquienvisita.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ff0000;\">*</span></p></body></html>", None))
        self.label_advertencia_dni.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; font-style:italic; color:#ff0000;\">(*) El c\u00f3digo es obligatorio</span></p></body></html>", None))
        self.label_area_2.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Celda:</span></p></body></html>", None))
        self.label_area_3.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Tipo Instalaci\u00f3n:</span></p></body></html>", None))
        self.label_autoriza_2.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Marca:</span></p></body></html>", None))
        self.label_autoriza_3.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">A\u00f1o:</span></p></body></html>", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("NewBook", u"Ubicaci\u00f3n Esquema:", None))
        self.label_motivoVisita_3.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">ANG:</span></p></body></html>", None))
        self.label_horaSalida_3.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Y:</span></p></body></html>", None))
        self.label_horaIngreso_3.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">X:</span></p></body></html>", None))
        self.groupBox.setTitle(QCoreApplication.translate("NewBook", u"Ubicaci\u00f3n dentro del Plano Planta:", None))
        self.label_motivoVisita_2.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Z:</span></p></body></html>", None))
        self.label_horaSalida_2.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Y:</span></p></body></html>", None))
        self.label_horaIngreso_2.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">X:</span></p></body></html>", None))
        self.label_horaIngreso_4.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">ANG:</span></p></body></html>", None))
    # retranslateUi

