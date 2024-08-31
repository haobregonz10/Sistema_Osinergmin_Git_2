from PySide2.QtWidgets import QDialog, QWidget, QFileDialog,QCompleter
from PySide2.QtCore import Qt, QDate
from PySide2.QtGui import *
import sqlite3
from sqlite3 import Error
from views.new_transmision_linea_Estructura import Ui_NewBook
from db.books import buscar_usuario_acceso,insert_book_transmision_linea_estructura,insert_book_transmision_linea_estructura_ubicacion_geografica,insert_book_transmision_linea_estructura_ubicacion_subestacion,insert_book_transmision_linea_estructura_ubicacion_central
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
        self.inputDatum.setText("WGS84")
        self.inputDatum.setEnabled(False)
        self.inputLineaTransmision.setText(str(_codCentral))
        self.inputLineaTransmision.setEnabled(False)
        self.addButton.clicked.connect(self.add_book)
        self.cancelButton.clicked.connect(self.close)
        self.populate_combobox()
        if(self.Usuario!="admin"):
            print("NO ES ADMIN!!!")
            self.inputCodEmpresa.hide()
            self.label_empresa.hide()
        else:
            print("ES ADMIN!!!") 
            self.inputCodEmpresa.setText(self.Usuario)
            self.inputCodEmpresa.setEnabled(False)
        self.label.setStyleSheet("background-color: #114692;")
        
        self.label_advertencia_dni.hide()
        self.label_nota_obligatoria.hide()
        #self.populate_comboboxPiso()
        if _codigo is not None:
            print("----------NO ES EDIT-----------:"+str(_codigo))
            self.populate_inputs(_codigo)
            self.inputCodigo.setText(str(_codigo))
            self.inputCodigo.setEnabled(False)
            self.addButton.setText("GUARDAR")
#
#
    def open_new_window_geo(self):
        from controllers.new_window_linea_estructura_geografica import NewBookWindow
        window= NewBookWindow(self)
        window.show()   
        #self.addButton.clicked.connect(self.add_book)
        #self.cancelButton.clicked.connect(self.close)

    def open_new_window_subestacion(self):
        from controllers.new_window_linea_estructura_subestacion import NewBookWindow
        window= NewBookWindow(self)
        window.show()   
        #self.addButton.clicked.connect(self.add_book)
        #self.cancelButton.clicked.connect(self.close)

    def open_new_window_central(self):
        from controllers.new_window_linea_estructura_central import NewBookWindow
        window= NewBookWindow(self)
        window.show()   
        #self.addButton.clicked.connect(self.add_book)
        #self.cancelButton.clicked.connect(self.close)

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

        inputNombre = self.inputLineaTransmision.text()
        inputNombre=inputNombre.strip()

        inputAltura = self.inputAltura.text()
        inputAltura=inputAltura.strip()

        inputLocalidad = self.inputLocalidad.text()
        inputLocalidad=inputLocalidad.strip()

        inputDatum = self.inputDatum.text()
        inputDatum=inputDatum.strip()

        inputZona = self.inputZona.text()
        inputZona=inputZona.strip()

        inputX = self.inputX.text()
        inputX=inputX.strip()

        inputY = self.inputY.text()
        inputY=inputY.strip()

        inputZ = self.inputZ.text()
        inputZ=inputZ.strip()

        inputANG = self.inputANG.text()
        inputANG=inputANG.strip()

        inputSubestacion = self.inputSubestacion.text()
        inputSubestacion=inputSubestacion.strip()

        inputX_2 = self.inputX_2.text()
        inputX_2=inputX_2.strip()

        inputY_2 = self.inputY_2.text()
        inputY_2=inputY_2.strip()

        inputZ_2 = self.inputZ_2.text()
        inputZ_2=inputZ_2.strip()

        inputANG_2 = self.inputANG_2.text()
        inputANG_2=inputANG_2.strip()

        inputCentral = self.inputCentral.text()
        inputCentral=inputCentral.strip()

        inputX_3 = self.inputX_3.text()
        inputX_3=inputX_3.strip()

        inputY_3 = self.inputY_3.text()
        inputY_3=inputY_3.strip()

        inputZ_3 = self.inputZ_3.text()
        inputZ_3=inputZ_3.strip()

        inputANG_3 = self.inputANG_3.text()
        inputANG_3=inputANG_3.strip()

        inputFecha = self.inputFecha.text()
        inputFecha=inputFecha.strip()
        

        cbTipo = self.cbTipo.currentText()
        cbCalificacion = self.cbCalificacion.currentText()
        cbFuncion = self.cbFuncion.currentText()
        cbNCables = self.cbNCables.currentText()
        cbNCircuitos=self.cbNCircuitos.currentText()
        cbFormacion=self.cbFormacion.currentText()
        cbEstado=self.cbEstado.currentText()


        self.label_advertencia_dni.hide()

        #self.ActualizarVisitante(dni,visitante)
        if self.check_inputs():
            #new_path = shutil.copy(path, "book_files")
            self.label_nota_obligatoria.hide()
            
            data = (self.Usuario, inputNombre, inputCodigo, cbCalificacion, cbTipo, cbFuncion, inputAltura, cbNCircuitos, cbFormacion,cbNCables, inputLocalidad, cbEstado, inputFecha)

            if insert_book_transmision_linea_estructura(data):
                data2 = (self.Usuario, inputNombre, inputCodigo, inputDatum, inputZona, inputX, inputY, inputZ, inputANG)
                data3 = (self.Usuario, inputNombre, inputCodigo, inputSubestacion, inputX_2, inputY_2, inputZ_2,inputANG_2)
                data4 = (self.Usuario, inputNombre, inputCodigo, inputCentral, inputX_3, inputY_3, inputZ_3,inputANG_3)
                insert_book_transmision_linea_estructura_ubicacion_geografica(data2)
                insert_book_transmision_linea_estructura_ubicacion_subestacion(data3)
                insert_book_transmision_linea_estructura_ubicacion_central(data4)
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


    def populate_combobox(self):
        # Llenar el combo de Tipo
        cb_options_tipo = ("", "Postes de Concreto y Acero", "Postes de Concreto", "Postes de Madera", "Torresde Acero", "Postes de Acero", "Postes de Madera y Acero","Instalación Subterránea","Sin Estructura o Red Compartida")
        self.cbTipo.addItems(cb_options_tipo)

        # Llenar el combo de Calificación
        cb_options_calificacion = ("", "Principal", "Secundario", "Garantizado", "Complementario")
        self.cbCalificacion.addItems(cb_options_calificacion)

        # Llenar el combo de Función de la estructura
        cb_options_funcion = ("", "Suspensión", "Angulo", "Retención Intermedia", "Terminal", "Transposición", "Derivación")
        self.cbFuncion.addItems(cb_options_funcion)

        # Llenar el combo de Número de Circuitos que puede soportar la estructura
        cb_options_num_cables = ("", "Ninguno", "Uno", "Dos")
        self.cbNCables.addItems(cb_options_num_cables)

        # Llenar el combo de Número de Circuitos que puede soportar la estructura
        cb_options_num_circuitos = ("", "Un Circuito", "Dos Circuitos", "Tres Circuitos")
        self.cbNCircuitos.addItems(cb_options_num_circuitos)

        # Llenar el combo de Formación de la fase en Haz de Conductores
        cb_options_formacion = ("", "Simple", "Duplex", "Triplex", "Cuádruplex")
        self.cbFormacion.addItems(cb_options_formacion)


        # Llenar el combo de Estado
        cb_options_estado = ("", "Nuevo", "Existente", "Eliminado", "Modificado", "Proyectado")
        self.cbEstado.addItems(cb_options_estado)


        

    
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

                # Consulta a la tabla Estructura
                sql = """SELECT COD_LINEA, COD_ESTRUCTURA, COD_CALIFICACION, TIPO, FUNCION, ALTURA, NUM_CIRCUITOS, 
                        FORMACION_FASE, NUM_CABLE_GUARDA, LOCALIDAD, ESTADO, FECHA_ALTA, COD_EMP 
                        FROM Estructura 
                        WHERE COD_ESTRUCTURA = ?"""
                cur.execute(sql, (cod_estructura,))
                row = cur.fetchone()
                if row:
                    self.inputCodEmpresa.setText(str(row[12]))
                    self.inputLineaTransmision.setText(str(row[0]))
                    self.inputCodigo.setText(str(row[1]))
                    self.cbCalificacion.setCurrentText(str(row[2]))
                    self.cbTipo.setCurrentText(str(row[3]))
                    self.cbFuncion.setCurrentText(str(row[4]))
                    self.inputAltura.setText(str(row[5]))
                    self.cbNCircuitos.setCurrentText(str(row[6]))
                    self.cbFormacion.setCurrentText(str(row[7]))
                    self.cbNCables.setCurrentText(str(row[8]))
                    self.inputLocalidad.setText(str(row[9]))
                    self.cbEstado.setCurrentText(str(row[10]))
                    inputFecha = str(row[11])
                    fechaConv = inputFecha.replace("/", "-")
                    qdate = QDate.fromString(fechaConv, "d-MM-yyyy")
                    self.inputFecha.setDate(qdate)

                # Consulta a la tabla Estructura_Ubicacion_Geografica
                sql = """SELECT DATUM, ZONA, X, Y, Z, ANG 
                        FROM Estructura_Ubicacion_Geografica 
                        WHERE COD_ESTRUCTURA = ?"""
                cur.execute(sql, (cod_estructura,))
                row = cur.fetchone()
                if row:
                    self.inputDatum.setText(row[0])
                    self.inputZona.setText(row[1])
                    self.inputX.setText(row[2])
                    self.inputY.setText(row[3])
                    self.inputZ.setText(row[4])
                    self.inputANG.setText(row[5])

                # Consulta a la tabla Estructura_Ubicacion_Plano_Planta_Subestacion
                sql = """SELECT COD_SE, X, Y, Z, ANG 
                        FROM Estructura_Ubicacion_Plano_Planta_Subestacion 
                        WHERE COD_ESTRUCTURA = ?"""
                cur.execute(sql, (cod_estructura,))
                row = cur.fetchone()
                if row:
                    self.inputSubestacion.setText(row[0])
                    self.inputX_2.setText(row[1])
                    self.inputY_2.setText(row[2])
                    self.inputZ_2.setText(row[3])
                    self.inputANG_2.setText(row[4])

                # Consulta a la tabla Estructura_Ubicacion_Plano_Planta_Central_Generacion
                sql = """SELECT COD_CENTRAL, X, Y, Z, ANG 
                        FROM Estructura_Ubicacion_Plano_Planta_Central_Generacion 
                        WHERE COD_ESTRUCTURA = ?"""
                cur.execute(sql, (cod_estructura,))
                row = cur.fetchone()
                if row:
                    self.inputCentral.setText(row[0])
                    self.inputX_3.setText(row[1])
                    self.inputY_3.setText(row[2])
                    self.inputZ_3.setText(row[3])
                    self.inputANG_3.setText(row[4])

            except Error as e:
                print("Error al consultar la base de datos: " + str(e))
            finally:
                cur.close()
                conn.close()
