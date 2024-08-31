from PySide2.QtWidgets import QMessageBox, QDialog,QAbstractItemView, QWidget, QFileDialog,QCompleter,QHeaderView,QTableWidgetItem
from PySide2.QtCore import Qt, QDate
from PySide2.QtGui import *
import sqlite3
from sqlite3 import Error
from views.new_central_portico import Ui_NewBook
from db.books import buscar_usuario_acceso,delete_book_Portico_Central_Generacion_Estructura,select_cod_estructura_portico,insert_book_portico_central_generacion,insert_book_portico_central_generacion_travesanio
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
        self.label.setStyleSheet("background-color: #114692;")
        
        self.btnAddEstructura.clicked.connect(self.open_new_window_estructura)
        #self.btnAddTravesanio.clicked.connect(self.open_new_window_travesanio)
        self.inputCentral.setText(str(_codCentral))
        self.Usuario= buscar_usuario_acceso();
        self.inputCentral.setEnabled(False)
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
        
        self.btnDeleteEstructura.clicked.connect(self.remove_book_estructura)

        self.addButton.clicked.connect(self.add_book)
        self.cancelButton.clicked.connect(self.close)

        self.table_config_estructuras()
        self.populate_table_estructura(select_cod_estructura_portico(_codCentral,_codigo))

        
        self.tableEstructura.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableEstructura.verticalHeader().setVisible(False)
        self.tableEstructura.setColumnWidth(0,19)
        headerVertical = self.tableEstructura.verticalHeader()
        headerVertical.resizeSections(QHeaderView.ResizeToContents)
        headerVertical.setStretchLastSection(True)
        self.tableEstructura.doubleClicked.connect(lambda: self.FilaSeleccionadaEstructura())


    def open_new_window_estructura(self):
        if(self.inputCodigo.isEnabled()):
            print("DEBE AGREGAR")
            msg_boxes.alert_msgbox_2("¡Error!","¡Primero debe agregar la Central de Generación!")
        else:        
            from controllers.new_window_central_portico_estructura import NewBookWindow
            codPortico= self.inputCodigo.text()
            codCentral= self.inputCentral.text()
            window= NewBookWindow(self,codPortico,codCentral)
            window.exec_()
    def open_new_window_travesanio(self):
        from controllers.new_window_central_portico_travesanio import NewBookWindow
        window= NewBookWindow(self)
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

        inputCentral = self.inputCentral.text()
        inputCentral=inputCentral.strip()

        inputAltura = self.inputAltura.text()
        inputAltura=inputAltura.strip()

        inputFecha = self.inputFecha.text()
        inputFecha=inputFecha.strip()

        inputAltura_2 = self.inputAltura_2.text()
        inputAltura_2=inputAltura_2.strip()

        inputEstructura = self.inputEstructura.text()
        inputEstructura=inputEstructura.strip()

        inputEstructura2 = self.inputEstructura2.text()
        inputEstructura2=inputEstructura2.strip()

        cbTipo = self.cbTipo.currentText()
        cbEstado=self.cbEstado.currentText()

        self.label_advertencia_dni.hide()

        #self.ActualizarVisitante(dni,visitante)
        if self.check_inputs():
            #new_path = shutil.copy(path, "book_files")
            self.label_nota_obligatoria.hide()
            data = (self.Usuario,inputCentral,inputCodigo,cbTipo,inputAltura,cbEstado,inputFecha) 
            
            if insert_book_portico_central_generacion(data):
                data2 = (self.Usuario,inputCentral,inputCodigo,inputAltura_2,inputEstructura,inputEstructura2) 
                insert_book_portico_central_generacion_travesanio(data2)
                #self.clean_inputs()
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

    def populate_table_estructura(self,data):
        if data is not None:
            self.tableEstructura.setRowCount(len(data))
            print("REFRESH4")
            for index_row, row in enumerate(data):
                # Incrementamos el índice de fila en 1 para comenzar con el número de orden en 1
                order_number = index_row + 1
                
                # Establecemos el número de orden en la primera columna
                self.tableEstructura.setItem(index_row, 0, QTableWidgetItem(str(order_number)))
                
                for index_cell, cell in enumerate(row):
                    # Llenamos los datos de la fila a partir de la segunda columna
                    self.tableEstructura.setItem(index_row, index_cell + 1, QTableWidgetItem(str(cell)))
                    
                    if index_cell == 13:
                        itemx = self.tableEstructura.item(index_row, index_cell + 1)  # Se ajusta el índice de la celda
                        print("EL ITEM ACTUAL ES: ", itemx)
                        if itemx.text() == "PENDIENTE":
                            itemx.setForeground(QBrush(QColor(255, 0, 0)))
                        else:
                            itemx.setForeground(QBrush(QColor(0, 0, 255)))

            print("REFRESH5")
            headerVertical = self.tableEstructura.verticalHeader()
            headerVertical.resizeSections(QHeaderView.ResizeToContents)
            headerVertical.setStretchLastSection(True)

            #self.records_qty()
        else:
            print("¡Error! No se cargaron los datos correctamente.")
    
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
                
        if conn:
            try:
                cur = conn.cursor()
                # Consulta a la tabla Portico_Central_Generacion
                sql = f"SELECT * FROM Portico_Central_Generacion WHERE COD_PORTICO = ?"
                cur.execute(sql, (book_id,))
                row = cur.fetchone()
                if row:
                    # Obtener los valores de la fila
                    inputCodEmpresa = str(row[0])
                    inputCodigo = str(row[2])
                    inputCentral = str(row[1])
                    inputAltura = str(row[4])
                    cbTipo = str(row[3])
                    cbEstado = str(row[5])
                    inputFecha = str(row[6])

                    # Poblar los campos de entrada de la tabla Portico_Central_Generacion
                    self.inputCodEmpresa.setText(inputCodEmpresa)
                    self.inputCodigo.setText(inputCodigo)
                    self.inputCentral.setText(inputCentral)
                    self.inputAltura.setText(inputAltura)
                    fechaConv = inputFecha
                    fechaConv2 = fechaConv.replace("/", "-")
                    qdate = QDate.fromString(fechaConv2, "d-MM-yyyy")
                    self.inputFecha.setDate(qdate)
                    self.cbTipo.setCurrentText(cbTipo)
                    self.cbEstado.setCurrentText(cbEstado)

                    # Consulta a la tabla Portico_Central_Generacion_Travesanio
                    sql_travesanio = f"SELECT * FROM Portico_Central_Generacion_Travesano WHERE COD_PORTICO = ?"
                    cur.execute(sql_travesanio, (book_id,))
                    row_travesanio = cur.fetchone()
                    if row_travesanio:
                        # Obtener los valores de la fila
                        inputAltura_2 = str(row_travesanio[3])
                        inputEstructura = str(row_travesanio[4])
                        inputEstructura2 = str(row_travesanio[5])

                        # Poblar los campos de entrada de la tabla Portico_Central_Generacion_Travesanio
                        self.inputAltura_2.setText(inputAltura_2)
                        self.inputEstructura.setText(inputEstructura)
                        self.inputEstructura2.setText(inputEstructura2)

            except Error as e:
                print("Error al obtener detalles del libro:", str(e))
            finally:
                if conn:
                    conn.close()


    def populate_combobox(self):
        # Llenar el combo de Tipo de Pórtico
        cb_options_tipo_portico = ("", "Postes de Concreto y Acero", "Postes de Concreto", "Postes de Madera","Torres de Acero","Postes de Acero","Postes de Madera y Acero","Instalación Subterránea","Sin Estructura o Red Compartida")
        self.cbTipo.addItems(cb_options_tipo_portico)

        # Llenar el combo de Estado
        cb_options_estado = ("", "Nuevo", "Existente", "Eliminado", "Modificado", "Proyectado")
        self.cbEstado.addItems(cb_options_estado)

    def refresh_table_from_child_window(self):
        print("REFRESH FROM CHILD...")
        print("REFRESH1")
        data = select_cod_estructura_portico(self.inputCentral.text(),self.inputCodigo.text())
        print("REFRESH2")
        self.populate_table_estructura(data)

    def table_config_estructuras(self):
        column_headers = ("#","Código","Altura","X","Y","Z")
        self.tableEstructura.setColumnCount(len(column_headers))
        self.tableEstructura.setHorizontalHeaderLabels(column_headers)
        self.tableEstructura.setSelectionMode(QAbstractItemView.SingleSelection)
        stylesheet = "::section{Background-color:#114692;border:1px solid black;color: white;}"
        self.tableEstructura.horizontalHeader().setStyleSheet(stylesheet)

        self.tableEstructura.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableEstructura.setStyleSheet("QTableWidget{ gridline-color:black;alternate-background-color: #E2DED0;}")
        self.tableEstructura.setAlternatingRowColors(True)

    def FilaSeleccionadaEstructura(self):
        print("ENTRO A DOUBLE CLICK!")
        from controllers.new_window_central_portico_estructura import NewBookWindow
        selected_row = self.tableEstructura.selectedItems()

        if selected_row:
            book_id = str(selected_row[1].text())
            window= NewBookWindow(self,self.inputCodigo.text(),self.inputCentral.text(),book_id)
        window.exec_()
        
        self.tableEstructura.clearSelection()

    def remove_book_estructura(self):
        selected_row = self.tableEstructura.selectedItems()
        print("SELECT ROWWWWW: "+str(selected_row))
        if len(selected_row)!=0:
            respuesta=msg_boxes.alert_msgbox("Corfirmar Eliminar","¿Estas seguro de eliminar el registro?")
            if respuesta== QMessageBox.Yes:
                if selected_row:
                    book_id = str(selected_row[1].text())
                    row = selected_row[1].row()

                    if delete_book_Portico_Central_Generacion_Estructura(book_id):
                    
                        self.tableEstructura.removeRow(row)