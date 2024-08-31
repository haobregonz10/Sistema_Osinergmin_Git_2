from PySide2.QtWidgets import QFileDialog, QDialog, QMessageBox, QAbstractItemView, QWidget, QTableWidgetItem, QHeaderView
from PySide2.QtCore import Qt
from views.new_carga import Ui_NewBook
from PySide2 import QtCore
from pys2_msgboxes import msg_boxes
from db.books import delete_usuario, SelectUsuarios, insert_usuario
from datetime import datetime
import sqlite3
from sqlite3 import Error
from PySide2.QtGui import *
import pandas as pd  # Necesitarás instalar pandas si no lo tienes instalado

class NewBookWindow(QDialog, Ui_NewBook):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)
        self.selected_file = None  # Variable para almacenar el archivo seleccionado
        # self.table_config()
        # self.populate_table(SelectUsuarios("1"))
        self.label.setStyleSheet("background-color: #114692;")
        self.searchButton.clicked.connect(self.ver_tabla_auditoria)
        self.SelectButton.clicked.connect(self.open_file_dialog)
        self.cancelButton.clicked.connect(self.close)
        self.addButton.clicked.connect(self.agregarBD)
        
        self.tableCarga.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableCarga.verticalHeader().setVisible(False)
        self.tableCarga.setColumnWidth(0, 19)
        headerVertical = self.tableCarga.verticalHeader()
        headerVertical.resizeSections(QHeaderView.ResizeToContents)
        headerVertical.setStretchLastSection(True)
        self.populate_combobox()

    def table_config(self):
        column_headers = ("#", "Usuario", "Contraseña")
        self.tableCarga.setColumnCount(len(column_headers))
        self.tableCarga.setHorizontalHeaderLabels(column_headers)
        self.tableCarga.setSelectionMode(QAbstractItemView.SingleSelection)
        stylesheet = "::section{Background-color:#114692;border:1px solid black;color: white;}"
        self.tableCarga.horizontalHeader().setStyleSheet(stylesheet)
        self.tableCarga.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableCarga.setStyleSheet("QTableWidget{ gridline-color:black;alternate-background-color: #E2DED0;}")
        self.tableCarga.setAlternatingRowColors(True)
        # Puedes agregar configuraciones adicionales aquí, como estilos de encabezado, colores de fondo, etc.

    def populate_table(self, data):
        if data is not None:
            self.tableCarga.setRowCount(len(data))
            print("REFRESH4")
            for index_row, row in enumerate(data):
                # Incrementamos el índice de fila en 1 para comenzar con el número de orden en 1
                order_number = index_row + 1
                
                # Establecemos el número de orden en la primera columna
                self.tableCarga.setItem(index_row, 0, QTableWidgetItem(str(order_number)))
                
                for index_cell, cell in enumerate(row):
                    # Llenamos los datos de la fila a partir de la segunda columna
                    self.tableCarga.setItem(index_row, index_cell + 1, QTableWidgetItem(str(cell)))
                    
                    if index_cell == 13:
                        itemx = self.tableCarga.item(index_row, index_cell + 1)  # Se ajusta el índice de la celda
                        print("EL ITEM ACTUAL ES: ", itemx)
                        if itemx.text() == "PENDIENTE":
                            itemx.setForeground(QBrush(QColor(255, 0, 0)))
                        else:
                            itemx.setForeground(QBrush(QColor(0, 0, 255)))

            print("REFRESH5")
            headerVertical = self.tableCarga.verticalHeader()
            headerVertical.resizeSections(QHeaderView.ResizeToContents)
            headerVertical.setStretchLastSection(True)

    def ver_tabla_auditoria(self):
        selected_table = self.cbTabla.currentText()
        tabla_auditoria_seleccionada = selected_table

        # Obtener los encabezados de columna de la tabla seleccionada
        column_headers = self.get_column_headers(tabla_auditoria_seleccionada)
        column_headers.insert(0, "N°")
        self.tableCarga.setColumnCount(len(column_headers))
        self.tableCarga.setHorizontalHeaderLabels(column_headers)
        self.tableCarga.setSelectionMode(QAbstractItemView.SingleSelection)
        stylesheet = "::section{Background-color:#114692;border:1px solid black;color: white;}"
        self.tableCarga.horizontalHeader().setStyleSheet(stylesheet)
        self.tableCarga.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableCarga.setStyleSheet("QTableWidget{ gridline-color:black;alternate-background-color: #E2DED0;}")
        self.tableCarga.setAlternatingRowColors(True)

        # Obtener y llenar los datos de la tabla seleccionada
        data = self.select_data_archivo()
        self.populate_table(data)
    
    def get_column_headers(self, nombreTabla):
        conn = None
        try:
            conn = sqlite3.connect('DATABASEAPP.db')  # Cambia 'DATABASEAPP.db' por la ruta a tu base de datos
            cur = conn.cursor()

            # Usar comillas dobles en el nombre de la tabla para evitar problemas con caracteres especiales
            sql = f"PRAGMA table_info(\"{nombreTabla}\")"
            cur.execute(sql)
            columns_info = cur.fetchall()

            # Extraer los nombres de las columnas
            column_headers = [column[1] for column in columns_info]
            return column_headers

        except Error as e:
            print("Error getting column headers: " + str(e))
            return []

        finally:
            if conn:
                conn.close()

    def open_file_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(self, "Seleccionar archivo", "", "Archivos Excel (*.xlsx *.xls)", options=options)
        if file_name:
            self.file_name = file_name  # Guardar el nombre del archivo seleccionado
            self.label_carga.setText(file_name)
            print(f"Archivo seleccionado: {file_name}")

    def populate_combobox(self):
        # Llenar el combo de Calificación
        cb_options_tabla = (
            "Area_Demanda",
            "Barra",
            "Barra_Ubicacion_Plano_Planta",
            "Barra_Ubicacion_Esquema",
            "Bobina_Bloqueo",
            "Bobina_Bloqueo_Ubicacion_Plano_Planta",
            "Bobina_Bloqueo_Ubicacion_Esquema",
            "Barra_Central_Generacion",
            "Barra_Central_Generacion_Ubicacion_Plano_Planta",
            "Barra_Central_Generacion_Ubicacion_Esquema",
            "Celda",
            "Celda_Ubicacion_Plano_Planta",
            "Celda_Ubicacion_Esquema",
            "Celda_Central_Generacion",
            "Celda_Central_Generacion_Ubicacion_Plano_Planta",
            "Celda_Central_Generacion_Ubicacion_Esquema",
            "Central_Generacion",
            "Central_Generacion_Vertice_Perimetro_Coordenadas_Geograficas",
            "Central_Generacion_Vertice_Perimetro_Plano_Planta",
            "Conductor",
            "Conductor_Ubicacion_Plano_Planta",
            "Conductor_Ubicacion_Esquema",
            "Conductor_Central_Generacion",
            "Conductor_Central_Generacion_Ubicacion_Plano_Planta",
            "Conductor_Central_Generacion_Ubicacion_Esquema",
            "Compensador_Reactivo",
            "Compensador_Reactivo_Ubicacion_Plano_Planta",
            "Compensador_Reactivo_Ubicacion_Esquema",
            "Estructura",
            "Estructura_Ubicacion_Geografica",
            "Estructura_Ubicacion_Plano_Planta_Central_Generacion",
            "Estructura_Ubicacion_Plano_Planta_Subestacion",
            "Generador_Central_Generacion",
            "Generador_Central_Generacion_Ubicacion_Esquema",
            "Generador_Central_Generacion_Ubicacion_Plano_Planta",
            "Interruptor_Central_Generacion",
            "Interruptor_Central_Generacion_Ubicacion_Esquema",
            "Interruptor_Central_Generacion_Ubicacion_Plano_Planta",
            "Interruptor_Potencia",
            "Interruptor_Potencia_Ubicacion_Esquema",
            "Interruptor_Potencia_Ubicacion_Plano_Planta",
            "Linea_Transmision",
            "Pararrayo",
            "Pararrayo_Ubicacion_Esquema",
            "Pararrayo_Ubicacion_Plano_Planta",
            "Pararrayo_Central_Generacion",
            "Pararrayo_Central_Generacion_Ubicacion_Esquema",
            "Pararrayo_Central_Generacion_Ubicacion_Plano_Planta",
            "Portico",
            "Portico_Estructura",
            "Portico_Travesanio",
            "Portico_Central_Generacion",
            "Portico_Central_Generacion_Estructura",
            "Portico_Central_Generacion_Travesano",
            "Seccionador",
            "Seccionador_Ubicacion_Esquema",
            "Seccionador_Ubicacion_Plano_Planta",
            "Seccionador_Central_Generacion",
            "Seccionador_Central_Generacion_Ubicacion_Esquema",
            "Seccionador_Central_Generacion_Ubicacion_Plano_Planta",
            "Subestacion",
            "Subestacion_Vertice_Perimetro_Coordenadas_Geograficas",
            "Subestacion_Vertice_Perimetro_Plano_Planta",
            "Transformador_Medicion",
            "Transformador_Medicion_Ubicacion_Esquema",
            "Transformador_Medicion_Ubicacion_Plano_Planta",
            "Transformador_Potencia",
            "Transformador_Potencia_Ubicacion_Esquema",
            "Transformador_Potencia_Ubicacion_Plano_Planta",
            "Transformador_Central_Generacion",
            "Transformador_Central_Generacion_Ubicacion_Esquema",
            "Transformador_Central_Generacion_Ubicacion_Plano_Planta",
            "Tramo_Linea_Transmision",
            "Tramo_Linea_Vertice_Ubicacion_Geografica",
            "UsuariosTabla"
        )

        self.cbTabla.addItems(cb_options_tabla)

    def select_data_archivo(self):
        if hasattr(self, 'file_name'):
            try:
                # Leer el archivo Excel usando pandas sin especificar el motor
                df = pd.read_excel(self.file_name)
                
                # Convertir el DataFrame en una lista de listas
                data = df.values.tolist()
                
                return data
            except Exception as e:
                print(f"Error al leer el archivo Excel: {str(e)}")
                return []
        else:
            print("No se ha seleccionado ningún archivo.")
            return []


    def agregarBD(self):
        selected_table = self.cbTabla.currentText()
        tabla_bd = selected_table

        column_headers = self.get_column_headers(tabla_bd)
        
        print("Encabezados de columna en la base de datos:", column_headers)
        
        # Verificar si existe una columna llamada 'Secuencia'
        secuencia_present = "Secuencia" in column_headers
        
        data = []
        row_count = self.tableCarga.rowCount()
        column_count = self.tableCarga.columnCount()
        
        for row in range(row_count):
            row_data = []
            for column in range(1, column_count):  # Comenzar desde 1 para excluir la primera columna
                item = self.tableCarga.item(row, column)
                row_data.append(item.text() if item else "")
            
            if len(row_data) == len(column_headers):
                data.append(row_data)
            else:
                print(f"Fila {row + 1} omitida: {row_data}")
                QMessageBox.warning(self, "Advertencia", f"El número de datos en la fila {row + 1} no coincide con el número de columnas en la base de datos. La fila ha sido omitida.")
        
        if not data:
            QMessageBox.warning(self, "Advertencia", "No hay datos válidos para insertar.")
            return

        conn = None
        try:
            conn = sqlite3.connect('DATABASEAPP.db')
            cur = conn.cursor()
            
            # Las tres primeras columnas se usan como claves únicas
            key_columns = column_headers[:3]
            
            for row_data in data:
                if secuencia_present:
                    # Si hay una columna 'Secuencia', solo hacer el INSERT
                    placeholders = ", ".join(["?"] * len(column_headers))
                    sql_insert = f"INSERT INTO {tabla_bd} ({', '.join(column_headers)}) VALUES ({placeholders})"
                    cur.execute(sql_insert, row_data)
                    print(f"Registro insertado: {row_data}")
                else:
                    # Extraer los valores de las claves únicas
                    key_values = row_data[:3]  # Asumiendo que las tres primeras columnas son clave
                    
                    # Crear la consulta SELECT para verificar existencia
                    where_clause = " AND ".join([f"{col} = ?" for col in key_columns])
                    cur.execute(f"SELECT COUNT(*) FROM {tabla_bd} WHERE {where_clause}", key_values)
                    exists = cur.fetchone()[0]
                    
                    if exists:
                        # Realizar un UPDATE
                        set_clause = ", ".join([f"{col} = ?" for col in column_headers[3:]])  # Excluir las tres columnas clave
                        sql_update = f"UPDATE {tabla_bd} SET {set_clause} WHERE {where_clause}"
                        update_values = row_data[3:] + key_values  # Excluir las claves en el SET y añadirlas al final para el WHERE
                        cur.execute(sql_update, update_values)
                        print(f"Registro actualizado: {row_data}")
                    else:
                        # Realizar un INSERT
                        placeholders = ", ".join(["?"] * len(column_headers))
                        sql_insert = f"INSERT INTO {tabla_bd} ({', '.join(column_headers)}) VALUES ({placeholders})"
                        cur.execute(sql_insert, row_data)
                        print(f"Registro insertado: {row_data}")

            conn.commit()

            # Actualización después de la inserción/actualización
            conn2 = sqlite3.connect('DATABASEAPP.db')
            cursor = conn2.cursor()
            
            sql_updates = {
                "Central_Generacion": """
                    UPDATE Central_Generacion SET TIPO_CENTRAL='Hidroeléctrica' WHERE TIPO_CENTRAL='H';
                    UPDATE Central_Generacion SET TIPO_CENTRAL='Térmica' WHERE TIPO_CENTRAL='T';
                    UPDATE Central_Generacion SET TIPO_CENTRAL='Eólica' WHERE TIPO_CENTRAL='E';
                    UPDATE Central_Generacion SET TIPO_CENTRAL='Solar' WHERE TIPO_CENTRAL='S';
                    UPDATE Central_Generacion SET TIPO_SISTEMA='Interconectado' WHERE TIPO_SISTEMA='I';
                    UPDATE Central_Generacion SET TIPO_SISTEMA='Aislado' WHERE TIPO_SISTEMA='A';
                    UPDATE Central_Generacion SET AREA_OPERATIVA='Norte' WHERE AREA_OPERATIVA='N';
                    UPDATE Central_Generacion SET AREA_OPERATIVA='Centro' WHERE AREA_OPERATIVA='C';
                    UPDATE Central_Generacion SET AREA_OPERATIVA='Sur' WHERE AREA_OPERATIVA='S';
                    UPDATE Central_Generacion SET AREA_OPERATIVA='Lima' WHERE AREA_OPERATIVA='L';
                    UPDATE Central_Generacion SET REGION_GEOGRAFICA='Costa' WHERE REGION_GEOGRAFICA='CO';
                    UPDATE Central_Generacion SET REGION_GEOGRAFICA='Sierra' WHERE REGION_GEOGRAFICA='SI';
                    UPDATE Central_Generacion SET REGION_GEOGRAFICA='Selva' WHERE REGION_GEOGRAFICA='SE';
                    UPDATE Central_Generacion SET ZONA='Urbana' WHERE ZONA='U';
                    UPDATE Central_Generacion SET ZONA='Rural' WHERE ZONA='R';
                    UPDATE Central_Generacion SET ESTADO='Nuevo' WHERE ESTADO='N';
                    UPDATE Central_Generacion SET ESTADO='Existente' WHERE ESTADO='E';
                    UPDATE Central_Generacion SET ESTADO='Eliminado' WHERE ESTADO='X';
                    UPDATE Central_Generacion SET ESTADO='Modificado' WHERE ESTADO='M';
                    UPDATE Central_Generacion SET ESTADO='Proyectado' WHERE ESTADO='P';
                """,
"Generador_Central_Generacion": """
                    UPDATE Generador_Central_Generacion SET TIPO_TURBINA='Pelton' WHERE TIPO_TURBINA='PE';
                    UPDATE Generador_Central_Generacion SET TIPO_TURBINA='Francis' WHERE TIPO_TURBINA='FR';
                    UPDATE Generador_Central_Generacion SET TIPO_TURBINA='Kaplan' WHERE TIPO_TURBINA='KA';
                    UPDATE Generador_Central_Generacion SET TIPO_TURBINA='Turbovapor' WHERE TIPO_TURBINA='TV';
                    UPDATE Generador_Central_Generacion SET TIPO_TURBINA='Turbogas' WHERE TIPO_TURBINA='TG';
                    UPDATE Generador_Central_Generacion SET ESTADO='Nuevo' WHERE ESTADO='N';
                    UPDATE Generador_Central_Generacion SET ESTADO='Existente' WHERE ESTADO='E';
                    UPDATE Generador_Central_Generacion SET ESTADO='Eliminado' WHERE ESTADO='X';
                    UPDATE Generador_Central_Generacion SET ESTADO='Modificado' WHERE ESTADO='M';
                    UPDATE Generador_Central_Generacion SET ESTADO='Proyectado' WHERE ESTADO='P';
                """,
"Barra_Central_Generacion": """
                    UPDATE Barra_Central_Generacion SET TIPO_ARREGLO='Simple Barra' WHERE TIPO_ARREGLO='SB';
                    UPDATE Barra_Central_Generacion SET TIPO_ARREGLO='Doble Barra' WHERE TIPO_ARREGLO='DB';
                    UPDATE Barra_Central_Generacion SET TIPO_ARREGLO='Anillo' WHERE TIPO_ARREGLO='AN';
                    UPDATE Barra_Central_Generacion SET TIPO_ARREGLO='Interruptor y Medio' WHERE TIPO_ARREGLO='IM';
                    UPDATE Barra_Central_Generacion SET TIPO_INSTALACION='Interior' WHERE TIPO_INSTALACION='I';
                    UPDATE Barra_Central_Generacion SET TIPO_INSTALACION='Exterior' WHERE TIPO_INSTALACION='E';
                    UPDATE Barra_Central_Generacion SET BARRA_REFERENCIA='Si' WHERE BARRA_REFERENCIA='S';
                    UPDATE Barra_Central_Generacion SET BARRA_REFERENCIA='No' WHERE BARRA_REFERENCIA='N';
                    UPDATE Barra_Central_Generacion SET ESTADO='Nuevo' WHERE ESTADO='N';
                    UPDATE Barra_Central_Generacion SET ESTADO='Existente' WHERE ESTADO='E';
                    UPDATE Barra_Central_Generacion SET ESTADO='Eliminado' WHERE ESTADO='X';
                    UPDATE Barra_Central_Generacion SET ESTADO='Modificado' WHERE ESTADO='M';
                    UPDATE Barra_Central_Generacion SET ESTADO='Proyectado' WHERE ESTADO='P';
                """,
"Celda_Central_Generacion": """
                    UPDATE Celda_Central_Generacion SET TIPO_CELDA='LÍNEA' WHERE TIPO_CELDA='LI';
                    UPDATE Celda_Central_Generacion SET TIPO_CELDA='TRANSFORMACIÓN' WHERE TIPO_CELDA='TR';
                    UPDATE Celda_Central_Generacion SET TIPO_CELDA='LÍNEA TRANSFORMADOR' WHERE TIPO_CELDA='LT';
                    UPDATE Celda_Central_Generacion SET TIPO_CELDA='ACOPLAMIENTO' WHERE TIPO_CELDA='AC';
                    UPDATE Celda_Central_Generacion SET TIPO_CELDA='ACOPLAMIENTO LONGITUDINAL' WHERE TIPO_CELDA='LA';
                    UPDATE Celda_Central_Generacion SET TIPO_CELDA='MEDICIÓN' WHERE TIPO_CELDA='MD';
                    UPDATE Celda_Central_Generacion SET TIPO_CELDA='ALIMENTADOR' WHERE TIPO_CELDA='AL';
                    UPDATE Celda_Central_Generacion SET TIPO_CELDA='REACTOR' WHERE TIPO_CELDA='RE';
                    UPDATE Celda_Central_Generacion SET TIPO_CELDA='COMPENSADOR SVC' WHERE TIPO_CELDA='CV';
                    UPDATE Celda_Central_Generacion SET TIPO_CELDA='COMPENSADOR SÍNCRONO' WHERE TIPO_CELDA='CS';
                    UPDATE Celda_Central_Generacion SET TIPO_CELDA='COMPENSADOR' WHERE TIPO_CELDA='CC';
                    UPDATE Celda_Central_Generacion SET TIPO_INSTALACION='Interior' WHERE TIPO_INSTALACION='I';
                    UPDATE Celda_Central_Generacion SET TIPO_INSTALACION='Exterior' WHERE TIPO_INSTALACION='E';
                    UPDATE Celda_Central_Generacion SET ESTADO='Nuevo' WHERE ESTADO='N';
                    UPDATE Celda_Central_Generacion SET ESTADO='Existente' WHERE ESTADO='E';
                    UPDATE Celda_Central_Generacion SET ESTADO='Eliminado' WHERE ESTADO='X';
                    UPDATE Celda_Central_Generacion SET ESTADO='Modificado' WHERE ESTADO='M';
                    UPDATE Celda_Central_Generacion SET ESTADO='Proyectado' WHERE ESTADO='P';
                """,
"Portico_Central_Generacion": """
                    UPDATE Portico_Central_Generacion SET TIPO='Acero' WHERE TIPO='AC';
                    UPDATE Portico_Central_Generacion SET TIPO='Concreto' WHERE TIPO='CO';
                    UPDATE Portico_Central_Generacion SET TIPO='Madera' WHERE TIPO='MA';
                    UPDATE Portico_Central_Generacion SET ESTADO='Nuevo' WHERE ESTADO='N';
                    UPDATE Portico_Central_Generacion SET ESTADO='Existente' WHERE ESTADO='E';
                    UPDATE Portico_Central_Generacion SET ESTADO='Eliminado' WHERE ESTADO='X';
                    UPDATE Portico_Central_Generacion SET ESTADO='Modificado' WHERE ESTADO='M';
                    UPDATE Portico_Central_Generacion SET ESTADO='Proyectado' WHERE ESTADO='P';
                """,
"Interruptor_Central_Generacion": """
                    UPDATE Interruptor_Central_Generacion SET TIPO_INSTALACION='Interior' WHERE TIPO_INSTALACION='I';
                    UPDATE Interruptor_Central_Generacion SET TIPO_INSTALACION='Exterior' WHERE TIPO_INSTALACION='E';
                    UPDATE Interruptor_Central_Generacion SET ESTADO='Nuevo' WHERE ESTADO='N';
                    UPDATE Interruptor_Central_Generacion SET ESTADO='Existente' WHERE ESTADO='E';
                    UPDATE Interruptor_Central_Generacion SET ESTADO='Eliminado' WHERE ESTADO='X';
                    UPDATE Interruptor_Central_Generacion SET ESTADO='Modificado' WHERE ESTADO='M';
                    UPDATE Interruptor_Central_Generacion SET ESTADO='Proyectado' WHERE ESTADO='P';
                """,
"Seccionador_Central_Generacion": """
                    UPDATE Seccionador_Central_Generacion SET TIPO_SECCIONADOR='Apertura Central' WHERE TIPO_SECCIONADOR='AC';
                    UPDATE Seccionador_Central_Generacion SET TIPO_SECCIONADOR='Apertura Lateral' WHERE TIPO_SECCIONADOR='AL';
                    UPDATE Seccionador_Central_Generacion SET TIPO_SECCIONADOR='Cierre' WHERE TIPO_SECCIONADOR='CI';
                    UPDATE Seccionador_Central_Generacion SET TIPO_INSTALACION='Interior' WHERE TIPO_INSTALACION='I';
                    UPDATE Seccionador_Central_Generacion SET TIPO_INSTALACION='Exterior' WHERE TIPO_INSTALACION='E';
                    UPDATE Seccionador_Central_Generacion SET ESTADO='Nuevo' WHERE ESTADO='N';
                    UPDATE Seccionador_Central_Generacion SET ESTADO='Existente' WHERE ESTADO='E';
                    UPDATE Seccionador_Central_Generacion SET ESTADO='Eliminado' WHERE ESTADO='X';
                    UPDATE Seccionador_Central_Generacion SET ESTADO='Modificado' WHERE ESTADO='M';
                    UPDATE Seccionador_Central_Generacion SET ESTADO='Proyectado' WHERE ESTADO='P';
                """,
                "Transformador_Central_Generacion": """
                    UPDATE Transformador_Central_Generacion SET TIPO_TRANSFORMADOR='Elevador' WHERE TIPO_TRANSFORMADOR='E';
                    UPDATE Transformador_Central_Generacion SET TIPO_TRANSFORMADOR='Reductor' WHERE TIPO_TRANSFORMADOR='R';
                    UPDATE Transformador_Central_Generacion SET TIPO_TRANSFORMADOR='Auto' WHERE TIPO_TRANSFORMADOR='A';
                    UPDATE Transformador_Central_Generacion SET ESTADO='Nuevo' WHERE ESTADO='N';
                    UPDATE Transformador_Central_Generacion SET ESTADO='Existente' WHERE ESTADO='E';
                    UPDATE Transformador_Central_Generacion SET ESTADO='Eliminado' WHERE ESTADO='X';
                    UPDATE Transformador_Central_Generacion SET ESTADO='Modificado' WHERE ESTADO='M';
                    UPDATE Transformador_Central_Generacion SET ESTADO='Proyectado' WHERE ESTADO='P';
                """,
                "Pararrayo_Central_Generacion": """
                    UPDATE Pararrayo_Central_Generacion SET ESTADO='Nuevo' WHERE ESTADO='N';
                    UPDATE Pararrayo_Central_Generacion SET ESTADO='Existente' WHERE ESTADO='E';
                    UPDATE Pararrayo_Central_Generacion SET ESTADO='Eliminado' WHERE ESTADO='X';
                    UPDATE Pararrayo_Central_Generacion SET ESTADO='Modificado' WHERE ESTADO='M';
                    UPDATE Pararrayo_Central_Generacion SET ESTADO='Proyectado' WHERE ESTADO='P';
                """,
                "Transformador_Medicion_Central_Generacion": """
                    UPDATE Transformador_Medicion_Central_Generacion SET TIPO_TRANSF='Corriente' WHERE TIPO_TRANSF='C';
                    UPDATE Transformador_Medicion_Central_Generacion SET TIPO_TRANSF='Tensión' WHERE TIPO_TRANSF='T';
                    UPDATE Transformador_Medicion_Central_Generacion SET TIPO_TRANSF='Medida Combinado' WHERE TIPO_TRANSF='M';
                    UPDATE Transformador_Medicion_Central_Generacion SET TIPO_INSTALACION='Interior' WHERE TIPO_INSTALACION='I';
                    UPDATE Transformador_Medicion_Central_Generacion SET TIPO_INSTALACION='Exterior' WHERE TIPO_INSTALACION='E';
                    UPDATE Transformador_Medicion_Central_Generacion SET ESTADO='Nuevo' WHERE ESTADO='N';
                    UPDATE Transformador_Medicion_Central_Generacion SET ESTADO='Existente' WHERE ESTADO='E';
                    UPDATE Transformador_Medicion_Central_Generacion SET ESTADO='Eliminado' WHERE ESTADO='X';
                    UPDATE Transformador_Medicion_Central_Generacion SET ESTADO='Modificado' WHERE ESTADO='M';
                    UPDATE Transformador_Medicion_Central_Generacion SET ESTADO='Proyectado' WHERE ESTADO='P';
                """,
                "Conductor_Central_Generacion": """
                    UPDATE Conductor_Central_Generacion SET ESTADO='Nuevo' WHERE ESTADO='N';
                    UPDATE Conductor_Central_Generacion SET ESTADO='Existente' WHERE ESTADO='E';
                    UPDATE Conductor_Central_Generacion SET ESTADO='Eliminado' WHERE ESTADO='X';
                    UPDATE Conductor_Central_Generacion SET ESTADO='Modificado' WHERE ESTADO='M';
                    UPDATE Conductor_Central_Generacion SET ESTADO='Proyectado' WHERE ESTADO='P';
                """,
                "Transformador_Central_Generacion": """
                    UPDATE Transformador_Central_Generacion SET TIPO_TRANSFORMADOR='POTENCIA DE TRANSMISIÓN' WHERE TIPO_TRANSFORMADOR='PD';
                    UPDATE Transformador_Central_Generacion SET TIPO_TRANSFORMADOR='POTENCIA DE DISTRIBUCIÓN' WHERE TIPO_TRANSFORMADOR='PO';
                    UPDATE Transformador_Central_Generacion SET TIPO_TRANSFORMADOR='DE SECCIONAMIENTO' WHERE TIPO_TRANSFORMADOR='SD';
                    UPDATE Transformador_Central_Generacion SET ESTADO='Nuevo' WHERE ESTADO='N';
                    UPDATE Transformador_Central_Generacion SET ESTADO='Existente' WHERE ESTADO='E';
                    UPDATE Transformador_Central_Generacion SET ESTADO='Eliminado' WHERE ESTADO='X';
                    UPDATE Transformador_Central_Generacion SET ESTADO='Modificado' WHERE ESTADO='M';
                    UPDATE Transformador_Central_Generacion SET ESTADO='Proyectado' WHERE ESTADO='P';
                """,
                "Subestacion": """
                    UPDATE Subestacion SET COD_CALIFICACION='Principal' WHERE COD_CALIFICACION='P';
                    UPDATE Subestacion SET COD_CALIFICACION='Secundario' WHERE COD_CALIFICACION='S';
                    UPDATE Subestacion SET COD_CALIFICACION='Garantizado' WHERE COD_CALIFICACION='G';
                    UPDATE Subestacion SET COD_CALIFICACION='Complementario' WHERE COD_CALIFICACION='C';
                    UPDATE Subestacion SET TIPO_SISTEMA='Interconectado' WHERE TIPO_SISTEMA='I';
                    UPDATE Subestacion SET TIPO_SISTEMA='Aislado' WHERE TIPO_SISTEMA='A';
                    UPDATE Subestacion SET TECNOLOGIA_SE='Convencional' WHERE TECNOLOGIA_SE='C1';
                    UPDATE Subestacion SET TECNOLOGIA_SE='Compacta' WHERE TECNOLOGIA_SE='C2';
                    UPDATE Subestacion SET TECNOLOGIA_SE='Encapsulada' WHERE TECNOLOGIA_SE='EN';
                    UPDATE Subestacion SET TECNOLOGIA_SE='Metal Clad' WHERE TECNOLOGIA_SE='MC';
                    UPDATE Subestacion SET FUNCION='Transformación' WHERE FUNCION='T';
                    UPDATE Subestacion SET FUNCION='Seccionamiento' WHERE FUNCION='S';
                    UPDATE Subestacion SET ATENDIDA='Si' WHERE ATENDIDA='S';
                    UPDATE Subestacion SET ATENDIDA='No' WHERE ATENDIDA='N';
                    UPDATE Subestacion SET ESTADO='Nuevo' WHERE ESTADO='N';
                    UPDATE Subestacion SET ESTADO='Existente' WHERE ESTADO='E';
                    UPDATE Subestacion SET ESTADO='Eliminado' WHERE ESTADO='X';
                    UPDATE Subestacion SET ESTADO='Modificado' WHERE ESTADO='M';
                    UPDATE Subestacion SET ESTADO='Proyectado' WHERE ESTADO='P';
                """,
                "Barra": """
                    UPDATE Barra SET TIPO_BARRA='Flexible' WHERE TIPO_BARRA='F';
                    UPDATE Barra SET TIPO_BARRA='Rígido' WHERE TIPO_BARRA='R';
                    UPDATE Barra SET COD_CALIFICACION='Principal' WHERE COD_CALIFICACION='P';
                    UPDATE Barra SET COD_CALIFICACION='Secundario' WHERE COD_CALIFICACION='S';
                    UPDATE Barra SET COD_CALIFICACION='Garantizado' WHERE COD_CALIFICACION='G';
                    UPDATE Barra SET COD_CALIFICACION='Complementario' WHERE COD_CALIFICACION='C';
                    UPDATE Barra SET BARRA_REFERENCIA='Si' WHERE BARRA_REFERENCIA='S';
                    UPDATE Barra SET BARRA_REFERENCIA='No' WHERE BARRA_REFERENCIA='N';
                    UPDATE Barra SET ESTADO='Nuevo' WHERE ESTADO='N';
                    UPDATE Barra SET ESTADO='Existente' WHERE ESTADO='E';
                    UPDATE Barra SET ESTADO='Eliminado' WHERE ESTADO='X';
                    UPDATE Barra SET ESTADO='Modificado' WHERE ESTADO='M';
                    UPDATE Barra SET ESTADO='Proyectado' WHERE ESTADO='P';
                """,
                "Portico": """
                    UPDATE Portico SET COD_CALIFICACION='Principal' WHERE COD_CALIFICACION='P';
                    UPDATE Portico SET COD_CALIFICACION='Secundario' WHERE COD_CALIFICACION='S';
                    UPDATE Portico SET COD_CALIFICACION='Garantizado' WHERE COD_CALIFICACION='G';
                    UPDATE Portico SET COD_CALIFICACION='Complementario' WHERE COD_CALIFICACION='C';
                    UPDATE Portico SET TIPO='Acero' WHERE TIPO='AC';
                    UPDATE Portico SET TIPO='Madera' WHERE TIPO='MA';
                    UPDATE Portico SET TIPO='Concreto' WHERE TIPO='CO';
                    UPDATE Portico SET ESTADO='Nuevo' WHERE ESTADO='N';
                    UPDATE Portico SET ESTADO='Existente' WHERE ESTADO='E';
                    UPDATE Portico SET ESTADO='Eliminado' WHERE ESTADO='X';
                    UPDATE Portico SET ESTADO='Modificado' WHERE ESTADO='M';
                    UPDATE Portico SET ESTADO='Proyectado' WHERE ESTADO='P';
                """,
                "Celda": """
                    UPDATE Celda SET COD_CALIFICACION='Principal' WHERE COD_CALIFICACION='P';
                    UPDATE Celda SET COD_CALIFICACION='Secundario' WHERE COD_CALIFICACION='S';
                    UPDATE Celda SET COD_CALIFICACION='Garantizado' WHERE COD_CALIFICACION='G';
                    UPDATE Celda SET COD_CALIFICACION='Complementario' WHERE COD_CALIFICACION='C';
                    UPDATE Celda SET TIPO_CELDA='LÍNEA' WHERE TIPO_CELDA='LI';
                    UPDATE Celda SET TIPO_CELDA='TRANSFORMACIÓN' WHERE TIPO_CELDA='TR';
                    UPDATE Celda SET TIPO_CELDA='LÍNEA TRANSFORMADOR' WHERE TIPO_CELDA='LT';
                    UPDATE Celda SET TIPO_CELDA='ACOPLAMIENTO' WHERE TIPO_CELDA='AC';
                    UPDATE Celda SET TIPO_CELDA='ACOPLAMIENTO LONGITUDINAL' WHERE TIPO_CELDA='LA';
                    UPDATE Celda SET TIPO_CELDA='MEDICIÓN' WHERE TIPO_CELDA='MD';
                    UPDATE Celda SET TIPO_CELDA='ALIMENTADOR' WHERE TIPO_CELDA='AL';
                    UPDATE Celda SET TIPO_CELDA='REACTOR' WHERE TIPO_CELDA='RE';
                    UPDATE Celda SET TIPO_CELDA='COMPENSADOR SVC' WHERE TIPO_CELDA='CV';
                    UPDATE Celda SET TIPO_CELDA='COMPENSADOR SÍNCRONO' WHERE TIPO_CELDA='CS';
                    UPDATE Celda SET TIPO_CELDA='COMPENSADOR' WHERE TIPO_CELDA='CC';
                    UPDATE Celda SET ESTADO='Nuevo' WHERE ESTADO='N';
                    UPDATE Celda SET ESTADO='Existente' WHERE ESTADO='E';
                    UPDATE Celda SET ESTADO='Eliminado' WHERE ESTADO='X';
                    UPDATE Celda SET ESTADO='Modificado' WHERE ESTADO='M';
                    UPDATE Celda SET ESTADO='Proyectado' WHERE ESTADO='P';
                """,
                "Transformador_Potencia": """
                    UPDATE Transformador_Potencia SET COD_CALIFICACION='Principal' WHERE COD_CALIFICACION='P';
                    UPDATE Transformador_Potencia SET COD_CALIFICACION='Secundario' WHERE COD_CALIFICACION='S';
                    UPDATE Transformador_Potencia SET COD_CALIFICACION='Garantizado' WHERE COD_CALIFICACION='G';
                    UPDATE Transformador_Potencia SET COD_CALIFICACION='Complementario' WHERE COD_CALIFICACION='C';
                    UPDATE Transformador_Potencia SET TIPO_TRANSF='Trifásico' WHERE TIPO_TRANSF='T';
                    UPDATE Transformador_Potencia SET TIPO_TRANSF='Monofásico' WHERE TIPO_TRANSF='M';
                    UPDATE Transformador_Potencia SET TIPO_TRANSF='Banco' WHERE TIPO_TRANSF='B';
                    UPDATE Transformador_Potencia SET TIPO_TRANSF='Autotransformador' WHERE TIPO_TRANSF='A';
                    UPDATE Transformador_Potencia SET TIPO_INSTALACION='Interior' WHERE TIPO_INSTALACION='I';
                    UPDATE Transformador_Potencia SET TIPO_INSTALACION='Exterior' WHERE TIPO_INSTALACION='E';
                    UPDATE Transformador_Potencia SET ESTADO='Nuevo' WHERE ESTADO='N';
                    UPDATE Transformador_Potencia SET ESTADO='Existente' WHERE ESTADO='E';
                    UPDATE Transformador_Potencia SET ESTADO='Eliminado' WHERE ESTADO='X';
                    UPDATE Transformador_Potencia SET ESTADO='Modificado' WHERE ESTADO='M';
                    UPDATE Transformador_Potencia SET ESTADO='Proyectado' WHERE ESTADO='P';
                """,
                "Interruptor_Potencia": """
                    UPDATE Interruptor_Potencia SET COD_CALIFICACION='Principal' WHERE COD_CALIFICACION='P';
                    UPDATE Interruptor_Potencia SET COD_CALIFICACION='Secundario' WHERE COD_CALIFICACION='S';
                    UPDATE Interruptor_Potencia SET COD_CALIFICACION='Garantizado' WHERE COD_CALIFICACION='G';
                    UPDATE Interruptor_Potencia SET COD_CALIFICACION='Complementario' WHERE COD_CALIFICACION='C';
                    UPDATE Interruptor_Potencia SET TIPO_INSTALACION='Interior' WHERE TIPO_INSTALACION='I';
                    UPDATE Interruptor_Potencia SET TIPO_INSTALACION='Exterior' WHERE TIPO_INSTALACION='E';
                    UPDATE Interruptor_Potencia SET ESTADO='Nuevo' WHERE ESTADO='N';
                    UPDATE Interruptor_Potencia SET ESTADO='Existente' WHERE ESTADO='E';
                    UPDATE Interruptor_Potencia SET ESTADO='Eliminado' WHERE ESTADO='X';
                    UPDATE Interruptor_Potencia SET ESTADO='Modificado' WHERE ESTADO='M';
                    UPDATE Interruptor_Potencia SET ESTADO='Proyectado' WHERE ESTADO='P';
                """,
                "Seccionador": """
                    UPDATE Seccionador SET COD_CALIFICACION='Principal' WHERE COD_CALIFICACION='P';
                    UPDATE Seccionador SET COD_CALIFICACION='Secundario' WHERE COD_CALIFICACION='S';
                    UPDATE Seccionador SET COD_CALIFICACION='Garantizado' WHERE COD_CALIFICACION='G';
                    UPDATE Seccionador SET COD_CALIFICACION='Complementario' WHERE COD_CALIFICACION='C';
                    UPDATE Seccionador SET TIPO_SECCIONADOR='Apertura Central' WHERE TIPO_SECCIONADOR='AC';
                    UPDATE Seccionador SET TIPO_SECCIONADOR='Rotación Central' WHERE TIPO_SECCIONADOR='RC';
                    UPDATE Seccionador SET TIPO_SECCIONADOR='Apertura Vertical' WHERE TIPO_SECCIONADOR='AV';
                    UPDATE Seccionador SET TIPO_SECCIONADOR='Pantógrafo' WHERE TIPO_SECCIONADOR='PA';
                    UPDATE Seccionador SET TIPO_SECCIONADOR='Semipantógrafo' WHERE TIPO_SECCIONADOR='SP';
                    UPDATE Seccionador SET TIPO_SECCIONADOR='Pantógrafo Horizontal' WHERE TIPO_SECCIONADOR='PH';
                    UPDATE Seccionador SET TIPO_INSTALACION='Interior' WHERE TIPO_INSTALACION='I';
                    UPDATE Seccionador SET TIPO_INSTALACION='Exterior' WHERE TIPO_INSTALACION='E';
                    UPDATE Seccionador SET ESTADO='Nuevo' WHERE ESTADO='N';
                    UPDATE Seccionador SET ESTADO='Existente' WHERE ESTADO='E';
                    UPDATE Seccionador SET ESTADO='Eliminado' WHERE ESTADO='X';
                    UPDATE Seccionador SET ESTADO='Modificado' WHERE ESTADO='M';
                    UPDATE Seccionador SET ESTADO='Proyectado' WHERE ESTADO='P';
                """,
                "Pararrayo": """
                    UPDATE Pararrayo SET COD_CALIFICACION='Principal' WHERE COD_CALIFICACION='P';
                    UPDATE Pararrayo SET COD_CALIFICACION='Secundario' WHERE COD_CALIFICACION='S';
                    UPDATE Pararrayo SET COD_CALIFICACION='Garantizado' WHERE COD_CALIFICACION='G';
                    UPDATE Pararrayo SET COD_CALIFICACION='Complementario' WHERE COD_CALIFICACION='C';
                    UPDATE Pararrayo SET ESTADO='Nuevo' WHERE ESTADO='N';
                    UPDATE Pararrayo SET ESTADO='Existente' WHERE ESTADO='E';
                    UPDATE Pararrayo SET ESTADO='Eliminado' WHERE ESTADO='X';
                    UPDATE Pararrayo SET ESTADO='Modificado' WHERE ESTADO='M';
                    UPDATE Pararrayo SET ESTADO='Proyectado' WHERE ESTADO='P';
                """,
                "Transformador_Medicion": """
                    UPDATE Transformador_Medicion SET COD_CALIFICACION='Principal' WHERE COD_CALIFICACION='P';
                    UPDATE Transformador_Medicion SET COD_CALIFICACION='Secundario' WHERE COD_CALIFICACION='S';
                    UPDATE Transformador_Medicion SET COD_CALIFICACION='Garantizado' WHERE COD_CALIFICACION='G';
                    UPDATE Transformador_Medicion SET COD_CALIFICACION='Complementario' WHERE COD_CALIFICACION='C';
                    UPDATE Transformador_Medicion SET TIPO_TRANSF='Corriente' WHERE TIPO_TRANSF='C';
                    UPDATE Transformador_Medicion SET TIPO_TRANSF='Tensión' WHERE TIPO_TRANSF='T';
                    UPDATE Transformador_Medicion SET TIPO_TRANSF='Medida Combinado' WHERE TIPO_TRANSF='M';
                    UPDATE Transformador_Medicion SET TIPO_INSTALACION='Interior' WHERE TIPO_INSTALACION='I';
                    UPDATE Transformador_Medicion SET TIPO_INSTALACION='Exterior' WHERE TIPO_INSTALACION='E';
                    UPDATE Transformador_Medicion SET ESTADO='Nuevo' WHERE ESTADO='N';
                    UPDATE Transformador_Medicion SET ESTADO='Existente' WHERE ESTADO='E';
                    UPDATE Transformador_Medicion SET ESTADO='Eliminado' WHERE ESTADO='X';
                    UPDATE Transformador_Medicion SET ESTADO='Modificado' WHERE ESTADO='M';
                    UPDATE Transformador_Medicion SET ESTADO='Proyectado' WHERE ESTADO='P';
                """,
                "Bobina_Bloqueo": """
                    UPDATE Bobina_Bloqueo SET COD_CALIFICACION='Principal' WHERE COD_CALIFICACION='P';
                    UPDATE Bobina_Bloqueo SET COD_CALIFICACION='Secundario' WHERE COD_CALIFICACION='S';
                    UPDATE Bobina_Bloqueo SET COD_CALIFICACION='Garantizado' WHERE COD_CALIFICACION='G';
                    UPDATE Bobina_Bloqueo SET COD_CALIFICACION='Complementario' WHERE COD_CALIFICACION='C';
                    UPDATE Bobina_Bloqueo SET ESTADO='Nuevo' WHERE ESTADO='N';
                    UPDATE Bobina_Bloqueo SET ESTADO='Existente' WHERE ESTADO='E';
                    UPDATE Bobina_Bloqueo SET ESTADO='Eliminado' WHERE ESTADO='X';
                    UPDATE Bobina_Bloqueo SET ESTADO='Modificado' WHERE ESTADO='M';
                    UPDATE Bobina_Bloqueo SET ESTADO='Proyectado' WHERE ESTADO='P';
                """,
                "Conductor": """
                    UPDATE Conductor SET COD_CALIFICACION='Principal' WHERE COD_CALIFICACION='P';
                    UPDATE Conductor SET COD_CALIFICACION='Secundario' WHERE COD_CALIFICACION='S';
                    UPDATE Conductor SET COD_CALIFICACION='Garantizado' WHERE COD_CALIFICACION='G';
                    UPDATE Conductor SET COD_CALIFICACION='Complementario' WHERE COD_CALIFICACION='C';
                    UPDATE Conductor SET ESTADO='Nuevo' WHERE ESTADO='N';
                    UPDATE Conductor SET ESTADO='Existente' WHERE ESTADO='E';
                    UPDATE Conductor SET ESTADO='Eliminado' WHERE ESTADO='X';
                    UPDATE Conductor SET ESTADO='Modificado' WHERE ESTADO='M';
                    UPDATE Conductor SET ESTADO='Proyectado' WHERE ESTADO='P';
                """,
                "Compensador_Reactivo": """
                    UPDATE Compensador_Reactivo SET COD_CALIFICACION='Principal' WHERE COD_CALIFICACION='P';
                    UPDATE Compensador_Reactivo SET COD_CALIFICACION='Secundario' WHERE COD_CALIFICACION='S';
                    UPDATE Compensador_Reactivo SET COD_CALIFICACION='Garantizado' WHERE COD_CALIFICACION='G';
                    UPDATE Compensador_Reactivo SET COD_CALIFICACION='Complementario' WHERE COD_CALIFICACION='C';
                    UPDATE Compensador_Reactivo SET TIPO_COMP='Banco Capacitivo' WHERE TIPO_COMP='BP';
                    UPDATE Compensador_Reactivo SET TIPO_COMP='Compensador Serie' WHERE TIPO_COMP='BS';
                    UPDATE Compensador_Reactivo SET TIPO_COMP='SVC' WHERE TIPO_COMP='SV';
                    UPDATE Compensador_Reactivo SET TIPO_COMP='Reactor' WHERE TIPO_COMP='RE';
                    UPDATE Compensador_Reactivo SET TIPO_COMP='Compensador Sincrono' WHERE TIPO_COMP='CS';
                    UPDATE Compensador_Reactivo SET TIPO_INSTALACION='Interior' WHERE TIPO_INSTALACION='I';
                    UPDATE Compensador_Reactivo SET TIPO_INSTALACION='Exterior' WHERE TIPO_INSTALACION='E';
                    UPDATE Compensador_Reactivo SET ESTADO='Nuevo' WHERE ESTADO='N';
                    UPDATE Compensador_Reactivo SET ESTADO='Existente' WHERE ESTADO='E';
                    UPDATE Compensador_Reactivo SET ESTADO='Eliminado' WHERE ESTADO='X';
                    UPDATE Compensador_Reactivo SET ESTADO='Modificado' WHERE ESTADO='M';
                    UPDATE Compensador_Reactivo SET ESTADO='Proyectado' WHERE ESTADO='P';
                """,
                "Transformador_Potencia": """
                    UPDATE Transformador_Potencia SET COD_CALIFICACION='Principal' WHERE COD_CALIFICACION='P';
                    UPDATE Transformador_Potencia SET COD_CALIFICACION='Secundario' WHERE COD_CALIFICACION='S';
                    UPDATE Transformador_Potencia SET COD_CALIFICACION='Garantizado' WHERE COD_CALIFICACION='G';
                    UPDATE Transformador_Potencia SET COD_CALIFICACION='Complementario' WHERE COD_CALIFICACION='C';
                    UPDATE Transformador_Potencia SET TIPO_TRANSF='Trifásico' WHERE TIPO_TRANSF='T';
                    UPDATE Transformador_Potencia SET TIPO_TRANSF='Monofásico' WHERE TIPO_TRANSF='M';
                    UPDATE Transformador_Potencia SET TIPO_TRANSF='Banco' WHERE TIPO_TRANSF='B';
                    UPDATE Transformador_Potencia SET TIPO_TRANSF='Autotransformador' WHERE TIPO_TRANSF='A';
                    UPDATE Transformador_Potencia SET TIPO_INSTALACION='Interior' WHERE TIPO_INSTALACION='I';
                    UPDATE Transformador_Potencia SET TIPO_INSTALACION='Exterior' WHERE TIPO_INSTALACION='E';
                    UPDATE Transformador_Potencia SET ESTADO='Nuevo' WHERE ESTADO='N';
                    UPDATE Transformador_Potencia SET ESTADO='Existente' WHERE ESTADO='E';
                    UPDATE Transformador_Potencia SET ESTADO='Eliminado' WHERE ESTADO='X';
                    UPDATE Transformador_Potencia SET ESTADO='Modificado' WHERE ESTADO='M';
                    UPDATE Transformador_Potencia SET ESTADO='Proyectado' WHERE ESTADO='P';
                """,
                "Linea_Transmision": """
                    UPDATE Linea_Transmision SET TIPO_SISTEMA='Interconectado' WHERE TIPO_SISTEMA='I';
                    UPDATE Linea_Transmision SET TIPO_SISTEMA='Aislado' WHERE TIPO_SISTEMA='A';
                """,
                "Tramo_Linea_Transmision": """
                    UPDATE Tramo_Linea_Transmision SET TIPO_CIRCUITO='Derivación' WHERE TIPO_CIRCUITO='D';
                    UPDATE Tramo_Linea_Transmision SET TIPO_CIRCUITO='Troncal' WHERE TIPO_CIRCUITO='T';
                    UPDATE Tramo_Linea_Transmision SET AREA_OPERATIVA='Norte' WHERE AREA_OPERATIVA='N';
                    UPDATE Tramo_Linea_Transmision SET AREA_OPERATIVA='Centro' WHERE AREA_OPERATIVA='C';
                    UPDATE Tramo_Linea_Transmision SET AREA_OPERATIVA='Sur' WHERE AREA_OPERATIVA='S';
                    UPDATE Tramo_Linea_Transmision SET AREA_OPERATIVA='Lima' WHERE AREA_OPERATIVA='L';
                    UPDATE Tramo_Linea_Transmision SET REGION_GEOGRAFICA='Costa' WHERE REGION_GEOGRAFICA='CO';
                    UPDATE Tramo_Linea_Transmision SET REGION_GEOGRAFICA='Sierra' WHERE REGION_GEOGRAFICA='SI';
                    UPDATE Tramo_Linea_Transmision SET REGION_GEOGRAFICA='Selva' WHERE REGION_GEOGRAFICA='SE';
                    UPDATE Tramo_Linea_Transmision SET ZONA='Urbana' WHERE ZONA='U';
                    UPDATE Tramo_Linea_Transmision SET ZONA='Rural' WHERE ZONA='R';
                    UPDATE Tramo_Linea_Transmision SET TIPO_RED='Aéreo' WHERE TIPO_RED='A';
                    UPDATE Tramo_Linea_Transmision SET TIPO_RED='Subterráneo' WHERE TIPO_RED='S';
                    UPDATE Tramo_Linea_Transmision SET DISPOSICION_FASES='Vertical' WHERE DISPOSICION_FASES='V';
                    UPDATE Tramo_Linea_Transmision SET DISPOSICION_FASES='Horizontal' WHERE DISPOSICION_FASES='H';
                    UPDATE Tramo_Linea_Transmision SET DISPOSICION_FASES='Triangular' WHERE DISPOSICION_FASES='T';
                    UPDATE Tramo_Linea_Transmision SET NUM_CABLE_GUARDA='Ninguno' WHERE NUM_CABLE_GUARDA='0';
                    UPDATE Tramo_Linea_Transmision SET NUM_CABLE_GUARDA='Uno' WHERE NUM_CABLE_GUARDA='1';
                    UPDATE Tramo_Linea_Transmision SET NUM_CABLE_GUARDA='Dos' WHERE NUM_CABLE_GUARDA='2';
                    UPDATE Tramo_Linea_Transmision SET TIPO_CONDUCTOR='AAAC' WHERE TIPO_CONDUCTOR='AAAC';
                    UPDATE Tramo_Linea_Transmision SET TIPO_CONDUCTOR='ACSR' WHERE TIPO_CONDUCTOR='ACSR';
                    UPDATE Tramo_Linea_Transmision SET TIPO_CONDUCTOR='ACAR' WHERE TIPO_CONDUCTOR='ACAR';
                    UPDATE Tramo_Linea_Transmision SET TIPO_CONDUCTOR='AAACE' WHERE TIPO_CONDUCTOR='AAACE';
                    UPDATE Tramo_Linea_Transmision SET TIPO_CONDUCTOR='AASC' WHERE TIPO_CONDUCTOR='AASC';
                    UPDATE Tramo_Linea_Transmision SET TIPO_CONDUCTOR='ALDREY' WHERE TIPO_CONDUCTOR='ALDREY';
                    UPDATE Tramo_Linea_Transmision SET TIPO_CONDUCTOR='ALMELEC' WHERE TIPO_CONDUCTOR='ALMELEC';
                    UPDATE Tramo_Linea_Transmision SET TIPO_CONDUCTOR='Cable de Cobre' WHERE TIPO_CONDUCTOR='CU';
                    UPDATE Tramo_Linea_Transmision SET TIPO_CONDUCTOR='Cable de Aluminio' WHERE TIPO_CONDUCTOR='AL';
                    UPDATE Tramo_Linea_Transmision SET MAT_CABLE_GUARDA='Acero Galvanizado' WHERE MAT_CABLE_GUARDA='AG';
                    UPDATE Tramo_Linea_Transmision SET MAT_CABLE_GUARDA='Alumoweld (Acero aleado con aluminio)' WHERE MAT_CABLE_GUARDA='AW';
                    UPDATE Tramo_Linea_Transmision SET MAT_CABLE_GUARDA='Aleación de Aluminio' WHERE MAT_CABLE_GUARDA='AA';
                    UPDATE Tramo_Linea_Transmision SET MAT_CABLE_GUARDA='Aluminio con Acero reforzado' WHERE MAT_CABLE_GUARDA='AR';
                    UPDATE Tramo_Linea_Transmision SET ESTADO='Nuevo' WHERE ESTADO='N';
                    UPDATE Tramo_Linea_Transmision SET ESTADO='Existente' WHERE ESTADO='E';
                    UPDATE Tramo_Linea_Transmision SET ESTADO='Eliminado' WHERE ESTADO='X';
                    UPDATE Tramo_Linea_Transmision SET ESTADO='Modificado' WHERE ESTADO='M';
                    UPDATE Tramo_Linea_Transmision SET ESTADO='Proyectado' WHERE ESTADO='P';
                    UPDATE Tramo_Linea_Transmision SET COD_CALIFICACION='Principal' WHERE COD_CALIFICACION='P';
                    UPDATE Tramo_Linea_Transmision SET COD_CALIFICACION='Secundario' WHERE COD_CALIFICACION='S';
                    UPDATE Tramo_Linea_Transmision SET COD_CALIFICACION='Garantizado' WHERE COD_CALIFICACION='G';
                    UPDATE Tramo_Linea_Transmision SET COD_CALIFICACION='Complementario' WHERE COD_CALIFICACION='C';
                """,
                "Estructura": """
                    UPDATE Estructura SET TIPO='Postes de Concreto y Acero' WHERE TIPO='AC';
                    UPDATE Estructura SET TIPO='Postes de Concreto' WHERE TIPO='PC';
                    UPDATE Estructura SET TIPO='Postes de Madera' WHERE TIPO='PM';
                    UPDATE Estructura SET TIPO='Torres de Acero' WHERE TIPO='TA';
                    UPDATE Estructura SET TIPO='Postes de Acero' WHERE TIPO='PA';
                    UPDATE Estructura SET TIPO='Postes de Madera y Acero' WHERE TIPO='AM';
                    UPDATE Estructura SET TIPO='Instalación Subterránea' WHERE TIPO='SS';
                    UPDATE Estructura SET TIPO='Sin Estructura o Red Compartida' WHERE TIPO='SE';
                    UPDATE Estructura SET FUNCION='Suspensión' WHERE FUNCION='S';
                    UPDATE Estructura SET FUNCION='Ángulo' WHERE FUNCION='A';
                    UPDATE Estructura SET FUNCION='Retención Intermedia' WHERE FUNCION='R';
                    UPDATE Estructura SET FUNCION='Terminal' WHERE FUNCION='T';
                    UPDATE Estructura SET FUNCION='Transposición' WHERE FUNCION='TR';
                    UPDATE Estructura SET FUNCION='Derivación' WHERE FUNCION='D';
                    UPDATE Estructura SET NUM_CIRCUITOS='Un Circuito' WHERE NUM_CIRCUITOS='1';
                    UPDATE Estructura SET NUM_CIRCUITOS='Dos Circuitos' WHERE NUM_CIRCUITOS='2';
                    UPDATE Estructura SET NUM_CIRCUITOS='Tres Circuitos' WHERE NUM_CIRCUITOS='3';
                    UPDATE Estructura SET NUM_CABLE_GUARDA='Ninguno' WHERE NUM_CABLE_GUARDA='0';
                    UPDATE Estructura SET NUM_CABLE_GUARDA='Uno' WHERE NUM_CABLE_GUARDA='1';
                    UPDATE Estructura SET NUM_CABLE_GUARDA='Dos' WHERE NUM_CABLE_GUARDA='2';
                    UPDATE Estructura SET FORMACION_FASE='Simple' WHERE FORMACION_FASE='1';
                    UPDATE Estructura SET FORMACION_FASE='Duplex' WHERE FORMACION_FASE='2';
                    UPDATE Estructura SET FORMACION_FASE='Triplex' WHERE FORMACION_FASE='3';
                    UPDATE Estructura SET FORMACION_FASE='Cuádruplex' WHERE FORMACION_FASE='4';
                """
                }

            sql = sql_updates.get(selected_table)
            
            if sql:
                try:
                    cursor.executescript(sql)
                    conn2.commit()
                    print(f"Actualización de la tabla '{selected_table}' realizada con éxito.")
                except sqlite3.Error as e:
                    print(f"Error al actualizar la tabla '{selected_table}': {e}")
                    conn2.rollback()
            else:
                print(f"No se encontraron actualizaciones definidas para la tabla '{selected_table}'.")

            QMessageBox.information(self, "Éxito", "Datos añadidos/actualizados en la base de datos con éxito.")
            self.parent.refresh_table_from_child_window()
            self.parent.refresh_table_from_child_window_subestacion()
            self.parent.refresh_table_from_child_window_linea()

        except sqlite3.Error as e:
            QMessageBox.critical(self, "Error", f"Error al insertar/actualizar datos en la base de datos: {str(e)}")
            
        finally:
            if conn:
                conn.close()
