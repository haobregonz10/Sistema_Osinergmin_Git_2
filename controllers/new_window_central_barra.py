from PySide2.QtWidgets import QMessageBox,QDialog,QHeaderView,QTableWidgetItem,QAbstractItemView, QWidget, QFileDialog,QCompleter
from PySide2.QtCore import Qt, QDate
from PySide2.QtGui import *
import sqlite3
from sqlite3 import Error
from views.new_central_barra import Ui_NewBook
from db.books import delete_plano_barra_central,delete_esquema_barra_central,buscar_usuario_acceso,insert_book_barra_central_generacion,select_plano_barra_central,select_esquema_barra_central
from PySide2 import QtCore
from pys2_msgboxes import msg_boxes
from datetime import date, datetime

class NewBookWindow(QDialog,Ui_NewBook):
    def __init__(self, parent=None,_codCentral=None,_codigo=None):
        self._codCentral=_codCentral
        super().__init__(parent)
        self.parent = parent
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)
        self.Usuario= buscar_usuario_acceso();
        self.inputNombre.setText(str(_codCentral))
        self.inputNombre.setEnabled(False)
        self.populate_combobox()
        #1231321
        if(self.Usuario!="admin"):
            print("NO ES ADMIN!!!")
            self.inputCodEmpresa.hide()
            self.label_empresa.hide()
        else:
            print("ES ADMIN!!!") 
            self.inputCodEmpresa.setText(self.Usuario)
            self.inputCodEmpresa.setEnabled(False)
        #123123132
        self.label.setStyleSheet("background-color: #114692;")
        self.label_advertencia_dni.hide()
        self.label_nota_obligatoria.hide()
        if _codigo is not None:
            print("----------NO ES EDIT-----------:"+str(_codigo))
            self.populate_inputs(_codigo)
            self.inputCodigo.setText(str(_codigo))
            self.inputCodigo.setEnabled(False)
            self.addButton.setText("GUARDAR")

        self.addButton.clicked.connect(self.add_book)

        self.btnAddPlano.clicked.connect(self.open_new_window_plano)
        self.btnAddEsquema.clicked.connect(self.open_new_window_coordenadas)
#
    
        #self.addButton.clicked.connect(self.add_book)
        self.cancelButton.clicked.connect(self.close)

        self.table_config_plano()
        self.table_config_esquema()
        self.populate_table_plano(select_plano_barra_central(self._codCentral,self.inputCodigo.text()))
        self.populate_table_esquema(select_esquema_barra_central(self._codCentral,self.inputCodigo.text()))
        #self.cancelButton.clicked.connect(self.close) 
        self.btnDeletePlano.clicked.connect(self.remove_book_plano)
        self.btnDeleteEsquema.clicked.connect(self.remove_book_esquema)

    def remove_book_plano(self):
        selected_row = self.tablePlano.selectedItems()
        print("SELECT ROWWWWW: "+str(selected_row))
        if len(selected_row)!=0:
            respuesta=msg_boxes.alert_msgbox("Corfirmar Eliminar","¿Estas seguro de eliminar el registro?")
            if respuesta== QMessageBox.Yes:
                if selected_row:
                    book_id = str(selected_row[3].text())
                    row = selected_row[3].row()

                    if delete_plano_barra_central(self.Usuario,self._codCentral,self.inputCodigo.text(),book_id):
                        self.tablePlano.removeRow(row)

    def remove_book_esquema(self):
        selected_row = self.tableEsquema.selectedItems()
        print("SELECT ROWWWWW: "+str(selected_row))
        if len(selected_row)!=0:
            respuesta=msg_boxes.alert_msgbox("Corfirmar Eliminar","¿Estas seguro de eliminar el registro?")
            if respuesta== QMessageBox.Yes:
                if selected_row:
                    book_id = str(selected_row[1].text())
                    row = selected_row[1].row()

                    if delete_esquema_barra_central(self.Usuario,self._codCentral,self.inputCodigo.text(),book_id):
                        self.tableEsquema.removeRow(row)

    def table_config_plano(self):
        column_headers = ("#","Segmento","Fase","Secuencia","X","Y","Z")
        self.tablePlano.setColumnCount(len(column_headers))
        self.tablePlano.setHorizontalHeaderLabels(column_headers)
        self.tablePlano.setSelectionMode(QAbstractItemView.SingleSelection)
        stylesheet = "::section{Background-color:#114692;border:1px solid black;color: white;}"
        self.tablePlano.horizontalHeader().setStyleSheet(stylesheet)

        self.tablePlano.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tablePlano.setStyleSheet("QTableWidget{ gridline-color:black;alternate-background-color: #E2DED0;}")
        self.tablePlano.setAlternatingRowColors(True)

        self.tablePlano.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tablePlano.verticalHeader().setVisible(False)
        self.tablePlano.setColumnWidth(0,19)
        headerVertical = self.tablePlano.verticalHeader()
        headerVertical.resizeSections(QHeaderView.ResizeToContents)
        headerVertical.setStretchLastSection(True)

    def populate_table_plano(self,data):
        if data is not None:
            self.tablePlano.setRowCount(len(data))
            print("REFRESH4")
            for index_row, row in enumerate(data):
                # Incrementamos el índice de fila en 1 para comenzar con el número de orden en 1
                order_number = index_row + 1
                
                # Establecemos el número de orden en la primera columna
                self.tablePlano.setItem(index_row, 0, QTableWidgetItem(str(order_number)))
                
                for index_cell, cell in enumerate(row):
                    # Llenamos los datos de la fila a partir de la segunda columna
                    self.tablePlano.setItem(index_row, index_cell + 1, QTableWidgetItem(str(cell)))
                    
                    if index_cell == 13:
                        itemx = self.tablePlano.item(index_row, index_cell + 1)  # Se ajusta el índice de la celda
                        print("EL ITEM ACTUAL ES: ", itemx)
                        if itemx.text() == "PENDIENTE":
                            itemx.setForeground(QBrush(QColor(255, 0, 0)))
                        else:
                            itemx.setForeground(QBrush(QColor(0, 0, 255)))

            print("REFRESH5")
            headerVertical = self.tablePlano.verticalHeader()
            headerVertical.resizeSections(QHeaderView.ResizeToContents)
            headerVertical.setStretchLastSection(True)

            #self.records_qty()
        else:
            print("¡Error! No se cargaron los datos correctamente.")
    
    def table_config_esquema(self):
        column_headers = ("#","Secuencia","X","Y")
        self.tableEsquema.setColumnCount(len(column_headers))
        self.tableEsquema.setHorizontalHeaderLabels(column_headers)
        self.tableEsquema.setSelectionMode(QAbstractItemView.SingleSelection)
        stylesheet = "::section{Background-color:#114692;border:1px solid black;color: white;}"
        self.tableEsquema.horizontalHeader().setStyleSheet(stylesheet)

        self.tableEsquema.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableEsquema.setStyleSheet("QTableWidget{ gridline-color:black;alternate-background-color: #E2DED0;}")
        self.tableEsquema.setAlternatingRowColors(True)

        self.tableEsquema.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableEsquema.verticalHeader().setVisible(False)
        self.tableEsquema.setColumnWidth(0,19)
        headerVertical = self.tableEsquema.verticalHeader()
        headerVertical.resizeSections(QHeaderView.ResizeToContents)
        headerVertical.setStretchLastSection(True)

    def populate_table_esquema(self,data):
        if data is not None:
            self.tableEsquema.setRowCount(len(data))
            print("REFRESH4")
            for index_row, row in enumerate(data):
                # Incrementamos el índice de fila en 1 para comenzar con el número de orden en 1
                order_number = index_row + 1
                
                # Establecemos el número de orden en la primera columna
                self.tableEsquema.setItem(index_row, 0, QTableWidgetItem(str(order_number)))
                
                for index_cell, cell in enumerate(row):
                    # Llenamos los datos de la fila a partir de la segunda columna
                    self.tableEsquema.setItem(index_row, index_cell + 1, QTableWidgetItem(str(cell)))
                    
                    if index_cell == 13:
                        itemx = self.tableEsquema.item(index_row, index_cell + 1)  # Se ajusta el índice de la celda
                        print("EL ITEM ACTUAL ES: ", itemx)
                        if itemx.text() == "PENDIENTE":
                            itemx.setForeground(QBrush(QColor(255, 0, 0)))
                        else:
                            itemx.setForeground(QBrush(QColor(0, 0, 255)))

            print("REFRESH5")
            headerVertical = self.tableEsquema.verticalHeader()
            headerVertical.resizeSections(QHeaderView.ResizeToContents)
            headerVertical.setStretchLastSection(True)

            #self.records_qty()
        else:
            print("¡Error! No se cargaron los datos correctamente.")
    
    
    def refresh_table_from_child_window(self):
        
        data = select_plano_barra_central(self._codCentral,self.inputCodigo.text())
        data2 = select_esquema_barra_central(self._codCentral,self.inputCodigo.text())
        self.populate_table_plano(data)
        self.populate_table_esquema(data2)



    def open_new_window_coordenadas(self,codCentral):
        if(self.inputCodigo.isEnabled()):
            print("DEBE AGREGAR")
            msg_boxes.alert_msgbox_2("¡Error!","¡Primero debe agregar la Central de Generación!")
        else:
            from controllers.new_window_central_barra_esquema import NewBookWindow
            codCelda= self.inputCodigo.text()
            codCentral= self.inputNombre.text()
            window= NewBookWindow(self,codCelda,codCentral)
            window.exec_()

    def open_new_window_plano(self,codCentral):
        if(self.inputCodigo.isEnabled()):
            print("DEBE AGREGAR")
            msg_boxes.alert_msgbox_2("¡Error!","¡Primero debe agregar la Central de Generación!")
        else:        
            from controllers.new_window_central_barra_plano import NewBookWindow
            codCelda= self.inputCodigo.text()
            codCentral= self.inputNombre.text()
            window= NewBookWindow(self,codCelda,codCentral)
            window.exec_()
    #def populate_inputs(self):

        #self.ast_autoriza.hide()
        #self.ast_aquienvisita.hide()
        #self.label_nota_obligatoria.hide()
        #self.ast_dni.hide()
        #self.ast_visitante.hide()
        #self.ast_entidadempresa.hide()
        #self.ast_horaingreso.hide()
        #self.ast_motivo.hide()
        #self.ast_area.hide()
        #self.ast_fecha.hide()
        #self.ast_piso.hide()
        #self.ast_estado.hide()


  
    #def VerificarDni(self,dni):
    #    print("EL DNI EN LABEL ES:"+dni)
    #    if (ExisteDni(dni)):
    #        print("DNI SI EXISTE - Verificacion!")
    #        nombreEncontrado= EncontrarDni(dni)
    #        print("NOMBRE ENCONTRADO:"+str(nombreEncontrado))
    #        self.nombreVisitanteLineEdit.setText(nombreEncontrado)
    #    else:
    #        print("DNI NO EXISTE - Verificacion!")
    #        #self.nombreVisitanteLineEdit.setText("")

    
    def check_inputs(self):
        
        inputCodigo = self.inputCodigo.text()
        inputCodigo=inputCodigo.strip()

        
        
        errors_count = 0
        
        if inputCodigo == "":
            self.label_advertencia_dni.show()
            self.label_nota_obligatoria.show()
            errors_count += 1
        else:
            self.label_advertencia_dni.hide()

        
        if errors_count==0:
            return (True)
    
    def add_book(self):
        
        inputCodigo = self.inputCodigo.text()
        inputCodigo=inputCodigo.strip()

        inputNombre = self.inputNombre.text()
        inputNombre=inputNombre.strip()

        inputTension = self.inputTension.text()
        inputTension=inputTension.strip()

        inputFecha = self.inputFecha.text()
        inputFecha=inputFecha.strip()

        #inputSegmento = self.inputSegmento.text()
        #inputSegmento=inputSegmento.strip()
#
        #inputSecuencia = self.inputSecuencia.text()
        #inputSecuencia=inputSecuencia.strip()
#
        #inputX = self.inputX.text()
        #inputX=inputX.strip()
#
        #inputY = self.inputY.text()
        #inputY=inputY.strip()
#
        #inputZ = self.inputZ.text()
        #inputZ=inputZ.strip()
#
        #inputSecuencia_2 = self.inputSecuencia_2.text()
        #inputSecuencia_2=inputSecuencia_2.strip()
#
        #inputX_2 = self.inputX_2.text()
        #inputX_2=inputX_2.strip()
#
        #inputY_2 = self.inputY_2.text()
        #inputY_2=inputY_2.strip()


        inputArreglo = self.inputArreglo.currentText()
        inputInstalacion = self.inputInstalacion.currentText()
        cbBarra = self.cbBarra.currentText()
        cbEstado=self.cbEstado.currentText()
        #cbFase = self.cbFase.currentText()
        self.label_advertencia_dni.hide()

        #self.ActualizarVisitante(dni,visitante)
        if self.check_inputs():
            #new_path = shutil.copy(path, "book_files")
            self.label_nota_obligatoria.hide()
            data = (self.Usuario,inputNombre,inputCodigo,inputArreglo,inputInstalacion,inputTension,cbBarra,cbEstado,inputFecha) 
            
            if insert_book_barra_central_generacion(data):
                #self.clean_inputs()
                #data2 = (self.Usuario, inputNombre, inputCodigo, inputSecuencia_2, inputX_2, inputY_2)
                #data3 = (self.Usuario, inputNombre,inputCodigo, inputSegmento,cbFase, inputSecuencia, inputX, inputY, inputZ)

                #insert_book_barra_central_generacion_ubicacion_esquema(data2)
                #insert_book_barra_central_generacion_planta(data3)

                msg_boxes.correct_msgbox("¡Registro Exitoso!","¡Se registró exitosamente!")
                self.inputCodigo.setEnabled(False)
                self.parent.refresh_table_from_child_window()
                #self.close()
            else: 
                print("ERROR EN EL REGISTRO!")
            '''
            if(len(dni)!=8):
                self.label_advertencia_dni.show()
                self.ast_dni.show()
            else:
            '''    



    def select_file(self):
        file_path = QFileDialog.getOpenFileName()[0]
        self.filePathLineEdit.setText(file_path)


    #def populate_comboboxPiso(self):
    #    cb_options = ("","SÓTANO 1", "SÓTANO 2", "SÓTANO 3", "SÓTANO 4", "1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26")
    #    self.comboBoxPiso.addItems(cb_options)
    #
    def populate_combobox(self):
        # Llenar el combo de Tipo de Arreglo
        cb_options_arreglo = ("", "Simple Barra", "Doble Barra", "Anillo", "Interruptor y Medio")
        self.inputArreglo.addItems(cb_options_arreglo)

        # Llenar el combo de Tipo de Instalación
        cb_options_instalacion = ("", "Interior", "Exterior")
        self.inputInstalacion.addItems(cb_options_instalacion)

        # Llenar el combo de Barra de Referencia
        cb_options_barra = ("", "Si", "No")
        self.cbBarra.addItems(cb_options_barra)

        # Llenar el combo de Estado
        cb_options_estado = ("", "Nuevo", "Existente", "Eliminado", "Modificado", "Proyectado")
        self.cbEstado.addItems(cb_options_estado)


    
    def config_comboBoxes(self):
        font1 = QFont()
        font1.setPointSize(12)
        
    def populate_inputs(self, book_id):
        conn = None
        try:
            conn = sqlite3.connect('DATABASEAPP.db')
            print("Conexión a la base de datos correcta.")
        except Error as e:
            print("Error al conectar a la base de datos: " + str(e))
                
        if conn:
            try:
                cur = conn.cursor()
                # Consulta a la tabla Barra_Central_Generacion
                sql = f"SELECT * FROM Barra_Central_Generacion WHERE COD_BARRA = ?"
                cur.execute(sql, (book_id,))
                row = cur.fetchone()
                if row:
                    # Obtener los valores de la fila
                    inputCodEmpresa = str(row[0])
                    inputCodigo = str(row[2])
                    inputNombre = str(row[1])
                    cbArreglo = str(row[3])
                    inputTension = str(row[5])
                    cbInstalacion = str(row[4])
                    cbBarra = str(row[6])
                    cbEstado = str(row[7])
                    inputFecha = str(row[8])
                    print("BBAARRAA: "+cbBarra)
                    print("TIPO INST: "+cbBarra)
                    print("TIPO ARREGLO: "+cbBarra)
                    # Poblar los campos de entrada de la tabla Barra_Central_Generacion
                    self.inputCodEmpresa.setText(inputCodEmpresa)
                    self.inputCodigo.setText(inputCodigo)
                    self.inputNombre.setText(inputNombre)
                    self.inputTension.setText(inputTension)
                    self.cbBarra.setCurrentText(cbBarra)
                    self.cbEstado.setCurrentText(cbEstado)
                    self.inputArreglo.setCurrentText(cbArreglo)
                    self.inputInstalacion.setCurrentText(cbInstalacion)

                    # setDate para la fecha
                    print("LA FECHA ESSS: "+inputFecha)
                    fechaConv = inputFecha
                    fechaConv2 = fechaConv.replace("/", "-")
                    qdate = QDate.fromString(fechaConv2, "d-MM-yyyy")
                    self.inputFecha.setDate(qdate)

                    ## Consulta a la tabla Barra_Central_Generacion_Ubicacion_Esquema
                    #sql_ubicacion_esquema = f"SELECT * FROM Barra_Central_Generacion_Ubicacion_Esquema WHERE COD_BARRA = ?"
                    #cur.execute(sql_ubicacion_esquema, (book_id,))
                    #row_ubicacion_esquema = cur.fetchone()
                    #if row_ubicacion_esquema:
                    #    # Obtener los valores de la fila
                    #    inputSecuencia_2 = str(row_ubicacion_esquema[3])
                    #    inputX_2 = str(row_ubicacion_esquema[4])
                    #    inputY_2 = str(row_ubicacion_esquema[5])
#
                    #    # Poblar los campos de entrada de la tabla Barra_Central_Generacion_Ubicacion_Esquema
                    #    self.inputSecuencia_2.setText(inputSecuencia_2)
                    #    self.inputX_2.setText(inputX_2)
                    #    self.inputY_2.setText(inputY_2)
#
                    ## Consulta a la tabla Barra_Central_Generacion_Ubicacion_Plano_Planta
                    #sql_ubicacion_planta = f"SELECT * FROM Barra_Central_Generacion_Ubicacion_Plano_Planta WHERE COD_BARRA = ?"
                    #cur.execute(sql_ubicacion_planta, (book_id,))
                    #row_ubicacion_planta = cur.fetchone()
                    #if row_ubicacion_planta:
                    #    # Obtener los valores de la fila
                    #    inputSegmento = str(row_ubicacion_planta[3])
                    #    cbFase = str(row_ubicacion_planta[4])
                    #    inputSecuencia = str(row_ubicacion_planta[5])
                    #    inputX = str(row_ubicacion_planta[6])
                    #    inputY = str(row_ubicacion_planta[7])
                    #    inputZ = str(row_ubicacion_planta[8])
#
                    #    # Poblar los campos de entrada de la tabla Barra_Central_Generacion_Ubicacion_Plano_Planta
                    #    self.inputSegmento.setText(inputSegmento)
                    #    self.cbFase.setCurrentText(cbFase)
                    #    self.inputSecuencia.setText(inputSecuencia)
                    #    self.inputX.setText(inputX)
                    #    self.inputY.setText(inputY)
                    #    self.inputZ.setText(inputZ)

            except Error as e:
                print("Error al obtener detalles del libro:", str(e))
            finally:
                if conn:
                    conn.close()
