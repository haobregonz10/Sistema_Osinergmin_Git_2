from PySide2.QtWidgets import QWidget, QTableWidgetItem,QMessageBox
from views.main_windows import *
from controllers.AlignDelegate import *
from PySide2 import QtCore
from db.books import select_all_books_linea_admin,select_all_books_subestacion_admin,select_all_books_admin,buscar_usuario_acceso,delete_book_Linea_Transmision,delete_book_Subestacion,delete_book_Central_Generacion,select_all_books,delete_book,select_book_by_all,EncontrarDni,ExisteDni,select_all_books_subestacion,select_all_books_linea
from db.bookstemp import update_database
from pys2_msgboxes import msg_boxes
import shutil
import sqlite3
from sqlite3 import Error
import pandas as pd
import os

class ListBookWindow(QWidget,Ui_ListBookForm):
    def __init__(self,parent=None):
        super().__init__()
        self.setupUi(self)
        self.parent = parent

        self.label_30.setStyleSheet("background-color: #114692;")
        self.label_18.setStyleSheet("background-color: #114692;")
        self.label_7.setStyleSheet("background-color: #114692;")
        self.label_8.setStyleSheet("color: white; font-weight: bold;")
        self.label_8.setText("Versión: 3.4")
        ######################## GENERACIÓN ##################################################
        self.open_button_generacion.clicked.connect(self.open_new_book_window)


        self.open_button_subestacion.clicked.connect(self.open_subestacion)

        self.open_button_linea.clicked.connect(self.open_linea)
        self.excel_btn_generacion.clicked.connect(self.descargar_excel_generacion)
        self.excel_btn_subestacion.clicked.connect(self.descargar_excel_generacion)
        self.excel_btn_linea.clicked.connect(self.descargar_excel_generacion)
        self.btn_guardar_bd.clicked.connect(self.descargar_DB)
        self.btn_cerrar_sesion.clicked.connect(self.cerrar_sesion)
        self.login_window = None
        self.btn_usuarios.clicked.connect(self.gestionar_usuarios)
        self.btn_auditoria.clicked.connect(self.ver_auditoria)
        self.btn_carga.clicked.connect(self.ver_carga)
        self.delete_btn_generacion.clicked.connect(self.remove_book)
        self.delete_btn_subestacion.clicked.connect(self.remove_book_subestacion)
        self.delete_btn_linea.clicked.connect(self.remove_book_linea)
        Usuario= buscar_usuario_acceso();
        self.userEs=Usuario
        print("EL USUARIO DE ACCESO ES:"+Usuario)
        if(Usuario!="admin"):
            print("NO ES ADMIN!!!")
            self.btn_usuarios.hide()
            self.btn_auditoria.hide()
            self.btn_carga.hide()
            self.table_config()
            self.table_config_subestacion()
            self.table_config_linea()
            self.populate_table(select_all_books(Usuario))
            self.populate_table_subestacion(select_all_books_subestacion(Usuario))
            self.populate_table_linea(select_all_books_linea(Usuario))
        #self.populate_comboboxEstado()
        else:
            print("ES ADMIN!!!") 
            self.table_config_admin()
            self.table_config_subestacion_admin()
            self.table_config_linea_admin()
            self.populate_table(select_all_books_admin())
            self.populate_table_subestacion(select_all_books_subestacion_admin())
            self.populate_table_linea(select_all_books_linea_admin())
            
        self.tableGeneracion.itemSelectionChanged.connect(lambda:(self.records_qty_select()))



        

        #Actualizar
        # self.searchButton_2.clicked.connect( lambda: self.populate_table_refresh(select_all_books()))
        # self.searchButton.clicked.connect(self.searchAll)#BUSCAR BOTON
        # self.delete_book_button.clicked.connect(self.remove_book)
        # self.excel_generate_button.clicked.connect(self.open_confirm_excel)

        self.tableGeneracion.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableGeneracion.verticalHeader().setVisible(False)
        self.tableGeneracion.setColumnWidth(0,19)



        headerVertical = self.tableGeneracion.verticalHeader()
        headerVertical.resizeSections(QHeaderView.ResizeToContents)
        headerVertical.setStretchLastSection(True)

        delegate= AlignDelegate(self.tableGeneracion)

        self.tableGeneracion.setItemDelegateForColumn(0,delegate)
        self.tableGeneracion.setItemDelegateForColumn(1,delegate)
        self.tableGeneracion.setItemDelegateForColumn(2,delegate)
        self.tableGeneracion.setItemDelegateForColumn(3,delegate)
        self.tableGeneracion.setItemDelegateForColumn(4,delegate)
        self.tableGeneracion.setItemDelegateForColumn(5,delegate)
        self.tableGeneracion.setItemDelegateForColumn(6,delegate)
        self.tableGeneracion.setItemDelegateForColumn(7,delegate)
        self.tableGeneracion.setItemDelegateForColumn(8,delegate)
        self.tableGeneracion.setItemDelegateForColumn(9,delegate)
        self.tableGeneracion.setItemDelegateForColumn(10,delegate)
        self.tableGeneracion.setItemDelegateForColumn(11,delegate)
        self.tableGeneracion.setItemDelegateForColumn(12,delegate)
        self.tableGeneracion.setItemDelegateForColumn(13,delegate)
        self.tableGeneracion.doubleClicked.connect(lambda: self.FilaSeleccionada())


        self.tableGeneracion.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableGeneracion.verticalHeader().setVisible(False)
        self.tableGeneracion.setColumnWidth(0,19)



        headerVertical2 = self.tableSubestacion.verticalHeader()
        headerVertical2.resizeSections(QHeaderView.ResizeToContents)
        headerVertical2.setStretchLastSection(True)

        delegate2= AlignDelegate(self.tableSubestacion)

        self.tableSubestacion.setItemDelegateForColumn(0,delegate2)
        self.tableSubestacion.setItemDelegateForColumn(1,delegate2)
        self.tableSubestacion.setItemDelegateForColumn(2,delegate2)
        self.tableSubestacion.setItemDelegateForColumn(3,delegate2)
        self.tableSubestacion.setItemDelegateForColumn(4,delegate2)
        self.tableSubestacion.setItemDelegateForColumn(5,delegate2)
        self.tableSubestacion.setItemDelegateForColumn(6,delegate2)
        self.tableSubestacion.setItemDelegateForColumn(7,delegate2)
        self.tableSubestacion.setItemDelegateForColumn(8,delegate2)
        self.tableSubestacion.setItemDelegateForColumn(9,delegate2)
        self.tableSubestacion.setItemDelegateForColumn(10,delegate2)
        self.tableSubestacion.setItemDelegateForColumn(11,delegate2)
        self.tableSubestacion.setItemDelegateForColumn(12,delegate2)
        self.tableSubestacion.setItemDelegateForColumn(13,delegate2)
        self.tableSubestacion.doubleClicked.connect(lambda: self.FilaSeleccionadaSubestacion())

        self.tableSubestacion.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableSubestacion.verticalHeader().setVisible(False)
        self.tableSubestacion.setColumnWidth(0,19)



        headerVertical3 = self.tableLinea.verticalHeader()
        headerVertical3.resizeSections(QHeaderView.ResizeToContents)
        headerVertical3.setStretchLastSection(True)

        delegate3= AlignDelegate(self.tableLinea)

        self.tableLinea.setItemDelegateForColumn(0,delegate3)
        self.tableLinea.setItemDelegateForColumn(1,delegate3)
        self.tableLinea.setItemDelegateForColumn(2,delegate3)
        self.tableLinea.setItemDelegateForColumn(3,delegate3)
        self.tableLinea.setItemDelegateForColumn(4,delegate3)
        self.tableLinea.setItemDelegateForColumn(5,delegate3)
        self.tableLinea.setItemDelegateForColumn(6,delegate3)
        self.tableLinea.setItemDelegateForColumn(7,delegate3)
        self.tableLinea.setItemDelegateForColumn(8,delegate3)
        self.tableLinea.setItemDelegateForColumn(9,delegate3)
        self.tableLinea.setItemDelegateForColumn(10,delegate3)
        self.tableLinea.setItemDelegateForColumn(11,delegate3)
        self.tableLinea.setItemDelegateForColumn(12,delegate3)
        self.tableLinea.setItemDelegateForColumn(13,delegate3)
        self.tableLinea.doubleClicked.connect(lambda: self.FilaSeleccionadaLinea())

        self.tableLinea.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableLinea.verticalHeader().setVisible(False)
        self.tableLinea.setColumnWidth(0,19)

        self.setWindowIcon(QIcon('./pys2_msgboxes/icons/banco_icon.png'))

    

    #################################FUNCIONES VISITAS#######################################
    def open_new_book_window(self):
        from controllers.new_window_central import NewBookWindow
        window= NewBookWindow(self)
        window.exec_()
    
    def open_subestacion(self):
        from controllers.new_window_subestacion import NewBookWindow
        window= NewBookWindow(self)
        window.exec_()

    def open_linea(self):
        from controllers.new_window_linea import NewBookWindow
        window= NewBookWindow(self)
        window.exec_()

    def open_confirm_excel(self):
        from controllers.confirm_excel import ConfirmExcel
        window= ConfirmExcel(self)
        window.show()

    def open_edit_book_window(self):
        from controllers.edit_book_window import EditBookWindow
        selected_row = self.tableGeneracion.selectedItems()

        if selected_row:
            book_id = int(selected_row[0].text())
            window = EditBookWindow(self, book_id)
            window.show()
        
        self.tableGeneracion.clearSelection()
       
    
    def open_book(self):
        selected_row = self.tableGeneracion.selectedItems()

        if selected_row:
            path = selected_row[5].text()
            os.startfile(path)
        self.tableGeneracion.clearSelection()

    def remove_book(self):
        selected_row = self.tableGeneracion.selectedItems()
        print("SELECT ROWWWWW: "+str(selected_row))
        if len(selected_row)!=0:
            respuesta=msg_boxes.alert_msgbox("Corfirmar Eliminar","¿Estas seguro de eliminar el registro?")
            if respuesta== QMessageBox.Yes:
                if selected_row:
                    book_id = str(selected_row[1].text())
                    row = selected_row[1].row()

                    if delete_book_Central_Generacion(book_id):
                    
                        self.tableGeneracion.removeRow(row)
                    
            self.records_qty()
        
    def remove_book_subestacion(self):
        selected_row = self.tableSubestacion.selectedItems()
        print("SELECT ROWWWWW: "+str(selected_row))
        if len(selected_row)!=0:
            respuesta=msg_boxes.alert_msgbox("Corfirmar Eliminar","¿Estas seguro de eliminar el registro?")
            if respuesta== QMessageBox.Yes:
                if selected_row:
                    book_id = str(selected_row[1].text())
                    row = selected_row[1].row()

                    if delete_book_Subestacion(book_id):
                    
                        self.tableSubestacion.removeRow(row)
                    
            self.records_qty()
    
    def remove_book_linea(self):
        selected_row = self.tableLinea.selectedItems()
        print("SELECT ROWWWWW: "+str(selected_row))
        if len(selected_row)!=0:
            respuesta=msg_boxes.alert_msgbox("Corfirmar Eliminar","¿Estas seguro de eliminar el registro?")
            if respuesta== QMessageBox.Yes:
                if selected_row:
                    book_id = str(selected_row[1].text())
                    row = selected_row[1].row()

                    if delete_book_Linea_Transmision(book_id):
                    
                        self.tableLinea.removeRow(row)
                    
            self.records_qty()

    def refresh_table_from_child_window(self):
        print("REFRESH FROM CHILD...")   
        print("REFRESH1")
        if(self.userEs!="admin"):
            print("NO ES ADMIN!!!")
            self.populate_table(select_all_books(self.userEs))
        else:
            print("ES ADMIN!!!") 
            self.populate_table(select_all_books_admin())

    def refresh_table_from_child_window_subestacion(self):
        print("REFRESH FROM CHILD...")   
        print("REFRESH1")
        if(self.userEs!="admin"):
            print("NO ES ADMIN!!!")
            self.populate_table_subestacion(select_all_books_subestacion(self.userEs))
        else:
            print("ES ADMIN!!!") 
            self.populate_table_subestacion(select_all_books_subestacion_admin())

    def refresh_table_from_child_window_linea(self):
        print("REFRESH FROM CHILD...")   
        print("REFRESH1")
        if(self.userEs!="admin"):
            print("NO ES ADMIN!!!")
            self.populate_table_linea(select_all_books_linea(self.userEs))
        else:
            print("ES ADMIN!!!") 
            self.populate_table_linea(select_all_books_linea_admin())

    def descargar_excel_generacion(self):
        opciones = QFileDialog.Options()
        nombre_archivo, _ = QFileDialog.getSaveFileName(self, "Guardar archivo Excel", "", "Archivos Excel (*.xlsx);;Todos los archivos (*)", options=opciones)
    
        if nombre_archivo:
            # Conectar a la base de datos SQLite
            conn = sqlite3.connect('DATABASEAPP.db')
            
            # Obtener la lista de tablas
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tablas = cursor.fetchall()
            
            # Crear un objeto ExcelWriter de Pandas para escribir en un archivo Excel
            with pd.ExcelWriter(nombre_archivo if nombre_archivo.endswith('.xlsx') else nombre_archivo + '.xlsx') as writer:
                for tabla in tablas:
                    nombre_tabla = tabla[0]
                    
                    # Truncar el nombre de la tabla si excede los 31 caracteres
                    nombre_hoja = nombre_tabla[:31]
                    
                    # Leer cada tabla de la base de datos como un DataFrame
                    df = pd.read_sql_query(f"SELECT * FROM {nombre_tabla}", conn)
                    
                    # Guardar el DataFrame en una hoja del archivo Excel
                    df.to_excel(writer, sheet_name=nombre_hoja, index=False)
            
            # Cerrar la conexión a la base de datos
            conn.close()
            
            print(f"Archivo '{nombre_archivo}' descargado exitosamente.")
            msg_boxes.correct_msgbox("¡Descarga Exitosa!", "¡Se ha guardado el archivo en la carpeta indicada!")

    def descargar_excel_subestacion(self):
            opciones = QFileDialog.Options()
            nombre_archivo, _ = QFileDialog.getSaveFileName(self, "Guardar archivo Excel", "", "Archivos Excel (*.xlsx);;Todos los archivos (*)", options=opciones)
            if nombre_archivo:
                # Convertir los datos de QTableWidget a un DataFrame de Pandas
                df = pd.DataFrame(columns=[self.tableSubestacion.horizontalHeaderItem(col).text() for col in range(self.tableSubestacion.columnCount())])

                for row in range(self.tableSubestacion.rowCount()):
                    data = []
                    for col in range(self.tableSubestacion.columnCount()):
                        item = self.tableSubestacion.item(row, col)
                        if item is not None:
                            data.append(item.text())
                        else:
                            data.append("")  # Manejar celdas vacías
                    df = pd.concat([df, pd.DataFrame([data], columns=df.columns)], ignore_index=True)

                # Guardar el DataFrame como un archivo Excel en la ruta especificada
                if not nombre_archivo.endswith('.xlsx'):
                    nombre_archivo += '.xlsx'
                df.to_excel(nombre_archivo, index=False)

                print(f"Archivo '{nombre_archivo}' descargado exitosamente.")
                msg_boxes.correct_msgbox("¡Descarga Exitosa!","¡Se ha guardado el archivo en la carpeta indicada!")


    def descargar_excel_linea(self):
            opciones = QFileDialog.Options()
            nombre_archivo, _ = QFileDialog.getSaveFileName(self, "Guardar archivo Excel", "", "Archivos Excel (*.xlsx);;Todos los archivos (*)", options=opciones)
            if nombre_archivo:
                # Convertir los datos de QTableWidget a un DataFrame de Pandas
                df = pd.DataFrame(columns=[self.tableLinea.horizontalHeaderItem(col).text() for col in range(self.tableLinea.columnCount())])

                for row in range(self.tableLinea.rowCount()):
                    data = []
                    for col in range(self.tableLinea.columnCount()):
                        item = self.tableLinea.item(row, col)
                        if item is not None:
                            data.append(item.text())
                        else:
                            data.append("")  # Manejar celdas vacías
                    df = pd.concat([df, pd.DataFrame([data], columns=df.columns)], ignore_index=True)

                # Guardar el DataFrame como un archivo Excel en la ruta especificada
                if not nombre_archivo.endswith('.xlsx'):
                    nombre_archivo += '.xlsx'
                df.to_excel(nombre_archivo, index=False)

                print(f"Archivo '{nombre_archivo}' descargado exitosamente.")
                msg_boxes.correct_msgbox("¡Descarga Exitosa!","¡Se ha guardado el archivo en la carpeta indicada!")

    def descargar_DB(self):
        #Copiar el archivo DATABASEAPP.db a DATABASEAPPTEMP.db, sobrescribiéndolo si ya existe
        try:
            shutil.copy2('./DATABASEAPP.db', './DATABASEAPPTEMP.db')
            print("Archivo DATABASEAPP.db copiado exitosamente a DATABASEAPPTEMP.db.")
        except Exception as e:
            print(f"Error al copiar la base de datos: {e}")
            msg_boxes.error_msgbox("Error", "Se produjo un error al copiar la base de datos.")
            return
        update_database("x")
        opciones = QFileDialog.Options()
        nombre_archivo, _ = QFileDialog.getSaveFileName(self, "Guardar base de datos", "", "Archivos de base de datos (*.db);;Todos los archivos (*)", options=opciones)
        
        if nombre_archivo:
            # Verificar si el archivo ya tiene la extensión .db
            if not nombre_archivo.endswith('.db'):
                nombre_archivo += '.db'
            
            # Copiar el archivo DATABASETEMP.db a la ubicación elegida por el usuario
            try:
                shutil.copy2('./DATABASEAPPTEMP.db', nombre_archivo)
                print(f"Base de datos '{nombre_archivo}' guardada exitosamente.")
                msg_boxes.correct_msgbox("¡Descarga Exitosa!", "¡Se ha guardado la base de datos en la carpeta indicada!")
            except Exception as e:
                print(f"Error al guardar la base de datos: {e}")
                msg_boxes.error_msgbox("Error", "Se produjo un error al guardar la base de datos.")

    def cerrar_sesion(self):
        from controllers.login_window import LoginWindowForm
        self.login_window = LoginWindowForm(self)
        self.login_window.show()
        self.hide()

    def populate_table(self,data):
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

        self.records_qty()
    
    def populate_table_subestacion(self,data):
        self.tableSubestacion.setRowCount(len(data))
        print("REFRESH4")
        for index_row, row in enumerate(data):
            # Incrementamos el índice de fila en 1 para comenzar con el número de orden en 1
            order_number = index_row + 1
            
            # Establecemos el número de orden en la primera columna
            self.tableSubestacion.setItem(index_row, 0, QTableWidgetItem(str(order_number)))
            
            for index_cell, cell in enumerate(row):
                # Llenamos los datos de la fila a partir de la segunda columna
                self.tableSubestacion.setItem(index_row, index_cell + 1, QTableWidgetItem(str(cell)))
                
                if index_cell == 13:
                    itemx = self.tableSubestacion.item(index_row, index_cell + 1)  # Se ajusta el índice de la celda
                    print("EL ITEM ACTUAL ES: ", itemx)
                    if itemx.text() == "PENDIENTE":
                        itemx.setForeground(QBrush(QColor(255, 0, 0)))
                    else:
                        itemx.setForeground(QBrush(QColor(0, 0, 255)))

        print("REFRESH5")
        headerVertical = self.tableSubestacion.verticalHeader()
        headerVertical.resizeSections(QHeaderView.ResizeToContents)
        headerVertical.setStretchLastSection(True)

        self.records_qty()

    
    def populate_table_linea(self,data):
        self.tableLinea.setRowCount(len(data))
        print("REFRESH4")
        for index_row, row in enumerate(data):
            # Incrementamos el índice de fila en 1 para comenzar con el número de orden en 1
            order_number = index_row + 1
            
            # Establecemos el número de orden en la primera columna
            self.tableLinea.setItem(index_row, 0, QTableWidgetItem(str(order_number)))
            
            for index_cell, cell in enumerate(row):
                # Llenamos los datos de la fila a partir de la segunda columna
                self.tableLinea.setItem(index_row, index_cell + 1, QTableWidgetItem(str(cell)))
                
                if index_cell == 13:
                    itemx = self.tableLinea.item(index_row, index_cell + 1)  # Se ajusta el índice de la celda
                    print("EL ITEM ACTUAL ES: ", itemx)
                    if itemx.text() == "PENDIENTE":
                        itemx.setForeground(QBrush(QColor(255, 0, 0)))
                    else:
                        itemx.setForeground(QBrush(QColor(0, 0, 255)))

        print("REFRESH5")
        headerVertical = self.tableLinea.verticalHeader()
        headerVertical.resizeSections(QHeaderView.ResizeToContents)
        headerVertical.setStretchLastSection(True)

        self.records_qty()

    def table_config(self):
        
        column_headers = ("#","CÓDIGO", "NOMBRE", "TIPO", "CÓDIGO ÁREA\nDEMANDA", "TIPO DE \nSISTEMA", "ÁREA OPERATIVA", "REGIÓN\nGEOGRÁFICA","ZONA","ALTITUD","CAUDAL\nDISEÑO","COEFICIENTE\nPRODUCCIÓN","CONSUMO\nPROPIO","DIRECCIÓN","TELEFONO","ESTADO","FECHA ALTA","DATUM UTM","ZONA UTM")
        self.tableGeneracion.setColumnCount(len(column_headers))
        self.tableGeneracion.setHorizontalHeaderLabels(column_headers)
        
        stylesheet = "::section{Background-color:#114692;border:1px solid black;color: white;}"
        self.tableGeneracion.horizontalHeader().setStyleSheet(stylesheet)
        self.tableGeneracion.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableGeneracion.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableGeneracion.setStyleSheet("QTableWidget{ gridline-color:black;alternate-background-color: #E2DED0;}")
        self.tableGeneracion.setAlternatingRowColors(True)
        #self.tableGeneracion.color

    def table_config_subestacion(self):  
        column_headers = ("#","CÓDIGO", "NOMBRE", "CALIFICACIÓN", "TIPO DE SISTEMA", "CÓDIGO ÁREA", "ÁREA OPERATIVA", "REGIÓN GEOGRÁFICA", "ZONA", "ALTITUD", "TECNOLOGÍA SE", "FUNCION", "ATENDIDA", "DIRECCIÓN", "TELÉFONO", "MODULO SERV AUX", "MODULO OBRA CIVIL", "MODULO EDIF CONTROL", "MODULO TIERRA PROF", "MODULO IEE", "ESTADO", "FECHA ALTA", "DATUM UTM", "ZONA UTM")
        self.tableSubestacion.setColumnCount(len(column_headers))
        self.tableSubestacion.setHorizontalHeaderLabels(column_headers)
        
        stylesheet = "::section{Background-color:#114692;border:1px solid black;color: white;}"
        self.tableSubestacion.horizontalHeader().setStyleSheet(stylesheet)
        self.tableSubestacion.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableSubestacion.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableSubestacion.setStyleSheet("QTableWidget{ gridline-color:black;alternate-background-color: #E2DED0;}")
        self.tableSubestacion.setAlternatingRowColors(True)
        #self.tableSubestacion.color
    
    def table_config_linea(self):
        column_headers = ("#","CÓDIGO", "NOMBRE", "TIPO DE SISTEMA", "TENSIÓN NOMINAL", "NODO DE SALIDA", "NODO DE LLEGADA", "CELDA DE SALIDA", "CELDA DE LLEGADA")
        self.tableLinea.setColumnCount(len(column_headers))
        self.tableLinea.setHorizontalHeaderLabels(column_headers)
        
        stylesheet = "::section{Background-color:#114692;border:1px solid black;color: white;}"
        self.tableLinea.horizontalHeader().setStyleSheet(stylesheet)
        self.tableLinea.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableLinea.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableLinea.setStyleSheet("QTableWidget{ gridline-color:black;alternate-background-color: #E2DED0;}")
        self.tableLinea.setAlternatingRowColors(True)

    def table_config_admin(self):
        
        column_headers = ("#","EMPRESA","CÓDIGO", "NOMBRE", "TIPO", "CÓDIGO ÁREA\nDEMANDA", "TIPO DE \nSISTEMA", "ÁREA OPERATIVA", "REGIÓN\nGEOGRÁFICA","ZONA","ALTITUD","CAUDAL\nDISEÑO","COEFICIENTE\nPRODUCCIÓN","CONSUMO\nPROPIO","DIRECCIÓN","TELEFONO","ESTADO","FECHA ALTA","DATUM UTM","ZONA UTM")
        self.tableGeneracion.setColumnCount(len(column_headers))
        self.tableGeneracion.setHorizontalHeaderLabels(column_headers)
        
        stylesheet = "::section{Background-color:#114692;border:1px solid black;color: white;}"
        self.tableGeneracion.horizontalHeader().setStyleSheet(stylesheet)
        self.tableGeneracion.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableGeneracion.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableGeneracion.setStyleSheet("QTableWidget{ gridline-color:black;alternate-background-color: #E2DED0;}")
        self.tableGeneracion.setAlternatingRowColors(True)
        #self.tableGeneracion.color

    def table_config_subestacion_admin(self):  
        column_headers = ("#","EMPRESA", "CÓDIGO", "NOMBRE", "CALIFICACIÓN", "TIPO DE SISTEMA", "CÓDIGO ÁREA", "ÁREA OPERATIVA", "REGIÓN GEOGRÁFICA", "ZONA", "ALTITUD", "TECNOLOGÍA SE", "FUNCION", "ATENDIDA", "DIRECCIÓN", "TELÉFONO", "MODULO SERV AUX", "MODULO OBRA CIVIL", "MODULO EDIF CONTROL", "MODULO TIERRA PROF", "MODULO IEE", "ESTADO", "FECHA ALTA", "DATUM UTM", "ZONA UTM")
        self.tableSubestacion.setColumnCount(len(column_headers))
        self.tableSubestacion.setHorizontalHeaderLabels(column_headers)
        
        stylesheet = "::section{Background-color:#114692;border:1px solid black;color: white;}"
        self.tableSubestacion.horizontalHeader().setStyleSheet(stylesheet)
        self.tableSubestacion.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableSubestacion.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableSubestacion.setStyleSheet("QTableWidget{ gridline-color:black;alternate-background-color: #E2DED0;}")
        self.tableSubestacion.setAlternatingRowColors(True)
        #self.tableSubestacion.color
    
    def table_config_linea_admin(self):
        column_headers = ("#","EMPRESA", "CÓDIGO", "NOMBRE", "TIPO DE SISTEMA", "TENSIÓN NOMINAL", "NODO DE SALIDA", "NODO DE LLEGADA", "CELDA DE SALIDA", "CELDA DE LLEGADA")
        self.tableLinea.setColumnCount(len(column_headers))
        self.tableLinea.setHorizontalHeaderLabels(column_headers)
        
        stylesheet = "::section{Background-color:#114692;border:1px solid black;color: white;}"
        self.tableLinea.horizontalHeader().setStyleSheet(stylesheet)
        self.tableLinea.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableLinea.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableLinea.setStyleSheet("QTableWidget{ gridline-color:black;alternate-background-color: #E2DED0;}")
        self.tableLinea.setAlternatingRowColors(True)

        #self.tableGeneracion.color

    #def check_inputs(self):
    #    parameterDni = self.parameterLineEditDNI.text()
    #    parameterDni=parameterDni.strip()
    #    parameterFecha = self.parameterLineEditFecha.text()
    #    parameterFecha=parameterFecha.strip()
    #    parameterMotivo = self.parameterLineEditMotivo.text()
    #    parameterMotivo=parameterMotivo.strip()
    #    parameterPiso =self.searchByPiso.currentText()
    #    parameterVisitante = self.parameterLineEditVisitante.text()
    #    parameterVisitante=parameterVisitante.strip()
    #    parameterEstado = self.searchByEstado.currentText()
    #    
    #    errors_count = 0
#
    #    if parameterDni == "" and parameterVisitante=="" and parameterFecha=="" and parameterMotivo=="" and parameterPiso=="" and parameterEstado=="":
    #        self.label_nota_obligatoria.show()
    #        errors_count = 1
#
    #    if errors_count == 0:
    #        self.label_nota_obligatoria.hide()
    #        return True
#
    #def populate_comboboxEstado(self):
    #    cb_options = ("","PENDIENTE", "REGISTRADO")
    #    self.cbEstado.addItems(cb_options)
#

    #def search_book_by_title(self, title):
    #    data = select_book_by_title(title)
    #    print(data)
    #
    #    self.populate_table(data)


    def search(self):
        option_selected = self.searchByCombobox.currentText()#obtiene el valor seleccionado del ComboBox
        parameter = self.parameterLineEditDNI.text()
        parameter=parameter.strip()

        if option_selected == "":
            print("Debe seleccionar una opcion")
        else:
            if parameter == "":
                print("Debe escribir lo que desea consultar")
                if option_selected == "DNI":
                    print("SELCCIONO DNI")
                    self.search_book_by_title(parameter)
                elif option_selected == "Categoria":
                    self.search_book_by_category(parameter)
            else:
                if option_selected == "DNI":
                    print("SELCCIONO DNI")
                    self.search_book_by_title(parameter)
                elif option_selected == "Categoria":
                    self.search_book_by_category(parameter)
        


    def records_qty(self):
        print("CANTIDAD1")
        qty_rows = str(self.tableGeneracion.rowCount())
        print("CANTIDAD2")
        self.labelNumeroRegistros.setText(qty_rows)

        #self.labelNumeroRegistros.setText(len(set(index.row() for index in QTableWidget.selectedIndexes())))

    def records_qty_select(self):
            print("CANTIDAD1")
            #qty_rows = str(self.tableGeneracion.rowCount())
            print("CANTIDAD2")
            #self.labelNumeroRegistros.setText(qty_rows)
            numeroseleccionado= len((self.tableGeneracion.selectedItems()))/14
            numeroseleccionado2 = int(numeroseleccionado)
            self.labelNumeroRegistros.setText(str(numeroseleccionado2))

    def searchAll(self):
        #option_selected = self.searchByCombobox.currentText()#obtiene el valor seleccionado del ComboBox
        parameterDni = self.parameterLineEditDNI.text()
        parameterDni=parameterDni.strip()
        parameterPiso = self.searchByPiso.currentText()
        
        parameterVisitante = self.parameterLineEditVisitante.text()
        parameterVisitante=parameterVisitante.strip()
        parameterFecha = self.parameterLineEditFecha.text()
        parameterFecha=parameterFecha.strip()
        parameterMotivo = self.parameterLineEditMotivo.text()
        parameterMotivo=parameterMotivo.strip()
        parameterEstado = self.searchByEstado.currentText()
        
        self.label_advertencia_filtros.hide()
        self.label_advertencia_sin_resultados.hide()
        self.label_advertencia_dni.hide()
        self.ast_dni.hide()
        if parameterDni == "" and parameterPiso=="" and parameterVisitante == "" and parameterFecha=="" and parameterMotivo == "" and parameterEstado=="" :
            print("Debe escribir lo que desea consultar")
            self.label_advertencia_filtros.show()
 
        else:
            self.label_advertencia_filtros.hide()

            self.label_advertencia_dni.hide()
            self.ast_dni.hide()
            dataAll= select_book_by_all(parameterDni,parameterPiso,parameterVisitante,parameterFecha,parameterMotivo,parameterEstado)
            print(dataAll)
            self.populate_table(dataAll)
            if(len(dataAll)==0):
                self.label_advertencia_sin_resultados.show()
            '''
            if(parameterDni!="" and len(parameterDni)!=8):
                self.label_advertencia_dni.show()
            else:
            '''    

    def limpiarCamposRefresh(self):
        self.parameterLineEditDNI.clear()
        self.searchByPiso.setCurrentIndex(0)
        self.parameterLineEditVisitante.clear()
        self.parameterLineEditFecha.clear()
        self.parameterLineEditMotivo.clear()
        self.searchByEstado.setCurrentIndex(0)
        

    def populate_table_refresh(self,data):
        self.limpiarCamposRefresh()
        self.label_advertencia_filtros.hide()
        self.label_advertencia_dni.hide()
        self.label_advertencia_sin_resultados.hide()
        self.tableGeneracion.setRowCount(len(data))
        print("REFRESH4")
        for (index_row, row) in enumerate(data):
            for(index_cell, cell) in enumerate(row):
                self.tableGeneracion.setItem(index_row, index_cell, QTableWidgetItem(str(cell)))
                if(index_cell==13):
                    itemx=self.tableGeneracion.item(index_row,index_cell)
                    print("EL ITEM ACTUAL ES: ",itemx)
                    if(itemx.text()=="PENDIENTE"):
                        itemx.setForeground(QBrush(QColor(255,0,0)))
                    else:
                        itemx.setForeground(QBrush(QColor(0, 0, 255)))
        print("REFRESH5")
        headerVertical = self.tableGeneracion.verticalHeader()
        headerVertical.resizeSections(QHeaderView.ResizeToContents)
        headerVertical.setStretchLastSection(True)
        self.records_qty()

    def populate_table_refresh_subestacion(self,data):
        self.limpiarCamposRefresh()
        self.label_advertencia_filtros.hide()
        self.label_advertencia_dni.hide()
        self.label_advertencia_sin_resultados.hide()
        self.tableSubestacion.setRowCount(len(data))
        print("REFRESH4")
        for (index_row, row) in enumerate(data):
            for(index_cell, cell) in enumerate(row):
                self.tableSubestacion.setItem(index_row, index_cell, QTableWidgetItem(str(cell)))
                if(index_cell==13):
                    itemx=self.tableSubestacion.item(index_row,index_cell)
                    print("EL ITEM ACTUAL ES: ",itemx)
                    if(itemx.text()=="PENDIENTE"):
                        itemx.setForeground(QBrush(QColor(255,0,0)))
                    else:
                        itemx.setForeground(QBrush(QColor(0, 0, 255)))
        print("REFRESH5")
        headerVertical = self.tableSubestacion.verticalHeader()
        headerVertical.resizeSections(QHeaderView.ResizeToContents)
        headerVertical.setStretchLastSection(True)
        self.booksQtyLabel_2()

    def populate_table_refresh_linea(self,data):
        self.limpiarCamposRefresh()
        self.label_advertencia_filtros.hide()
        self.label_advertencia_dni.hide()
        self.label_advertencia_sin_resultados.hide()
        self.tableLinea.setRowCount(len(data))
        print("REFRESH4")
        for (index_row, row) in enumerate(data):
            for(index_cell, cell) in enumerate(row):
                self.tableLinea.setItem(index_row, index_cell, QTableWidgetItem(str(cell)))
                if(index_cell==13):
                    itemx=self.tableLinea.item(index_row,index_cell)
                    print("EL ITEM ACTUAL ES: ",itemx)
                    if(itemx.text()=="PENDIENTE"):
                        itemx.setForeground(QBrush(QColor(255,0,0)))
                    else:
                        itemx.setForeground(QBrush(QColor(0, 0, 255)))
        print("REFRESH5")
        headerVertical = self.tableLinea.verticalHeader()
        headerVertical.resizeSections(QHeaderView.ResizeToContents)
        headerVertical.setStretchLastSection(True)
        self.booksQtyLabel_4()

    def VerificarDni(self,dni):
        print("EL DNI EN LABEL ES:"+dni)
        
        if (ExisteDni(dni)):
            print("DNI SI EXISTE - Verificacion!")
            nombreEncontrado= EncontrarDni(dni)
            print("NOMBRE ENCONTRADO:"+str(nombreEncontrado))
            self.parameterLineEditVisitante.setText(nombreEncontrado)
        else:
            print("DNI NO EXISTE - Verificacion!")
            self.parameterLineEditVisitante.setText("")
    
    def to_upperVisitante(self, txt):
        self.parameterLineEditVisitante.setText(txt.upper())
    

    def to_upperMotivo(self, txt):
        self.parameterLineEditMotivo.setText(txt.upper())

    def FilaSeleccionada(self):
        print("ENTRO A DOUBLE CLICK!")
        from controllers.new_window_central import NewBookWindow
        UsuarioF= buscar_usuario_acceso();
        print(UsuarioF)
        selected_row = self.tableGeneracion.selectedItems()

        if selected_row:
            if(UsuarioF!="admin"):
                book_id = str(selected_row[1].text())
            else:
                book_id = str(selected_row[2].text())
            window= NewBookWindow(self,book_id)
        window.exec_()
        
        self.tableGeneracion.clearSelection()

    def FilaSeleccionadaSubestacion(self):
        print("ENTRO A DOUBLE CLICK!")
        from controllers.new_window_subestacion import NewBookWindow
        UsuarioF= buscar_usuario_acceso();
        selected_row = self.tableSubestacion.selectedItems()

        if selected_row:
            if(UsuarioF!="admin"):
                book_id = str(selected_row[1].text())
            else:
                book_id = str(selected_row[2].text())
            window= NewBookWindow(self,book_id)
        window.exec_()
        
        self.tableSubestacion.clearSelection()

    def FilaSeleccionadaLinea(self):
        print("ENTRO A DOUBLE CLICK!")
        
        from controllers.new_window_linea import NewBookWindow
        UsuarioF= buscar_usuario_acceso();
        selected_row = self.tableLinea.selectedItems()
        print("EL CODIGO ESSSS: "+str(selected_row[1].text()))
        if selected_row:
            if(UsuarioF!="admin"):
                book_id = str(selected_row[1].text())
            else:
                book_id = str(selected_row[2].text())
            window= NewBookWindow(self,book_id)
        window.exec_()
        
        self.tableLinea.clearSelection()



    def gestionar_usuarios(self):
        from controllers.gestion_usuarios import NewBookWindow
        window= NewBookWindow(self)
        window.exec_()

    def ver_auditoria(self):
        from controllers.ver_auditoria import NewBookWindow
        window= NewBookWindow(self)
        window.exec_()

    def ver_carga(self):
        from controllers.ver_carga import NewBookWindow
        window= NewBookWindow(self)
        window.exec_()