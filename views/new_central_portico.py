# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_central_portico.ui'
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
        NewBook.resize(701, 534)
        NewBook.setMinimumSize(QSize(695, 534))
        NewBook.setMaximumSize(QSize(701, 534))
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
        self.label.setGeometry(QRect(20, 10, 661, 41))
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
        self.inputCentral.setGeometry(QRect(140, 95, 151, 31))
        self.inputCentral.setFont(font1)
        self.addButton = QPushButton(NewBook)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setGeometry(QRect(40, 480, 291, 41))
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
        self.cancelButton.setGeometry(QRect(370, 480, 271, 41))
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
        self.label_area.setGeometry(QRect(550, 70, 131, 25))
        self.label_4 = QLabel(NewBook)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 260, 191, 21))
        self.label_horaSalida = QLabel(NewBook)
        self.label_horaSalida.setObjectName(u"label_horaSalida")
        self.label_horaSalida.setGeometry(QRect(20, 130, 81, 25))
        self.label_motivoVisita = QLabel(NewBook)
        self.label_motivoVisita.setObjectName(u"label_motivoVisita")
        self.label_motivoVisita.setGeometry(QRect(150, 130, 131, 25))
        self.label_nota_obligatoria = QLabel(NewBook)
        self.label_nota_obligatoria.setObjectName(u"label_nota_obligatoria")
        self.label_nota_obligatoria.setGeometry(QRect(20, 460, 281, 21))
        self.ast_aquienvisita = QLabel(NewBook)
        self.ast_aquienvisita.setObjectName(u"ast_aquienvisita")
        self.ast_aquienvisita.setGeometry(QRect(70, 70, 21, 21))
        self.label_advertencia_dni = QLabel(NewBook)
        self.label_advertencia_dni.setObjectName(u"label_advertencia_dni")
        self.label_advertencia_dni.setGeometry(QRect(20, 460, 251, 21))
        self.cbTipo = QComboBox(NewBook)
        self.cbTipo.setObjectName(u"cbTipo")
        self.cbTipo.setGeometry(QRect(300, 95, 241, 31))
        self.cbTipo.setFont(font1)
        self.cbTipo.setEditable(False)
        self.label_area_2 = QLabel(NewBook)
        self.label_area_2.setObjectName(u"label_area_2")
        self.label_area_2.setGeometry(QRect(300, 70, 61, 25))
        self.cbEstado = QComboBox(NewBook)
        self.cbEstado.setObjectName(u"cbEstado")
        self.cbEstado.setGeometry(QRect(20, 155, 121, 31))
        self.cbEstado.setFont(font1)
        self.cbEstado.setEditable(False)
        self.inputFecha = QDateEdit(NewBook)
        self.inputFecha.setObjectName(u"inputFecha")
        self.inputFecha.setGeometry(QRect(150, 155, 131, 31))
        font3 = QFont()
        font3.setPointSize(11)
        font3.setBold(False)
        font3.setWeight(50)
        self.inputFecha.setFont(font3)
        self.btnDeleteEstructura = QPushButton(NewBook)
        self.btnDeleteEstructura.setObjectName(u"btnDeleteEstructura")
        self.btnDeleteEstructura.setGeometry(QRect(650, 250, 31, 31))
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(True)
        font4.setWeight(75)
        self.btnDeleteEstructura.setFont(font4)
        self.btnDeleteEstructura.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnDeleteEstructura.setStyleSheet(u"QPushButton\n"
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
        self.btnDeleteEstructura.setIcon(icon2)
        self.btnDeleteEstructura.setIconSize(QSize(30, 30))
        self.btnDeleteEstructura.setAutoDefault(True)
        self.btnDeleteEstructura.setFlat(True)
        self.btnAddEstructura = QPushButton(NewBook)
        self.btnAddEstructura.setObjectName(u"btnAddEstructura")
        self.btnAddEstructura.setGeometry(QRect(610, 250, 31, 31))
        self.btnAddEstructura.setFont(font4)
        self.btnAddEstructura.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnAddEstructura.setStyleSheet(u"QPushButton\n"
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
        self.btnAddEstructura.setIcon(icon)
        self.btnAddEstructura.setIconSize(QSize(30, 30))
        self.btnAddEstructura.setAutoDefault(True)
        self.btnAddEstructura.setFlat(True)
        self.inputAltura = QLineEdit(NewBook)
        self.inputAltura.setObjectName(u"inputAltura")
        self.inputAltura.setGeometry(QRect(550, 95, 131, 31))
        self.inputAltura.setFont(font1)
        self.inputAltura.setMaxLength(7)
        self.tableEstructura = QTableWidget(NewBook)
        self.tableEstructura.setObjectName(u"tableEstructura")
        self.tableEstructura.setGeometry(QRect(20, 280, 661, 181))
        self.tableEstructura.setAutoFillBackground(True)
        self.tableEstructura.setLineWidth(5)
        self.tableEstructura.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableEstructura.setTextElideMode(Qt.ElideLeft)
        self.tableEstructura.horizontalHeader().setMinimumSectionSize(10)
        self.groupBox = QGroupBox(NewBook)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(300, 130, 381, 111))
        font5 = QFont()
        font5.setPointSize(11)
        font5.setBold(True)
        font5.setWeight(75)
        self.groupBox.setFont(font5)
        self.groupBox.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_autoriza_3 = QLabel(self.groupBox)
        self.label_autoriza_3.setObjectName(u"label_autoriza_3")
        self.label_autoriza_3.setGeometry(QRect(250, 30, 111, 25))
        self.inputEstructura = QLineEdit(self.groupBox)
        self.inputEstructura.setObjectName(u"inputEstructura")
        self.inputEstructura.setGeometry(QRect(120, 55, 121, 31))
        self.inputEstructura.setFont(font1)
        self.label_autoriza_2 = QLabel(self.groupBox)
        self.label_autoriza_2.setObjectName(u"label_autoriza_2")
        self.label_autoriza_2.setGeometry(QRect(120, 30, 111, 25))
        self.inputEstructura2 = QLineEdit(self.groupBox)
        self.inputEstructura2.setObjectName(u"inputEstructura2")
        self.inputEstructura2.setGeometry(QRect(250, 55, 121, 31))
        self.inputEstructura2.setFont(font1)
        self.inputAltura_2 = QLineEdit(self.groupBox)
        self.inputAltura_2.setObjectName(u"inputAltura_2")
        self.inputAltura_2.setGeometry(QRect(10, 55, 101, 31))
        self.inputAltura_2.setFont(font1)
        self.inputAltura_2.setMaxLength(7)
        self.label_horaIngreso_2 = QLabel(self.groupBox)
        self.label_horaIngreso_2.setObjectName(u"label_horaIngreso_2")
        self.label_horaIngreso_2.setGeometry(QRect(10, 30, 71, 25))
        self.inputCodEmpresa = QLineEdit(NewBook)
        self.inputCodEmpresa.setObjectName(u"inputCodEmpresa")
        self.inputCodEmpresa.setGeometry(QRect(20, 215, 121, 31))
        self.inputCodEmpresa.setFont(font1)
        self.inputCodEmpresa.setMaxLength(5)
        self.label_empresa = QLabel(NewBook)
        self.label_empresa.setObjectName(u"label_empresa")
        self.label_empresa.setGeometry(QRect(20, 190, 111, 21))
        self.label_empresa.setScaledContents(True)
        QWidget.setTabOrder(self.inputCodigo, self.inputCentral)
        QWidget.setTabOrder(self.inputCentral, self.addButton)
        QWidget.setTabOrder(self.addButton, self.cancelButton)

        self.retranslateUi(NewBook)

        self.addButton.setDefault(True)
        self.cancelButton.setDefault(True)
        self.btnDeleteEstructura.setDefault(True)
        self.btnAddEstructura.setDefault(True)


        QMetaObject.connectSlotsByName(NewBook)
    # setupUi

    def retranslateUi(self, NewBook):
        NewBook.setWindowTitle(QCoreApplication.translate("NewBook", u"Nuevo Registro", None))
        self.label.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">P\u00d3RTICO</span></p></body></html>", None))
        self.label_autoriza.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Codigo:</span></p></body></html>", None))
        self.addButton.setText(QCoreApplication.translate("NewBook", u"AGREGAR", None))
        self.cancelButton.setText(QCoreApplication.translate("NewBook", u"CANCELAR", None))
        self.label_aquienVisita.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Central:</span></p></body></html>", None))
        self.label_area.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Altura:</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Estructuras:</span></p></body></html>", None))
        self.label_horaSalida.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Estado:</span></p></body></html>", None))
        self.label_motivoVisita.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Fecha de Alta:</span></p></body></html>", None))
        self.label_nota_obligatoria.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; font-style:italic; color:#ff0000;\">(*) El c\u00f3digo es obligatorio</span></p></body></html>", None))
        self.ast_aquienvisita.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ff0000;\">*</span></p></body></html>", None))
        self.label_advertencia_dni.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; font-style:italic; color:#ff0000;\">(*) El c\u00f3digo es obligatorio</span></p></body></html>", None))
        self.label_area_2.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Tipo:</span></p></body></html>", None))
        self.btnDeleteEstructura.setText("")
        self.btnAddEstructura.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("NewBook", u"Travesa\u00f1o", None))
        self.label_autoriza_3.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Estructura 2:</span></p></body></html>", None))
        self.label_autoriza_2.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Estructura 1:</span></p></body></html>", None))
        self.label_horaIngreso_2.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Altura:</span></p></body></html>", None))
        self.label_empresa.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Empresa:</span></p></body></html>", None))
    # retranslateUi

