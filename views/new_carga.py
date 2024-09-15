# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_carga.ui'
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
        NewBook.resize(994, 544)
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
        self.label.setGeometry(QRect(20, 10, 961, 41))
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
        self.searchButton.setGeometry(QRect(820, 90, 161, 31))
        font1 = QFont()
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
        self.cancelButton.setGeometry(QRect(510, 490, 271, 41))
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
        self.tableCarga = QTableWidget(NewBook)
        self.tableCarga.setObjectName(u"tableCarga")
        self.tableCarga.setGeometry(QRect(20, 130, 961, 351))
        self.tableCarga.setAutoFillBackground(True)
        self.tableCarga.setLineWidth(5)
        self.tableCarga.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableCarga.setTextElideMode(Qt.ElideLeft)
        self.tableCarga.horizontalHeader().setMinimumSectionSize(10)
        self.cbTabla = QComboBox(NewBook)
        self.cbTabla.setObjectName(u"cbTabla")
        self.cbTabla.setGeometry(QRect(20, 90, 321, 31))
        font3 = QFont()
        font3.setPointSize(8)
        self.cbTabla.setFont(font3)
        self.cbTabla.setEditable(False)
        self.SelectButton = QPushButton(NewBook)
        self.SelectButton.setObjectName(u"SelectButton")
        self.SelectButton.setGeometry(QRect(600, 90, 211, 31))
        self.SelectButton.setFont(font1)
        self.SelectButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.SelectButton.setStyleSheet(u"QPushButton\n"
"{	\n"
"	height: 2em;\n"
" 	border-style: solid;\n"
"	border-width: 2px;\n"
" 	border-color: black;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   	background-color:green;\n"
"	color:white;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"./assets/icons/carpeta.png", QSize(), QIcon.Normal, QIcon.Off)
        self.SelectButton.setIcon(icon2)
        self.SelectButton.setIconSize(QSize(25, 25))
        self.SelectButton.setAutoDefault(True)
        self.SelectButton.setFlat(True)
        self.label_carga = QLabel(NewBook)
        self.label_carga.setObjectName(u"label_carga")
        self.label_carga.setGeometry(QRect(350, 100, 241, 21))
        font4 = QFont()
        font4.setPointSize(9)
        self.label_carga.setFont(font4)
        self.label_carga.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.addButton = QPushButton(NewBook)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setGeometry(QRect(220, 490, 271, 41))
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
        icon3 = QIcon()
        icon3.addFile(u"./assets/icons/cargardata.png", QSize(), QIcon.Normal, QIcon.Off)
        self.addButton.setIcon(icon3)
        self.addButton.setIconSize(QSize(35, 35))
        self.addButton.setAutoDefault(True)
        self.addButton.setFlat(True)
        QWidget.setTabOrder(self.searchButton, self.cancelButton)

        self.retranslateUi(NewBook)

        self.searchButton.setDefault(True)
        self.cancelButton.setDefault(True)
        self.SelectButton.setDefault(True)
        self.addButton.setDefault(True)


        QMetaObject.connectSlotsByName(NewBook)
    # setupUi

    def retranslateUi(self, NewBook):
        NewBook.setWindowTitle(QCoreApplication.translate("NewBook", u"Nuevo Registro", None))
        self.label.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">CARGA DE DATOS MASIVA</span></p></body></html>", None))
        self.label_autoriza.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Tabla:</span></p></body></html>", None))
        self.searchButton.setText(QCoreApplication.translate("NewBook", u"Previsualizar", None))
        self.cancelButton.setText(QCoreApplication.translate("NewBook", u"SALIR", None))
        self.SelectButton.setText(QCoreApplication.translate("NewBook", u"Seleccionar Archivo", None))
        self.label_carga.setText(QCoreApplication.translate("NewBook", u"Ning\u00fan archivo seleccionado...", None))
        self.addButton.setText(QCoreApplication.translate("NewBook", u"Cargar Data", None))
    # retranslateUi

