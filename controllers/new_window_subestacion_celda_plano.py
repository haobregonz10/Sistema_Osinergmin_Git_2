from PySide2.QtWidgets import QMessageBox,QDialog,QHeaderView,QTableWidgetItem,QAbstractItemView,QPushButton, QWidget, QFileDialog,QCompleter
from PySide2.QtCore import Qt, QDate
from PySide2.QtGui import *
from views.new_transmision_celda_ubicacion_plano import Ui_NewBook
from db.books import delete_plano_celda_subestacion,buscar_usuario_acceso,insert_book_celda_plano_planta,select_plano_celda_subestacion
from PySide2 import QtCore
from pys2_msgboxes import msg_boxes
from datetime import date, datetime



class NewBookWindow(QDialog,Ui_NewBook):
    def __init__(self, parent=None,_codCelda=None,_codCentral=None,_codigo=None):
        self._codCentral=_codCentral
        super().__init__(parent)
        self.parent = parent
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)
        self.Usuario= buscar_usuario_acceso();
        self.label.setStyleSheet("background-color: #114692;")
        #self.label_advertencia_dni.hide()
        #self.label_nota_obligatoria.hide()
        if _codigo is not None:
            print("----------NO ES EDIT-----------:"+str(_codigo))
            self.populate_inputs(_codigo)
            self.inputCodigo.setText(str(_codigo))
            self.inputCodigo.setEnabled(False)
            self.btnAddPlano.setText("GUARDAR")
        self.btnAddPlano.clicked.connect(self.add_book)
        #self.btnAddEsquema.clicked.connect(self.open_new_window_coordenadas)
        #self.btnAddPlanta.clicked.connect(self.open_new_window_plano)
        self.btnDeletePlano.clicked.connect(self.remove_book)
        self.cancelButton.clicked.connect(self.close)
        
        self.inputCodigo.setText(str(_codCentral))
        self.inputCodigo.setEnabled(False)

        self.inputCelda.setText(str(_codCelda))
        self.inputCelda.setEnabled(False)

        self.table_config()
        self.populate_table(select_plano_celda_subestacion(self._codCentral,self.inputCelda.text()))
    
    def remove_book(self):
        selected_row = self.tablePlano.selectedItems()
        print("SELECT ROWWWWW: "+str(selected_row))
        if len(selected_row)!=0:
            respuesta=msg_boxes.alert_msgbox("Corfirmar Eliminar","¿Estas seguro de eliminar el registro?")
            if respuesta== QMessageBox.Yes:
                if selected_row:
                    book_id = str(selected_row[1].text())
                    row = selected_row[1].row()

                    if delete_plano_celda_subestacion(self.Usuario,self._codCentral,self.inputCelda.text(),book_id):
                    
                        self.tablePlano.removeRow(row)
    def table_config(self):
        column_headers = ("#","Secuencia","X","Y","Z")
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

    def populate_table(self,data):
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
    def refresh_table_from_child_window(self):

        data = select_plano_celda_subestacion(self._codCentral,self.inputCelda.text())
        self.populate_table(data)











    def check_inputs(self):


        inputSecuencia = self.inputSecuencia.text()
        inputSecuencia=inputSecuencia.strip()

        inputX = self.inputX.text()
        inputX=inputX.strip()

        inputY = self.inputY.text()
        inputY=inputY.strip()

        
        errors_count = 0
        
        #if inputSecuencia == "":
        #    self.label_advertencia_dni.show()
        #    self.label_advertencia_dni.show()
        #    print("El campo aquienvisita es obligatorio")
        #    errors_count +=1
        #else:
        #    self.label_advertencia_dni.hide()
#
        #if inputX == "":
        #    print("El campo areavisitada es obligatorio")
        #    self.label_advertencia_dni.show()
        #    self.label_advertencia_dni.show()
        #    errors_count +=1
        #else:
        #    self.label_advertencia_dni.hide()

        if errors_count==0:
            return (True)

    def add_book(self):
        

        inputCodigo = self.inputCodigo.text()
        inputCodigo=inputCodigo.strip()
        
        inputCelda = self.inputCelda.text()
        inputCelda=inputCelda.strip()

        inputSecuencia = self.inputSecuencia.text()
        inputSecuencia=inputSecuencia.strip()

        inputX = self.inputX.text()
        inputX=inputX.strip()

        inputY = self.inputY.text()
        inputY=inputY.strip()

        inputZ = self.inputZ.text()
        inputZ=inputZ.strip()
        #self.label_advertencia_dni.hide()

        #self.ActualizarVisitante(dni,visitante)
        if self.check_inputs():
            #new_path = shutil.copy(path, "book_files")
            #self.label_nota_obligatoria.hide()
            data = (self.Usuario,inputCodigo,inputCelda,inputSecuencia,inputX,inputY,inputZ) 
            
            if insert_book_celda_plano_planta(data):
                self.clean_inputs_vertices()
                msg_boxes.correct_msgbox("¡Registro Exitoso!","¡Se registró exitosamente!")
                self.inputCodigo.setEnabled(False)
                self.refresh_table_from_child_window()
                #self.close()
            else: 
                print("ERROR EN EL REGISTRO!")
            '''
            if(len(dni)!=8):
                self.label_advertencia_dni.show()
                self.ast_dni.show()
            else:
            '''    
    def clean_inputs_vertices(self):
        self.inputSecuencia.clear()
        self.inputX.clear()
        self.inputY.clear()
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
        
        #line_editcomboBoxAreaVisitada = self.comboBoxAreaVisitada.lineEdit()  
        #line_editcomboBoxAreaVisitada.setFont(font1)

        #line_editcomboBoxPiso = self.comboBoxPiso.lineEdit()  
        #line_editcomboBoxPiso.setFont(font1)

        #line_editcomboBoxEstado = self.comboBoxEstado.lineEdit()  
        #line_editcomboBoxEstado.setFont(font1)
        #line_edit.setAlignment(QtCore.Qt.AlignCenter)

    #def to_upperTitle(self, txt):
    #    pos2=self.titleLineEdit.cursorPosition()
    #    self.titleLineEdit.setText(txt.upper())
    #    self.titleLineEdit.setCursorPosition(pos2)
    #
    
    

    
    #def AnadirNuevos(self, dni,visitante,entidadempresa,motivovisita,aquienvisita,autoriza,areavisitada):
    #    if (ExisteDni(dni)):
    #        print("DNI SI EXISTE!")
    #    else:
    #        print("DNI NO EXISTE!")
    #        insert_NuevoDNI(dni,visitante)
    #    
    #    if (ExisteEntidad(entidadempresa)):
    #        print("Entidad SI EXISTE!")
    #    else:
    #        print("Entidad NO EXISTE!")
    #        insert_NuevoEntidad(entidadempresa) 
    #    
    #    if (ExisteMotivo(motivovisita)):
    #        print("Motivo SI EXISTE!")
    #    else:
    #        print("Motivo NO EXISTE!")
    #        insert_NuevoMotivo(motivovisita) 
    #    
    #    if (ExisteVisita(aquienvisita)):
    #        print("Visita SI EXISTE!")
    #    else:
    #        print("Visita NO EXISTE!")
    #        insert_NuevoVisita(aquienvisita) 
#
    #    if (ExisteAutoriza(autoriza)):
    #        print("Autoriza SI EXISTE!")
    #        UpdateAutoriza(autoriza,areavisitada)
    #    else:
    #        print("Autoriza NO EXISTE!")
    #        insert_NuevoAutoriza(autoriza,areavisitada)    

    #def ObtenerHoraActual(self):
    #    now = datetime.now()
    #    current_time = now.strftime("%H:%M")
    #    print("Current Time =", current_time)
    #    return current_time
    
    #def ActualizarVisitante(self,dni,visitante):
    #    nombreEncontrado= EncontrarDni(dni)
    #    if nombreEncontrado==visitante:
    #        print("No hay nada que actualizar")
    #    else:
    #        print("NOMBRE NUEVO:: "+visitante)
    #        UpdateVisitante(dni,visitante)
    #        print("Actualizado!!!")

    

    