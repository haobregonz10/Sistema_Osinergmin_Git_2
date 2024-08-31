from PySide2.QtWidgets import QDialog, QWidget, QFileDialog,QCompleter
from PySide2.QtCore import Qt, QDate
from PySide2.QtGui import *
import sqlite3
from sqlite3 import Error
from views.new_central_transformador import Ui_NewBook
from db.books import buscar_usuario_acceso,insert_book_transformador_central_generacion,insert_book_transformador_central_generacion_ubicacion_esquema,insert_book_transformador_central_generacion_planta
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
        #self.btnAddEsquema.clicked.connect(self.open_new_window_esquemas)
        #self.btnAddPlanta.clicked.connect(self.open_new_window_plano)
        self.Usuario= buscar_usuario_acceso();
        self.inputCentral.setText(str(_codCentral))
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

            
        self.addButton.clicked.connect(self.add_book)
#
    
        #self.addButton.clicked.connect(self.add_book)
        self.cancelButton.clicked.connect(self.close)
    def open_new_window_esquemas(self):
        from controllers.new_window_central_transformador_esquema import NewBookWindow
        window= NewBookWindow(self)
        window.show()
    def open_new_window_plano(self):
        from controllers.new_window_central_transformador_plano import NewBookWindow
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

        inputConexion = self.inputConexion.text()
        inputConexion=inputConexion.strip()

        inputSerie = self.inputSerie.text()
        inputSerie=inputSerie.strip()

        inputTension = self.inputTension.text()
        inputTension=inputTension.strip()

        inputTension2 = self.inputTension2.text()
        inputTension2=inputTension2.strip()

        inputTension3 = self.inputTension3.text()
        inputTension3=inputTension3.strip()

        inputPotenciaLado = self.inputPotenciaLado.text()
        inputPotenciaLado=inputPotenciaLado.strip()

        inputPotenciaLado2 = self.inputPotenciaLado2.text()
        inputPotenciaLado2=inputPotenciaLado2.strip()

        inputPotenciaLado3 = self.inputPotenciaLado3.text()
        inputPotenciaLado3=inputPotenciaLado3.strip()

        inputMarca = self.inputMarca.text()
        inputMarca=inputMarca.strip()

        inputAnio = self.inputAnio.text()
        inputAnio=inputAnio.strip()

        inputVCC = self.inputVCC.text()
        inputVCC=inputVCC.strip()

        inputVCC2 = self.inputVCC2.text()
        inputVCC2=inputVCC2.strip()

        inputVCC3 = self.inputVCC3.text()
        inputVCC3=inputVCC3.strip()

        inputPotenciaBase = self.inputPotenciaBase.text()
        inputPotenciaBase=inputPotenciaBase.strip()

        inputPerdidaCu = self.inputPerdidaCu.text()
        inputPerdidaCu=inputPerdidaCu.strip()

        inputPerdidaCu2 = self.inputPerdidaCu2.text()
        inputPerdidaCu2=inputPerdidaCu2.strip()

        inputPerdidaCu3 = self.inputPerdidaCu3.text()
        inputPerdidaCu3=inputPerdidaCu3.strip()

        inputPerdidaFe = self.inputPerdidaFe.text()
        inputPerdidaFe=inputPerdidaFe.strip()

        inputPerdidaFe2 = self.inputPerdidaFe2.text()
        inputPerdidaFe2=inputPerdidaFe2.strip()

        inputPerdidaFe3 = self.inputPerdidaFe3.text()
        inputPerdidaFe3=inputPerdidaFe3.strip()

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
        inputTipoInstalacion = self.inputTipoInstalacion.currentText()
        cbDisponibilidad = self.cbDisponibilidad.currentText()
        cbEstado=self.cbEstado.currentText()

        self.label_advertencia_dni.hide()

        #self.ActualizarVisitante(dni,visitante)
        if self.check_inputs():
            #new_path = shutil.copy(path, "book_files")
            self.label_nota_obligatoria.hide()
            data = (self.Usuario,inputCentral,inputCodigo,cbTipo,inputTipoInstalacion,inputConexion,inputSerie,inputTension,inputTension2,inputTension3,inputPotenciaLado,inputPotenciaLado2,inputPotenciaLado3,inputMarca,inputAnio,cbDisponibilidad,inputVCC,inputVCC2,inputVCC3,inputPotenciaBase,inputPerdidaCu,inputPerdidaCu2,inputPerdidaCu3,inputPerdidaFe,inputPerdidaFe2,inputPerdidaFe3,cbEstado,inputFecha) 
            
            if insert_book_transformador_central_generacion(data):
                #self.clean_inputs()
                data2 = (self.Usuario, inputCentral, inputCodigo, inputX_2, inputY_2,inputANG_2)
                data3 = (self.Usuario, inputCentral, inputCodigo, inputX, inputY, inputZ, inputANG)
                insert_book_transformador_central_generacion_ubicacion_esquema(data2)
                insert_book_transformador_central_generacion_planta(data3)

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
            conn = sqlite3.connect('DATABASEAPP.db')  # Utiliza tu función para crear la conexión
            print("Conexión a la base de datos correcta.")
        except Error as e:
            print("Error al conectar a la base de datos: " + str(e))
                
        if conn:
            try:
                cur = conn.cursor()
                # Consulta a la tabla Transformador_Central_Generacion
                sql = f"SELECT * FROM Transformador_Central_Generacion WHERE COD_TRANSF = ?"
                cur.execute(sql, (book_id,))
                row = cur.fetchone()
                if row:
                    # Obtener los valores de la fila
                    inputCodEmpresa = str(row[0])
                    inputCodigo = str(row[2])
                    inputCentral = str(row[1])
                    inputTipo = str(row[3])
                    inputTipoInstalacion = str(row[4])
                    inputConexion = str(row[5])
                    inputSerie = str(row[6])
                    inputTension = str(row[7])
                    inputTension2 = str(row[8])
                    inputTension3 = str(row[9])
                    inputPotenciaLado = str(row[10])
                    inputPotenciaLado2 = str(row[11])
                    inputPotenciaLado3 = str(row[12])
                    inputMarca = str(row[13])
                    inputAnio = str(row[14])
                    cbDisponibilidad = str(row[15])
                    inputVCC = str(row[16])
                    inputVCC2 = str(row[17])
                    inputVCC3 = str(row[18])
                    inputPotenciaBase = str(row[19])
                    inputPerdidaCu = str(row[20])
                    inputPerdidaCu2 = str(row[21])
                    inputPerdidaCu3 = str(row[22])
                    inputPerdidaFe = str(row[23])
                    inputPerdidaFe2 = str(row[24])
                    inputPerdidaFe3 = str(row[25])
                    cbEstado = str(row[26])
                    inputFecha = str(row[27])

                    # Poblar los campos de entrada de la tabla Transformador_Central_Generacion
                    self.inputCodEmpresa.setText(inputCodEmpresa)
                    self.inputCodigo.setText(inputCodigo)
                    self.inputCentral.setText(inputCentral)
                    self.cbTipo.setCurrentText(inputTipo)
                    self.inputTipoInstalacion.setCurrentText(inputTipoInstalacion)
                    self.inputConexion.setText(inputConexion)
                    self.inputSerie.setText(inputSerie)
                    self.inputTension.setText(inputTension)
                    self.inputTension2.setText(inputTension2)
                    self.inputTension3.setText(inputTension3)
                    self.inputPotenciaLado.setText(inputPotenciaLado)
                    self.inputPotenciaLado2.setText(inputPotenciaLado2)
                    self.inputPotenciaLado3.setText(inputPotenciaLado3)
                    self.inputMarca.setText(inputMarca)
                    self.inputAnio.setText(inputAnio)
                    self.cbDisponibilidad.setCurrentText(cbDisponibilidad)
                    self.inputVCC.setText(inputVCC)
                    self.inputVCC2.setText(inputVCC2)
                    self.inputVCC3.setText(inputVCC3)
                    self.inputPotenciaBase.setText(inputPotenciaBase)
                    self.inputPerdidaCu.setText(inputPerdidaCu)
                    self.inputPerdidaCu2.setText(inputPerdidaCu2)
                    self.inputPerdidaCu3.setText(inputPerdidaCu3)
                    self.inputPerdidaFe.setText(inputPerdidaFe)
                    self.inputPerdidaFe2.setText(inputPerdidaFe2)
                    self.inputPerdidaFe3.setText(inputPerdidaFe3)
                    self.cbEstado.setCurrentText(cbEstado)
                    fechaConv = inputFecha
                    fechaConv2 = fechaConv.replace("/", "-")
                    qdate = QDate.fromString(fechaConv2, "d-MM-yyyy")
                    self.inputFecha.setDate(qdate)

                    # Consulta a la tabla Transformador_Central_Generacion_Ubicacion_Esquema
                    sql_esquema = f"SELECT * FROM Transformador_Central_Generacion_Ubicacion_Esquema WHERE COD_TRANSF = ?"
                    cur.execute(sql_esquema, (book_id,))
                    row_esquema = cur.fetchone()
                    if row_esquema:
                        # Obtener los valores de la fila
                        inputX_2 = str(row_esquema[3])
                        inputY_2 = str(row_esquema[4])
                        inputANG_2 = str(row_esquema[5])
                        # Poblar los campos de entrada de la tabla Transformador_Central_Generacion_Ubicacion_Esquema
                        self.inputX_2.setText(inputX_2)
                        self.inputY_2.setText(inputY_2)
                        self.inputANG_2.setText(inputANG_2)

                    # Consulta a la tabla Transformador_Central_Generacion_Ubicacion_Plano_Planta
                    sql_planta = f"SELECT * FROM Transformador_Central_Generacion_Ubicacion_Plano_Planta WHERE COD_TRANSF = ?"
                    cur.execute(sql_planta, (book_id,))
                    row_planta = cur.fetchone()
                    if row_planta:
                        # Obtener los valores de la fila
                        inputX = str(row_planta[3])
                        inputY = str(row_planta[4])
                        inputZ = str(row_planta[5])
                        inputANG = str(row_planta[6])
                        # Poblar los campos de entrada de la tabla Transformador_Central_Generacion_Ubicacion_Plano_Planta
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
        cb_options_tipo_transformador = ("", "Trifásico", "Monofásico", "Banco", "Autotransformador", "Zigzag")
        self.cbTipo.addItems(cb_options_tipo_transformador)

        # Llenar el combo de Tipo de Instalación
        cb_options_tipo_instalacion = ("", "Interior", "Exterior")
        self.inputTipoInstalacion.addItems(cb_options_tipo_instalacion)

        # Llenar el combo de Disponibilidad del Transformador
        cb_options_disponibilidad = ("", "Operación", "Reserva")
        self.cbDisponibilidad.addItems(cb_options_disponibilidad)

        # Llenar el combo de Estado
        cb_options_estado = ("", "Nuevo", "Existente", "Eliminado", "Modificado", "Proyectado")
        self.cbEstado.addItems(cb_options_estado)
