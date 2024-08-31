from PySide2.QtWidgets import QDialog,QMessageBox,QPushButton, QWidget, QFileDialog,QCompleter,QTableWidgetItem,QAbstractItemView,QHeaderView
from PySide2.QtCore import Qt, QDate
from PySide2.QtGui import *
import sqlite3
from sqlite3 import Error
from views.new_transmision_linea import Ui_NewBook
from db.books import buscar_usuario_acceso,delete_book_Estructura,delete_book_Tramo_Linea_Transmision,insert_book_linea_transmision,select_cod_tramo_linea,select_cod_estructura
from PySide2 import QtCore
from pys2_msgboxes import msg_boxes
from datetime import date, datetime

class NewBookWindow(QDialog,Ui_NewBook):
    def __init__(self, parent=None,_codCentral=None):
        super().__init__(parent)
        self.parent = parent
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)
        self.Usuario= buscar_usuario_acceso();
        self.populate_combobox()
        if(self.Usuario!="admin"):
            print("NO ES ADMIN!!!")
            self.inputCodEmpresa.hide()
            self.label_empresa.hide()
        else:
            print("ES ADMIN!!!") 
            self.inputCodEmpresa.setText(self.Usuario)
            self.inputCodEmpresa.setEnabled(False)
        if _codCentral is not None:
            print("----------NO ES EDIT-----------:"+str(_codCentral))
            self.populate_inputs(_codCentral)
            self.refresh_table_from_child_window()
            self.inputCodigo.setEnabled(False)
            self.addButton.setText("GUARDAR")

        self.btnAddInterruptor.clicked.connect(self.open_new_window_tramo)
        self.addButton_7.clicked.connect(self.open_new_window_estructura)
        self.cancelButton.clicked.connect(self.close)
        self.label.setStyleSheet("background-color: #114692;")
        
        self.label_advertencia_dni.hide()
        self.label_nota_obligatoria.hide()
        #self.populate_comboboxPiso()
        idcodCentral= self.inputCodigo.text()           
        self.table_config_tramo_linea()
        self.populate_table_tramo_linea(select_cod_tramo_linea(idcodCentral))

        self.table_config_estructura()
        self.populate_table_estructura(select_cod_estructura(idcodCentral))

        self.addButton.clicked.connect(self.add_book)
        
        self.btnDeleteInterruptor.clicked.connect(self.remove_book_tramo)
        self.btnDeleteSeccionador.clicked.connect(self.remove_book_estructura)

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
        self.tableSeccionadores.doubleClicked.connect(lambda: self.FilaSeleccionadaEstructura())

        #self.populate_comboboxPiso()
        #self.populate_comboboxEstado()
        #self.populate_inputs()
        #self.config_comboBoxes()
#
    
        #self.addButton.clicked.connect(self.add_book)
        #self.cancelButton.clicked.connect(self.close)
    def open_new_window_estructura(self):
        if(self.inputCodigo.isEnabled()):
            print("DEBE AGREGAR")
            msg_boxes.alert_msgbox_2("¡Error!","¡Primero debe agregar la Linea de Transmisión!")
        else:        
            from controllers.new_window_linea_estructura import NewBookWindow
            codCentral= self.inputCodigo.text()
            window= NewBookWindow(self,codCentral)
            window.exec_()

    def open_new_window_tramo(self):
        if(self.inputCodigo.isEnabled()):
            print("DEBE AGREGAR")
            msg_boxes.alert_msgbox_2("¡Error!","¡Primero debe agregar la Linea de Transmisión!")
        else:        
            from controllers.new_window_linea_tramo import NewBookWindow
            codCentral= self.inputCodigo.text()
            window= NewBookWindow(self,codCentral)
            window.exec_()

        
        

    # def open_add_generadores(self):
    #     from controllers.new_window_central_generador import NewBookWindow
    #     window= NewBookWindow(self)
    #     window.show()

    
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

        inputNodoSalida = self.inputNodoSalida.text()
        inputNodoSalida=inputNodoSalida.strip()

        inputNodoLlegada = self.inputNodoLlegada.text()
        inputNodoLlegada=inputNodoLlegada.strip()

        inputCeldaSalida = self.inputCeldaSalida.text()
        inputCeldaSalida=inputCeldaSalida.strip()

        inputCeldaLlegada = self.inputCeldaLlegada.text()
        inputCeldaLlegada=inputCeldaLlegada.strip()



        cbTipo = self.cbTipo.currentText()


        self.label_advertencia_dni.hide()

        #self.ActualizarVisitante(dni,visitante)
        if self.check_inputs():
            #new_path = shutil.copy(path, "book_files")
            self.label_nota_obligatoria.hide()
            data = (self.Usuario,inputCodigo,inputNombre,cbTipo,inputTension,inputNodoSalida,inputNodoLlegada,inputCeldaSalida,inputCeldaLlegada) 
            
            if insert_book_linea_transmision(data):
                #self.clean_inputs()
                msg_boxes.correct_msgbox("¡Registro Exitoso!","¡Se registró exitosamente!")
                self.inputCodigo.setEnabled(False)
                self.parent.refresh_table_from_child_window_linea() 
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


    #def populate_comboboxPiso(self):
    #    cb_options = ("","SÓTANO 1", "SÓTANO 2", "SÓTANO 3", "SÓTANO 4", "1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26")
    #    self.comboBoxPiso.addItems(cb_options)
    #

    

    
    def config_comboBoxes(self):
        font1 = QFont()
        font1.setPointSize(12)
        
    def FilaSeleccionadaInterruptores(self):
        print("ENTRO A DOUBLE CLICK!")
        from controllers.new_window_linea_tramo import NewBookWindow
        selected_row = self.tableInterruptores.selectedItems()

        if selected_row:
            book_id = str(selected_row[1].text())
            window= NewBookWindow(self,self.inputCodigo.text(),book_id)
        window.exec_()
        
        self.tableInterruptores.clearSelection()
    
    def FilaSeleccionadaEstructura(self):
        print("ENTRO A DOUBLE CLICK!")
        from controllers.new_window_linea_estructura import NewBookWindow
        selected_row = self.tableSeccionadores.selectedItems()

        if selected_row:
            book_id = str(selected_row[1].text())
            window= NewBookWindow(self,self.inputCodigo.text(),book_id)
        window.exec_()
        
        self.tableSeccionadores.clearSelection()
    
    

    def table_config_tramo_linea(self):
        column_headers = ("#","Código")
        self.tableInterruptores.setColumnCount(len(column_headers))
        self.tableInterruptores.setHorizontalHeaderLabels(column_headers)
        
        stylesheet = "::section{Background-color:#114692;border:1px solid black;color: white;}"
        self.tableInterruptores.horizontalHeader().setStyleSheet(stylesheet)
        self.tableInterruptores.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableInterruptores.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableInterruptores.setStyleSheet("QTableWidget{ gridline-color:black;alternate-background-color: #E2DED0;}")
        self.tableInterruptores.setAlternatingRowColors(True)
        #self.tableInterruptores.color


    def table_config_estructura(self):
        column_headers = ("#","Código")
        self.tableSeccionadores.setColumnCount(len(column_headers))
        self.tableSeccionadores.setHorizontalHeaderLabels(column_headers)
        self.tableSeccionadores.setSelectionMode(QAbstractItemView.SingleSelection)
        stylesheet = "::section{Background-color:#114692;border:1px solid black;color: white;}"
        self.tableSeccionadores.horizontalHeader().setStyleSheet(stylesheet)

        self.tableSeccionadores.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableSeccionadores.setStyleSheet("QTableWidget{ gridline-color:black;alternate-background-color: #E2DED0;}")
        self.tableSeccionadores.setAlternatingRowColors(True)
        #self.tableGeneradores.color
    
    def populate_table_tramo_linea(self,data):
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

    def populate_table_estructura(self,data):
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

    def refresh_table_from_child_window(self):
        print("REFRESH FROM CHILD...")
        print("REFRESH1")
        data = select_cod_estructura(self.inputCodigo.text())
        data2 = select_cod_tramo_linea(self.inputCodigo.text())
        
        print("REFRESH2")
        self.populate_table_estructura(data)
        self.populate_table_tramo_linea(data2)
    
    def populate_inputs(self, cod_linea):
        conn = None
        try:
            conn = sqlite3.connect('DATABASEAPP.db')
            print("Conexión a la base de datos correcta.")
        except Error as e:
            print("Error al conectar a la base de datos: " + str(e))
            
        if conn:
            try:
                cur = conn.cursor()

                # Consulta a la tabla Linea_Transmision
                sql = """SELECT COD_LINEA, NOMBRE, TIPO_SISTEMA, TENSION_NOM, NODO_SALIDA, NODO_LLEGADA, CELDA_SALIDA, CELDA_LLEGADA, COD_EMP
                        FROM Linea_Transmision 
                        WHERE COD_LINEA = ?"""
                cur.execute(sql, (cod_linea,))
                row = cur.fetchone()
                if row:
                    self.inputCodEmpresa.setText(str(row[8]))
                    self.inputCodigo.setText(str(row[0]))
                    self.inputNombre.setText(str(row[1]))
                    self.cbTipo.setCurrentText(str(row[2]))
                    self.inputTension.setText(str(row[3]))
                    self.inputNodoSalida.setText(str(row[4]))
                    self.inputNodoLlegada.setText(str(row[5]))
                    self.inputCeldaSalida.setText(str(row[6]))
                    self.inputCeldaLlegada.setText(str(row[7]))

            except Error as e:
                print("Error al consultar la base de datos: " + str(e))
            finally:
                cur.close()
                conn.close()

    def populate_combobox(self):
        # Llenar el combo de Tipo
        cb_options_tipo = ("", "Interconectado", "Aislado")
        self.cbTipo.addItems(cb_options_tipo)


    def remove_book_tramo(self):
        selected_row = self.tableInterruptores.selectedItems()
        print("SELECT ROWWWWW: "+str(selected_row))
        if len(selected_row)!=0:
            respuesta=msg_boxes.alert_msgbox("Corfirmar Eliminar","¿Estas seguro de eliminar el registro?")
            if respuesta== QMessageBox.Yes:
                if selected_row:
                    book_id = str(selected_row[1].text())
                    row = selected_row[1].row()

                    if delete_book_Tramo_Linea_Transmision(book_id):
                    
                        self.tableInterruptores.removeRow(row)

    def remove_book_estructura(self):
        selected_row = self.tableSeccionadores.selectedItems()
        print("SELECT ROWWWWW: "+str(selected_row))
        if len(selected_row)!=0:
            respuesta=msg_boxes.alert_msgbox("Corfirmar Eliminar","¿Estas seguro de eliminar el registro?")
            if respuesta== QMessageBox.Yes:
                if selected_row:
                    book_id = str(selected_row[1].text())
                    row = selected_row[1].row()

                    if delete_book_Estructura(book_id):
                    
                        self.tableSeccionadores.removeRow(row)