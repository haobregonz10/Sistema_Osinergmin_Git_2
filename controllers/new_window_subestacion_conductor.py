from PySide2.QtWidgets import QMessageBox,QDialog,QHeaderView,QTableWidgetItem,QAbstractItemView, QWidget, QFileDialog,QCompleter
from PySide2.QtCore import Qt, QDate
from PySide2.QtGui import *
import sqlite3
from sqlite3 import Error
from views.new_transmision_conductor import Ui_NewBook
from db.books import delete_plano_conductor_subestacion,delete_esquema_conductor_subestacion,buscar_usuario_acceso,insert_book_conductor,select_plano_conductor_subestacion,select_esquema_conductor_subestacion
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
        self.label.setStyleSheet("background-color: #114692;")
        self.inputSubestacion.setText(str(_codCentral))
        self.inputSubestacion.setEnabled(False)
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
        
        self.label_advertencia_dni.hide()
        self.label_nota_obligatoria.hide()
        
        if _codigo is not None:
            print("----------NO ES EDIT-----------:"+str(_codigo))
            self.populate_inputs(_codigo)
            self.inputCodigo.setText(str(_codigo))
            self.inputCodigo.setEnabled(False)
            self.addButton.setText("GUARDAR")

        self.btnAddPlano.clicked.connect(self.open_new_window_plano)
        self.btnAddEsquema.clicked.connect(self.open_new_window_coordenadas)
        #self.populate_comboboxPiso()
        #self.populate_comboboxEstado()
        #self.populate_inputs()
        #self.config_comboBoxes()
#
    
        self.addButton.clicked.connect(self.add_book)
        self.cancelButton.clicked.connect(self.close)

        self.table_config_plano()
        self.table_config_esquema()
        self.populate_table_plano(select_plano_conductor_subestacion(self._codCentral,self.inputCodigo.text()))
        self.populate_table_esquema(select_esquema_conductor_subestacion(self._codCentral,self.inputCodigo.text()))
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
                    book_id = str(selected_row[2].text())
                    row = selected_row[2].row()

                    if delete_plano_conductor_subestacion(self.Usuario,self._codCentral,self.inputCodigo.text(),book_id):
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

                    if delete_esquema_conductor_subestacion(self.Usuario,self._codCentral,self.inputCodigo.text(),book_id):
                        self.tableEsquema.removeRow(row)
                        
    def table_config_plano(self):
        column_headers = ("#","Fase","Secuencia","X","Y","Z")
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
        
        data = select_plano_conductor_subestacion(self._codCentral,self.inputCodigo.text())
        data2 = select_esquema_conductor_subestacion(self._codCentral,self.inputCodigo.text())
        self.populate_table_plano(data)
        self.populate_table_esquema(data2)



    def open_new_window_coordenadas(self,codCentral):
        if(self.inputCodigo.isEnabled()):
            print("DEBE AGREGAR")
            msg_boxes.alert_msgbox_2("¡Error!","¡Primero debe agregar el código de Conductor!")
        else:
            from controllers.new_window_subestacion_conductor_esquema import NewBookWindow
            codCelda= self.inputCodigo.text()
            codCentral= self.inputSubestacion.text()
            window= NewBookWindow(self,codCelda,codCentral)
            window.exec_()

    def open_new_window_plano(self,codCentral):
        if(self.inputCodigo.isEnabled()):
            print("DEBE AGREGAR")
            msg_boxes.alert_msgbox_2("¡Error!","¡Primero debe agregar el código de Conductor!")
        else:        
            from controllers.new_window_subestacion_conductor_plano import NewBookWindow
            codCelda= self.inputCodigo.text()
            codCentral= self.inputSubestacion.text()
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
            print("El campo areavisitada es obligatorio")
            self.label_advertencia_dni.show()
            errors_count +=1
        else:
            self.label_advertencia_dni.hide()

        if errors_count==0:
            return (True)
            
            
    def add_book(self):
        
        inputCodigo = self.inputCodigo.text()
        inputCodigo=inputCodigo.strip()

        inputNombre = self.inputSubestacion.text()
        inputNombre=inputNombre.strip()

        inputFecha = self.inputFecha.text()

        inputTension = self.inputTension.text()
        inputTension=inputTension.strip()

        


        #inputX = self.inputX.text()
        #inputX=inputX.strip()
#
        #inputY = self.inputY.text()
        #inputY=inputY.strip()
#
        #inputZ = self.inputZ.text()
        #inputZ=inputZ.strip()
#
        #inputSecuencia = self.inputSecuencia.text()
        #inputSecuencia=inputSecuencia.strip()
#
        #inputSecuencia_2 = self.inputSecuencia_2.text()
        #inputSecuencia_2=inputSecuencia_2.strip()
#
        #inputX_2 = self.inputX_2.text()
        #inputX_2=inputX_2.strip()
#
        #inputY_2 = self.inputY_2.text()
        #inputY_2=inputY_2.strip()


        cbCalificacion = self.cbCalificacion.currentText()
        cbEstado = self.cbEstado.currentText()
        #cbFase = self.cbFase.currentText()

        self.label_advertencia_dni.hide()

        
        #self.ActualizarVisitante(dni,visitante)
        if self.check_inputs():
            #new_path = shutil.copy(path, "book_files")
            self.label_nota_obligatoria.hide()
            data = (self.Usuario, inputNombre, cbCalificacion, inputCodigo, inputTension, cbEstado, inputFecha)

            if insert_book_conductor(data):
                #self.clean_inputs()
                #data2 = (self.Usuario, inputNombre, inputCodigo, inputSecuencia_2, inputX_2, inputY_2)
                #data3 = (self.Usuario, inputNombre, inputCodigo, cbFase, inputSecuencia, inputX, inputY, inputZ)
                #insert_book_conductor_ubicacion_esquema(data2)
                #insert_book_conductor_ubicacion_plano(data3)

                msg_boxes.correct_msgbox("¡Registro Exitoso!","¡Se registró exitosamente!")
                self.inputCodigo.setEnabled(False)
                self.addButton.setText("Guardar")
                self.parent.refresh_table_from_child_window()
                self.close()
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


    #def populate_comboboxPiso(self):
    #    cb_options = ("","SÓTANO 1", "SÓTANO 2", "SÓTANO 3", "SÓTANO 4", "1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26")
    #    self.comboBoxPiso.addItems(cb_options)
    #

    

    
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
            return
                
        if conn:
            try:
                cur = conn.cursor()

                # Consulta a la tabla Conductor
                sql = "SELECT * FROM Conductor WHERE COD_CONDUCTOR = ?"
                cur.execute(sql, (book_id,))
                row = cur.fetchone()
                if row:
                    # Obtener los valores de la fila
                    inputCodEmpresa = str(row[0])
                    inputCodigo = str(row[3])
                    inputNombre = str(row[1])
                    cbCalificacion = str(row[2])
                    inputTension = str(row[4])
                    cbEstado = str(row[5])
                    inputFecha = str(row[6])

                    # Poblar los campos de entrada de la tabla Conductor
                    self.inputCodigo.setText(inputCodigo)
                    self.inputCodEmpresa.setText(inputCodEmpresa)
                    self.inputSubestacion.setText(inputNombre)
                    self.cbCalificacion.setCurrentText(cbCalificacion)
                    self.inputTension.setText(inputTension)
                    self.cbEstado.setCurrentText(cbEstado)
                    fechaConv = inputFecha.replace("/", "-")
                    qdate = QDate.fromString(fechaConv, "d-MM-yyyy")
                    self.inputFecha.setDate(qdate)

                    ## Consulta a la tabla Conductor_Ubicacion_Esquema
                    #sql_esquema = "SELECT * FROM Conductor_Ubicacion_Esquema WHERE COD_CONDUCTOR = ?"
                    #cur.execute(sql_esquema, (book_id,))
                    #row_esquema = cur.fetchone()
                    #if row_esquema:
                    #    inputSecuencia_2 = str(row_esquema[3])
                    #    inputX_2 = str(row_esquema[4])
                    #    inputY_2 = str(row_esquema[5])
#
                    #    # Poblar los campos de entrada de la tabla Conductor_Ubicacion_Esquema
                    #    self.inputSecuencia_2.setText(inputSecuencia_2)
                    #    self.inputX_2.setText(inputX_2)
                    #    self.inputY_2.setText(inputY_2)
#
                    ## Consulta a la tabla Conductor_Ubicacion_Plano_Planta
                    #sql_plano = "SELECT * FROM Conductor_Ubicacion_Plano_Planta WHERE COD_CONDUCTOR = ?"
                    #cur.execute(sql_plano, (book_id,))
                    #row_plano = cur.fetchone()
                    #if row_plano:
                    #    cbFase = str(row_plano[3])
                    #    inputSecuencia = str(row_plano[4])
                    #    inputX = str(row_plano[5])
                    #    inputY = str(row_plano[6])
                    #    inputZ = str(row_plano[7])
#
                    #    # Poblar los campos de entrada de la tabla Conductor_Ubicacion_Plano_Planta
                    #    self.cbFase.setCurrentText(cbFase)
                    #    self.inputSecuencia.setText(inputSecuencia)
                    #    self.inputX.setText(inputX)
                    #    self.inputY.setText(inputY)
                    #    self.inputZ.setText(inputZ)

            except Error as e:
                print("Error al obtener detalles del conductor:", str(e))
            finally:
                if conn:
                    conn.close()

    def populate_combobox(self):
        # Llenar el combo de Calificación
        cb_options_calificacion = ("", "Principal", "Secundario", "Garantizado", "Complementario")
        self.cbCalificacion.addItems(cb_options_calificacion)

        # Llenar el combo de Estado
        cb_options_estado = ("", "Nuevo", "Existente", "Eliminado", "Modificado", "Proyectado")
        self.cbEstado.addItems(cb_options_estado)


