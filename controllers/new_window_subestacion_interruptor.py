from PySide2.QtWidgets import QDialog, QWidget, QFileDialog,QCompleter
from PySide2.QtCore import Qt, QDate
from PySide2.QtGui import *
import sqlite3
from sqlite3 import Error
from views.new_transmision_interruptor import Ui_NewBook
from db.books import buscar_usuario_acceso,insert_book_transmision_interruptor_ubicacion_esquema,insert_book_transmision_interruptor_ubicacion_plano,insert_book_transmision_interruptor
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
        self.inputSubestacion.setText(str(_codCentral))
        self.inputSubestacion.setEnabled(False)

        self.inputCelda.setText(str(_codCelda))
        self.inputCelda.setEnabled(False)

        self.label_advertencia_dni.hide()
        self.label_nota_obligatoria.hide()
        self.populate_combobox()
        if _codigo is not None:
            print("----------NO ES EDIT-----------:"+str(_codigo))
            self.populate_inputs(_codigo)
            self.inputCodigo.setText(str(_codigo))
            self.inputCodigo.setEnabled(False)
            self.addButton.setText("GUARDAR")
        #self.btnAddEsquema.clicked.connect(self.open_new_window_coordenadas)
        #self.btnAddPlanta.clicked.connect(self.open_new_window_plano)
        #self.populate_comboboxPiso()
        #self.populate_comboboxEstado()
        #self.populate_inputs()
        #self.config_comboBoxes()
        
#
    
        self.addButton.clicked.connect(self.add_book)
        self.cancelButton.clicked.connect(self.close)
    def open_new_window_coordenadas(self):
        from controllers.new_window_subestacion_interruptor_esquema import NewBookWindow
        window= NewBookWindow(self)
        window.show()
    def open_new_window_plano(self):
        from controllers.new_window_subestacion_interruptor_plano import NewBookWindow
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

        errors_count = 0
        
        if inputCodigo == "":
            print("El campo areavisitada es obligatorio")
            self.label_advertencia_dni.show()
            errors_count +=1
        else:
            self.label_advertencia_dni.hide()

        if errors_count==0:
            return (True)
            
    #    
    def add_book(self):
        
        inputCodigo = self.inputCodigo.text()
        inputCodigo=inputCodigo.strip()

        inputNombre = self.inputSubestacion.text()
        inputNombre=inputNombre.strip()

        inputCelda = self.inputCelda.text()
        inputCelda=inputCelda.strip()

        inputFecha = self.inputFecha.text()

        inputTension = self.inputTension.text()
        inputTension=inputTension.strip()

        inputMarca = self.inputMarca.text()
        inputMarca=inputMarca.strip()

        inputAnio = self.inputAnio.text()
        inputAnio=inputAnio.strip()


        inputX = self.inputX.text()
        inputX=inputX.strip()

        inputY = self.inputY.text()
        inputY=inputY.strip()

        inputZ = self.inputZ.text()
        inputZ=inputZ.strip()

        inputANG = self.inputANG.text()
        inputANG=inputANG.strip()

        inputANG_2 = self.inputANG_2.text()
        inputANG_2=inputANG_2.strip()

        inputX_2 = self.inputX_2.text()
        inputX_2=inputX_2.strip()

        inputY_2 = self.inputY_2.text()
        inputY_2=inputY_2.strip()


        cbCalificacion = self.cbCalificacion.currentText()
        cbTipo = self.cbTipo.currentText()
        cbEstado = self.cbEstado.currentText()

        self.label_advertencia_dni.hide()

        
        #self.ActualizarVisitante(dni,visitante)
        if self.check_inputs():
            #new_path = shutil.copy(path, "book_files")
            self.label_nota_obligatoria.hide()
            data = (self.Usuario, inputNombre, inputCodigo, inputCelda, cbCalificacion, cbTipo, inputTension, inputMarca, inputAnio, cbEstado, inputFecha)

            #self.AnadirNuevos(dni,visitante,entidadempresa,motivovisita,aquienvisita,autoriza,areavisitada) 
            if insert_book_transmision_interruptor(data):
                #self.clean_inputs()
                data2 = (self.Usuario, inputNombre, inputCodigo, inputX_2, inputY_2, inputANG_2)
                data3 = (self.Usuario, inputNombre, inputCodigo, inputX, inputY, inputZ, inputANG)

                insert_book_transmision_interruptor_ubicacion_esquema(data2)
                insert_book_transmision_interruptor_ubicacion_plano(data3)

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
        
    def populate_inputs(self, interruptor_id):
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

                # Consulta a la tabla Interruptor_Potencia
                sql = "SELECT * FROM Interruptor_Potencia WHERE COD_INTERRUPTOR = ?"
                cur.execute(sql, (interruptor_id,))
                row = cur.fetchone()
                if row:
                    # Obtener los valores de la fila
                    inputCodigo = str(row[2])
                    inputNombre = str(row[1])
                    inputCelda = str(row[3])
                    cbCalificacion = str(row[4])
                    cbTipo = str(row[5])
                    inputTension = str(row[6])
                    inputMarca = str(row[7])
                    inputAnio = str(row[8])
                    cbEstado = str(row[9])
                    inputFecha = str(row[10])

                    # Poblar los campos de entrada de la tabla Interruptor_Potencia
                    self.inputCodigo.setText(inputCodigo)
                    self.inputSubestacion.setText(inputNombre)
                    self.inputCelda.setText(inputCelda)
                    self.cbCalificacion.setCurrentText(cbCalificacion)
                    self.cbTipo.setCurrentText(cbTipo)
                    self.inputTension.setText(inputTension)
                    self.inputMarca.setText(inputMarca)
                    self.inputAnio.setText(inputAnio)
                    self.cbEstado.setCurrentText(cbEstado)
                    fechaConv = inputFecha.replace("/", "-")
                    qdate = QDate.fromString(fechaConv, "d-MM-yyyy")
                    self.inputFecha.setDate(qdate)

                    # Consulta a la tabla Interruptor_Potencia_Ubicacion_Esquema
                    sql_esquema = "SELECT * FROM Interruptor_Potencia_Ubicacion_Esquema WHERE COD_INTERRUPTOR = ?"
                    cur.execute(sql_esquema, (interruptor_id,))
                    row_esquema = cur.fetchone()
                    if row_esquema:
                        inputX_2 = str(row_esquema[3])
                        inputY_2 = str(row_esquema[4])
                        inputANG_2 = str(row_esquema[5])

                        # Poblar los campos de entrada de la tabla Interruptor_Potencia_Ubicacion_Esquema
                        self.inputX_2.setText(inputX_2)
                        self.inputY_2.setText(inputY_2)
                        self.inputANG_2.setText(inputANG_2)

                    # Consulta a la tabla Interruptor_Potencia_Ubicacion_Plano_Planta
                    sql_plano = "SELECT * FROM Interruptor_Potencia_Ubicacion_Plano_Planta WHERE COD_INTERRUPTOR = ?"
                    cur.execute(sql_plano, (interruptor_id,))
                    row_plano = cur.fetchone()
                    if row_plano:
                        inputX = str(row_plano[3])
                        inputY = str(row_plano[4])
                        inputZ = str(row_plano[5])
                        inputANG = str(row_plano[6])

                        # Poblar los campos de entrada de la tabla Interruptor_Potencia_Ubicacion_Plano_Planta
                        self.inputX.setText(inputX)
                        self.inputY.setText(inputY)
                        self.inputZ.setText(inputZ)
                        self.inputANG.setText(inputANG)

            except Error as e:
                print("Error al obtener detalles del interruptor:", str(e))
            finally:
                if conn:
                    conn.close()

    def populate_combobox(self):
        # Llenar el combo de Calificación
        cb_options_calificacion = ("", "Principal", "Secundario", "Garantizado", "Complementario")
        self.cbCalificacion.addItems(cb_options_calificacion)

        # Llenar el combo de Tipo de Instalación
        cb_options_tipo_instalacion = ("", "Interior", "Exterior")
        self.cbTipo.addItems(cb_options_tipo_instalacion)

        # Llenar el combo de Estado
        cb_options_estado = ("", "Nuevo", "Existente", "Eliminado", "Modificado", "Proyectado")
        self.cbEstado.addItems(cb_options_estado)
