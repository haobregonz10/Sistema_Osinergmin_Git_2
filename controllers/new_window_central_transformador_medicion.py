from PySide2.QtWidgets import QDialog, QWidget, QFileDialog,QCompleter
from PySide2.QtCore import Qt, QDate
from PySide2.QtGui import *
import sqlite3
from sqlite3 import Error
from views.new_central_transformador_medicion import Ui_NewBook
from db.books import buscar_usuario_acceso,insert_book_transformador_medicion_central_generacion,insert_book_transformador_medicion_central_generacion_planta,insert_book_transformador_medicion_central_generacion_ubicacion_esquema
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
        #self.btnAddEsquema.clicked.connect(self.open_new_window_esquemas)
        #self.btnAddPlanta.clicked.connect(self.open_new_window_plano)
        self.inputCentral.setText(str(_codCentral))
        self.inputCentral.setEnabled(False)

        self.label_advertencia_dni.hide()
        self.label_nota_obligatoria.hide()
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
        self.populate_combobox()

        if _codigo is not None:
            print("----------NO ES EDIT-----------:"+str(_codigo))
            self.populate_inputs(_codigo)
            self.inputCodigo.setText(str(_codigo))
            self.inputCodigo.setEnabled(False)
            self.addButton.setText("GUARDAR")
            
        self.addButton.clicked.connect(self.add_book)
#
    
        #self.addButton.clicked.connect(self.add_book)
        self.cancelButton.clicked.connect(self.close)
    def open_new_window_esquemas(self):
        from controllers.new_window_central_transformador_medicion_esquema import NewBookWindow
        window= NewBookWindow(self)
        window.show()
    def open_new_window_plano(self):
        from controllers.new_window_central_transformador_medicion_plano import NewBookWindow
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

        inputTension = self.inputTension.text()
        inputTension=inputTension.strip()

        inputMarca = self.inputMarca.text()
        inputMarca=inputMarca.strip()

        inputAnio = self.inputAnio.text()
        inputAnio=inputAnio.strip()

        inputFecha = self.inputFecha.text()
        inputFecha=inputFecha.strip()

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

        cbTipo = self.cbTipo.currentText()
        cbTipoInstalacion = self.cbTipoInstalacion.currentText()
        cbEstado=self.cbEstado.currentText()

        self.label_advertencia_dni.hide()

        #self.ActualizarVisitante(dni,visitante)
        if self.check_inputs():
            #new_path = shutil.copy(path, "book_files")
            self.label_nota_obligatoria.hide()
            data = (self.Usuario,inputCentral,inputCodigo,cbTipo,cbTipoInstalacion,inputTension,inputMarca,inputAnio,cbEstado,inputFecha) 
            
            if insert_book_transformador_medicion_central_generacion(data):
                #self.clean_inputs()
                data2 = (self.Usuario, inputCentral, inputCodigo, inputX_2, inputY_2,inputANG_2)
                data3 = (self.Usuario, inputCentral, inputCodigo, inputX, inputY, inputZ, inputANG)
                
                insert_book_transformador_medicion_central_generacion_ubicacion_esquema(data2)
                insert_book_transformador_medicion_central_generacion_planta(data3)

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
                
        if conn:
            try:
                cur = conn.cursor()
                # Consulta a la tabla Transformador_Medicion_Central_Generacion
                sql = f"SELECT * FROM Transformador_Medicion_Central_Generacion WHERE COD_TRANSF = ?"
                cur.execute(sql, (book_id,))
                row = cur.fetchone()
                if row:
                    # Obtener los valores de la fila
                    inputCodEmpresa = str(row[0])
                    inputCodigo = str(row[2])
                    inputCentral = str(row[1])
                    inputTipo = str(row[3])
                    inputTipoInstalacion = str(row[4])
                    inputTension = str(row[5])
                    inputMarca = str(row[6])
                    inputAnio = str(row[7])
                    cbEstado = str(row[8])
                    inputFecha = str(row[9])

                    # Poblar los campos de entrada de la tabla Transformador_Medicion_Central_Generacion
                    self.inputCodEmpresa.setText(inputCodEmpresa)
                    self.inputCodigo.setText(inputCodigo)
                    self.inputCentral.setText(inputCentral)
                    self.cbTipo.setCurrentText(inputTipo)
                    self.cbTipoInstalacion.setCurrentText(inputTipoInstalacion)
                    self.inputTension.setText(inputTension)
                    self.inputMarca.setText(inputMarca)
                    self.inputAnio.setText(inputAnio)
                    self.cbEstado.setCurrentText(cbEstado)
                    fechaConv = inputFecha
                    fechaConv2 = fechaConv.replace("/", "-")
                    qdate = QDate.fromString(fechaConv2, "d-MM-yyyy")
                    self.inputFecha.setDate(qdate)

                    # Consulta a la tabla Transformador_Medicion_Central_Ubicacion_Esquema
                    sql_esquema = f"SELECT * FROM Transformador_Medicion_Central_Ubicacion_Esquema WHERE COD_TRANSF = ?"
                    cur.execute(sql_esquema, (book_id,))
                    row_esquema = cur.fetchone()
                    if row_esquema:
                        # Obtener los valores de la fila
                        inputX_2 = str(row_esquema[3])
                        inputY_2 = str(row_esquema[4])
                        inputANG_2 = str(row_esquema[5])
                        # Poblar los campos de entrada de la tabla Transformador_Medicion_Central_Ubicacion_Esquema
                        self.inputX_2.setText(inputX_2)
                        self.inputY_2.setText(inputY_2)
                        self.inputANG_2.setText(inputANG_2)

                    # Consulta a la tabla Transformador_Medicion_Central_Ubicacion_Plano_Planta
                    sql_planta = f"SELECT * FROM Transformador_Medicion_Central_Ubicacion_Plano_Planta WHERE COD_TRANSF = ?"
                    cur.execute(sql_planta, (book_id,))
                    row_planta = cur.fetchone()
                    if row_planta:
                        # Obtener los valores de la fila
                        inputX = str(row_planta[3])
                        inputY = str(row_planta[4])
                        inputZ = str(row_planta[5])
                        inputANG = str(row_planta[6])
                        # Poblar los campos de entrada de la tabla Transformador_Medicion_Central_Ubicacion_Plano_Planta
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
        # Llenar el combo de Tipo de Transformador
        cb_options_tipo_transformador = ("", "Corriente", "Tensión", "Medida Combinado")
        self.cbTipo.addItems(cb_options_tipo_transformador)

        # Llenar el combo de Tipo de Instalación
        cb_options_tipo_instalacion = ("", "Interior", "Exterior")
        self.cbTipoInstalacion.addItems(cb_options_tipo_instalacion)

        # Llenar el combo de Estado
        cb_options_estado = ("", "Nuevo", "Existente", "Eliminado", "Modificado", "Proyectado")
        self.cbEstado.addItems(cb_options_estado)
