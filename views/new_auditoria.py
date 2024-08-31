# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_auditoria.ui'
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
        NewBook.resize(892, 544)
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
        self.searchButton = QPushButton(NewBook)
        self.searchButton.setObjectName(u"searchButton")
        self.searchButton.setGeometry(QRect(750, 90, 131, 31))
        font1 = QFont()
        font1.setPointSize(13)
        font1.setBold(True)
        font1.setWeight(75)
        self.searchButton.setFont(font1)
        self.searchButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.searchButton.setStyleSheet(u"QPushButton\n"
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
        icon.addFile(u"./assets/icons/search-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.searchButton.setIcon(icon)
        self.searchButton.setIconSize(QSize(30, 30))
        self.searchButton.setAutoDefault(True)
        self.searchButton.setFlat(True)
        self.cancelButton = QPushButton(NewBook)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setGeometry(QRect(270, 490, 271, 41))
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
        icon1 = QIcon()
        icon1.addFile(u"./assets/icons/cancel-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cancelButton.setIcon(icon1)
        self.cancelButton.setIconSize(QSize(30, 30))
        self.cancelButton.setAutoDefault(True)
        self.cancelButton.setFlat(True)
        self.label_aquienVisita = QLabel(NewBook)
        self.label_aquienVisita.setObjectName(u"label_aquienVisita")
        self.label_aquienVisita.setGeometry(QRect(350, 70, 111, 25))
        self.tableAuditoria = QTableWidget(NewBook)
        self.tableAuditoria.setObjectName(u"tableAuditoria")
        self.tableAuditoria.setGeometry(QRect(20, 130, 861, 351))
        self.tableAuditoria.setAutoFillBackground(True)
        self.tableAuditoria.setLineWidth(5)
        self.tableAuditoria.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableAuditoria.setTextElideMode(Qt.ElideLeft)
        self.tableAuditoria.horizontalHeader().setMinimumSectionSize(10)
        self.inputFechaInicio = QDateEdit(NewBook)
        self.inputFechaInicio.setObjectName(u"inputFechaInicio")
        self.inputFechaInicio.setGeometry(QRect(350, 90, 111, 31))
        font3 = QFont()
        font3.setPointSize(11)
        font3.setBold(False)
        font3.setWeight(50)
        self.inputFechaInicio.setFont(font3)
        self.inputFechaFin = QDateEdit(NewBook)
        self.inputFechaFin.setObjectName(u"inputFechaFin")
        self.inputFechaFin.setGeometry(QRect(470, 90, 111, 31))
        self.inputFechaFin.setFont(font3)
        self.label_aquienVisita_2 = QLabel(NewBook)
        self.label_aquienVisita_2.setObjectName(u"label_aquienVisita_2")
        self.label_aquienVisita_2.setGeometry(QRect(470, 70, 111, 25))
        self.cbTipo = QComboBox(NewBook)
        self.cbTipo.setObjectName(u"cbTipo")
        self.cbTipo.setGeometry(QRect(590, 90, 151, 31))
        font4 = QFont()
        font4.setPointSize(12)
        self.cbTipo.setFont(font4)
        self.cbTipo.setEditable(False)
        self.label_aquienVisita_3 = QLabel(NewBook)
        self.label_aquienVisita_3.setObjectName(u"label_aquienVisita_3")
        self.label_aquienVisita_3.setGeometry(QRect(590, 70, 131, 25))
        self.cbTabla = QComboBox(NewBook)
        self.cbTabla.setObjectName(u"cbTabla")
        self.cbTabla.setGeometry(QRect(20, 90, 321, 31))
        self.cbTabla.setFont(font4)
        self.cbTabla.setEditable(False)
        QWidget.setTabOrder(self.searchButton, self.cancelButton)

        self.retranslateUi(NewBook)

        self.searchButton.setDefault(True)
        self.cancelButton.setDefault(True)


        QMetaObject.connectSlotsByName(NewBook)
    # setupUi

    def retranslateUi(self, NewBook):
        NewBook.setWindowTitle(QCoreApplication.translate("NewBook", u"Nuevo Registro", None))
        self.label.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">M\u00d3DULO DE AUDITOR\u00cdA</span></p></body></html>", None))
        self.label_autoriza.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Tabla:</span></p></body></html>", None))
        self.searchButton.setText(QCoreApplication.translate("NewBook", u"Buscar", None))
        self.cancelButton.setText(QCoreApplication.translate("NewBook", u"SALIR", None))
        self.label_aquienVisita.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Fecha Inicio:</span></p></body></html>", None))
        self.label_aquienVisita_2.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Fecha Fin:</span></p></body></html>", None))
        self.label_aquienVisita_3.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Tipo:</span></p></body></html>", None))
    # retranslateUi

