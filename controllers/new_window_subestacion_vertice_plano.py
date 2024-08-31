from PySide2.QtWidgets import QMessageBox,QDialog,QPushButton, QHeaderView,QTableWidgetItem,QAbstractItemView,QWidget, QFileDialog,QCompleter
from PySide2.QtCore import Qt, QDate
from PySide2.QtGui import *
from views.new_transmision_subestacion_plano import Ui_NewBook
from db.books import delete_plano_subestacion,buscar_usuario_acceso,insert_book_subestacion_plano_planta,select_plano_subestacion
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
        self.Usuario= buscar_usuario_acceso();
        self.label.setStyleSheet("background-color: #114692;")
#       
    
        self.btnAddPlano.clicked.connect(self.add_book)
        
        self.table_config()
        self.populate_table(select_plano_subestacion(self._codCentral))
        self.btnDeletePlano.clicked.connect(self.remove_book)
        self.cancelButton.clicked.connect(self.close)

    def remove_book(self):
        selected_row = self.tablePlano.selectedItems()
        print("SELECT ROWWWWW: "+str(selected_row))
        if len(selected_row)!=0:
            respuesta=msg_boxes.alert_msgbox("Corfirmar Eliminar","¿Estas seguro de eliminar el registro?")
            if respuesta== QMessageBox.Yes:
                if selected_row:
                    book_id = str(selected_row[1].text())
                    row = selected_row[1].row()
                    if delete_plano_subestacion(self.Usuario,self._codCentral,book_id):
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

        data = select_plano_subestacion(self._codCentral)
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
            self.label_nota_obligatoria.hide()
            data = (self.Usuario,inputCodigoCentral,inputSecuencia,inputX,inputY,inputZ) 
            
            if insert_book_subestacion_plano_planta(data):
                self.clean_inputs_vertices()
                msg_boxes.correct_msgbox("¡Registro Exitoso!","¡Se registró exitosamente!")
                
                #self.parent.refresh_table_from_child_window()
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