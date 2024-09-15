# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windows.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ListBookForm(object):
    def setupUi(self, ListBookForm):
        if not ListBookForm.objectName():
            ListBookForm.setObjectName(u"ListBookForm")
        ListBookForm.resize(1357, 701)
        ListBookForm.setToolTipDuration(1)
        self.tabWidget = QTabWidget(ListBookForm)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 0, 1341, 691))
        self.tabWidget.setToolTipDuration(-2)
        self.tabWidget.setAutoFillBackground(True)
        self.tabWidget.setStyleSheet(u"QTabWidget::pane { \n"
"   border: none;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"  background: #D7D0D0;\n"
"  color: black;\n"
"  padding: 5px;\n"
" }\n"
"QTabBar::tab:selected {\n"
"  background: red;\n"
"  color: white;\n"
" }\n"
"\n"
"QTabWidget::tab-bar {\n"
"   border: 1px solid black;\n"
"}")
        self.tabWidget.setTabPosition(QTabWidget.South)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setElideMode(Qt.ElideNone)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(True)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.label_6 = QLabel(self.tab)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(0, 630, 171, 21))
        font = QFont()
        font.setPointSize(9)
        self.label_6.setFont(font)
        self.buttonsFrame = QFrame(self.tab)
        self.buttonsFrame.setObjectName(u"buttonsFrame")
        self.buttonsFrame.setGeometry(QRect(0, 0, 1331, 121))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonsFrame.sizePolicy().hasHeightForWidth())
        self.buttonsFrame.setSizePolicy(sizePolicy)
        self.buttonsFrame.setFrameShape(QFrame.StyledPanel)
        self.buttonsFrame.setFrameShadow(QFrame.Raised)
        self.open_button_generacion = QPushButton(self.buttonsFrame)
        self.open_button_generacion.setObjectName(u"open_button_generacion")
        self.open_button_generacion.setGeometry(QRect(0, 50, 141, 71))
        self.open_button_generacion.setCursor(QCursor(Qt.PointingHandCursor))
        self.open_button_generacion.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#0069c0;\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u"./assets/icons/icon_nuevo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.open_button_generacion.setIcon(icon)
        self.open_button_generacion.setIconSize(QSize(150, 200))
        self.open_button_generacion.setFlat(True)
        self.delete_btn_generacion = QPushButton(self.buttonsFrame)
        self.delete_btn_generacion.setObjectName(u"delete_btn_generacion")
        self.delete_btn_generacion.setGeometry(QRect(150, 50, 141, 71))
        self.delete_btn_generacion.setCursor(QCursor(Qt.PointingHandCursor))
        self.delete_btn_generacion.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#0069c0;\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"./assets/icons/icon_del.png", QSize(), QIcon.Normal, QIcon.Off)
        self.delete_btn_generacion.setIcon(icon1)
        self.delete_btn_generacion.setIconSize(QSize(150, 200))
        self.delete_btn_generacion.setFlat(True)
        self.label_7 = QLabel(self.buttonsFrame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(0, 10, 1321, 41))
        self.label_7.setStyleSheet(u"background-color: red;")
        self.excel_btn_generacion = QPushButton(self.buttonsFrame)
        self.excel_btn_generacion.setObjectName(u"excel_btn_generacion")
        self.excel_btn_generacion.setGeometry(QRect(300, 50, 141, 71))
        self.excel_btn_generacion.setCursor(QCursor(Qt.PointingHandCursor))
        self.excel_btn_generacion.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#0069c0;\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u"./assets/icons/icon_gen_reporte.png", QSize(), QIcon.Normal, QIcon.Off)
        self.excel_btn_generacion.setIcon(icon2)
        self.excel_btn_generacion.setIconSize(QSize(150, 200))
        self.excel_btn_generacion.setFlat(True)
        self.btn_guardar_bd = QPushButton(self.buttonsFrame)
        self.btn_guardar_bd.setObjectName(u"btn_guardar_bd")
        self.btn_guardar_bd.setGeometry(QRect(1010, 50, 171, 71))
        font1 = QFont()
        font1.setPointSize(10)
        self.btn_guardar_bd.setFont(font1)
        self.btn_guardar_bd.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_guardar_bd.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#0069c0;\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u"./assets/icons/downloaddb.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_guardar_bd.setIcon(icon3)
        self.btn_guardar_bd.setIconSize(QSize(150, 200))
        self.btn_guardar_bd.setFlat(True)
        self.btn_usuarios = QPushButton(self.buttonsFrame)
        self.btn_usuarios.setObjectName(u"btn_usuarios")
        self.btn_usuarios.setGeometry(QRect(830, 50, 171, 71))
        self.btn_usuarios.setFont(font1)
        self.btn_usuarios.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_usuarios.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#0069c0;\n"
"}\n"
"")
        icon4 = QIcon()
        icon4.addFile(u"./assets/icons/user_manager.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_usuarios.setIcon(icon4)
        self.btn_usuarios.setIconSize(QSize(70, 70))
        self.btn_usuarios.setFlat(True)
        self.btn_cerrar_sesion = QPushButton(self.buttonsFrame)
        self.btn_cerrar_sesion.setObjectName(u"btn_cerrar_sesion")
        self.btn_cerrar_sesion.setGeometry(QRect(1190, 50, 131, 71))
        font2 = QFont()
        font2.setPointSize(11)
        self.btn_cerrar_sesion.setFont(font2)
        self.btn_cerrar_sesion.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cerrar_sesion.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#0069c0;\n"
"}\n"
"")
        icon5 = QIcon()
        icon5.addFile(u"./assets/icons/307612.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cerrar_sesion.setIcon(icon5)
        self.btn_cerrar_sesion.setIconSize(QSize(50, 50))
        self.btn_cerrar_sesion.setFlat(True)
        self.btn_auditoria = QPushButton(self.buttonsFrame)
        self.btn_auditoria.setObjectName(u"btn_auditoria")
        self.btn_auditoria.setGeometry(QRect(650, 50, 171, 71))
        self.btn_auditoria.setFont(font1)
        self.btn_auditoria.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_auditoria.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#0069c0;\n"
"}\n"
"")
        icon6 = QIcon()
        icon6.addFile(u"./assets/icons/auditicon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_auditoria.setIcon(icon6)
        self.btn_auditoria.setIconSize(QSize(70, 70))
        self.btn_auditoria.setFlat(True)
        self.btn_carga = QPushButton(self.buttonsFrame)
        self.btn_carga.setObjectName(u"btn_carga")
        self.btn_carga.setGeometry(QRect(470, 50, 171, 71))
        self.btn_carga.setFont(font1)
        self.btn_carga.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_carga.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#0069c0;\n"
"}\n"
"")
        icon7 = QIcon()
        icon7.addFile(u"./assets/icons/cargardata.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_carga.setIcon(icon7)
        self.btn_carga.setIconSize(QSize(60, 70))
        self.btn_carga.setFlat(True)
        self.label_8 = QLabel(self.buttonsFrame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(1170, 20, 141, 16))
        self.label_8.setFont(font1)
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.tableGeneracion = QTableWidget(self.tab)
        self.tableGeneracion.setObjectName(u"tableGeneracion")
        self.tableGeneracion.setGeometry(QRect(0, 130, 1321, 501))
        self.tableGeneracion.setAutoFillBackground(True)
        self.tableGeneracion.setLineWidth(5)
        self.tableGeneracion.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableGeneracion.setTextElideMode(Qt.ElideLeft)
        self.tableGeneracion.horizontalHeader().setMinimumSectionSize(10)
        self.labelNumeroRegistros = QLabel(self.tab)
        self.labelNumeroRegistros.setObjectName(u"labelNumeroRegistros")
        self.labelNumeroRegistros.setGeometry(QRect(180, 630, 47, 16))
        self.labelNumeroRegistros.setFont(font)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.buttonsFrame_2 = QFrame(self.tab_2)
        self.buttonsFrame_2.setObjectName(u"buttonsFrame_2")
        self.buttonsFrame_2.setGeometry(QRect(0, 0, 1331, 131))
        sizePolicy.setHeightForWidth(self.buttonsFrame_2.sizePolicy().hasHeightForWidth())
        self.buttonsFrame_2.setSizePolicy(sizePolicy)
        self.buttonsFrame_2.setFrameShape(QFrame.StyledPanel)
        self.buttonsFrame_2.setFrameShadow(QFrame.Raised)
        self.open_button_subestacion = QPushButton(self.buttonsFrame_2)
        self.open_button_subestacion.setObjectName(u"open_button_subestacion")
        self.open_button_subestacion.setGeometry(QRect(0, 50, 141, 71))
        self.open_button_subestacion.setCursor(QCursor(Qt.PointingHandCursor))
        self.open_button_subestacion.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#0069c0;\n"
"}\n"
"")
        self.open_button_subestacion.setIcon(icon)
        self.open_button_subestacion.setIconSize(QSize(150, 150))
        self.open_button_subestacion.setFlat(True)
        self.delete_btn_subestacion = QPushButton(self.buttonsFrame_2)
        self.delete_btn_subestacion.setObjectName(u"delete_btn_subestacion")
        self.delete_btn_subestacion.setGeometry(QRect(150, 50, 141, 71))
        self.delete_btn_subestacion.setCursor(QCursor(Qt.PointingHandCursor))
        self.delete_btn_subestacion.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#0069c0;\n"
"}\n"
"")
        self.delete_btn_subestacion.setIcon(icon1)
        self.delete_btn_subestacion.setIconSize(QSize(150, 200))
        self.delete_btn_subestacion.setFlat(True)
        self.excel_btn_subestacion = QPushButton(self.buttonsFrame_2)
        self.excel_btn_subestacion.setObjectName(u"excel_btn_subestacion")
        self.excel_btn_subestacion.setGeometry(QRect(300, 50, 141, 71))
        self.excel_btn_subestacion.setCursor(QCursor(Qt.PointingHandCursor))
        self.excel_btn_subestacion.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#0069c0;\n"
"}\n"
"")
        self.excel_btn_subestacion.setIcon(icon2)
        self.excel_btn_subestacion.setIconSize(QSize(150, 200))
        self.excel_btn_subestacion.setFlat(True)
        self.label_18 = QLabel(self.tab_2)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(0, 10, 1321, 41))
        self.label_18.setStyleSheet(u"background-color: green;")
        self.tableSubestacion = QTableWidget(self.tab_2)
        self.tableSubestacion.setObjectName(u"tableSubestacion")
        self.tableSubestacion.setGeometry(QRect(0, 130, 1321, 501))
        self.tableSubestacion.setAutoFillBackground(True)
        self.tableSubestacion.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableSubestacion.setTextElideMode(Qt.ElideLeft)
        self.tableSubestacion.horizontalHeader().setMinimumSectionSize(10)
        self.label_20 = QLabel(self.tab_2)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(0, 630, 141, 16))
        self.label_20.setFont(font1)
        self.booksQtyLabel_2 = QLabel(self.tab_2)
        self.booksQtyLabel_2.setObjectName(u"booksQtyLabel_2")
        self.booksQtyLabel_2.setGeometry(QRect(150, 630, 47, 16))
        self.booksQtyLabel_2.setFont(font1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tabWidget_2 = QTabWidget(self.tab_4)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setGeometry(QRect(0, 0, 1341, 681))
        self.tabWidget_2.setToolTipDuration(-2)
        self.tabWidget_2.setAutoFillBackground(True)
        self.tabWidget_2.setStyleSheet(u"QTabWidget::pane { \n"
"   border: none;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"  background: #D7D0D0;\n"
"  color: black;\n"
"  padding: 5px;\n"
" }\n"
"QTabBar::tab:selected {\n"
"  background: red;\n"
"  color: white;\n"
" }\n"
"\n"
"QTabWidget::tab-bar {\n"
"   border: 1px solid black;\n"
"}")
        self.tabWidget_2.setTabPosition(QTabWidget.South)
        self.tabWidget_2.setTabShape(QTabWidget.Rounded)
        self.tabWidget_2.setElideMode(Qt.ElideNone)
        self.tabWidget_2.setUsesScrollButtons(True)
        self.tabWidget_2.setDocumentMode(True)
        self.tabWidget_2.setTabsClosable(False)
        self.tabWidget_2.setMovable(True)
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.label_29 = QLabel(self.tab_5)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(0, 630, 141, 16))
        self.label_29.setFont(font1)
        self.buttonsFrame_4 = QFrame(self.tab_5)
        self.buttonsFrame_4.setObjectName(u"buttonsFrame_4")
        self.buttonsFrame_4.setGeometry(QRect(0, 0, 1331, 121))
        sizePolicy.setHeightForWidth(self.buttonsFrame_4.sizePolicy().hasHeightForWidth())
        self.buttonsFrame_4.setSizePolicy(sizePolicy)
        self.buttonsFrame_4.setFrameShape(QFrame.StyledPanel)
        self.buttonsFrame_4.setFrameShadow(QFrame.Raised)
        self.open_button_linea = QPushButton(self.buttonsFrame_4)
        self.open_button_linea.setObjectName(u"open_button_linea")
        self.open_button_linea.setGeometry(QRect(0, 50, 141, 71))
        self.open_button_linea.setCursor(QCursor(Qt.PointingHandCursor))
        self.open_button_linea.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#0069c0;\n"
"}\n"
"")
        self.open_button_linea.setIcon(icon)
        self.open_button_linea.setIconSize(QSize(150, 150))
        self.open_button_linea.setFlat(True)
        self.delete_btn_linea = QPushButton(self.buttonsFrame_4)
        self.delete_btn_linea.setObjectName(u"delete_btn_linea")
        self.delete_btn_linea.setGeometry(QRect(150, 50, 141, 71))
        self.delete_btn_linea.setCursor(QCursor(Qt.PointingHandCursor))
        self.delete_btn_linea.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#0069c0;\n"
"}\n"
"")
        self.delete_btn_linea.setIcon(icon1)
        self.delete_btn_linea.setIconSize(QSize(150, 150))
        self.delete_btn_linea.setFlat(True)
        self.label_30 = QLabel(self.buttonsFrame_4)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(0, 10, 1321, 41))
        self.label_30.setStyleSheet(u"background-color: #8a36d2;")
        self.excel_btn_linea = QPushButton(self.buttonsFrame_4)
        self.excel_btn_linea.setObjectName(u"excel_btn_linea")
        self.excel_btn_linea.setGeometry(QRect(300, 50, 141, 71))
        self.excel_btn_linea.setCursor(QCursor(Qt.PointingHandCursor))
        self.excel_btn_linea.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#0069c0;\n"
"}\n"
"")
        self.excel_btn_linea.setIcon(icon2)
        self.excel_btn_linea.setIconSize(QSize(150, 150))
        self.excel_btn_linea.setFlat(True)
        self.tableLinea = QTableWidget(self.tab_5)
        self.tableLinea.setObjectName(u"tableLinea")
        self.tableLinea.setGeometry(QRect(0, 130, 1321, 501))
        self.tableLinea.setAutoFillBackground(True)
        self.tableLinea.setLineWidth(5)
        self.tableLinea.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableLinea.setTextElideMode(Qt.ElideLeft)
        self.tableLinea.horizontalHeader().setMinimumSectionSize(10)
        self.booksQtyLabel_4 = QLabel(self.tab_5)
        self.booksQtyLabel_4.setObjectName(u"booksQtyLabel_4")
        self.booksQtyLabel_4.setGeometry(QRect(150, 630, 47, 16))
        self.booksQtyLabel_4.setFont(font1)
        self.tabWidget_2.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.searchButton_9 = QPushButton(self.tab_6)
        self.searchButton_9.setObjectName(u"searchButton_9")
        self.searchButton_9.setGeometry(QRect(1170, 150, 151, 41))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setWeight(75)
        self.searchButton_9.setFont(font3)
        self.searchButton_9.setCursor(QCursor(Qt.PointingHandCursor))
        self.searchButton_9.setStyleSheet(u"QPushButton\n"
"{	\n"
"	height: 2em;\n"
" 	border-style: solid;\n"
"	border-width: 2px;\n"
" 	border-color: #00AAFF;\n"
"	background-color:#00AAFF;\n"
"	font-weight: bold;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   	background-color:#0069c0;\n"
"	color:white;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"")
        icon8 = QIcon()
        icon8.addFile(u"./assets/icons/search-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.searchButton_9.setIcon(icon8)
        self.searchButton_9.setIconSize(QSize(25, 25))
        self.parameterLineEditMotivo_5 = QLineEdit(self.tab_6)
        self.parameterLineEditMotivo_5.setObjectName(u"parameterLineEditMotivo_5")
        self.parameterLineEditMotivo_5.setGeometry(QRect(700, 160, 301, 31))
        font4 = QFont()
        font4.setPointSize(12)
        self.parameterLineEditMotivo_5.setFont(font4)
        self.parameterLineEditDNI_5 = QLineEdit(self.tab_6)
        self.parameterLineEditDNI_5.setObjectName(u"parameterLineEditDNI_5")
        self.parameterLineEditDNI_5.setGeometry(QRect(0, 160, 101, 31))
        self.parameterLineEditDNI_5.setFont(font4)
        self.label_37 = QLabel(self.tab_6)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(0, 190, 31, 21))
        self.label_37.setFont(font2)
        self.parameterLineEditFecha_5 = QLineEdit(self.tab_6)
        self.parameterLineEditFecha_5.setObjectName(u"parameterLineEditFecha_5")
        self.parameterLineEditFecha_5.setGeometry(QRect(200, 160, 111, 31))
        self.parameterLineEditFecha_5.setFont(font4)
        self.parameterLineEditVisitante_5 = QLineEdit(self.tab_6)
        self.parameterLineEditVisitante_5.setObjectName(u"parameterLineEditVisitante_5")
        self.parameterLineEditVisitante_5.setGeometry(QRect(320, 160, 371, 31))
        self.parameterLineEditVisitante_5.setFont(font4)
        self.label_38 = QLabel(self.tab_6)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setGeometry(QRect(700, 190, 191, 21))
        self.label_38.setFont(font2)
        self.label_39 = QLabel(self.tab_6)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setGeometry(QRect(1010, 190, 101, 21))
        self.label_39.setFont(font2)
        self.ast_dni_5 = QLabel(self.tab_6)
        self.ast_dni_5.setObjectName(u"ast_dni_5")
        self.ast_dni_5.setGeometry(QRect(30, 190, 21, 21))
        self.ast_dni_5.setFont(font1)
        self.label_40 = QLabel(self.tab_6)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setGeometry(QRect(200, 190, 81, 21))
        self.label_40.setFont(font2)
        self.searchByPiso_5 = QComboBox(self.tab_6)
        self.searchByPiso_5.setObjectName(u"searchByPiso_5")
        self.searchByPiso_5.setGeometry(QRect(110, 160, 81, 31))
        self.searchByPiso_5.setFont(font4)
        self.label_41 = QLabel(self.tab_6)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setGeometry(QRect(320, 190, 191, 21))
        self.label_41.setFont(font2)
        self.searchByEstado_5 = QComboBox(self.tab_6)
        self.searchByEstado_5.setObjectName(u"searchByEstado_5")
        self.searchByEstado_5.setGeometry(QRect(1010, 160, 141, 31))
        self.searchByEstado_5.setFont(font4)
        self.buttonsFrame_5 = QFrame(self.tab_6)
        self.buttonsFrame_5.setObjectName(u"buttonsFrame_5")
        self.buttonsFrame_5.setGeometry(QRect(0, 0, 1331, 151))
        sizePolicy.setHeightForWidth(self.buttonsFrame_5.sizePolicy().hasHeightForWidth())
        self.buttonsFrame_5.setSizePolicy(sizePolicy)
        self.buttonsFrame_5.setFrameShape(QFrame.StyledPanel)
        self.buttonsFrame_5.setFrameShadow(QFrame.Raised)
        self.open_new_button_9 = QPushButton(self.buttonsFrame_5)
        self.open_new_button_9.setObjectName(u"open_new_button_9")
        self.open_new_button_9.setGeometry(QRect(20, 50, 201, 91))
        self.open_new_button_9.setCursor(QCursor(Qt.PointingHandCursor))
        self.open_new_button_9.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#0069c0;\n"
"}\n"
"")
        self.open_new_button_9.setIcon(icon)
        self.open_new_button_9.setIconSize(QSize(200, 200))
        self.open_new_button_9.setFlat(True)
        self.open_new_button_10 = QPushButton(self.buttonsFrame_5)
        self.open_new_button_10.setObjectName(u"open_new_button_10")
        self.open_new_button_10.setGeometry(QRect(230, 50, 201, 91))
        self.open_new_button_10.setCursor(QCursor(Qt.PointingHandCursor))
        self.open_new_button_10.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#0069c0;\n"
"}\n"
"")
        icon9 = QIcon()
        icon9.addFile(u"./assets/icons/icon_mod.png", QSize(), QIcon.Normal, QIcon.Off)
        self.open_new_button_10.setIcon(icon9)
        self.open_new_button_10.setIconSize(QSize(200, 200))
        self.open_new_button_10.setFlat(True)
        self.delete_book_button_5 = QPushButton(self.buttonsFrame_5)
        self.delete_book_button_5.setObjectName(u"delete_book_button_5")
        self.delete_book_button_5.setGeometry(QRect(440, 50, 201, 91))
        self.delete_book_button_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.delete_book_button_5.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#0069c0;\n"
"}\n"
"")
        self.delete_book_button_5.setIcon(icon1)
        self.delete_book_button_5.setIconSize(QSize(200, 200))
        self.delete_book_button_5.setFlat(True)
        self.excel_generate_button_5 = QPushButton(self.buttonsFrame_5)
        self.excel_generate_button_5.setObjectName(u"excel_generate_button_5")
        self.excel_generate_button_5.setGeometry(QRect(850, 50, 201, 91))
        self.excel_generate_button_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.excel_generate_button_5.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#0069c0;\n"
"}\n"
"")
        self.excel_generate_button_5.setIcon(icon2)
        self.excel_generate_button_5.setIconSize(QSize(200, 200))
        self.excel_generate_button_5.setFlat(True)
        self.marcar_salida_button_5 = QPushButton(self.buttonsFrame_5)
        self.marcar_salida_button_5.setObjectName(u"marcar_salida_button_5")
        self.marcar_salida_button_5.setGeometry(QRect(650, 50, 201, 91))
        self.marcar_salida_button_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.marcar_salida_button_5.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#0069c0;\n"
"}\n"
"")
        icon10 = QIcon()
        icon10.addFile(u"./assets/icons/icon_marcar_exit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.marcar_salida_button_5.setIcon(icon10)
        self.marcar_salida_button_5.setIconSize(QSize(200, 200))
        self.marcar_salida_button_5.setFlat(True)
        self.searchButton_10 = QPushButton(self.buttonsFrame_5)
        self.searchButton_10.setObjectName(u"searchButton_10")
        self.searchButton_10.setGeometry(QRect(1170, 100, 151, 41))
        self.searchButton_10.setFont(font3)
        self.searchButton_10.setStyleSheet(u"QPushButton\n"
"{	\n"
"	height: 2em;\n"
" 	border-style: solid;\n"
"	border-width: 2px;\n"
" 	border-color: #1D6F42;\n"
"	background-color:#26914A;\n"
"	font-weight: bold;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   	background-color:#1D6F42;\n"
"	color:white;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"")
        icon11 = QIcon()
        icon11.addFile(u"./assets/icons/refresh-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.searchButton_10.setIcon(icon11)
        self.searchButton_10.setIconSize(QSize(25, 25))
        self.label_42 = QLabel(self.tab_6)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setGeometry(QRect(110, 190, 81, 21))
        self.label_42.setFont(font2)
        self.label_43 = QLabel(self.tab_6)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setGeometry(QRect(0, 10, 1321, 41))
        self.label_43.setStyleSheet(u"background-color: green;")
        self.listBooksTable_5 = QTableWidget(self.tab_6)
        self.listBooksTable_5.setObjectName(u"listBooksTable_5")
        self.listBooksTable_5.setGeometry(QRect(0, 220, 1321, 411))
        self.listBooksTable_5.setAutoFillBackground(True)
        self.listBooksTable_5.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.listBooksTable_5.setTextElideMode(Qt.ElideLeft)
        self.listBooksTable_5.horizontalHeader().setMinimumSectionSize(10)
        self.label_advertencia_sin_resultados_5 = QLabel(self.tab_6)
        self.label_advertencia_sin_resultados_5.setObjectName(u"label_advertencia_sin_resultados_5")
        self.label_advertencia_sin_resultados_5.setGeometry(QRect(790, 140, 351, 21))
        self.label_advertencia_sin_resultados_5.setFont(font1)
        self.label_44 = QLabel(self.tab_6)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setGeometry(QRect(0, 630, 141, 16))
        self.label_44.setFont(font1)
        self.booksQtyLabel_5 = QLabel(self.tab_6)
        self.booksQtyLabel_5.setObjectName(u"booksQtyLabel_5")
        self.booksQtyLabel_5.setGeometry(QRect(150, 630, 47, 16))
        self.booksQtyLabel_5.setFont(font1)
        self.label_advertencia_filtros_5 = QLabel(self.tab_6)
        self.label_advertencia_filtros_5.setObjectName(u"label_advertencia_filtros_5")
        self.label_advertencia_filtros_5.setGeometry(QRect(730, 140, 431, 21))
        self.label_advertencia_filtros_5.setFont(font1)
        self.label_advertencia_dni_5 = QLabel(self.tab_6)
        self.label_advertencia_dni_5.setObjectName(u"label_advertencia_dni_5")
        self.label_advertencia_dni_5.setGeometry(QRect(800, 140, 351, 21))
        self.label_advertencia_dni_5.setFont(font1)
        self.tabWidget_2.addTab(self.tab_6, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.tabWidget_2.addTab(self.tab_7, "")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.buttonsFrame_6 = QFrame(self.tab_8)
        self.buttonsFrame_6.setObjectName(u"buttonsFrame_6")
        self.buttonsFrame_6.setGeometry(QRect(0, 0, 1331, 151))
        sizePolicy.setHeightForWidth(self.buttonsFrame_6.sizePolicy().hasHeightForWidth())
        self.buttonsFrame_6.setSizePolicy(sizePolicy)
        self.buttonsFrame_6.setFrameShape(QFrame.StyledPanel)
        self.buttonsFrame_6.setFrameShadow(QFrame.Raised)
        self.open_new_button_11 = QPushButton(self.buttonsFrame_6)
        self.open_new_button_11.setObjectName(u"open_new_button_11")
        self.open_new_button_11.setGeometry(QRect(20, 50, 201, 91))
        self.open_new_button_11.setCursor(QCursor(Qt.PointingHandCursor))
        self.open_new_button_11.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#0069c0;\n"
"}\n"
"")
        self.open_new_button_11.setIcon(icon)
        self.open_new_button_11.setIconSize(QSize(200, 200))
        self.open_new_button_11.setFlat(True)
        self.open_new_button_12 = QPushButton(self.buttonsFrame_6)
        self.open_new_button_12.setObjectName(u"open_new_button_12")
        self.open_new_button_12.setGeometry(QRect(230, 50, 201, 91))
        self.open_new_button_12.setCursor(QCursor(Qt.PointingHandCursor))
        self.open_new_button_12.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#0069c0;\n"
"}\n"
"")
        self.open_new_button_12.setIcon(icon9)
        self.open_new_button_12.setIconSize(QSize(200, 200))
        self.open_new_button_12.setFlat(True)
        self.delete_book_button_6 = QPushButton(self.buttonsFrame_6)
        self.delete_book_button_6.setObjectName(u"delete_book_button_6")
        self.delete_book_button_6.setGeometry(QRect(440, 50, 201, 91))
        self.delete_book_button_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.delete_book_button_6.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#0069c0;\n"
"}\n"
"")
        self.delete_book_button_6.setIcon(icon1)
        self.delete_book_button_6.setIconSize(QSize(200, 200))
        self.delete_book_button_6.setFlat(True)
        self.excel_generate_button_6 = QPushButton(self.buttonsFrame_6)
        self.excel_generate_button_6.setObjectName(u"excel_generate_button_6")
        self.excel_generate_button_6.setGeometry(QRect(850, 50, 201, 91))
        self.excel_generate_button_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.excel_generate_button_6.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#0069c0;\n"
"}\n"
"")
        self.excel_generate_button_6.setIcon(icon2)
        self.excel_generate_button_6.setIconSize(QSize(200, 200))
        self.excel_generate_button_6.setFlat(True)
        self.marcar_salida_button_6 = QPushButton(self.buttonsFrame_6)
        self.marcar_salida_button_6.setObjectName(u"marcar_salida_button_6")
        self.marcar_salida_button_6.setGeometry(QRect(650, 50, 201, 91))
        self.marcar_salida_button_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.marcar_salida_button_6.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#0069c0;\n"
"}\n"
"")
        self.marcar_salida_button_6.setIcon(icon10)
        self.marcar_salida_button_6.setIconSize(QSize(200, 200))
        self.marcar_salida_button_6.setFlat(True)
        self.searchButton_11 = QPushButton(self.buttonsFrame_6)
        self.searchButton_11.setObjectName(u"searchButton_11")
        self.searchButton_11.setGeometry(QRect(1170, 110, 151, 41))
        self.searchButton_11.setFont(font3)
        self.searchButton_11.setStyleSheet(u"QPushButton\n"
"{	\n"
"	height: 2em;\n"
" 	border-style: solid;\n"
"	border-width: 2px;\n"
" 	border-color: #1D6F42;\n"
"	background-color:#26914A;\n"
"	font-weight: bold;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   	background-color:#1D6F42;\n"
"	color:white;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"")
        self.searchButton_11.setIcon(icon11)
        self.searchButton_11.setIconSize(QSize(25, 25))
        self.label_45 = QLabel(self.buttonsFrame_6)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setGeometry(QRect(0, 10, 1321, 41))
        self.label_45.setStyleSheet(u"background-color: BLUE;")
        self.label_advertencia_filtros_6 = QLabel(self.tab_8)
        self.label_advertencia_filtros_6.setObjectName(u"label_advertencia_filtros_6")
        self.label_advertencia_filtros_6.setGeometry(QRect(740, 140, 431, 21))
        self.label_advertencia_filtros_6.setFont(font1)
        self.label_46 = QLabel(self.tab_8)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setGeometry(QRect(110, 190, 81, 21))
        self.label_46.setFont(font2)
        self.searchByPiso_6 = QComboBox(self.tab_8)
        self.searchByPiso_6.setObjectName(u"searchByPiso_6")
        self.searchByPiso_6.setGeometry(QRect(110, 160, 81, 31))
        self.searchByPiso_6.setFont(font4)
        self.label_47 = QLabel(self.tab_8)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setGeometry(QRect(200, 190, 81, 21))
        self.label_47.setFont(font2)
        self.searchByEstado_6 = QComboBox(self.tab_8)
        self.searchByEstado_6.setObjectName(u"searchByEstado_6")
        self.searchByEstado_6.setGeometry(QRect(1010, 160, 141, 31))
        self.searchByEstado_6.setFont(font4)
        self.label_48 = QLabel(self.tab_8)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setGeometry(QRect(700, 190, 191, 21))
        self.label_48.setFont(font2)
        self.parameterLineEditDNI_6 = QLineEdit(self.tab_8)
        self.parameterLineEditDNI_6.setObjectName(u"parameterLineEditDNI_6")
        self.parameterLineEditDNI_6.setGeometry(QRect(0, 160, 101, 31))
        self.parameterLineEditDNI_6.setFont(font4)
        self.parameterLineEditFecha_6 = QLineEdit(self.tab_8)
        self.parameterLineEditFecha_6.setObjectName(u"parameterLineEditFecha_6")
        self.parameterLineEditFecha_6.setGeometry(QRect(200, 160, 111, 31))
        self.parameterLineEditFecha_6.setFont(font4)
        self.parameterLineEditMotivo_6 = QLineEdit(self.tab_8)
        self.parameterLineEditMotivo_6.setObjectName(u"parameterLineEditMotivo_6")
        self.parameterLineEditMotivo_6.setGeometry(QRect(700, 160, 301, 31))
        self.parameterLineEditMotivo_6.setFont(font4)
        self.label_49 = QLabel(self.tab_8)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setGeometry(QRect(0, 190, 81, 21))
        self.label_49.setFont(font2)
        self.parameterLineEditVisitante_6 = QLineEdit(self.tab_8)
        self.parameterLineEditVisitante_6.setObjectName(u"parameterLineEditVisitante_6")
        self.parameterLineEditVisitante_6.setGeometry(QRect(320, 160, 371, 31))
        self.parameterLineEditVisitante_6.setFont(font4)
        self.label_advertencia_sin_resultados_6 = QLabel(self.tab_8)
        self.label_advertencia_sin_resultados_6.setObjectName(u"label_advertencia_sin_resultados_6")
        self.label_advertencia_sin_resultados_6.setGeometry(QRect(790, 140, 351, 21))
        self.label_advertencia_sin_resultados_6.setFont(font1)
        self.searchButton_12 = QPushButton(self.tab_8)
        self.searchButton_12.setObjectName(u"searchButton_12")
        self.searchButton_12.setGeometry(QRect(1170, 160, 151, 41))
        self.searchButton_12.setFont(font3)
        self.searchButton_12.setCursor(QCursor(Qt.PointingHandCursor))
        self.searchButton_12.setStyleSheet(u"QPushButton\n"
"{	\n"
"	height: 2em;\n"
" 	border-style: solid;\n"
"	border-width: 2px;\n"
" 	border-color: #00AAFF;\n"
"	background-color:#00AAFF;\n"
"	font-weight: bold;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   	background-color:#0069c0;\n"
"	color:white;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"")
        self.searchButton_12.setIcon(icon8)
        self.searchButton_12.setIconSize(QSize(25, 25))
        self.ast_dni_6 = QLabel(self.tab_8)
        self.ast_dni_6.setObjectName(u"ast_dni_6")
        self.ast_dni_6.setGeometry(QRect(30, 190, 21, 21))
        self.ast_dni_6.setFont(font1)
        self.label_50 = QLabel(self.tab_8)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setGeometry(QRect(320, 190, 191, 21))
        self.label_50.setFont(font2)
        self.label_51 = QLabel(self.tab_8)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setGeometry(QRect(1010, 190, 101, 21))
        self.label_51.setFont(font2)
        self.listBooksTable_6 = QTableWidget(self.tab_8)
        self.listBooksTable_6.setObjectName(u"listBooksTable_6")
        self.listBooksTable_6.setGeometry(QRect(0, 220, 1321, 411))
        self.listBooksTable_6.setToolTipDuration(-1)
        self.listBooksTable_6.setAutoFillBackground(True)
        self.listBooksTable_6.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.listBooksTable_6.setTextElideMode(Qt.ElideLeft)
        self.listBooksTable_6.horizontalHeader().setMinimumSectionSize(10)
        self.label_52 = QLabel(self.tab_8)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setGeometry(QRect(0, 630, 141, 16))
        self.label_52.setFont(font1)
        self.booksQtyLabel_6 = QLabel(self.tab_8)
        self.booksQtyLabel_6.setObjectName(u"booksQtyLabel_6")
        self.booksQtyLabel_6.setGeometry(QRect(150, 630, 47, 16))
        self.booksQtyLabel_6.setFont(font1)
        self.label_advertencia_dni_6 = QLabel(self.tab_8)
        self.label_advertencia_dni_6.setObjectName(u"label_advertencia_dni_6")
        self.label_advertencia_dni_6.setGeometry(QRect(810, 140, 351, 21))
        self.label_advertencia_dni_6.setFont(font1)
        self.tabWidget_2.addTab(self.tab_8, "")
        self.tabWidget.addTab(self.tab_4, "")
        QWidget.setTabOrder(self.tableGeneracion, self.open_button_generacion)
        QWidget.setTabOrder(self.open_button_generacion, self.delete_btn_generacion)
        QWidget.setTabOrder(self.delete_btn_generacion, self.excel_btn_generacion)

        self.retranslateUi(ListBookForm)

        self.tabWidget.setCurrentIndex(0)
        self.open_button_generacion.setDefault(True)
        self.delete_btn_generacion.setDefault(True)
        self.excel_btn_generacion.setDefault(True)
        self.btn_guardar_bd.setDefault(True)
        self.btn_usuarios.setDefault(True)
        self.btn_cerrar_sesion.setDefault(True)
        self.btn_auditoria.setDefault(True)
        self.btn_carga.setDefault(True)
        self.open_button_subestacion.setDefault(True)
        self.delete_btn_subestacion.setDefault(True)
        self.excel_btn_subestacion.setDefault(True)
        self.tabWidget_2.setCurrentIndex(0)
        self.open_button_linea.setDefault(True)
        self.delete_btn_linea.setDefault(True)
        self.excel_btn_linea.setDefault(True)
        self.searchButton_9.setDefault(True)
        self.open_new_button_9.setDefault(True)
        self.open_new_button_10.setDefault(True)
        self.delete_book_button_5.setDefault(True)
        self.excel_generate_button_5.setDefault(True)
        self.marcar_salida_button_5.setDefault(True)
        self.searchButton_10.setDefault(True)
        self.open_new_button_11.setDefault(True)
        self.open_new_button_12.setDefault(True)
        self.delete_book_button_6.setDefault(True)
        self.excel_generate_button_6.setDefault(True)
        self.marcar_salida_button_6.setDefault(True)
        self.searchButton_11.setDefault(True)
        self.searchButton_12.setDefault(True)


        QMetaObject.connectSlotsByName(ListBookForm)
    # setupUi

    def retranslateUi(self, ListBookForm):
        ListBookForm.setWindowTitle(QCoreApplication.translate("ListBookForm", u"Sistema de Registro de Centrales de Energ\u00eda El\u00e9ctrica - OSINERGMIN", None))
        self.label_6.setText(QCoreApplication.translate("ListBookForm", u"<html><head/><body><p><span style=\" font-weight:600;\">N\u00famero de registros:</span></p></body></html>", None))
        self.open_button_generacion.setText("")
        self.delete_btn_generacion.setText("")
        self.label_7.setText(QCoreApplication.translate("ListBookForm", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">INSTALACIONES EL\u00c9CTRICAS - CENTRAL DE GENERACI\u00d3N </span></p></body></html>", None))
        self.excel_btn_generacion.setText("")
        self.btn_guardar_bd.setText(QCoreApplication.translate("ListBookForm", u"Guardar Base\n"
"de Datos", None))
        self.btn_usuarios.setText(QCoreApplication.translate("ListBookForm", u"Gesti\u00f3n de\n"
" Usuarios", None))
        self.btn_cerrar_sesion.setText(QCoreApplication.translate("ListBookForm", u"Cerrar\n"
"Sesi\u00f3n", None))
        self.btn_auditoria.setText(QCoreApplication.translate("ListBookForm", u"M\u00f3dulo de\n"
" Auditor\u00eda", None))
        self.btn_carga.setText(QCoreApplication.translate("ListBookForm", u"Carga\n"
"Masiva", None))
        self.label_8.setText(QCoreApplication.translate("ListBookForm", u"<html><head/><body><p><span style=\" font-weight:600; color:#ffffff;\">Versi\u00f3n: 3.2</span></p></body></html>", None))
        self.labelNumeroRegistros.setText(QCoreApplication.translate("ListBookForm", u"#", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("ListBookForm", u"GENERACI\u00d3N", None))
        self.open_button_subestacion.setText("")
        self.delete_btn_subestacion.setText("")
        self.excel_btn_subestacion.setText("")
        self.label_18.setText(QCoreApplication.translate("ListBookForm", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\"> TRANSMISI\u00d3N - SUBESTACI\u00d3N </span></p></body></html>", None))
        self.label_20.setText(QCoreApplication.translate("ListBookForm", u"<html><head/><body><p><span style=\" font-weight:600;\">N\u00famero de registros:</span></p></body></html>", None))
        self.booksQtyLabel_2.setText(QCoreApplication.translate("ListBookForm", u"#", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("ListBookForm", u"SUBESTACI\u00d3N", None))
        self.label_29.setText(QCoreApplication.translate("ListBookForm", u"<html><head/><body><p><span style=\" font-weight:600;\">N\u00famero de registros:</span></p></body></html>", None))
        self.open_button_linea.setText("")
        self.delete_btn_linea.setText("")
        self.label_30.setText(QCoreApplication.translate("ListBookForm", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">TRANSMISI\u00d3N - L\u00cdNEA DE TRASMISI\u00d3N </span></p></body></html>", None))
        self.excel_btn_linea.setText("")
        self.booksQtyLabel_4.setText(QCoreApplication.translate("ListBookForm", u"#", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), QCoreApplication.translate("ListBookForm", u"VISITAS", None))
        self.searchButton_9.setText(QCoreApplication.translate("ListBookForm", u" BUSCAR", None))
        self.label_37.setText(QCoreApplication.translate("ListBookForm", u"DNI", None))
        self.label_38.setText(QCoreApplication.translate("ListBookForm", u"MOTIVO", None))
        self.label_39.setText(QCoreApplication.translate("ListBookForm", u"ESTADO", None))
        self.ast_dni_5.setText(QCoreApplication.translate("ListBookForm", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; font-style:italic; color:#ff0000;\">*</span></p><p><span style=\" font-weight:600;\"><br/></span></p></body></html>", None))
        self.label_40.setText(QCoreApplication.translate("ListBookForm", u"FECHA", None))
        self.label_41.setText(QCoreApplication.translate("ListBookForm", u"NOMBRE DEL LOCADOR", None))
        self.open_new_button_9.setText("")
        self.open_new_button_10.setText("")
        self.delete_book_button_5.setText("")
        self.excel_generate_button_5.setText("")
        self.marcar_salida_button_5.setText("")
        self.searchButton_10.setText(QCoreApplication.translate("ListBookForm", u" ACTUALIZAR", None))
        self.label_42.setText(QCoreApplication.translate("ListBookForm", u"PISO", None))
        self.label_43.setText(QCoreApplication.translate("ListBookForm", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">REGISTRO DE LOCADORES - FEBAN</span></p></body></html>", None))
        self.label_advertencia_sin_resultados_5.setText(QCoreApplication.translate("ListBookForm", u"<html><head/><body><p align=\"right\"><span style=\" font-style:italic; color:#ff0000;\">No existen registros con los par\u00e1metros brindados...</span></p></body></html>", None))
        self.label_44.setText(QCoreApplication.translate("ListBookForm", u"<html><head/><body><p><span style=\" font-weight:600;\">N\u00famero de registros:</span></p></body></html>", None))
        self.booksQtyLabel_5.setText(QCoreApplication.translate("ListBookForm", u"#", None))
        self.label_advertencia_filtros_5.setText(QCoreApplication.translate("ListBookForm", u"<html><head/><body><p><span style=\" font-style:italic; color:#ff0000;\">\u00a1Ingrese datos en al menos uno de los campos para realizar la b\u00fasqueda!</span></p></body></html>", None))
        self.label_advertencia_dni_5.setText(QCoreApplication.translate("ListBookForm", u"<html><head/><body><p align=\"right\"><span style=\" font-style:italic; color:#ff0000;\">El DNI debe contener 8 d\u00edgitos!</span></p></body></html>", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), QCoreApplication.translate("ListBookForm", u"LOCADORES", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_7), QCoreApplication.translate("ListBookForm", u"PERSONAL FEBAN", None))
        self.open_new_button_11.setText("")
        self.open_new_button_12.setText("")
        self.delete_book_button_6.setText("")
        self.excel_generate_button_6.setText("")
        self.marcar_salida_button_6.setText("")
        self.searchButton_11.setText(QCoreApplication.translate("ListBookForm", u" ACTUALIZAR", None))
        self.label_45.setText(QCoreApplication.translate("ListBookForm", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">REGISTRO DE PERSONAL DE MANTENIMIENTO - FEBAN</span></p></body></html>", None))
        self.label_advertencia_filtros_6.setText(QCoreApplication.translate("ListBookForm", u"<html><head/><body><p><span style=\" font-style:italic; color:#ff0000;\">\u00a1Ingrese datos en al menos uno de los campos para realizar la b\u00fasqueda!</span></p></body></html>", None))
        self.label_46.setText(QCoreApplication.translate("ListBookForm", u"PISO", None))
        self.label_47.setText(QCoreApplication.translate("ListBookForm", u"FECHA", None))
        self.label_48.setText(QCoreApplication.translate("ListBookForm", u"MOTIVO", None))
        self.label_49.setText(QCoreApplication.translate("ListBookForm", u"DNI", None))
        self.label_advertencia_sin_resultados_6.setText(QCoreApplication.translate("ListBookForm", u"<html><head/><body><p align=\"right\"><span style=\" font-style:italic; color:#ff0000;\">No existen registros con los par\u00e1metros brindados...</span></p></body></html>", None))
        self.searchButton_12.setText(QCoreApplication.translate("ListBookForm", u" BUSCAR", None))
        self.ast_dni_6.setText(QCoreApplication.translate("ListBookForm", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; font-style:italic; color:#ff0000;\">*</span></p><p><span style=\" font-weight:600;\"><br/></span></p></body></html>", None))
        self.label_50.setText(QCoreApplication.translate("ListBookForm", u"NOMBRE DEL PERSONAL", None))
        self.label_51.setText(QCoreApplication.translate("ListBookForm", u"ESTADO", None))
        self.label_52.setText(QCoreApplication.translate("ListBookForm", u"<html><head/><body><p><span style=\" font-weight:600;\">N\u00famero de registros:</span></p></body></html>", None))
        self.booksQtyLabel_6.setText(QCoreApplication.translate("ListBookForm", u"#", None))
        self.label_advertencia_dni_6.setText(QCoreApplication.translate("ListBookForm", u"<html><head/><body><p align=\"right\"><span style=\" font-style:italic; color:#ff0000;\">El DNI debe contener 8 d\u00edgitos!</span></p></body></html>", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_8), QCoreApplication.translate("ListBookForm", u"MANTENIMIENTO", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("ListBookForm", u"L\u00cdNEA DE TRANSMISI\u00d3N", None))
    # retranslateUi

