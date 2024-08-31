from PySide2.QtWidgets import QDialog,QMessageBox,QAbstractItemView,QWidget,QTableWidgetItem,QHeaderView
from PySide2.QtCore import Qt
from views.new_usuarios import Ui_NewBook
from PySide2 import QtCore
from pys2_msgboxes import msg_boxes
from db.books import delete_usuario,SelectUsuarios,insert_usuario
from datetime import date
from PySide2.QtGui import *

class NewBookWindow(QDialog,Ui_NewBook):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)
        #self.setMaximumSize(QtCore.QSize(902, 408))
        self.table_config()
        self.populate_table(SelectUsuarios("1"))
        self.label.setStyleSheet("background-color: #114692;")
        self.addButton.clicked.connect(self.add_user)
        self.btnDelete.clicked.connect(self.remove_book)
        self.cancelButton.clicked.connect(self.close)
        
        self.tableGeneracion.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableGeneracion.verticalHeader().setVisible(False)
        self.tableGeneracion.setColumnWidth(0,19)
        headerVertical = self.tableGeneracion.verticalHeader()
        headerVertical.resizeSections(QHeaderView.ResizeToContents)
        headerVertical.setStretchLastSection(True)
 

    def table_config(self):
        column_headers = ("#", "Usuario","Contraseña")
        self.tableGeneracion.setColumnCount(len(column_headers))
        self.tableGeneracion.setHorizontalHeaderLabels(column_headers)
        self.tableGeneracion.setSelectionMode(QAbstractItemView.SingleSelection)
        stylesheet = "::section{Background-color:#114692;border:1px solid black;color: white;}"
        self.tableGeneracion.horizontalHeader().setStyleSheet(stylesheet)
        self.tableGeneracion.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableGeneracion.setStyleSheet("QTableWidget{ gridline-color:black;alternate-background-color: #E2DED0;}")
        self.tableGeneracion.setAlternatingRowColors(True)
        # Puedes agregar configuraciones adicionales aquí, como estilos de encabezado, colores de fondo, etc.

    def populate_table(self,data):
        
        if data is not None:
            self.tableGeneracion.setRowCount(len(data))
            print("REFRESH4")
            for index_row, row in enumerate(data):
                # Incrementamos el índice de fila en 1 para comenzar con el número de orden en 1
                order_number = index_row + 1
                
                # Establecemos el número de orden en la primera columna
                self.tableGeneracion.setItem(index_row, 0, QTableWidgetItem(str(order_number)))
                
                for index_cell, cell in enumerate(row):
                    # Llenamos los datos de la fila a partir de la segunda columna
                    self.tableGeneracion.setItem(index_row, index_cell + 1, QTableWidgetItem(str(cell)))
                    
                    if index_cell == 13:
                        itemx = self.tableGeneracion.item(index_row, index_cell + 1)  # Se ajusta el índice de la celda
                        print("EL ITEM ACTUAL ES: ", itemx)
                        if itemx.text() == "PENDIENTE":
                            itemx.setForeground(QBrush(QColor(255, 0, 0)))
                        else:
                            itemx.setForeground(QBrush(QColor(0, 0, 255)))

            print("REFRESH5")
            headerVertical = self.tableGeneracion.verticalHeader()
            headerVertical.resizeSections(QHeaderView.ResizeToContents)
            headerVertical.setStretchLastSection(True)

    def add_user(self):
        usuario = self.inputUsuario.text()
        contrasenia = self.inputPass.text()
        insert_usuario(usuario,contrasenia,"")
        self.inputUsuario.setText("")
        self.inputPass.setText("")
        self.populate_table(SelectUsuarios("1"))
    
    def remove_book(self):
        selected_row = self.tableGeneracion.selectedItems()
        print("SELECT ROWWWWW: "+str(selected_row))
        if len(selected_row)!=0:
            respuesta=msg_boxes.alert_msgbox("Corfirmar Eliminar","¿Estas seguro de eliminar el registro?")
            if respuesta== QMessageBox.Yes:
                if selected_row:
                    book_id = str(selected_row[1].text())
                    row = selected_row[1].row()

                    if delete_usuario(book_id):
                    
                        self.tableGeneracion.removeRow(row)

