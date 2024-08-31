from PySide2.QtWidgets import QDialog,QPushButton, QWidget, QFileDialog,QCompleter
from PySide2.QtCore import Qt, QDate
from PySide2.QtGui import *
import sqlite3
from sqlite3 import Error
from views.new_central_generador import Ui_NewBook
from db.books import buscar_usuario_acceso,insert_book_central_generador,insert_book_central_generador_planta,insert_book_central_generador_ubicacion_esquema
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
        if _codigo is not None:
            print("----------NO ES EDIT-----------:"+str(_codigo))
            self.populate_inputs(_codigo)
            self.inputCodigo.setText(str(_codigo))
            self.inputCodigo.setEnabled(False)
            self.addButton.setText("GUARDAR")

        self.addButton.clicked.connect(self.add_book)
#
        self.label_advertencia_dni.hide()
        self.label_nota_obligatoria.hide()
        #self.addButton.clicked.connect(self.add_book)
        self.cancelButton.clicked.connect(self.close)
    def open_new_window_coordenadas(self):
        from controllers.new_window_central_generador_ubicacion_esquema import NewBookWindow
        window= NewBookWindow(self)
        window.show()
    def open_new_window_plano(self):
        from controllers.new_window_central_generador_ubicacion_plano import NewBookWindow
        window= NewBookWindow(self)
        window.show()
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

        inputNombre = self.inputNombre.text()
        inputNombre=inputNombre.strip()

        inputPotencia = self.inputPotencia.text()
        inputPotencia=inputPotencia.strip()

        inputTension = self.inputTension.text()
        inputTension=inputTension.strip()

        
        
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

        inputPotencia = self.inputPotencia.text()
        inputPotencia=inputPotencia.strip()

        inputTension = self.inputTension.text()
        inputTension=inputTension.strip()

        inputFecha = self.inputFecha.text()
        inputFecha=inputFecha.strip()

        cbTurbina = self.cbTurbina.currentText()
        cbEstado=self.cbEstado.currentText()
  
        inputANG = self.inputANG.text()
        inputANG=inputANG.strip()

        inputX = self.inputX.text()
        inputX=inputX.strip()

        inputY = self.inputY.text()
        inputY=inputY.strip()

        inputZ = self.inputZ.text()
        inputZ=inputZ.strip()

        inputANG_2 = self.inputANG_2.text()
        inputANG_2=inputANG_2.strip()

        inputX_2 = self.inputX_2.text()
        inputX_2=inputX_2.strip()

        inputY_2 = self.inputY_2.text()
        inputY_2=inputY_2.strip()

        

        self.label_advertencia_dni.hide()

        #self.ActualizarVisitante(dni,visitante)
        if self.check_inputs():
            #new_path = shutil.copy(path, "book_files")
            self.label_nota_obligatoria.hide()
            data = (self.Usuario,inputNombre,inputCodigo,inputPotencia,inputTension,cbTurbina,cbEstado,inputFecha) 
            
            if insert_book_central_generador(data):
                #self.clean_inputs()
                data2 = (self.Usuario, inputNombre, inputCodigo, inputX_2, inputY_2,inputANG_2)
                data3 = (self.Usuario, inputNombre, inputCodigo, inputX, inputY, inputZ, inputANG)

                insert_book_central_generador_ubicacion_esquema(data2)
                insert_book_central_generador_planta(data3)

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
    def populate_combobox(self):
        # Llenar el combo de Tipo de Turbina
        cb_options_turbina = ("", "Pelton", "Francis", "Kaplan", "Turbovapor", "Turbogas")
        self.cbTurbina.addItems(cb_options_turbina)

        # Llenar el combo de Estado
        cb_options_estado = ("", "Nuevo", "Existente", "Eliminado", "Modificado", "Proyectado")
        self.cbEstado.addItems(cb_options_estado)

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
            print("Conexión a la base de datos correcta.ID ES: "+str(book_id))
        except Error as e:
            print("Error al conectar a la base de datos: " + str(e))
                
        if conn:
            try:
                cur = conn.cursor()
                # Consulta a la tabla Generador_Central_Generacion
                sql = f"SELECT * FROM Generador_Central_Generacion WHERE COD_GENERADOR = ?"
                cur.execute(sql, (book_id,))
                row = cur.fetchone()
                if row:
                    # Obtener los valores de la fila
                    inputCodEmpresa = row[0]
                    inputCodigo = row[2]
                    inputNombre = row[1]
                    inputPotencia = row[3]
                    inputTension = row[4]
                    cbTurbina = row[5]
                    cbEstado = row[6]
                    inputFecha = row[7]

                    # Poblar los campos de entrada de la tabla Generador_Central_Generacion
                    self.inputCodEmpresa.setText(str(inputCodEmpresa))
                    self.inputCodigo.setText(str(inputCodigo))
                    self.inputNombre.setText(str(inputNombre))
                    self.inputPotencia.setText(str(inputPotencia))
                    self.inputTension.setText(str(inputTension))
                    self.cbTurbina.setCurrentText(str(cbTurbina))
                    self.cbEstado.setCurrentText(str(cbEstado))
                    
                    print("LA FECHA ESSS: "+inputFecha)
                    fechaConv = inputFecha
                    fechaConv2 = fechaConv.replace("/", "-")
                    qdate = QDate.fromString(fechaConv2, "d-MM-yyyy")
                    self.inputFecha.setDate(qdate)


                    # Consulta a la tabla Generador_Central_Generacion_Ubicacion_Esquema
                    sql_coord = f"SELECT * FROM Generador_Central_Generacion_Ubicacion_Esquema WHERE COD_GENERADOR = ?"
                    cur.execute(sql_coord, (book_id,))
                    row_coord = cur.fetchone()
                    if row_coord:
                        # Obtener los valores de la fila
                        inputANG = row_coord[5]
                        inputX = row_coord[3]
                        inputY = row_coord[4]

                        # Poblar los campos de entrada de la tabla Generador_Central_Generacion_Ubicacion_Esquema
                        self.inputANG_2.setText(str(inputANG))
                        self.inputX_2.setText(str(inputX))
                        self.inputY_2.setText(str(inputY))

                    # Consulta a la tabla Generador_Central_Generacion_Ubicacion_Plano_Planta
                    sql_coord_planta = f"SELECT * FROM Generador_Central_Generacion_Ubicacion_Plano_Planta WHERE COD_GENERADOR = ?"
                    cur.execute(sql_coord_planta, (book_id,))
                    row_coord_planta = cur.fetchone()
                    if row_coord_planta:
                        # Obtener los valores de la fila
                        inputANG_2 = row_coord_planta[6]
                        inputX_2 = row_coord_planta[3]
                        inputY_2 = row_coord_planta[4]
                        inputZ = row_coord_planta[5]

                        # Poblar los campos de entrada de la tabla Generador_Central_Generacion_Ubicacion_Plano_Planta
                        self.inputANG.setText(str(inputANG_2))
                        self.inputX.setText(str(inputX_2))
                        self.inputY.setText(str(inputY_2))
                        self.inputZ.setText(str(inputZ))

            except Error as e:
                print("Error al obtener detalles del libro:", str(e))
            finally:
                if conn:
                    conn.close()
