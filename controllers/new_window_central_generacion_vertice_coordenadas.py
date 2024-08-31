from PySide2.QtWidgets import QMessageBox,QDialog,QPushButton, QHeaderView,QTableWidgetItem,QAbstractItemView,QWidget, QFileDialog,QCompleter
from PySide2.QtCore import Qt, QDate
from PySide2.QtGui import *
from views.new_central_generacion_vertice_coordenadas import Ui_NewBook
from db.books import delete_geografica_central,buscar_usuario_acceso,insert_book_central_generacion_coordenadas,select_geografica_central
from PySide2 import QtCore
from pys2_msgboxes import msg_boxes
from datetime import date, datetime

class NewBookWindow(QDialog,Ui_NewBook):
    def __init__(self, parent=None,_codCentral=None):
        self._codCentral=_codCentral
        super().__init__(parent)
        self.parent = parent
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)
        self.Usuario= buscar_usuario_acceso();
        self.inputCodigoCentral.setText(str(_codCentral))
        self.inputCodigoCentral.setEnabled(False)
        #self.populate_comboboxPiso()
        self.label_advertencia_dni.hide()
        self.btnAgregar.clicked.connect(self.add_book)
        self.label.setStyleSheet("background-color: #114692;")
        
        self.btnEliminar.clicked.connect(self.remove_book)
        #self.addButton.clicked.connect(self.add_book)
        self.cancelButton.clicked.connect(self.close)

        self.table_config()
        self.populate_table(select_geografica_central(self._codCentral))
    
    def remove_book(self):
        selected_row = self.tableVertices.selectedItems()
        print("SELECT ROWWWWW: "+str(selected_row))
        if len(selected_row)!=0:
            respuesta=msg_boxes.alert_msgbox("Corfirmar Eliminar","¿Estas seguro de eliminar el registro?")
            if respuesta== QMessageBox.Yes:
                if selected_row:
                    book_id = str(selected_row[1].text())
                    row = selected_row[1].row()

                    if delete_geografica_central(self.Usuario,self._codCentral,book_id):
                    
                        self.tableVertices.removeRow(row)
                    

    def table_config(self):
        column_headers = ("#","Secuencia","X","Y","Z")
        self.tableVertices.setColumnCount(len(column_headers))
        self.tableVertices.setHorizontalHeaderLabels(column_headers)
        self.tableVertices.setSelectionMode(QAbstractItemView.SingleSelection)
        stylesheet = "::section{Background-color:#114692;border:1px solid black;color: white;}"
        self.tableVertices.horizontalHeader().setStyleSheet(stylesheet)

        self.tableVertices.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableVertices.setStyleSheet("QTableWidget{ gridline-color:black;alternate-background-color: #E2DED0;}")
        self.tableVertices.setAlternatingRowColors(True)

        self.tableVertices.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableVertices.verticalHeader().setVisible(False)
        self.tableVertices.setColumnWidth(0,19)
        headerVertical = self.tableVertices.verticalHeader()
        headerVertical.resizeSections(QHeaderView.ResizeToContents)
        headerVertical.setStretchLastSection(True)

    def populate_table(self,data):
        if data is not None:
            self.tableVertices.setRowCount(len(data))
            print("REFRESH4")
            for index_row, row in enumerate(data):
                # Incrementamos el índice de fila en 1 para comenzar con el número de orden en 1
                order_number = index_row + 1
                
                # Establecemos el número de orden en la primera columna
                self.tableVertices.setItem(index_row, 0, QTableWidgetItem(str(order_number)))
                
                for index_cell, cell in enumerate(row):
                    # Llenamos los datos de la fila a partir de la segunda columna
                    self.tableVertices.setItem(index_row, index_cell + 1, QTableWidgetItem(str(cell)))
                    
                    if index_cell == 13:
                        itemx = self.tableVertices.item(index_row, index_cell + 1)  # Se ajusta el índice de la celda
                        print("EL ITEM ACTUAL ES: ", itemx)
                        if itemx.text() == "PENDIENTE":
                            itemx.setForeground(QBrush(QColor(255, 0, 0)))
                        else:
                            itemx.setForeground(QBrush(QColor(0, 0, 255)))

            print("REFRESH5")
            headerVertical = self.tableVertices.verticalHeader()
            headerVertical.resizeSections(QHeaderView.ResizeToContents)
            headerVertical.setStretchLastSection(True)

            #self.records_qty()
        else:
            print("¡Error! No se cargaron los datos correctamente.")
    def refresh_table_from_child_window(self):

        data = select_geografica_central(self._codCentral.text())
        self.populate_table(data)



    def check_inputs(self):
        

        inputCodigoCentral = self.inputCodigoCentral.text()
        inputCodigoCentral=inputCodigoCentral.strip()

        inputSecuencia = self.inputSecuencia.text()
        inputSecuencia=inputSecuencia.strip()

        inputX = self.inputX.text()
        inputX=inputX.strip()

        inputY = self.inputY.text()
        inputY=inputY.strip()

        inputZ = self.inputZ.text()
        inputZ=inputZ.strip()

        
        errors_count = 0
        
        if inputSecuencia == "":
            self.label_advertencia_dni.show()
            self.label_advertencia_dni.show()
            print("El campo aquienvisita es obligatorio")
            errors_count +=1
        else:
            self.label_advertencia_dni.hide()

        if inputX == "":
            print("El campo areavisitada es obligatorio")
            self.label_advertencia_dni.show()
            self.label_advertencia_dni.show()
            errors_count +=1
        else:
            self.label_advertencia_dni.hide()

        if errors_count==0:
            return (True)


    def add_book(self):

        inputCodigoCentral = self.inputCodigoCentral.text()
        inputCodigoCentral=inputCodigoCentral.strip()

        inputSecuencia = self.inputSecuencia.text()
        inputSecuencia=inputSecuencia.strip()

        inputX = self.inputX.text()
        inputX=inputX.strip()

        inputY = self.inputY.text()
        inputY=inputY.strip()

        inputZ = self.inputZ.text()
        inputZ=inputZ.strip()

        

        self.label_advertencia_dni.hide()

        #self.ActualizarVisitante(dni,visitante)
        if self.check_inputs():
            #new_path = shutil.copy(path, "book_files")
            data = (self.Usuario,inputCodigoCentral,inputSecuencia,inputX,inputY,inputZ) 
            
            if insert_book_central_generacion_coordenadas(data):
                self.clean_inputs_vertices()
                msg_boxes.correct_msgbox("¡Registro Exitoso!","¡Se registró exitosamente!")
                self.populate_table(select_geografica_central(self._codCentral))
                #self.parent.refresh_table_from_child_window()
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
        self.inputZ.clear()
        
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

    

    