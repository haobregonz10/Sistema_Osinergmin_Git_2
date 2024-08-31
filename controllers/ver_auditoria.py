from PySide2.QtWidgets import QDialog,QMessageBox,QAbstractItemView,QWidget,QTableWidgetItem,QHeaderView
from PySide2.QtCore import Qt
from views.new_auditoria import Ui_NewBook
from PySide2 import QtCore
from pys2_msgboxes import msg_boxes
from db.books import delete_usuario,SelectUsuarios,insert_usuario
from datetime import datetime
import sqlite3
from sqlite3 import Error
from PySide2.QtGui import *

class NewBookWindow(QDialog,Ui_NewBook):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)
        #self.table_config()
        #self.populate_table(SelectUsuarios("1"))
        self.label.setStyleSheet("background-color: #114692;")
        self.searchButton.clicked.connect(self.ver_tabla_auditoria)
        self.cancelButton.clicked.connect(self.close)
        
        self.tableAuditoria.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableAuditoria.verticalHeader().setVisible(False)
        self.tableAuditoria.setColumnWidth(0,19)
        headerVertical = self.tableAuditoria.verticalHeader()
        headerVertical.resizeSections(QHeaderView.ResizeToContents)
        headerVertical.setStretchLastSection(True)
        self.populate_combobox()

    def table_config(self):
        column_headers = ("#", "Usuario","Contraseña")
        self.tableAuditoria.setColumnCount(len(column_headers))
        self.tableAuditoria.setHorizontalHeaderLabels(column_headers)
        self.tableAuditoria.setSelectionMode(QAbstractItemView.SingleSelection)
        stylesheet = "::section{Background-color:#114692;border:1px solid black;color: white;}"
        self.tableAuditoria.horizontalHeader().setStyleSheet(stylesheet)
        self.tableAuditoria.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableAuditoria.setStyleSheet("QTableWidget{ gridline-color:black;alternate-background-color: #E2DED0;}")
        self.tableAuditoria.setAlternatingRowColors(True)
        # Puedes agregar configuraciones adicionales aquí, como estilos de encabezado, colores de fondo, etc.

    def populate_table(self, data):
        if data is not None:
            self.tableAuditoria.setRowCount(len(data))
            print("REFRESH4")
            
            for index_row, row in enumerate(data):
                for index_cell, cell in enumerate(row):
                    # Llenamos los datos de la fila desde la primera columna (sin agregar número de orden)
                    self.tableAuditoria.setItem(index_row, index_cell, QTableWidgetItem(str(cell)))
                    
                    if index_cell == 13:  # Aquí asegúrate de que el índice sea correcto
                        itemx = self.tableAuditoria.item(index_row, index_cell)  # Ya no se ajusta el índice de la celda
                        print("EL ITEM ACTUAL ES: ", itemx)
                        if itemx.text() == "PENDIENTE":
                            itemx.setForeground(QBrush(QColor(255, 0, 0)))  # Rojo para "PENDIENTE"
                        else:
                            itemx.setForeground(QBrush(QColor(0, 0, 255)))  # Azul para otros valores

            print("REFRESH5")
            headerVertical = self.tableAuditoria.verticalHeader()
            headerVertical.resizeSections(QHeaderView.ResizeToContents)
            headerVertical.setStretchLastSection(True)

    def ver_tabla_auditoria(self):
        selected_table = self.cbTabla.currentText()
        selected_tipo = self.cbTipo.currentText()
        fechaInicio=self.inputFechaInicio.text()
        fechaFin=self.inputFechaFin.text()
        tabla_auditoria_seleccionada= selected_table+"_Auditoria"

        # Obtener los encabezados de columna de la tabla seleccionada
        column_headers = self.get_column_headers(tabla_auditoria_seleccionada)
        self.tableAuditoria.setColumnCount(len(column_headers))
        self.tableAuditoria.setHorizontalHeaderLabels(column_headers)
        self.tableAuditoria.setSelectionMode(QAbstractItemView.SingleSelection)
        stylesheet = "::section{Background-color:#114692;border:1px solid black;color: white;}"
        self.tableAuditoria.horizontalHeader().setStyleSheet(stylesheet)
        self.tableAuditoria.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableAuditoria.setStyleSheet("QTableWidget{ gridline-color:black;alternate-background-color: #E2DED0;}")
        self.tableAuditoria.setAlternatingRowColors(True)

        # Obtener y llenar los datos de la tabla seleccionada
        
        data = self.select_tabla_auditoria(tabla_auditoria_seleccionada,fechaInicio,fechaFin,selected_tipo)
        self.populate_table(data)
    
    def get_column_headers(self,nombreTabla):
        conn = None
        try:
            conn = sqlite3.connect('DATABASEAPP.db')  # Cambia 'your_database.db' por la ruta a tu base de datos
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

    def populate_combobox(self):
            # Llenar el combo de Calificación
            cb_options = ("", "Inserción (I)", "Actualizacion (U)", "Eliminacion (D)")
            self.cbTipo.addItems(cb_options)

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

    


    def select_tabla_auditoria(self, nombreTabla, fechaInicio, fechaFin, tipoOperacion):
        conn = None
        print("nombreTabla: " + nombreTabla)
        print("fechaInicio: " + fechaInicio)
        print("fechaFin: " + fechaFin)
        print("tipoOperacion: " + tipoOperacion)

        # Transformar tipoOperacion
        tipoOperacion_transformed = ""
        if tipoOperacion == "Inserción (I)":
            tipoOperacion_transformed = "I"
        elif tipoOperacion == "Actualizacion (U)":
            tipoOperacion_transformed = "U"
        elif tipoOperacion == "Eliminacion (D)":
            tipoOperacion_transformed = "D"
        else:
            print("Tipo de operación desconocido: " + tipoOperacion)

        print("tipoOperacion_transformed: " + tipoOperacion_transformed)

        # Convertir fechas al formato adecuado
        fechaInicio_formateada = self.convertir_fecha(fechaInicio)
        fechaFin_formateada = self.convertir_fecha(fechaFin)

        if not fechaInicio_formateada or not fechaFin_formateada:
            print("Error en la conversión de fechas.")
            return []

        print("fechaInicio_formateada: " + fechaInicio_formateada)
        print("fechaFin_formateada: " + fechaFin_formateada)

        try:
            conn = sqlite3.connect('DATABASEAPP.db')  # Cambia 'DATABASEAPP.db' por la ruta a tu base de datos
            cur = conn.cursor()

            # Construir la consulta SQL dinámicamente
            if tipoOperacion_transformed == "":
                sql = f"SELECT * FROM {nombreTabla} WHERE FECHA_OPERACION BETWEEN ? AND ?"
                params = (fechaInicio_formateada, fechaFin_formateada)
            else:
                sql = f"SELECT * FROM {nombreTabla} WHERE FECHA_OPERACION BETWEEN ? AND ? AND TIPO_OPERACION = ?"
                params = (fechaInicio_formateada, fechaFin_formateada, tipoOperacion_transformed)
                
            print(f"Consulta SQL: {sql}")  # Imprimir la consulta para verificarla

            # Ejecutar la consulta con los parámetros proporcionados
            cur.execute(sql, params)
            rows = cur.fetchall()
            
            # Imprimir el número de filas obtenidas para verificar
            print(f"Número de filas obtenidas: {len(rows)}")
            print(f"Filas obtenidas: {rows}")  # Imprimir las filas obtenidas para ver los resultados
            return rows


        except Error as e:
            print("Error selecting data: " + str(e))

        finally:
            if conn:
                conn.close()
    def convertir_fecha(self,fecha_str):
        try:
            # Convertir de formato dd/mm/aaaa a formato aaaa-mm-dd HH:MM:SS
            fecha = datetime.strptime(fecha_str, '%d/%m/%Y')
            return fecha.strftime('%Y-%m-%d 00:00:00')  # Puedes ajustar la hora según sea necesario
        except ValueError:
            print(f"Formato de fecha incorrecto: {fecha_str}")
            return None