from PySide2.QtWidgets import QDialog, QWidget, QFileDialog,QCompleter
from PySide2.QtCore import Qt, QDate
from PySide2.QtGui import *
import sqlite3
from sqlite3 import Error
from views.new_transmision_transformador_medicion import Ui_NewBook
from db.books import buscar_usuario_acceso,insert_book_transformador_medicion_ubicacion_plano,insert_book_transformador_medicion_ubicacion_esquema,insert_book_transformador_medicion
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
        
        self.inputSubestacion.setText(str(_codCentral))
        self.inputSubestacion.setEnabled(False)
        self.Usuario= buscar_usuario_acceso();
        self.label.setStyleSheet("background-color: #114692;")
        self.label_advertencia_dni.hide()
        self.label_nota_obligatoria.hide()
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
        if _codigo is not None:
            print("----------NO ES EDIT-----------:"+str(_codigo))
            self.populate_inputs(_codigo)
            self.inputCodigo.setText(str(_codigo))
            self.inputCodigo.setEnabled(False)
            self.addButton.setText("GUARDAR")

        #self.btnAddEsquema.clicked.connect(self.open_new_window_coordenadas)
        #self.btnAddPlanta.clicked.connect(self.open_new_window_plano)
        
        #self.populate_comboboxEstado()
        #self.populate_inputs()
        #self.config_comboBoxes()
#
    
        self.addButton.clicked.connect(self.add_book)
        self.cancelButton.clicked.connect(self.close)
    def open_new_window_coordenadas(self):
        from controllers.new_window_subestacion_transformador_medicion_esquema import NewBookWindow
        window= NewBookWindow(self)
        window.show()
    def open_new_window_plano(self):
        from controllers.new_window_subestacion_transformador_medicion_plano import NewBookWindow
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
            
            
    def add_book(self):
        
        inputCodigo = self.inputCodigo.text()
        inputCodigo=inputCodigo.strip()

        inputNombre = self.inputSubestacion.text()
        inputNombre=inputNombre.strip()

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
        cbTipoInstalacion = self.cbTipoInstalacion.currentText()
        cbEstado = self.cbEstado.currentText()

        self.label_advertencia_dni.hide()

        
        #self.ActualizarVisitante(dni,visitante)
        if self.check_inputs():
            #new_path = shutil.copy(path, "book_files")
            self.label_nota_obligatoria.hide()
            data = (self.Usuario, inputNombre, inputCodigo, cbCalificacion, cbTipo, cbTipoInstalacion, inputTension, inputMarca, inputAnio, cbEstado, inputFecha)

            #self.AnadirNuevos(dni,visitante,entidadempresa,motivovisita,aquienvisita,autoriza,areavisitada) 
            if insert_book_transformador_medicion(data):
                #self.clean_inputs()
                data2 = (self.Usuario, inputNombre, inputCodigo, inputX_2, inputY_2, inputANG_2)
                data3 = (self.Usuario, inputNombre, inputCodigo, inputX, inputY, inputZ, inputANG)
                insert_book_transformador_medicion_ubicacion_esquema(data2)
                insert_book_transformador_medicion_ubicacion_plano(data3)

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

                # Consulta a la tabla Transformador_Medicion
                sql = "SELECT * FROM Transformador_Medicion WHERE COD_TRANSF = ?"
                cur.execute(sql, (book_id,))
                row = cur.fetchone()
                if row:
                    # Obtener los valores de la fila
                    inputCodEmpresa = str(row[0])
                    inputCodigo = str(row[2])
                    inputNombre = str(row[1])
                    cbCalificacion = str(row[3])
                    cbTipo = str(row[4])
                    cbTipoInstalacion = str(row[5])
                    inputTension = str(row[6])
                    inputMarca = str(row[7])
                    inputAnio = str(row[8])
                    cbEstado = str(row[9])
                    inputFecha = str(row[10])

                    # Poblar los campos de entrada de la tabla Transformador_Medicion
                    self.inputCodEmpresa.setText(inputCodEmpresa)
                    self.inputCodigo.setText(inputCodigo)
                    self.inputSubestacion.setText(inputNombre)
                    self.cbCalificacion.setCurrentText(cbCalificacion)
                    self.cbTipo.setCurrentText(cbTipo)
                    self.cbTipoInstalacion.setCurrentText(cbTipoInstalacion)
                    self.inputTension.setText(inputTension)
                    self.inputMarca.setText(inputMarca)
                    self.inputAnio.setText(inputAnio)
                    self.cbEstado.setCurrentText(cbEstado)
                    fechaConv = inputFecha.replace("/", "-")
                    qdate = QDate.fromString(fechaConv, "d-MM-yyyy")
                    self.inputFecha.setDate(qdate)

                    # Consulta a la tabla Transformador_Medicion_Ubicacion_Esquema
                    sql_esquema = "SELECT * FROM Transformador_Medicion_Ubicacion_Esquema WHERE COD_TRANSF = ?"
                    cur.execute(sql_esquema, (book_id,))
                    row_esquema = cur.fetchone()
                    if row_esquema:
                        inputX_2 = str(row_esquema[3])
                        inputY_2 = str(row_esquema[4])
                        inputANG_2 = str(row_esquema[5])

                        # Poblar los campos de entrada de la tabla Transformador_Medicion_Ubicacion_Esquema
                        self.inputX_2.setText(inputX_2)
                        self.inputY_2.setText(inputY_2)
                        self.inputANG_2.setText(inputANG_2)

                    # Consulta a la tabla Transformador_Medicion_Ubicacion_Plano_Planta
                    sql_plano = "SELECT * FROM Transformador_Medicion_Ubicacion_Plano_Planta WHERE COD_TRANSF = ?"
                    cur.execute(sql_plano, (book_id,))
                    row_plano = cur.fetchone()
                    if row_plano:
                        inputX = str(row_plano[3])
                        inputY = str(row_plano[4])
                        inputZ = str(row_plano[5])
                        inputANG = str(row_plano[6])

                        # Poblar los campos de entrada de la tabla Transformador_Medicion_Ubicacion_Plano_Planta
                        self.inputX.setText(inputX)
                        self.inputY.setText(inputY)
                        self.inputZ.setText(inputZ)
                        self.inputANG.setText(inputANG)

            except Error as e:
                print("Error al obtener detalles del libro:", str(e))
            finally:
                if conn:
                    conn.close()

    def populate_combobox(self):
        # Llenar el combo de Calificación
        cb_options_calificacion = ("", "Principal", "Secundario", "Garantizado", "Complementario")
        self.cbCalificacion.addItems(cb_options_calificacion)

        # Llenar el combo de Tipo de Transformador
        cb_options_tipo_transformador = ("", "Corriente", "Tensión", "Medida Combinado")
        self.cbTipo.addItems(cb_options_tipo_transformador)

        # Llenar el combo de Tipo de Instalación
        cb_options_tipo_instalacion = ("", "Interior", "Exterior")
        self.cbTipoInstalacion.addItems(cb_options_tipo_instalacion)

        # Llenar el combo de Estado
        cb_options_estado = ("", "Nuevo", "Existente", "Eliminado", "Modificado", "Proyectado")
        self.cbEstado.addItems(cb_options_estado)
