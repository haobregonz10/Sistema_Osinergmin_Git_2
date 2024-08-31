# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_central_generacion_vertice_coordenadas.ui'
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
        NewBook.resize(708, 412)
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
        self.inputCodigoCentral = QLineEdit(NewBook)
        self.inputCodigoCentral.setObjectName(u"inputCodigoCentral")
        self.inputCodigoCentral.setGeometry(QRect(20, 90, 131, 31))
        font1 = QFont()
        font1.setPointSize(12)
        self.inputCodigoCentral.setFont(font1)
        self.cancelButton = QPushButton(NewBook)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setGeometry(QRect(220, 360, 271, 41))
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setWeight(75)
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
        icon = QIcon()
        icon.addFile(u"./assets/icons/exitoso.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cancelButton.setIcon(icon)
        self.cancelButton.setIconSize(QSize(30, 30))
        self.cancelButton.setAutoDefault(True)
        self.cancelButton.setFlat(True)
        self.label_aquienVisita = QLabel(NewBook)
        self.label_aquienVisita.setObjectName(u"label_aquienVisita")
        self.label_aquienVisita.setGeometry(QRect(20, 70, 191, 21))
        font3 = QFont()
        font3.setPointSize(8)
        font3.setBold(False)
        font3.setWeight(50)
        self.label_aquienVisita.setFont(font3)
        self.inputZ = QLineEdit(NewBook)
        self.inputZ.setObjectName(u"inputZ")
        self.inputZ.setGeometry(QRect(550, 90, 141, 31))
        self.inputZ.setFont(font1)
        self.label_fecha = QLabel(NewBook)
        self.label_fecha.setObjectName(u"label_fecha")
        self.label_fecha.setGeometry(QRect(270, 70, 101, 16))
        font4 = QFont()
        font4.setPointSize(8)
        self.label_fecha.setFont(font4)
        self.label_visitante = QLabel(NewBook)
        self.label_visitante.setObjectName(u"label_visitante")
        self.label_visitante.setGeometry(QRect(550, 70, 141, 21))
        self.label_visitante.setFont(font4)
        self.inputY = QLineEdit(NewBook)
        self.inputY.setObjectName(u"inputY")
        self.inputY.setGeometry(QRect(410, 90, 131, 31))
        self.inputY.setFont(font1)
        self.inputY.setInputMethodHints(Qt.ImhDigitsOnly)
        self.label_dni = QLabel(NewBook)
        self.label_dni.setObjectName(u"label_dni")
        self.label_dni.setGeometry(QRect(410, 70, 91, 21))
        self.label_dni.setFont(font4)
        self.label_area_2 = QLabel(NewBook)
        self.label_area_2.setObjectName(u"label_area_2")
        self.label_area_2.setGeometry(QRect(160, 70, 101, 21))
        self.label_area_2.setFont(font4)
        self.btnAgregar = QPushButton(NewBook)
        self.btnAgregar.setObjectName(u"btnAgregar")
        self.btnAgregar.setGeometry(QRect(440, 130, 121, 31))
        font5 = QFont()
        font5.setPointSize(12)
        font5.setBold(True)
        font5.setWeight(75)
        self.btnAgregar.setFont(font5)
        self.btnAgregar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnAgregar.setStyleSheet(u"QPushButton\n"
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
        self.btnAgregar.setIcon(icon1)
        self.btnAgregar.setIconSize(QSize(30, 30))
        self.btnAgregar.setAutoDefault(True)
        self.btnAgregar.setFlat(True)
        self.tableVertices = QTableWidget(NewBook)
        self.tableVertices.setObjectName(u"tableVertices")
        self.tableVertices.setGeometry(QRect(20, 170, 671, 151))
        self.tableVertices.setAutoFillBackground(True)
        self.tableVertices.setLineWidth(5)
        self.tableVertices.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableVertices.setTextElideMode(Qt.ElideLeft)
        self.tableVertices.horizontalHeader().setMinimumSectionSize(10)
        self.inputSecuencia = QLineEdit(NewBook)
        self.inputSecuencia.setObjectName(u"inputSecuencia")
        self.inputSecuencia.setGeometry(QRect(160, 90, 101, 31))
        self.inputSecuencia.setFont(font1)
        self.btnEliminar = QPushButton(NewBook)
        self.btnEliminar.setObjectName(u"btnEliminar")
        self.btnEliminar.setGeometry(QRect(570, 130, 121, 31))
        self.btnEliminar.setFont(font5)
        self.btnEliminar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnEliminar.setStyleSheet(u"QPushButton\n"
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
        self.btnEliminar.setIcon(icon2)
        self.btnEliminar.setIconSize(QSize(30, 30))
        self.btnEliminar.setAutoDefault(True)
        self.btnEliminar.setFlat(True)
        self.inputX = QLineEdit(NewBook)
        self.inputX.setObjectName(u"inputX")
        self.inputX.setGeometry(QRect(270, 90, 131, 31))
        self.inputX.setFont(font1)
        self.inputX.setInputMethodHints(Qt.ImhDigitsOnly)
        self.label_advertencia_dni = QLabel(NewBook)
        self.label_advertencia_dni.setObjectName(u"label_advertencia_dni")
        self.label_advertencia_dni.setGeometry(QRect(20, 320, 251, 21))
        self.adv_1 = QLabel(NewBook)
        self.adv_1.setObjectName(u"adv_1")
        self.adv_1.setGeometry(QRect(230, 70, 16, 21))
        self.adv_2 = QLabel(NewBook)
        self.adv_2.setObjectName(u"adv_2")
        self.adv_2.setGeometry(QRect(290, 70, 16, 21))
        self.adv_3 = QLabel(NewBook)
        self.adv_3.setObjectName(u"adv_3")
        self.adv_3.setGeometry(QRect(430, 70, 16, 21))
        self.adv_4 = QLabel(NewBook)
        self.adv_4.setObjectName(u"adv_4")
        self.adv_4.setGeometry(QRect(570, 70, 16, 21))
        QWidget.setTabOrder(self.inputCodigoCentral, self.inputY)
        QWidget.setTabOrder(self.inputY, self.inputZ)
        QWidget.setTabOrder(self.inputZ, self.cancelButton)

        self.retranslateUi(NewBook)

        self.cancelButton.setDefault(True)
        self.btnAgregar.setDefault(True)
        self.btnEliminar.setDefault(True)


        QMetaObject.connectSlotsByName(NewBook)
    # setupUi

    def retranslateUi(self, NewBook):
        NewBook.setWindowTitle(QCoreApplication.translate("NewBook", u"Nuevo Registro", None))
        self.label.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Vertices Coordenadas Geogr\u00e1ficas</span></p></body></html>", None))
        self.cancelButton.setText(QCoreApplication.translate("NewBook", u"Listo", None))
        self.label_aquienVisita.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">C\u00f3digo Central:</span></p></body></html>", None))
        self.label_fecha.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">X:</span></p></body></html>", None))
        self.label_visitante.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Z:</span></p></body></html>", None))
        self.label_dni.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Y:</span></p></body></html>", None))
        self.label_area_2.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Secuencia:</span></p></body></html>", None))
        self.btnAgregar.setText(QCoreApplication.translate("NewBook", u"Agregar", None))
        self.btnEliminar.setText(QCoreApplication.translate("NewBook", u"Eliminar", None))
        self.label_advertencia_dni.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; font-style:italic; color:#ff0000;\">(*) Campos Obligatorios</span></p></body></html>", None))
        self.adv_1.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; font-style:italic; color:#ff0000;\">*</span></p></body></html>", None))
        self.adv_2.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; font-style:italic; color:#ff0000;\">*</span></p></body></html>", None))
        self.adv_3.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; font-style:italic; color:#ff0000;\">*</span></p></body></html>", None))
        self.adv_4.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; font-style:italic; color:#ff0000;\">*</span></p></body></html>", None))
    # retranslateUi

