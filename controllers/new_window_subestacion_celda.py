from PySide2.QtWidgets import QMessageBox,QDialog, QWidget, QFileDialog,QCompleter,QAbstractItemView,QHeaderView,QTableWidgetItem
from PySide2.QtCore import Qt, QDate
from PySide2.QtGui import *
import sqlite3
from sqlite3 import Error
from views.new_transmision_celda import Ui_NewBook
from db.books import buscar_usuario_acceso,delete_book_Interruptor_Potencia,delete_book_Seccionador,select_cod_seccionadores_sub,select_cod_interruptores_sub,insert_book_celda,insert_book_celda_ubicacion_esquema,insert_book_celda_plano_planta
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
        self.label.setStyleSheet("background-color: #114692;")

        #self.btnEsquema.clicked.connect(self.open_new_window_coordenadas)
        #self.btnPlano.clicked.connect(self.open_new_window_plano)
        self.btnAddInterruptor.clicked.connect(self.open_new_window_interruptor)
        self.addButton_7.clicked.connect(self.open_new_window_seccionador)
        self.label_advertencia_dni.hide()
        self.label_nota_obligatoria.hide()
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
        self.populate_combobox()
        if _codigo is not None:
            print("----------NO ES EDIT-----------:"+str(_codigo))
            self.populate_inputs(_codigo)
            self.inputCodigo.setText(str(_codigo))
            self.inputCodigo.setEnabled(False)
            self.addButton.setText("GUARDAR")
#
        
        self.btnEsquema.clicked.connect(self.open_new_window_coordenadas)
        self.btnPlano.clicked.connect(self.open_new_window_plano)

        self.btnDeleteInterruptor.clicked.connect(self.remove_book_interruptor)
        self.btnDeleteSeccionador.clicked.connect(self.remove_book_seccionador)

        self.addButton.clicked.connect(self.add_book)
        self.cancelButton.clicked.connect(self.close)

        self.table_config_interruptores()
        self.populate_table_interruptores(select_cod_interruptores_sub(_codCentral,_codigo))
        self.table_config_seccionadores()
        self.populate_table_seccionadores(select_cod_seccionadores_sub(_codCentral,_codigo))


        self.tableInterruptores.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableInterruptores.verticalHeader().setVisible(False)
        self.tableInterruptores.setColumnWidth(0,19)
        headerVertical = self.tableInterruptores.verticalHeader()
        headerVertical.resizeSections(QHeaderView.ResizeToContents)
        headerVertical.setStretchLastSection(True)
        self.tableInterruptores.doubleClicked.connect(lambda: self.FilaSeleccionadaInterruptores())

        self.tableSeccionadores.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableSeccionadores.verticalHeader().setVisible(False)
        self.tableSeccionadores.setColumnWidth(0,19)
        headerVertical = self.tableSeccionadores.verticalHeader()
        headerVertical.resizeSections(QHeaderView.ResizeToContents)
        headerVertical.setStretchLastSection(True)
        self.tableSeccionadores.doubleClicked.connect(lambda: self.FilaSeleccionadaSeccionadores())
    
    def open_new_window_coordenadas(self,codCentral):
        if(self.inputCodigo.isEnabled()):
            print("DEBE AGREGAR")
            msg_boxes.alert_msgbox_2("¡Error!","¡Primero debe agregar la Celda!")
        else:
            from controllers.new_window_subestacion_celda_esquema import NewBookWindow
            codCelda= self.inputCodigo.text()
            codCentral= self.inputNombre.text()
            window= NewBookWindow(self,codCelda,codCentral)
            window.exec_()

    def open_new_window_plano(self,codCentral):
        if(self.inputCodigo.isEnabled()):
            print("DEBE AGREGAR")
            msg_boxes.alert_msgbox_2("¡Error!","¡Primero debe agregar la Celda!")
        else:        
            from controllers.new_window_subestacion_celda_plano import NewBookWindow
            codCelda= self.inputCodigo.text()
            codCentral= self.inputNombre.text()
            window= NewBookWindow(self,codCelda,codCentral)
            window.exec_()


    def open_new_window_interruptor(self):
        if(self.inputCodigo.isEnabled()):
            print("DEBE AGREGAR")
            msg_boxes.alert_msgbox_2("¡Error!","¡Primero debe agregar la Celda!")
        else:        
            from controllers.new_window_subestacion_interruptor import NewBookWindow
            codCelda= self.inputCodigo.text()
            codCentral= self.inputNombre.text()
            window= NewBookWindow(self,codCelda,codCentral)
            window.exec_()

            
    def open_new_window_seccionador(self):
        if(self.inputCodigo.isEnabled()):
            print("DEBE AGREGAR")
            msg_boxes.alert_msgbox_2("¡Error!","¡Primero debe agregar la Celda!")
        else:        
            from controllers.new_window_subestacion_seccionador import NewBookWindow
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
        inputCodigo =inputCodigo.strip()

        inputNombre = self.inputNombre.text()
        inputNombre =inputNombre.strip()

        inputTension = self.inputTension.text()
        inputTension =inputTension.strip()

        inputModulo = self.inputModulo.text()
        inputModulo =inputModulo.strip()

        inputFecha = self.inputFecha.text()
        inputFecha =inputFecha.strip()

        #inputSecuencia = self.inputSecuencia.text()
        #inputSecuencia =inputSecuencia.strip()
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
#
        cbCalificacion = self.cbCalificacion.currentText()
        cbTipo = self.cbTipo.currentText()
        cbInstalacion = self.cbInstalacion.currentText()
        cbEstado=self.cbEstado.currentText()

        self.label_advertencia_dni.hide()

        #self.ActualizarVisitante(dni,visitante)
        if self.check_inputs():
            #new_path = shutil.copy(path, "book_files")
            self.label_nota_obligatoria.hide()
            data = (self.Usuario,inputNombre,inputCodigo,cbCalificacion,cbTipo,cbInstalacion,inputTension,inputModulo,cbEstado,inputFecha) 
            
            if insert_book_celda(data):
                #self.clean_inputs()
                #data2 = (self.Usuario, inputNombre, inputCodigo, inputSecuencia_2, inputX_2, inputY_2)
                #data3 = (self.Usuario, inputNombre, inputCodigo,inputSecuencia, inputX, inputY, inputZ)

                #insert_book_celda_ubicacion_esquema(data2)
                #insert_book_celda_plano_planta(data3)

                msg_boxes.correct_msgbox("¡Registro Exitoso!","¡Se registró exitosamente!")
                self.inputCodigo.setEnabled(False)
                self.parent.refresh_table_from_child_window()
                self.addButton.setText("GUARDAR")
                #self.close()
            else: 
                print("ERROR EN EL REGISTRO!")
            '''
            if(len(dni)!=8):
                self.label_advertencia_dni.show()
                self.ast_dni.show()
            else:
            '''    


    #def clean_inputs(self):
    #    self.titleLineEdit.clear()
    #    self.categoryLineEdit.clear()
    #    self.areaVisitadaLineEdit.clear()
    #    self.dniLineEdit.clear()
    #    self.nombreVisitanteLineEdit.clear()
    #    self.categoryLineEditEntidadEmpresa.clear()
    #    self.horaIngresoLineEdit.clear()
    #    self.horaSalidaLineEdit.clear()
    #    self.motivoVisitaLineEdit.clear()
    #    self.comboBoxPiso.setCurrentText("")
    #    self.comboBoxEstado.setCurrentText("")
#
    def select_file(self):
        file_path = QFileDialog.getOpenFileName()[0]
        self.filePathLineEdit.setText(file_path)

    def refresh_table_from_child_window(self):
        print("REFRESH FROM CHILD...")
        print("REFRESH1")
        data = select_cod_seccionadores_sub(self.inputNombre.text(),self.inputCodigo.text())
        data2 = select_cod_interruptores_sub(self.inputNombre.text(),self.inputCodigo.text())
        
        print("REFRESH2")
        self.populate_table_seccionadores(data)
        self.populate_table_interruptores(data2)


    def table_config_interruptores(self):
        column_headers = ("#","Código","Calificación","Tipo Instalación","Tension N.","Marca","Año Fab.")
        self.tableInterruptores.setColumnCount(len(column_headers))
        self.tableInterruptores.setHorizontalHeaderLabels(column_headers)
        self.tableInterruptores.setSelectionMode(QAbstractItemView.SingleSelection)
        stylesheet = "::section{Background-color:#114692;border:1px solid black;color: white;}"
        self.tableInterruptores.horizontalHeader().setStyleSheet(stylesheet)

        self.tableInterruptores.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableInterruptores.setStyleSheet("QTableWidget{ gridline-color:black;alternate-background-color: #E2DED0;}")
        self.tableInterruptores.setAlternatingRowColors(True)

    def table_config_seccionadores(self):
        column_headers = ("#","Código","Calificación","Tipo","Tipo Instalacion","Tension N.","Marca")
        
        self.tableSeccionadores.setColumnCount(len(column_headers))
        self.tableSeccionadores.setHorizontalHeaderLabels(column_headers)
        self.tableSeccionadores.setSelectionMode(QAbstractItemView.SingleSelection)
        stylesheet = "::section{Background-color:#114692;border:1px solid black;color: white;}"
        self.tableSeccionadores.horizontalHeader().setStyleSheet(stylesheet)

        self.tableSeccionadores.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableSeccionadores.setStyleSheet("QTableWidget{ gridline-color:black;alternate-background-color: #E2DED0;}")
        self.tableSeccionadores.setAlternatingRowColors(True)
    
    def populate_table_interruptores(self,data):
        if data is not None:
            self.tableInterruptores.setRowCount(len(data))
            print("REFRESH4")
            for index_row, row in enumerate(data):
                # Incrementamos el índice de fila en 1 para comenzar con el número de orden en 1
                order_number = index_row + 1
                
                # Establecemos el número de orden en la primera columna
                self.tableInterruptores.setItem(index_row, 0, QTableWidgetItem(str(order_number)))
                
                for index_cell, cell in enumerate(row):
                    # Llenamos los datos de la fila a partir de la segunda columna
                    self.tableInterruptores.setItem(index_row, index_cell + 1, QTableWidgetItem(str(cell)))
                    
                    if index_cell == 13:
                        itemx = self.tableInterruptores.item(index_row, index_cell + 1)  # Se ajusta el índice de la celda
                        print("EL ITEM ACTUAL ES: ", itemx)
                        if itemx.text() == "PENDIENTE":
                            itemx.setForeground(QBrush(QColor(255, 0, 0)))
                        else:
                            itemx.setForeground(QBrush(QColor(0, 0, 255)))

            print("REFRESH5")
            headerVertical = self.tableInterruptores.verticalHeader()
            headerVertical.resizeSections(QHeaderView.ResizeToContents)
            headerVertical.setStretchLastSection(True)

            #self.records_qty()
        else:
            print("¡Error! No se cargaron los datos correctamente.")
    
    def populate_table_seccionadores(self,data):
        if data is not None:
            self.tableSeccionadores.setRowCount(len(data))
            print("REFRESH4")
            for index_row, row in enumerate(data):
                # Incrementamos el índice de fila en 1 para comenzar con el número de orden en 1
                order_number = index_row + 1
                
                # Establecemos el número de orden en la primera columna
                self.tableSeccionadores.setItem(index_row, 0, QTableWidgetItem(str(order_number)))
                
                for index_cell, cell in enumerate(row):
                    # Llenamos los datos de la fila a partir de la segunda columna
                    self.tableSeccionadores.setItem(index_row, index_cell + 1, QTableWidgetItem(str(cell)))
                    
                    if index_cell == 13:
                        itemx = self.tableSeccionadores.item(index_row, index_cell + 1)  # Se ajusta el índice de la celda
                        print("EL ITEM ACTUAL ES: ", itemx)
                        if itemx.text() == "PENDIENTE":
                            itemx.setForeground(QBrush(QColor(255, 0, 0)))
                        else:
                            itemx.setForeground(QBrush(QColor(0, 0, 255)))

            print("REFRESH5")
            headerVertical = self.tableSeccionadores.verticalHeader()
            headerVertical.resizeSections(QHeaderView.ResizeToContents)
            headerVertical.setStretchLastSection(True)

            #self.records_qty()
        else:
            print("¡Error! No se cargaron los datos correctamente.")
    #def populate_comboboxPiso(self):
    #    cb_options = ("","SÓTANO 1", "SÓTANO 2", "SÓTANO 3", "SÓTANO 4", "1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26")
    #    self.comboBoxPiso.addItems(cb_options)
    #

    def FilaSeleccionadaInterruptores(self):
        print("ENTRO A DOUBLE CLICK!")
        from controllers.new_window_subestacion_interruptor import NewBookWindow
        selected_row = self.tableInterruptores.selectedItems()

        if selected_row:
            book_id = str(selected_row[1].text())
            window= NewBookWindow(self,self.inputCodigo.text(),self.inputNombre.text(),book_id)
        window.exec_()
        
        self.tableInterruptores.clearSelection()
    
    def FilaSeleccionadaSeccionadores(self):
        print("ENTRO A DOUBLE CLICK!")
        from controllers.new_window_subestacion_seccionador import NewBookWindow
        selected_row = self.tableSeccionadores.selectedItems()

        if selected_row:
            book_id = str(selected_row[1].text())
            window= NewBookWindow(self,self.inputCodigo.text(),self.inputNombre.text(),book_id)
        window.exec_()
        
        self.tableSeccionadores.clearSelection()
    

    
    def config_comboBoxes(self):
        font1 = QFont()
        font1.setPointSize(12)
        
    
    def populate_inputs(self, celda_id):
        conn = None
        try:
            conn = sqlite3.connect('DATABASEAPP.db')
            print("Conexión a la base de datos correcta.")
        except Error as e:
            print("Error al conectar a la base de datos: " + str(e))
            return

        if conn:
            try:
                cur = conn.cursor()

                # Consulta a la tabla Celda
                sql = "SELECT * FROM Celda WHERE COD_CELDA = ?"
                cur.execute(sql, (celda_id,))
                row = cur.fetchone()
                if row:
                    # Obtener los valores de la fila
                    inputCodEmpresa = str(row[0])
                    inputCodigo = str(row[2])
                    inputNombre = str(row[1])
                    cbCalificacion = str(row[3])
                    cbTipo = str(row[4])
                    cbInstalacion = str(row[5])
                    inputTension = str(row[6])
                    inputModulo = str(row[7])
                    cbEstado = str(row[8])
                    inputFecha = str(row[9])

                    # Poblar los campos de entrada de la tabla Celda
                    self.inputCodEmpresa.setText(inputCodEmpresa)
                    self.inputCodigo.setText(inputCodigo)
                    self.inputNombre.setText(inputNombre)
                    self.cbCalificacion.setCurrentText(cbCalificacion)
                    self.cbTipo.setCurrentText(cbTipo)
                    self.cbInstalacion.setCurrentText(cbInstalacion)
                    self.inputTension.setText(inputTension)
                    self.inputModulo.setText(inputModulo)
                    self.cbEstado.setCurrentText(cbEstado)
                    fechaConv = inputFecha.replace("/", "-")
                    qdate = QDate.fromString(fechaConv, "d-MM-yyyy")
                    self.inputFecha.setDate(qdate)

                    ## Consulta a la tabla Celda_Ubicacion_Esquema
                    #sql_esquema = "SELECT * FROM Celda_Ubicacion_Esquema WHERE COD_CELDA = ?"
                    #cur.execute(sql_esquema, (celda_id,))
                    #row_esquema = cur.fetchone()
                    #if row_esquema:
                    #    inputSecuencia_2 = str(row_esquema[3])
                    #    inputX_2 = str(row_esquema[4])
                    #    inputY_2 = str(row_esquema[5])
#
                    #    # Poblar los campos de entrada de la tabla Celda_Ubicacion_Esquema
                    #    self.inputSecuencia_2.setText(inputSecuencia_2)
                    #    self.inputX_2.setText(inputX_2)
                    #    self.inputY_2.setText(inputY_2)
#
                    ## Consulta a la tabla Celda_Ubicacion_Plano_Planta
                    #sql_plano = "SELECT * FROM Celda_Ubicacion_Plano_Planta WHERE COD_CELDA = ?"
                    #cur.execute(sql_plano, (celda_id,))
                    #row_plano = cur.fetchone()
                    #if row_plano:
                    #    inputSecuencia = str(row_plano[3])
                    #    inputX = str(row_plano[4])
                    #    inputY = str(row_plano[5])
                    #    inputZ = str(row_plano[6])
#
                    #    # Poblar los campos de entrada de la tabla Celda_Ubicacion_Plano_Planta
                    #    self.inputSecuencia.setText(inputSecuencia)
                    #    self.inputX.setText(inputX)
                    #    self.inputY.setText(inputY)
                    #    self.inputZ.setText(inputZ)

            except Error as e:
                print("Error al obtener detalles de la celda:", str(e))
            finally:
                if conn:
                    conn.close()


    def populate_combobox(self):
        # Llenar el combo de Calificación
        cb_options_calificacion = ("", "Principal", "Secundario", "Garantizado", "Complementario")
        self.cbCalificacion.addItems(cb_options_calificacion)

        # Llenar el combo de Tipo de Instalación
        cb_options_tipo_instalacion = ("", "Interior", "Exterior")
        self.cbInstalacion.addItems(cb_options_tipo_instalacion)

        # Llenar el combo de Tipo de Celda
        cb_options_tipo_celda = (
            "", 
            "LÍNEA", 
            "TRANSFORMACIÓN", 
            "LÍNEA TRANSFORMADOR", 
            "ACOPLAMIENTO", 
            "ACOPLAMIENTO LONGITUDINAL", 
            "MEDICIÓN", 
            "ALIMENTADOR", 
            "REACTOR", 
            "COMPENSADOR SVC", 
            "COMPENSADOR SÍNCRONO", 
            "COMPENSADOR"
        )
        self.cbTipo.addItems(cb_options_tipo_celda)

        # Llenar el combo de Estado
        cb_options_estado = ("", "Nuevo", "Existente", "Eliminado", "Modificado", "Proyectado")
        self.cbEstado.addItems(cb_options_estado)

    def remove_book_interruptor(self):
        selected_row = self.tableInterruptores.selectedItems()
        print("SELECT ROWWWWW: "+str(selected_row))
        if len(selected_row)!=0:
            respuesta=msg_boxes.alert_msgbox("Corfirmar Eliminar","¿Estas seguro de eliminar el registro?")
            if respuesta== QMessageBox.Yes:
                if selected_row:
                    book_id = str(selected_row[1].text())
                    row = selected_row[1].row()

                    if delete_book_Interruptor_Potencia(book_id):
                    
                        self.tableInterruptores.removeRow(row)
    
    def remove_book_seccionador(self):
        selected_row = self.tableSeccionadores.selectedItems()
        print("SELECT ROWWWWW: "+str(selected_row))
        if len(selected_row)!=0:
            respuesta=msg_boxes.alert_msgbox("Corfirmar Eliminar","¿Estas seguro de eliminar el registro?")
            if respuesta== QMessageBox.Yes:
                if selected_row:
                    book_id = str(selected_row[1].text())
                    row = selected_row[1].row()

                    if delete_book_Seccionador(book_id):
                    
                        self.tableSeccionadores.removeRow(row)