from PySide2.QtWidgets import QMessageBox,QDialog, QWidget,QHeaderView,QTableWidgetItem,QAbstractItemView, QFileDialog,QCompleter
from PySide2.QtCore import Qt, QDate
from PySide2.QtGui import *
import sqlite3
from sqlite3 import Error
from views.new_transmision_tramo_linea import Ui_NewBook
from db.books import delete_ubicacion_tramo_linea,select_ubicacion_tramo_linea,buscar_usuario_acceso,insert_book_tramo_linea_transmision,insert_book_tramo_linea_transmision_ubicacion_geografica
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
        self.label.setStyleSheet("background-color: #114692;")
        self.inputCentral.setText(str(_codCentral))
        self.inputCentral.setEnabled(False)
        self.btnAddInterruptor.clicked.connect(self.open_new_window_tramo)
        self.addButton.clicked.connect(self.add_book)
        self.cancelButton.clicked.connect(self.close)
        self.populate_combobox()
        
        self.label_advertencia_dni.hide()
        self.label_nota_obligatoria.hide()

        #self.populate_comboboxPiso()
        if(self.Usuario!="admin"):
            print("NO ES ADMIN!!!")
            self.inputCodEmpresa.hide()
            self.label_empresa.hide()
        else:
            print("ES ADMIN!!!") 
            self.inputCodEmpresa.setText(self.Usuario)
            self.inputCodEmpresa.setEnabled(False)
        if _codigo is not None:
            print("----------NO ES EDIT-----------:"+str(_codigo))
            self.populate_inputs(_codigo)
            self.inputCodigo.setText(str(_codigo))
            self.inputCodigo.setEnabled(False)
            self.addButton.setText("GUARDAR")
        
        self.table_config()
        self.populate_table(select_ubicacion_tramo_linea(self.inputCentral.text(),self.inputCodigo.text()))
        #self.cancelButton.clicked.connect(self.close)
        self.btnDeleteInterruptor.clicked.connect(self.remove_book)
    
    def remove_book(self):
        selected_row = self.tableInterruptores.selectedItems()
        print("SELECT ROWWWWW: "+str(selected_row))
        if len(selected_row)!=0:
            respuesta=msg_boxes.alert_msgbox("Corfirmar Eliminar","¿Estas seguro de eliminar el registro?")
            if respuesta== QMessageBox.Yes:
                if selected_row:
                    book_id = str(selected_row[1].text())
                    row = selected_row[1].row()

                    if delete_ubicacion_tramo_linea(self.Usuario,self._codCentral,self.inputCodigo.text(),book_id):
                        self.tableInterruptores.removeRow(row)

    def table_config(self):
        column_headers = ("#","Secuencia","X","Y","Z")
        self.tableInterruptores.setColumnCount(len(column_headers))
        self.tableInterruptores.setHorizontalHeaderLabels(column_headers)
        self.tableInterruptores.setSelectionMode(QAbstractItemView.SingleSelection)
        stylesheet = "::section{Background-color:#114692;border:1px solid black;color: white;}"
        self.tableInterruptores.horizontalHeader().setStyleSheet(stylesheet)

        self.tableInterruptores.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableInterruptores.setStyleSheet("QTableWidget{ gridline-color:black;alternate-background-color: #E2DED0;}")
        self.tableInterruptores.setAlternatingRowColors(True)

        self.tableInterruptores.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableInterruptores.verticalHeader().setVisible(False)
        self.tableInterruptores.setColumnWidth(0,19)
        headerVertical = self.tableInterruptores.verticalHeader()
        headerVertical.resizeSections(QHeaderView.ResizeToContents)
        headerVertical.setStretchLastSection(True)

    def populate_table(self,data):
        if data is not None:
            self.tableInterruptores.setRowCount(len(data))
            print("REFRESH4")
            for index_row, row in enumerate(data):
                # Incrementamos el índice de fila en 1 para comenzar con el número de orden en 1
                order_number = index_row + 1
                
                # Establecemos el número de orden en la primera columna
                self.tableInterruptores.setItem(index_row, 0, QTableWidgetItem(str(order_number)))
                
                for index_cell, cell in enumerate(row):
                    # Llenamos los datos de la fila a partir de la segunda columna
                    self.tableInterruptores.setItem(index_row, index_cell + 1, QTableWidgetItem(str(cell)))
                    
                    if index_cell == 13:
                        itemx = self.tableInterruptores.item(index_row, index_cell + 1)  # Se ajusta el índice de la celda
                        print("EL ITEM ACTUAL ES: ", itemx)
                        if itemx.text() == "PENDIENTE":
                            itemx.setForeground(QBrush(QColor(255, 0, 0)))
                        else:
                            itemx.setForeground(QBrush(QColor(0, 0, 255)))

            print("REFRESH5")
            headerVertical = self.tableInterruptores.verticalHeader()
            headerVertical.resizeSections(QHeaderView.ResizeToContents)
            headerVertical.setStretchLastSection(True)

            #self.records_qty()
        else:
            print("¡Error! No se cargaron los datos correctamente.")
    def refresh_table_from_child_window(self):

        data = select_ubicacion_tramo_linea(self.inputCentral.text(),self.inputCodigo.text())
        self.populate_table(data)


    def open_new_window_tramo(self,codCentral):
        if(self.inputCodigo.isEnabled()):
            print("DEBE AGREGAR")
            msg_boxes.alert_msgbox_2("¡Error!","¡Primero debe agregar el Tramo de Línea!")
        else:
            from controllers.new_window_linea_tramo_ubicacion import NewBookWindow
            codCelda= self.inputCodigo.text()
            codCentral= self.inputCentral.text()
            window= NewBookWindow(self,codCelda,codCentral)
            window.exec_()
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

        inputNombre = self.inputCentral.text()
        inputNombre=inputNombre.strip()

        
        
        inputAltitud = self.inputAltitud.text()
        inputAltitud=inputAltitud.strip()

        inputLogitud = self.inputLogitud.text()
        inputLogitud=inputLogitud.strip()

        

        inputConductoresXFases = self.inputConductoresXFases.text()
        inputConductoresXFases=inputConductoresXFases.strip()

        inputSeccionConductor = self.inputSeccionConductor.text()
        inputSeccionConductor=inputSeccionConductor.strip()

        inputPotenciaN = self.inputPotenciaN.text()
        inputPotenciaN=inputPotenciaN.strip()

        inputCorrienteN = self.inputCorrienteN.text()
        inputCorrienteN=inputCorrienteN.strip()

        inputTensionN = self.inputTensionN.text()
        inputTensionN=inputTensionN.strip()

        inputTensionOpe = self.inputTensionOpe.text()
        inputTensionOpe=inputTensionOpe.strip()

        inputTensionAisl = self.inputTensionAisl.text()
        inputTensionAisl=inputTensionAisl.strip()

        inputResistencia = self.inputResistencia.text()
        inputResistencia=inputResistencia.strip()

        inputReactancia = self.inputReactancia.text()
        inputReactancia=inputReactancia.strip()

        inputSuceptancia = self.inputSuceptancia.text()
        inputSuceptancia=inputSuceptancia.strip()

        inputConductancia = self.inputConductancia.text()
        inputConductancia=inputConductancia.strip()

        

        inputSeccionCableG = self.inputSeccionCableG.text()
        inputSeccionCableG=inputSeccionCableG.strip()

        inputModulo = self.inputModulo.text()
        inputModulo=inputModulo.strip()

        inputFecha = self.inputFecha.text()
        inputFecha=inputFecha.strip()

        inputDatum = self.inputDatum.text()
        inputDatum=inputDatum.strip()

        inputZonaUTM = self.inputZonaUTM.text()
        inputZonaUTM=inputZonaUTM.strip()

        #inputSecuencia = self.inputSecuencia.text()
        #inputSecuencia=inputSecuencia.strip()
#
        #inputX = self.inputX.text()
        #inputX=inputX.strip()
#
        #inputY = self.inputY.text()
        #inputY=inputY.strip()
#
        #inputZ = self.inputZ.text()
        #inputZ=inputZ.strip()

        cbCalificacion = self.cbCalificacion.currentText()
        cbTipo = self.cbTipo.currentText()
        cbAreaOpe=self.cbAreaOpe.currentText()
        cbAreaDemanda=self.cbAreaDemanda.currentText()
        cbDispFases=self.cbDispFases.currentText()
        cbNCablesGuarda=self.cbNCablesGuarda.currentText()
        cbRegionGeografica=self.cbRegionGeografica.currentText()
        cbZona=self.cbZona.currentText()
        cbTipoRed=self.cbTipoRed.currentText()
        cbTipoConductor=self.cbTipoConductor.currentText()
        cbMatCable=self.cbMatCable.currentText()
        cbEstado=self.cbEstado.currentText()


        self.label_advertencia_dni.hide()

        #self.ActualizarVisitante(dni,visitante)
        if self.check_inputs():
            #new_path = shutil.copy(path, "book_files")
            self.label_nota_obligatoria.hide()
            
            data = (self.Usuario, inputNombre, inputCodigo, cbCalificacion, cbTipo, cbAreaDemanda, cbAreaOpe, cbRegionGeografica, cbZona, inputAltitud, cbTipoRed, inputLogitud, cbDispFases, inputConductoresXFases, cbTipoConductor, inputSeccionConductor, inputPotenciaN, inputCorrienteN, inputTensionN, inputTensionOpe, inputTensionAisl, inputResistencia, inputReactancia, inputSuceptancia, inputConductancia, cbNCablesGuarda, cbMatCable, inputSeccionCableG, inputModulo, cbEstado, inputFecha, inputDatum, inputZonaUTM)
            if insert_book_tramo_linea_transmision(data):
                #data2 = (self.Usuario, inputNombre, inputCodigo, inputSecuencia, inputX, inputY, inputZ)
                #insert_book_tramo_linea_transmision_ubicacion_geografica(data2)
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

        # Llenar el combo de Calificación
        cb_options_calificacion = ("", "Principal", "Secundario", "Garantizado", "Complementario")
        self.cbCalificacion.addItems(cb_options_calificacion)

        # Llenar el combo de Tipo de circuito
        cb_options_tipo_circuito = ("", "Derivación", "Troncal")
        self.cbTipo.addItems(cb_options_tipo_circuito)

        # Llenar el combo de Área Operativa
        cb_options_area_demanda = ("", "Ad1", "Ad2", "Ad3", "Ad4")
        self.cbAreaDemanda.addItems(cb_options_area_demanda)

        # Llenar el combo de Área Operativa
        cb_options_area_operativa = ("", "Norte", "Centro", "Sur", "Lima")
        self.cbAreaOpe.addItems(cb_options_area_operativa)

        # Llenar el combo de Región geográfica
        cb_options_region_geografica = ("", "Costa", "Sierra", "Selva")
        self.cbRegionGeografica.addItems(cb_options_region_geografica)

        # Llenar el combo de Zona
        cb_options_zona = ("", "Urbana", "Rural")
        self.cbZona.addItems(cb_options_zona)

        # Llenar el combo de Disposición de fases
        cb_options_tipo_red = ("", "Aéreo", "Subterréneo")
        self.cbTipoRed.addItems(cb_options_tipo_red)

        # Llenar el combo de Disposición de fases
        cb_options_disp_fases = ("", "Vertical", "Horizontal","Triangular")
        self.cbDispFases.addItems(cb_options_disp_fases)

        # Llenar el combo de Disposición de fases
        cb_options_n_cables = ("", "Ninguno", "Uno","Dos")
        self.cbNCablesGuarda.addItems(cb_options_n_cables)

        # Llenar el combo de Tipo de conductor
        cb_options_tipo_conductor = ("", "AAAC", "ACSR", "ACAR", "AAACE", "AASC", "ALDREY", "ALMELEC", "Cable de Cobre", "Cable de Aluminio")
        self.cbTipoConductor.addItems(cb_options_tipo_conductor)

        # Llenar el combo de Material del cable de guarda
        cb_options_material_guarda = ("", "Acero Galvanizado", "Alumoweld (Acero aleado con aluminio)", "Aleación de Aluminio", "Aluminio con Acero reforzado")
        self.cbMatCable.addItems(cb_options_material_guarda)

        # Llenar el combo de Estado
        cb_options_estado = ("", "Nuevo", "Existente", "Eliminado", "Modificado", "Proyectado")
        self.cbEstado.addItems(cb_options_estado)

        

    
    def config_comboBoxes(self):
        font1 = QFont()
        font1.setPointSize(12)
        
    def populate_inputs(self, cod_tramo):
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

                # Consulta a la tabla Tramo_Linea_Transmision
                sql = """SELECT COD_LINEA, COD_TRAMO, COD_CALIFICACION, TIPO_CIRCUITO, COD_AREA, AREA_OPERATIVA, REGION_GEOGRAFICA,
                                ZONA, ALTITUD, TIPO_RED, LONGITUD, DISPOSICION_FASES, NUM_COND_X_FASE, TIPO_CONDUCTOR, SECCION_CONDUCTOR,
                                POTENCIA_NOM, CORRIENTE_NOM, TENSION_NOM, TENSION_OPERACION, TENSION_AISLAMIENTO, R1_TRAMO, X1_TRAMO,
                                B1_TRAMO, G1_TRAMO, NUM_CABLE_GUARDA, MAT_CABLE_GUARDA, SECCION_CABLE_GUARDA, COD_MODULO, ESTADO,
                                FECHA_ALTA, DATUM_UTM, ZONA_UTM, COD_EMP
                        FROM Tramo_Linea_Transmision 
                        WHERE COD_TRAMO = ?"""
                cur.execute(sql, (cod_tramo,))
                row = cur.fetchone()
                print("CODIGO DE LINEA: "+str(row[0]))
                print("CODIGO DE TRAMO: "+str(row[1]))
                if row:
                    inputFecha = str(row[29])
                    self.inputCodigo.setText(str(row[1]))
                    self.inputCentral.setText(str(row[0]))
                    self.cbCalificacion.setCurrentText(str(row[2]))
                    self.cbTipo.setCurrentText(str(row[3]))
                    
                    self.cbAreaOpe.setCurrentText(str(row[5]))
                    self.cbRegionGeografica.setCurrentText(str(row[6]))
                    self.cbZona.setCurrentText(str(row[7]))
                    self.inputAltitud.setText(str(row[8]))
                    self.cbTipoRed.setCurrentText(str(row[9]))
                    self.inputLogitud.setText(str(row[10]))
                    
                    self.inputConductoresXFases.setText(str(row[12]))
                    self.cbTipoConductor.setCurrentText(str(row[13]))
                    self.inputSeccionConductor.setText(str(row[14]))
                    self.inputPotenciaN.setText(str(row[15]))
                    self.inputCorrienteN.setText(str(row[16]))
                    self.inputTensionN.setText(str(row[17]))
                    self.inputTensionOpe.setText(str(row[18]))
                    self.inputTensionAisl.setText(str(row[19]))
                    self.inputResistencia.setText(str(row[20]))
                    self.inputReactancia.setText(str(row[21]))
                    self.inputSuceptancia.setText(str(row[22]))
                    self.inputConductancia.setText(str(row[23]))
                    
                    self.cbMatCable.setCurrentText(str(row[25]))
                    self.inputSeccionCableG.setText(str(row[26]))
                    self.inputModulo.setText(str(row[27]))
                    self.cbEstado.setCurrentText(str(row[28]))
                    fechaConv = inputFecha.replace("/", "-")
                    qdate = QDate.fromString(fechaConv, "d-MM-yyyy")
                    self.inputFecha.setDate(qdate)
                    self.inputDatum.setText(str(row[30]))
                    self.inputZonaUTM.setText(str(row[31]))
                    self.inputCodEmpresa.setText(str(row[32]))

                    self.cbAreaDemanda.setCurrentText(str(row[4]))
                    self.cbDispFases.setCurrentText(str(row[11]))
                    self.cbNCablesGuarda.setCurrentText(str(row[24]))
                ## Consulta a la tabla Tramo_Linea_Vertice_Ubicacion_Geografica
                #sql = """SELECT SECUENCIA, X, Y, Z
                #        FROM Tramo_Linea_Vertice_Ubicacion_Geografica
                #        WHERE COD_TRAMO = ?"""
                #cur.execute(sql, (cod_tramo,))
                #row = cur.fetchone()
                #if row:
                #    self.inputSecuencia.setText(row[0])
                #    self.inputX.setText(row[1])
                #    self.inputY.setText(row[2])
                #    self.inputZ.setText(row[3])

            except Error as e:
                print("Error al consultar la base de datos: " + str(e))
            finally:
                cur.close()
                conn.close()
