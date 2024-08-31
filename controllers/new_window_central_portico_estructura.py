from PySide2.QtWidgets import QDialog, QWidget, QFileDialog,QCompleter
from PySide2.QtCore import Qt, QDate
from PySide2.QtGui import *
import sqlite3
from sqlite3 import Error
from views.new_central_portico_estructura import Ui_NewBook
from db.books import buscar_usuario_acceso,insert_book_portico_central_generacion_estructura
from PySide2 import QtCore
from pys2_msgboxes import msg_boxes
from datetime import date, datetime



class NewBookWindow(QDialog,Ui_NewBook):
    def __init__(self, parent=None,_codPortico=None,_codCentral=None,_codigo=None):
        self._codCentral=_codCentral
        super().__init__(parent)
        self.parent = parent
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)
        self.Usuario= buscar_usuario_acceso();
        self.label.setStyleSheet("background-color: #114692;")
        self.label_advertencia_dni.hide()
        if _codigo is not None:
            print("----------NO ES EDIT-----------:"+str(_codigo))
            self.populate_inputs(_codigo)
            self.inputCodigo.setText(str(_codigo))
            self.inputCodigo.setEnabled(False)
            self.addButton.setText("GUARDAR")
        
        self.inputNombre.setText(str(_codCentral))
        self.inputNombre.setEnabled(False)

        self.inputPortico.setText(str(_codPortico))
        self.inputPortico.setEnabled(False)
        #self.populate_combobox()

        self.addButton.clicked.connect(self.add_book)
        self.cancelButton.clicked.connect(self.close)



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

        inputCodigoCentral = self.inputNombre.text()
        inputCodigoCentral=inputCodigoCentral.strip()

        inputPortico = self.inputPortico.text()
        inputPortico=inputPortico.strip()

        inputAltura = self.inputAltura.text()
        inputAltura=inputAltura.strip()

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
            
            data = (self.Usuario,inputCodigoCentral,inputPortico,inputCodigo,inputAltura,inputX, inputY,inputZ) 
            if insert_book_portico_central_generacion_estructura(data):
                #self.clean_inputs()
                msg_boxes.correct_msgbox("¡Registro Exitoso!","¡Se registró exitosamente!")
                self.inputCodigo.setEnabled(False)
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
        
    def populate_inputs(self, cod_estructura):
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

                # Consulta a la tabla Portico_Central_Generacion_Estructura
                sql = """SELECT COD_CENTRAL, COD_PORTICO, COD_ESTRUCTURA, ALTURA, X, Y, Z 
                        FROM Portico_Central_Generacion_Estructura 
                        WHERE COD_ESTRUCTURA = ?"""
                cur.execute(sql, (cod_estructura,))
                row = cur.fetchone()
                if row:
                    self.inputNombre.setText(str(row[0]))
                    self.inputPortico.setText(str(row[1]))
                    self.inputCodigo.setText(str(row[2]))
                    self.inputAltura.setText(str(row[3]))
                    self.inputX.setText(str(row[4]))
                    self.inputY.setText(str(row[5]))
                    self.inputZ.setText(str(row[6]))

            except Error as e:
                print("Error al consultar la base de datos: " + str(e))
            finally:
                cur.close()
                conn.close()
