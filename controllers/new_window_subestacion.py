from PySide2.QtWidgets import QDialog,QMessageBox,QPushButton,QTableWidgetItem, QWidget, QFileDialog,QCompleter,QAbstractItemView,QHeaderView
from PySide2.QtCore import Qt, QDate
from PySide2.QtGui import *
import sqlite3
from sqlite3 import Error
from views.new_transmision_subestacion import Ui_NewBook
from db.books import buscar_usuario_acceso,select_cod_compensador_sub,delete_book_compensador,delete_book_Conductor,delete_book_Bobina_Bloqueo,delete_book_Transformador_Medicion,delete_book_Pararrayo,delete_book_Transformador_Potencia,delete_book_Celda,delete_book_Portico,delete_book_Barra,insert_book_subestacion,insert_book_subestacion_coordenadas_geograficas,insert_book_subestacion_plano_planta,select_cod_barras_sub,select_cod_porticos_sub,select_cod_celdas_sub,select_cod_transp_sub,select_cod_pararrayos_sub,select_cod_transm_sub,select_cod_bobinas_sub,select_cod_conductor_sub
from PySide2 import QtCore
from pys2_msgboxes import msg_boxes
from datetime import date, datetime

class NewBookWindow(QDialog,Ui_NewBook):
    def __init__(self, parent=None,_codCentral=None):
        print("CODIGO CENTRAL!: "+str(_codCentral))
        self._codCentral=_codCentral
        super().__init__(parent)
        self.parent = parent
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)
        self.Usuario= buscar_usuario_acceso();
        self.inputDatum.setText("WGS84")
        self.inputDatum.setEnabled(False)
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
        if _codCentral is not None:
            print("----------NO ES EDIT-----------:"+str(_codCentral))
            self.populate_inputs(_codCentral)
            self.refresh_table_from_child_window()
            self.inputCodigo.setEnabled(False)
            self.addButton.setText("GUARDAR")

        self.btnCoordenadas.clicked.connect(self.open_new_window_coordenadas)
        self.btnPlano.clicked.connect(self.open_new_window_plano)

        #self.btnCoordenadas.clicked.connect(self.open_new_window_coordenadas)
        #self.btnPlano.clicked.connect(self.open_new_window_plano)
        self.btnAddCeldas.clicked.connect(self.open_add_celdas)
        self.btnAddBarras.clicked.connect(self.open_add_barras)
        self.btnAddPorticos.clicked.connect(self.open_add_porticos)
        #self.btnAddInterruptor.clicked.connect(self.open_add_interruptor)
        #self.btnAddSeccionador.clicked.connect(self.open_add_seccionador)
        self.btnAddTransformadores.clicked.connect(self.open_add_transformador)
        self.btnAddPararrayo.clicked.connect(self.open_add_pararrayo)
        self.btnAddTransfMed.clicked.connect(self.open_add_transformacion_medicion)
        self.btnAddConductores.clicked.connect(self.open_add_conductor)
        self.btnAddBobina.clicked.connect(self.open_add_bobina)
        self.btnAddCompensador.clicked.connect(self.open_add_compensador)
        
        self.btnDeleteCeldas.clicked.connect(self.remove_book_celda)
        self.btnDeleteBarras.clicked.connect(self.remove_book_barra)
        self.btnDeletePorticos.clicked.connect(self.remove_book_portico)
        self.btnDeleteTransformador.clicked.connect(self.remove_book_transformador)
        self.btnDeletePararrayo.clicked.connect(self.remove_book_pararrayo)
        self.btnDeleteTransfMed.clicked.connect(self.remove_book_medicion)
        self.btnDeleteBobina.clicked.connect(self.remove_book_bobina)
        self.btnDeleteConductor.clicked.connect(self.remove_book_conductor)
        self.btnDeleteCompensador.clicked.connect(self.remove_book_compensador)

        
        #self.populate_comboboxEstado()
        #self.populate_inputs()
        #self.config_comboBoxes()

        idcodCentral= self.inputCodigo.text()           
        self.table_config_barras_sub()
        self.populate_table_barras_sub(select_cod_barras_sub(idcodCentral))

        self.table_config_porticos_sub()
        self.populate_table_porticos_sub(select_cod_porticos_sub(idcodCentral))

        self.table_config_celdas_sub()
        self.populate_table_celdas_sub(select_cod_celdas_sub(idcodCentral))

        self.table_config_transp_sub()
        self.populate_table_transp_sub(select_cod_transp_sub(idcodCentral))

        self.table_config_pararrayos_sub()
        self.populate_table_pararrayos_sub(select_cod_pararrayos_sub(idcodCentral))

        self.table_config_transm_sub()
        self.populate_table_transm_sub(select_cod_transm_sub(idcodCentral))

        self.table_config_bobinas_sub()
        self.populate_table_bobinas_sub(select_cod_bobinas_sub(idcodCentral))

        self.table_config_conductor_sub()
        self.populate_table_conductor_sub(select_cod_conductor_sub(idcodCentral))

        self.table_config_compensador_sub()
        self.populate_table_compensador_sub(select_cod_compensador_sub(idcodCentral))

        self.table_config_celdas_sub()
        self.populate_table_celdas_sub(select_cod_celdas_sub(idcodCentral))

        self.addButton.clicked.connect(self.add_book)
        self.cancelButton.clicked.connect(self.close)

        self.tableBarras.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableBarras.verticalHeader().setVisible(False)
        self.tableBarras.setColumnWidth(0,19)
        headerVertical = self.tableBarras.verticalHeader()
        headerVertical.resizeSections(QHeaderView.ResizeToContents)
        headerVertical.setStretchLastSection(True)
        self.tableBarras.doubleClicked.connect(lambda: self.FilaSeleccionadaBarras())

        self.tablePorticos.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tablePorticos.verticalHeader().setVisible(False)
        self.tablePorticos.setColumnWidth(0,19)
        headerVertical = self.tablePorticos.verticalHeader()
        headerVertical.resizeSections(QHeaderView.ResizeToContents)
        headerVertical.setStretchLastSection(True)
        self.tablePorticos.doubleClicked.connect(lambda: self.FilaSeleccionadaPorticos())

        self.tableCeldas.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableCeldas.verticalHeader().setVisible(False)
        self.tableCeldas.setColumnWidth(0,19)
        headerVertical = self.tableCeldas.verticalHeader()
        headerVertical.resizeSections(QHeaderView.ResizeToContents)
        headerVertical.setStretchLastSection(True)
        self.tableCeldas.doubleClicked.connect(lambda: self.FilaSeleccionadaCeldas())

        self.tableTransformador.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableTransformador.verticalHeader().setVisible(False)
        self.tableTransformador.setColumnWidth(0,19)
        headerVertical = self.tableTransformador.verticalHeader()
        headerVertical.resizeSections(QHeaderView.ResizeToContents)
        headerVertical.setStretchLastSection(True)
        self.tableTransformador.doubleClicked.connect(lambda: self.FilaSeleccionadaTransfPotencia())

        self.tablePararrayo.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tablePararrayo.verticalHeader().setVisible(False)
        self.tablePararrayo.setColumnWidth(0,19)
        headerVertical = self.tablePararrayo.verticalHeader()
        headerVertical.resizeSections(QHeaderView.ResizeToContents)
        headerVertical.setStretchLastSection(True)
        self.tablePararrayo.doubleClicked.connect(lambda: self.FilaSeleccionadaPararrayos())

        self.tableMedicion.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableMedicion.verticalHeader().setVisible(False)
        self.tableMedicion.setColumnWidth(0,19)
        headerVertical = self.tableMedicion.verticalHeader()
        headerVertical.resizeSections(QHeaderView.ResizeToContents)
        headerVertical.setStretchLastSection(True)
        self.tableMedicion.doubleClicked.connect(lambda: self.FilaSeleccionadaTranfMedicion())

        self.tableBobina.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableBobina.verticalHeader().setVisible(False)
        self.tableBobina.setColumnWidth(0,19)
        headerVertical = self.tableBobina.verticalHeader()
        headerVertical.resizeSections(QHeaderView.ResizeToContents)
        headerVertical.setStretchLastSection(True)
        self.tableBobina.doubleClicked.connect(lambda: self.FilaSeleccionadaBobinas())

        self.tableConductor.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableConductor.verticalHeader().setVisible(False)
        self.tableConductor.setColumnWidth(0,19)
        headerVertical = self.tableConductor.verticalHeader()
        headerVertical.resizeSections(QHeaderView.ResizeToContents)
        headerVertical.setStretchLastSection(True)
        self.tableConductor.doubleClicked.connect(lambda: self.FilaSeleccionadaConductores())

        self.tableCompensador.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableCompensador.verticalHeader().setVisible(False)
        self.tableCompensador.setColumnWidth(0,19)
        headerVertical = self.tableCompensador.verticalHeader()
        headerVertical.resizeSections(QHeaderView.ResizeToContents)
        headerVertical.setStretchLastSection(True)
        self.tableCompensador.doubleClicked.connect(lambda: self.FilaSeleccionadaCompensadores())

        

    def open_add_celdas(self,codCentral):
        if(self.inputCodigo.isEnabled()):
            print("DEBE AGREGAR")
            msg_boxes.alert_msgbox_2("¡Error!","¡Primero debe agregar la Subestación!")
        else:        
            from controllers.new_window_subestacion_celda import NewBookWindow
            codCentral= self.inputCodigo.text()
            window= NewBookWindow(self,codCentral)
            window.exec_()

    def open_add_barras(self,codCentral):
        if(self.inputCodigo.isEnabled()):
            print("DEBE AGREGAR")
            msg_boxes.alert_msgbox_2("¡Error!","¡Primero debe agregar la Subestación!")
        else:        
            from controllers.new_window_subestacion_barra import NewBookWindow
            codCentral= self.inputCodigo.text()
            window= NewBookWindow(self,codCentral)
            window.exec_()
#
    def open_add_porticos(self,codCentral):
        if(self.inputCodigo.isEnabled()):
            print("DEBE AGREGAR")
            msg_boxes.alert_msgbox_2("¡Error!","¡Primero debe agregar la Subestación!")
        else:        
            from controllers.new_window_subestacion_portico import NewBookWindow
            codCentral= self.inputCodigo.text()
            window= NewBookWindow(self,codCentral)
            window.exec_()
#
    def open_add_interruptor(self,codCentral):
        if(self.inputCodigo.isEnabled()):
            print("DEBE AGREGAR")
            msg_boxes.alert_msgbox_2("¡Error!","¡Primero debe agregar la Subestación!")
        else:        
            from controllers.new_window_subestacion_interruptor import NewBookWindow
            codCentral= self.inputCodigo.text()
            window= NewBookWindow(self,codCentral)
            window.exec_()

    def open_add_seccionador(self,codCentral):
        if(self.inputCodigo.isEnabled()):
            print("DEBE AGREGAR")
            msg_boxes.alert_msgbox_2("¡Error!","¡Primero debe agregar la Subestación!")
        else:        
            from controllers.new_window_subestacion_seccionador import NewBookWindow
            codCentral= self.inputCodigo.text()
            window= NewBookWindow(self,codCentral)
            window.exec_()

    def open_add_transformador(self,codCentral):
        if(self.inputCodigo.isEnabled()):
            print("DEBE AGREGAR")
            msg_boxes.alert_msgbox_2("¡Error!","¡Primero debe agregar la Subestación!")
        else:        
            from controllers.new_window_subestacion_transformador import NewBookWindow
            codCentral= self.inputCodigo.text()
            window= NewBookWindow(self,codCentral)
            window.exec_()
            
    def open_add_pararrayo(self,codCentral):
        if(self.inputCodigo.isEnabled()):
            print("DEBE AGREGAR")
            msg_boxes.alert_msgbox_2("¡Error!","¡Primero debe agregar la Subestación!")
        else:        
            from controllers.new_window_subestacion_pararrayo import NewBookWindow
            codCentral= self.inputCodigo.text()
            window= NewBookWindow(self,codCentral)
            window.exec_()

    def open_add_transformacion_medicion(self,codCentral):
        if(self.inputCodigo.isEnabled()):
            print("DEBE AGREGAR")
            msg_boxes.alert_msgbox_2("¡Error!","¡Primero debe agregar la Subestación!")
        else:        
            from controllers.new_window_subestacion_transformador_medicion import NewBookWindow
            codCentral= self.inputCodigo.text()
            window= NewBookWindow(self,codCentral)
            window.exec_()

    def open_add_conductor(self,codCentral):
        if(self.inputCodigo.isEnabled()):
            print("DEBE AGREGAR")
            msg_boxes.alert_msgbox_2("¡Error!","¡Primero debe agregar la Subestación!")
        else:        
            from controllers.new_window_subestacion_conductor import NewBookWindow
            codCentral= self.inputCodigo.text()
            window= NewBookWindow(self,codCentral)
            window.exec_()

    def open_add_bobina(self,codCentral):
        if(self.inputCodigo.isEnabled()):
            print("DEBE AGREGAR")
            msg_boxes.alert_msgbox_2("¡Error!","¡Primero debe agregar la Subestación!")
        else:        
            from controllers.new_window_subestacion_bobina import NewBookWindow
            codCentral= self.inputCodigo.text()
            window= NewBookWindow(self,codCentral)
            window.exec_()

    def open_add_compensador(self,codCentral):
        if(self.inputCodigo.isEnabled()):
            print("DEBE AGREGAR")
            msg_boxes.alert_msgbox_2("¡Error!","¡Primero debe agregar la Subestación!")
        else:        
            from controllers.new_window_subestacion_compensador import NewBookWindow
            codCentral= self.inputCodigo.text()
            window= NewBookWindow(self,codCentral)
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

        inputNombre = self.inputNombre.text()
        inputNombre=inputNombre.strip()

        inputAltitud = self.inputAltitud.text()
        inputAltitud=inputAltitud.strip()

        inputDireccion = self.inputDireccion.text()
        inputDireccion=inputDireccion.strip()

        inputTelefono = self.inputTelefono.text()
        inputTelefono=inputTelefono.strip()

        inputServicios = self.inputServicios.text()
        inputServicios=inputServicios.strip()

        inputObras = self.inputObras.text()
        inputObras=inputObras.strip()

        inputEdificios = self.inputEdificios.text()
        inputEdificios=inputEdificios.strip()

        inputRed = self.inputRed.text()
        inputRed=inputRed.strip()

        inputInstalaciones = self.inputInstalaciones.text()
        inputInstalaciones=inputInstalaciones.strip()

        inputFecha = self.inputFecha.text()

        inputDatum = self.inputDatum.text()
        inputDatum=inputDatum.strip()

        inputZona = self.inputZona.text()
        inputZona=inputZona.strip()

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
#
        #inputSecuencia_2 = self.inputSecuencia_2.text()
        #inputSecuencia_2=inputSecuencia_2.strip()
#
        #inputX_2 = self.inputX_2.text()
        #inputX_2=inputX_2.strip()
#
        #inputY_2 = self.inputY_2.text()
        #inputY_2=inputY_2.strip()
#
        #inputZ_2 = self.inputZ_2.text()
        #inputZ_2=inputZ_2.strip()

        cbCalificacion = self.cbCalificacion.currentText()
        cbTipoSistema = self.cbTipoSistema.currentText()
        cbAreaDemanda = self.cbAreaDemanda.currentText()
        cbTecnologia = self.cbTecnologia.currentText()
        cbFuncion = self.cbFuncion.currentText()
        cbAtendida = self.cbAtendida.currentText()
        cbAreaOperativa = self.cbAreaOperativa.currentText()
        cbRegion = self.cbRegion.currentText()
        cbZona = self.cbZona.currentText()
        cbEstado = self.cbEstado.currentText()

        self.label_advertencia_dni.hide()

        self.ast_aquienvisita.hide()
        #self.ActualizarVisitante(dni,visitante)
        if self.check_inputs():
            #new_path = shutil.copy(path, "book_files")
            self.label_nota_obligatoria.hide()
            data = (self.Usuario,inputCodigo,inputNombre,cbCalificacion,cbTipoSistema,cbAreaDemanda,cbAreaOperativa,cbRegion,cbZona,inputAltitud,cbTecnologia,cbFuncion,cbAtendida,inputDireccion,inputTelefono,inputServicios,inputObras,inputEdificios,inputRed,inputInstalaciones,cbEstado,inputFecha,inputDatum,inputZona)
            #self.AnadirNuevos(dni,visitante,entidadempresa,motivovisita,aquienvisita,autoriza,areavisitada) 
            if insert_book_subestacion(data):
                #self.clean_inputs()
                #data2 = (self.Usuario, inputCodigo, inputSecuencia, inputX,inputY,inputZ )
                #data3 = (self.Usuario, inputCodigo, inputSecuencia_2, inputX_2,inputY_2,inputZ_2 )
#
                #insert_book_subestacion_coordenadas_geograficas(data2)
                #insert_book_subestacion_plano_planta(data3)

                msg_boxes.correct_msgbox("¡Registro Exitoso!","¡Se registró exitosamente!")
                self.inputCodigo.setEnabled(False)
                self.addButton.setText("Guardar")
                self.parent.refresh_table_from_child_window_subestacion()
                #self.close()
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

    

    def table_config_barras_sub(self):
        column_headers = ("#","Código")
        self.tableBarras.setColumnCount(len(column_headers))
        self.tableBarras.setHorizontalHeaderLabels(column_headers)
        self.tableBarras.setSelectionMode(QAbstractItemView.SingleSelection)
        stylesheet = "::section{Background-color:#114692;border:1px solid black;color: white;}"
        self.tableBarras.horizontalHeader().setStyleSheet(stylesheet)

        self.tableBarras.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableBarras.setStyleSheet("QTableWidget{ gridline-color:black;alternate-background-color: #E2DED0;}")
        self.tableBarras.setAlternatingRowColors(True)
    
    def table_config_porticos_sub(self):
        column_headers = ("#","Código")
        self.tablePorticos.setColumnCount(len(column_headers))
        self.tablePorticos.setHorizontalHeaderLabels(column_headers)
        self.tablePorticos.setSelectionMode(QAbstractItemView.SingleSelection)
        stylesheet = "::section{Background-color:#114692;border:1px solid black;color: white;}"
        self.tablePorticos.horizontalHeader().setStyleSheet(stylesheet)

        self.tablePorticos.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tablePorticos.setStyleSheet("QTableWidget{ gridline-color:black;alternate-background-color: #E2DED0;}")
        self.tablePorticos.setAlternatingRowColors(True)

    def table_config_celdas_sub(self):
        column_headers = ("#","Código")
        self.tableCeldas.setColumnCount(len(column_headers))
        self.tableCeldas.setHorizontalHeaderLabels(column_headers)
        self.tableCeldas.setSelectionMode(QAbstractItemView.SingleSelection)
        stylesheet = "::section{Background-color:#114692;border:1px solid black;color: white;}"
        self.tableCeldas.horizontalHeader().setStyleSheet(stylesheet)

        self.tableCeldas.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableCeldas.setStyleSheet("QTableWidget{ gridline-color:black;alternate-background-color: #E2DED0;}")
        self.tableCeldas.setAlternatingRowColors(True)

    def table_config_transp_sub(self):
        column_headers = ("#","Código")
        self.tableTransformador.setColumnCount(len(column_headers))
        self.tableTransformador.setHorizontalHeaderLabels(column_headers)
        self.tableTransformador.setSelectionMode(QAbstractItemView.SingleSelection)
        stylesheet = "::section{Background-color:#114692;border:1px solid black;color: white;}"
        self.tableTransformador.horizontalHeader().setStyleSheet(stylesheet)

        self.tableTransformador.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableTransformador.setStyleSheet("QTableWidget{ gridline-color:black;alternate-background-color: #E2DED0;}")
        self.tableTransformador.setAlternatingRowColors(True)

    def table_config_pararrayos_sub(self):
        column_headers = ("#","Código")
        self.tablePararrayo.setColumnCount(len(column_headers))
        self.tablePararrayo.setHorizontalHeaderLabels(column_headers)
        self.tablePararrayo.setSelectionMode(QAbstractItemView.SingleSelection)
        stylesheet = "::section{Background-color:#114692;border:1px solid black;color: white;}"
        self.tablePararrayo.horizontalHeader().setStyleSheet(stylesheet)

        self.tablePararrayo.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tablePararrayo.setStyleSheet("QTableWidget{ gridline-color:black;alternate-background-color: #E2DED0;}")
        self.tablePararrayo.setAlternatingRowColors(True)

    def table_config_transm_sub(self):
        column_headers = ("#","Código")
        self.tableMedicion.setColumnCount(len(column_headers))
        self.tableMedicion.setHorizontalHeaderLabels(column_headers)
        self.tableMedicion.setSelectionMode(QAbstractItemView.SingleSelection)
        stylesheet = "::section{Background-color:#114692;border:1px solid black;color: white;}"
        self.tableMedicion.horizontalHeader().setStyleSheet(stylesheet)

        self.tableMedicion.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableMedicion.setStyleSheet("QTableWidget{ gridline-color:black;alternate-background-color: #E2DED0;}")
        self.tableMedicion.setAlternatingRowColors(True)

    def table_config_bobinas_sub(self):
        column_headers = ("#","Código")
        self.tableBobina.setColumnCount(len(column_headers))
        self.tableBobina.setHorizontalHeaderLabels(column_headers)
        self.tableBobina.setSelectionMode(QAbstractItemView.SingleSelection)
        stylesheet = "::section{Background-color:#114692;border:1px solid black;color: white;}"
        self.tableBobina.horizontalHeader().setStyleSheet(stylesheet)

        self.tableBobina.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableBobina.setStyleSheet("QTableWidget{ gridline-color:black;alternate-background-color: #E2DED0;}")
        self.tableBobina.setAlternatingRowColors(True)

    def table_config_conductor_sub(self):
        column_headers = ("#","Código")
        self.tableConductor.setColumnCount(len(column_headers))
        self.tableConductor.setHorizontalHeaderLabels(column_headers)
        self.tableConductor.setSelectionMode(QAbstractItemView.SingleSelection)
        stylesheet = "::section{Background-color:#114692;border:1px solid black;color: white;}"
        self.tableConductor.horizontalHeader().setStyleSheet(stylesheet)

        self.tableConductor.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableConductor.setStyleSheet("QTableWidget{ gridline-color:black;alternate-background-color: #E2DED0;}")
        self.tableConductor.setAlternatingRowColors(True)

    def table_config_compensador_sub(self):
        column_headers = ("#","Código")
        self.tableCompensador.setColumnCount(len(column_headers))
        self.tableCompensador.setHorizontalHeaderLabels(column_headers)
        self.tableCompensador.setSelectionMode(QAbstractItemView.SingleSelection)
        stylesheet = "::section{Background-color:#114692;border:1px solid black;color: white;}"
        self.tableCompensador.horizontalHeader().setStyleSheet(stylesheet)

        self.tableCompensador.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableCompensador.setStyleSheet("QTableWidget{ gridline-color:black;alternate-background-color: #E2DED0;}")
        self.tableCompensador.setAlternatingRowColors(True)

    def populate_table_barras_sub(self,data):
        if data is not None:
            self.tableBarras.setRowCount(len(data))
            print("REFRESH4")
            for index_row, row in enumerate(data):
                # Incrementamos el índice de fila en 1 para comenzar con el número de orden en 1
                order_number = index_row + 1
                
                # Establecemos el número de orden en la primera columna
                self.tableBarras.setItem(index_row, 0, QTableWidgetItem(str(order_number)))
                
                for index_cell, cell in enumerate(row):
                    # Llenamos los datos de la fila a partir de la segunda columna
                    self.tableBarras.setItem(index_row, index_cell + 1, QTableWidgetItem(str(cell)))
                    
                    if index_cell == 13:
                        itemx = self.tableBarras.item(index_row, index_cell + 1)  # Se ajusta el índice de la celda
                        print("EL ITEM ACTUAL ES: ", itemx)
                        if itemx.text() == "PENDIENTE":
                            itemx.setForeground(QBrush(QColor(255, 0, 0)))
                        else:
                            itemx.setForeground(QBrush(QColor(0, 0, 255)))

            print("REFRESH5")
            headerVertical = self.tableBarras.verticalHeader()
            headerVertical.resizeSections(QHeaderView.ResizeToContents)
            headerVertical.setStretchLastSection(True)

            #self.records_qty()
        else:
            print("¡Error! No se cargaron los datos correctamente.")
    
    def populate_table_porticos_sub(self,data):
        if data is not None:
            self.tablePorticos.setRowCount(len(data))
            print("REFRESH4")
            for index_row, row in enumerate(data):
                # Incrementamos el índice de fila en 1 para comenzar con el número de orden en 1
                order_number = index_row + 1
                
                # Establecemos el número de orden en la primera columna
                self.tablePorticos.setItem(index_row, 0, QTableWidgetItem(str(order_number)))
                
                for index_cell, cell in enumerate(row):
                    # Llenamos los datos de la fila a partir de la segunda columna
                    self.tablePorticos.setItem(index_row, index_cell + 1, QTableWidgetItem(str(cell)))
                    
                    if index_cell == 13:
                        itemx = self.tablePorticos.item(index_row, index_cell + 1)  # Se ajusta el índice de la celda
                        print("EL ITEM ACTUAL ES: ", itemx)
                        if itemx.text() == "PENDIENTE":
                            itemx.setForeground(QBrush(QColor(255, 0, 0)))
                        else:
                            itemx.setForeground(QBrush(QColor(0, 0, 255)))

            print("REFRESH5")
            headerVertical = self.tablePorticos.verticalHeader()
            headerVertical.resizeSections(QHeaderView.ResizeToContents)
            headerVertical.setStretchLastSection(True)

            #self.records_qty()
        else:
            print("¡Error! No se cargaron los datos correctamente.")
    
    def populate_table_celdas_sub(self,data):
        if data is not None:
            self.tableCeldas.setRowCount(len(data))
            print("REFRESH4")
            for index_row, row in enumerate(data):
                # Incrementamos el índice de fila en 1 para comenzar con el número de orden en 1
                order_number = index_row + 1
                
                # Establecemos el número de orden en la primera columna
                self.tableCeldas.setItem(index_row, 0, QTableWidgetItem(str(order_number)))
                
                for index_cell, cell in enumerate(row):
                    # Llenamos los datos de la fila a partir de la segunda columna
                    self.tableCeldas.setItem(index_row, index_cell + 1, QTableWidgetItem(str(cell)))
                    
                    if index_cell == 13:
                        itemx = self.tableCeldas.item(index_row, index_cell + 1)  # Se ajusta el índice de la celda
                        print("EL ITEM ACTUAL ES: ", itemx)
                        if itemx.text() == "PENDIENTE":
                            itemx.setForeground(QBrush(QColor(255, 0, 0)))
                        else:
                            itemx.setForeground(QBrush(QColor(0, 0, 255)))

            print("REFRESH5")
            headerVertical = self.tableCeldas.verticalHeader()
            headerVertical.resizeSections(QHeaderView.ResizeToContents)
            headerVertical.setStretchLastSection(True)

            #self.records_qty()
        else:
            print("¡Error! No se cargaron los datos correctamente.")
    
    def populate_table_transp_sub(self,data):
        if data is not None:
            self.tableTransformador.setRowCount(len(data))
            print("REFRESH4")
            for index_row, row in enumerate(data):
                # Incrementamos el índice de fila en 1 para comenzar con el número de orden en 1
                order_number = index_row + 1
                
                # Establecemos el número de orden en la primera columna
                self.tableTransformador.setItem(index_row, 0, QTableWidgetItem(str(order_number)))
                
                for index_cell, cell in enumerate(row):
                    # Llenamos los datos de la fila a partir de la segunda columna
                    self.tableTransformador.setItem(index_row, index_cell + 1, QTableWidgetItem(str(cell)))
                    
                    if index_cell == 13:
                        itemx = self.tableTransformador.item(index_row, index_cell + 1)  # Se ajusta el índice de la celda
                        print("EL ITEM ACTUAL ES: ", itemx)
                        if itemx.text() == "PENDIENTE":
                            itemx.setForeground(QBrush(QColor(255, 0, 0)))
                        else:
                            itemx.setForeground(QBrush(QColor(0, 0, 255)))

            print("REFRESH5")
            headerVertical = self.tableTransformador.verticalHeader()
            headerVertical.resizeSections(QHeaderView.ResizeToContents)
            headerVertical.setStretchLastSection(True)

            #self.records_qty()
        else:
            print("¡Error! No se cargaron los datos correctamente.")
    
    def populate_table_pararrayos_sub(self,data):
        if data is not None:
            self.tablePararrayo.setRowCount(len(data))
            print("REFRESH4")
            for index_row, row in enumerate(data):
                # Incrementamos el índice de fila en 1 para comenzar con el número de orden en 1
                order_number = index_row + 1
                
                # Establecemos el número de orden en la primera columna
                self.tablePararrayo.setItem(index_row, 0, QTableWidgetItem(str(order_number)))
                
                for index_cell, cell in enumerate(row):
                    # Llenamos los datos de la fila a partir de la segunda columna
                    self.tablePararrayo.setItem(index_row, index_cell + 1, QTableWidgetItem(str(cell)))
                    
                    if index_cell == 13:
                        itemx = self.tablePararrayo.item(index_row, index_cell + 1)  # Se ajusta el índice de la celda
                        print("EL ITEM ACTUAL ES: ", itemx)
                        if itemx.text() == "PENDIENTE":
                            itemx.setForeground(QBrush(QColor(255, 0, 0)))
                        else:
                            itemx.setForeground(QBrush(QColor(0, 0, 255)))

            print("REFRESH5")
            headerVertical = self.tablePararrayo.verticalHeader()
            headerVertical.resizeSections(QHeaderView.ResizeToContents)
            headerVertical.setStretchLastSection(True)

            #self.records_qty()
        else:
            print("¡Error! No se cargaron los datos correctamente.")
    
    def populate_table_transm_sub(self,data):
        if data is not None:
            self.tableMedicion.setRowCount(len(data))
            print("REFRESH4")
            for index_row, row in enumerate(data):
                # Incrementamos el índice de fila en 1 para comenzar con el número de orden en 1
                order_number = index_row + 1
                
                # Establecemos el número de orden en la primera columna
                self.tableMedicion.setItem(index_row, 0, QTableWidgetItem(str(order_number)))
                
                for index_cell, cell in enumerate(row):
                    # Llenamos los datos de la fila a partir de la segunda columna
                    self.tableMedicion.setItem(index_row, index_cell + 1, QTableWidgetItem(str(cell)))
                    
                    if index_cell == 13:
                        itemx = self.tableMedicion.item(index_row, index_cell + 1)  # Se ajusta el índice de la celda
                        print("EL ITEM ACTUAL ES: ", itemx)
                        if itemx.text() == "PENDIENTE":
                            itemx.setForeground(QBrush(QColor(255, 0, 0)))
                        else:
                            itemx.setForeground(QBrush(QColor(0, 0, 255)))

            print("REFRESH5")
            headerVertical = self.tableMedicion.verticalHeader()
            headerVertical.resizeSections(QHeaderView.ResizeToContents)
            headerVertical.setStretchLastSection(True)

            #self.records_qty()
        else:
            print("¡Error! No se cargaron los datos correctamente.")
    
    def populate_table_bobinas_sub(self,data):
        if data is not None:
            self.tableBobina.setRowCount(len(data))
            print("REFRESH4")
            for index_row, row in enumerate(data):
                # Incrementamos el índice de fila en 1 para comenzar con el número de orden en 1
                order_number = index_row + 1
                
                # Establecemos el número de orden en la primera columna
                self.tableBobina.setItem(index_row, 0, QTableWidgetItem(str(order_number)))
                
                for index_cell, cell in enumerate(row):
                    # Llenamos los datos de la fila a partir de la segunda columna
                    self.tableBobina.setItem(index_row, index_cell + 1, QTableWidgetItem(str(cell)))
                    
                    if index_cell == 13:
                        itemx = self.tableBobina.item(index_row, index_cell + 1)  # Se ajusta el índice de la celda
                        print("EL ITEM ACTUAL ES: ", itemx)
                        if itemx.text() == "PENDIENTE":
                            itemx.setForeground(QBrush(QColor(255, 0, 0)))
                        else:
                            itemx.setForeground(QBrush(QColor(0, 0, 255)))

            print("REFRESH5")
            headerVertical = self.tableBobina.verticalHeader()
            headerVertical.resizeSections(QHeaderView.ResizeToContents)
            headerVertical.setStretchLastSection(True)

            #self.records_qty()
        else:
            print("¡Error! No se cargaron los datos correctamente.")
    
    def populate_table_conductor_sub(self,data):
        if data is not None:
            self.tableConductor.setRowCount(len(data))
            print("REFRESH4")
            for index_row, row in enumerate(data):
                # Incrementamos el índice de fila en 1 para comenzar con el número de orden en 1
                order_number = index_row + 1
                
                # Establecemos el número de orden en la primera columna
                self.tableConductor.setItem(index_row, 0, QTableWidgetItem(str(order_number)))
                
                for index_cell, cell in enumerate(row):
                    # Llenamos los datos de la fila a partir de la segunda columna
                    self.tableConductor.setItem(index_row, index_cell + 1, QTableWidgetItem(str(cell)))
                    
                    if index_cell == 13:
                        itemx = self.tableConductor.item(index_row, index_cell + 1)  # Se ajusta el índice de la celda
                        print("EL ITEM ACTUAL ES: ", itemx)
                        if itemx.text() == "PENDIENTE":
                            itemx.setForeground(QBrush(QColor(255, 0, 0)))
                        else:
                            itemx.setForeground(QBrush(QColor(0, 0, 255)))

            print("REFRESH5")
            headerVertical = self.tableConductor.verticalHeader()
            headerVertical.resizeSections(QHeaderView.ResizeToContents)
            headerVertical.setStretchLastSection(True)

            #self.records_qty()
        else:
            print("¡Error! No se cargaron los datos correctamente.")

    
    
    def populate_table_compensador_sub(self,data):
        if data is not None:
            self.tableCompensador.setRowCount(len(data))
            print("REFRESH4")
            for index_row, row in enumerate(data):
                # Incrementamos el índice de fila en 1 para comenzar con el número de orden en 1
                order_number = index_row + 1
                
                # Establecemos el número de orden en la primera columna
                self.tableCompensador.setItem(index_row, 0, QTableWidgetItem(str(order_number)))
                
                for index_cell, cell in enumerate(row):
                    # Llenamos los datos de la fila a partir de la segunda columna
                    self.tableCompensador.setItem(index_row, index_cell + 1, QTableWidgetItem(str(cell)))
                    
                    if index_cell == 13:
                        itemx = self.tableCompensador.item(index_row, index_cell + 1)  # Se ajusta el índice de la celda
                        print("EL ITEM ACTUAL ES: ", itemx)
                        if itemx.text() == "PENDIENTE":
                            itemx.setForeground(QBrush(QColor(255, 0, 0)))
                        else:
                            itemx.setForeground(QBrush(QColor(0, 0, 255)))

            print("REFRESH5")
            headerVertical = self.tableCompensador.verticalHeader()
            headerVertical.resizeSections(QHeaderView.ResizeToContents)
            headerVertical.setStretchLastSection(True)

            #self.records_qty()
        else:
            print("¡Error! No se cargaron los datos correctamente.")

    
    
    def refresh_table_from_child_window(self):
        print("REFRESH FROM CHILD...")
        print("REFRESH1")
        data = select_cod_barras_sub(self.inputCodigo.text())
        data2 = select_cod_porticos_sub(self.inputCodigo.text())
        data3 = select_cod_celdas_sub(self.inputCodigo.text())
        data4 = select_cod_transp_sub(self.inputCodigo.text())
        data5 = select_cod_pararrayos_sub(self.inputCodigo.text())
        data6 = select_cod_transm_sub(self.inputCodigo.text())
        data7 = select_cod_bobinas_sub(self.inputCodigo.text())
        data8 = select_cod_conductor_sub(self.inputCodigo.text())
        data9 = select_cod_compensador_sub(self.inputCodigo.text())

        print("REFRESH2")
        self.populate_table_barras_sub(data)
        self.populate_table_porticos_sub(data2)
        self.populate_table_celdas_sub(data3)
        self.populate_table_transp_sub(data4)
        self.populate_table_pararrayos_sub(data5)
        self.populate_table_transm_sub(data6)
        self.populate_table_bobinas_sub(data7)
        self.populate_table_conductor_sub(data8)
        self.populate_table_compensador_sub(data9)

    
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
                # Consulta a la tabla Subestacion
                sql = f"SELECT * FROM Subestacion WHERE COD_SE = ?"
                cur.execute(sql, (book_id,))
                row = cur.fetchone()
                if row:
                    # Obtener los valores de la fila
                    inputCodEmpresa = str(row[0])
                    inputCodigo = str(row[1])
                    inputNombre = str(row[2])
                    cbCalificacion = str(row[3])
                    cbTipoSistema = str(row[4])
                    cbAreaDemanda = str(row[5])
                    cbAreaOperativa = str(row[6])
                    cbRegion = str(row[7])
                    cbZona = str(row[8])
                    inputAltitud = str(row[9])
                    inputTecnologia = str(row[10])
                    inputFuncion = str(row[11])
                    inputAtendida = str(row[12])
                    inputDireccion = str(row[13])
                    inputTelefono = str(row[14])
                    inputServicios = str(row[15])
                    inputObras = str(row[16])
                    inputEdificios = str(row[17])
                    inputRed = str(row[18])
                    inputInstalaciones = str(row[19])
                    cbEstado = str(row[20])
                    inputFecha = str(row[21])
                    inputDatum = str(row[22])
                    inputZona = str(row[23])

                    # Poblar los campos de entrada de la tabla Subestacion
                    self.inputCodEmpresa.setText(inputCodEmpresa)
                    self.inputCodigo.setText(inputCodigo)
                    self.inputNombre.setText(inputNombre)
                    self.cbCalificacion.setCurrentText(cbCalificacion)
                    self.cbTipoSistema.setCurrentText(cbTipoSistema)
                    self.cbAreaDemanda.setCurrentText(cbAreaDemanda)
                    self.cbAreaOperativa.setCurrentText(cbAreaOperativa)
                    self.cbRegion.setCurrentText(cbRegion)
                    self.cbZona.setCurrentText(cbZona)
                    self.inputAltitud.setText(inputAltitud)
                    self.cbTecnologia.setCurrentText(inputTecnologia)
                    self.cbFuncion.setCurrentText(inputFuncion)
                    self.cbAtendida.setCurrentText(inputAtendida)
                    self.inputDireccion.setText(inputDireccion)
                    self.inputTelefono.setText(inputTelefono)
                    self.inputServicios.setText(inputServicios)
                    self.inputObras.setText(inputObras)
                    self.inputEdificios.setText(inputEdificios)
                    self.inputRed.setText(inputRed)
                    self.inputInstalaciones.setText(inputInstalaciones)
                    self.cbEstado.setCurrentText(cbEstado)
                    fechaConv = inputFecha
                    fechaConv2 = fechaConv.replace("/", "-")
                    qdate = QDate.fromString(fechaConv2, "d-MM-yyyy")
                    self.inputFecha.setDate(qdate)
                    self.inputDatum.setText(inputDatum)
                    self.inputZona.setText(inputZona)

                    ## Consulta a la tabla Subestacion_Vertice_Perimetro_Coordenadas_Geograficas
                    #sql_coord_geo = f"SELECT * FROM Subestacion_Vertice_Perimetro_Coordenadas_Geograficas WHERE COD_SE = ?"
                    #cur.execute(sql_coord_geo, (book_id,))
                    #row_coord_geo = cur.fetchone()
                    #if row_coord_geo:
                    #    # Obtener los valores de la fila
                    #    inputSecuencia = str(row_coord_geo[2])
                    #    inputX = str(row_coord_geo[3])
                    #    inputY = str(row_coord_geo[4])
                    #    inputZ = str(row_coord_geo[5])
                    #    # Poblar los campos de entrada de la tabla Subestacion_Vertice_Perimetro_Coordenadas_Geograficas
                    #    self.inputSecuencia.setText(inputSecuencia)
                    #    self.inputX.setText(inputX)
                    #    self.inputY.setText(inputY)
                    #    self.inputZ.setText(inputZ)
#
                    ## Consulta a la tabla Subestacion_Vertice_Perimetro_Plano_Planta
                    #sql_plano_planta = f"SELECT * FROM Subestacion_Vertice_Perimetro_Plano_Planta WHERE COD_SE = ?"
                    #cur.execute(sql_plano_planta, (book_id,))
                    #row_plano_planta = cur.fetchone()
                    #if row_plano_planta:
                    #    # Obtener los valores de la fila
                    #    inputSecuencia_2 = str(row_plano_planta[2])
                    #    inputX_2 = str(row_plano_planta[3])
                    #    inputY_2 = str(row_plano_planta[4])
                    #    inputZ_2 = str(row_plano_planta[5])
                    #    # Poblar los campos de entrada de la tabla Subestacion_Vertice_Perimetro_Plano_Planta
                    #    self.inputSecuencia_2.setText(inputSecuencia_2)
                    #    self.inputX_2.setText(inputX_2)
                    #    self.inputY_2.setText(inputY_2)
                    #    self.inputZ_2.setText(inputZ_2)

            except Error as e:
                print("Error al obtener detalles del libro:", str(e))
            finally:
                if conn:
                    conn.close()


    def FilaSeleccionadaBarras(self):
        print("ENTRO A DOUBLE CLICK!")
        from controllers.new_window_subestacion_barra import NewBookWindow
        selected_row = self.tableBarras.selectedItems()

        if selected_row:
            book_id = str(selected_row[1].text())
            window= NewBookWindow(self,self._codCentral,book_id)
        window.exec_()
        
        self.tableBarras.clearSelection()

    def FilaSeleccionadaPorticos(self):
        print("ENTRO A DOUBLE CLICK!")
        from controllers.new_window_subestacion_portico import NewBookWindow
        selected_row = self.tablePorticos.selectedItems()

        if selected_row:
            book_id = str(selected_row[1].text())
            window= NewBookWindow(self,self._codCentral,book_id)
        window.exec_()
        
        self.tablePorticos.clearSelection()
    
    def FilaSeleccionadaCeldas(self):
        print("ENTRO A DOUBLE CLICK!")
        from controllers.new_window_subestacion_celda import NewBookWindow
        selected_row = self.tableCeldas.selectedItems()

        if selected_row:
            book_id = str(selected_row[1].text())
            window= NewBookWindow(self,self._codCentral,book_id)
        window.exec_()
        
        self.tableCeldas.clearSelection()
    
    def FilaSeleccionadaTransfPotencia(self):
        print("ENTRO A DOUBLE CLICK!")
        from controllers.new_window_subestacion_transformador import NewBookWindow
        selected_row = self.tableTransformador.selectedItems()

        if selected_row:
            book_id = str(selected_row[1].text())
            window= NewBookWindow(self,self._codCentral,book_id)
        window.exec_()
        
        self.tableTransformador.clearSelection()
    
    def FilaSeleccionadaPararrayos(self):
        print("ENTRO A DOUBLE CLICK!")
        from controllers.new_window_subestacion_pararrayo import NewBookWindow
        selected_row = self.tablePararrayo.selectedItems()

        if selected_row:
            book_id = str(selected_row[1].text())
            window= NewBookWindow(self,self._codCentral,book_id)
        window.exec_()
        
        self.tablePararrayo.clearSelection()
    
    def FilaSeleccionadaTranfMedicion(self):
        print("ENTRO A DOUBLE CLICK!")
        from controllers.new_window_subestacion_transformador_medicion import NewBookWindow
        selected_row = self.tableMedicion.selectedItems()

        if selected_row:
            book_id = str(selected_row[1].text())
            window= NewBookWindow(self,self._codCentral,book_id)
        window.exec_()
        
        self.tableMedicion.clearSelection()
    
    def FilaSeleccionadaBobinas(self):
        print("ENTRO A DOUBLE CLICK!")
        from controllers.new_window_subestacion_bobina import NewBookWindow
        selected_row = self.tableBobina.selectedItems()

        if selected_row:
            book_id = str(selected_row[1].text())
            window= NewBookWindow(self,self._codCentral,book_id)
        window.exec_()
        
        self.tableBobina.clearSelection()
    
    def FilaSeleccionadaConductores(self):
        print("ENTRO A DOUBLE CLICK!")
        from controllers.new_window_subestacion_conductor import NewBookWindow
        selected_row = self.tableConductor.selectedItems()

        if selected_row:
            book_id = str(selected_row[1].text())
            window= NewBookWindow(self,self._codCentral,book_id)
        window.exec_()
        
        self.tableConductor.clearSelection()
    
    def FilaSeleccionadaCompensadores(self):
        print("ENTRO A DOUBLE CLICK!")
        from controllers.new_window_subestacion_compensador import NewBookWindow
        selected_row = self.tableCompensador.selectedItems()

        if selected_row:
            book_id = str(selected_row[1].text())
            window= NewBookWindow(self,self._codCentral,book_id)
        window.exec_()
        
        self.tableCompensador.clearSelection()

    def populate_combobox(self):
        # Llenar el combo de Calificación
        cb_options_calificacion = ("", "Principal", "Secundario", "Garantizado", "Complementario")
        self.cbCalificacion.addItems(cb_options_calificacion)

        # Llenar el combo de Tipo de Sistema
        cb_options_tipo_sistema = ("", "Interconectado", "Aislado")
        self.cbTipoSistema.addItems(cb_options_tipo_sistema)

        # Llenar el combo de Área de Demanda
        cb_options_area_demanda = ("", "AREA 1", "AREA 2")
        self.cbAreaDemanda.addItems(cb_options_area_demanda)

        # Llenar el combo de Área Operativa
        cb_options_area_operativa = ("", "Norte", "Centro", "Sur", "Lima")
        self.cbAreaOperativa.addItems(cb_options_area_operativa)

        # Llenar el combo de Región geográfica
        cb_options_region = ("", "Costa", "Sierra", "Selva")
        self.cbRegion.addItems(cb_options_region)

        # Llenar el combo de Zona
        cb_options_zona = ("", "Urbana", "Rural")
        self.cbZona.addItems(cb_options_zona)

        # Llenar el combo de Zona
        cb_options_tecnologia = ("", "Convencional", "Compacta","Encapsulada","Matal Clad")
        self.cbTecnologia.addItems(cb_options_tecnologia)

        # Llenar el combo de Zona
        cb_options_funcion = ("", "Transformación", "Seccionamiento")
        self.cbFuncion.addItems(cb_options_funcion)

        # Llenar el combo de Zona
        cb_options_atendida = ("", "Si", "No")
        self.cbAtendida.addItems(cb_options_atendida)

        # Llenar el combo de Estado
        cb_options_estado = ("", "Nuevo", "Existente", "Eliminado", "Modificado", "Proyectado")
        self.cbEstado.addItems(cb_options_estado)


    def open_new_window_coordenadas(self,codCentral):
        if(self.inputCodigo.isEnabled()):
            print("DEBE AGREGAR")
            msg_boxes.alert_msgbox_2("¡Error!","¡Primero debe agregar la Subestación!")
        else:
            from controllers.new_window_subestacion_vertice_coordenadas import NewBookWindow
            codCentral= self.inputCodigo.text()
            window= NewBookWindow(self,codCentral)
            window.exec_()

    def open_new_window_plano(self,codCentral):
        if(self.inputCodigo.isEnabled()):
            print("DEBE AGREGAR")
            msg_boxes.alert_msgbox_2("¡Error!","¡Primero debe agregar la Subestación!")
        else:        
            from controllers.new_window_subestacion_vertice_plano import NewBookWindow
            codCentral= self.inputCodigo.text()
            window= NewBookWindow(self,codCentral)
            window.exec_()

    def remove_book_celda(self):
        selected_row = self.tableCeldas.selectedItems()
        print("SELECT ROWWWWW: "+str(selected_row))
        if len(selected_row)!=0:
            respuesta=msg_boxes.alert_msgbox("Corfirmar Eliminar","¿Estas seguro de eliminar el registro?")
            if respuesta== QMessageBox.Yes:
                if selected_row:
                    book_id = str(selected_row[1].text())
                    row = selected_row[1].row()

                    if delete_book_Celda(book_id):
                    
                        self.tableCeldas.removeRow(row)

    def remove_book_barra(self):
        selected_row = self.tableBarras.selectedItems()
        print("SELECT ROWWWWW: "+str(selected_row))
        if len(selected_row)!=0:
            respuesta=msg_boxes.alert_msgbox("Corfirmar Eliminar","¿Estas seguro de eliminar el registro?")
            if respuesta== QMessageBox.Yes:
                if selected_row:
                    book_id = str(selected_row[1].text())
                    row = selected_row[1].row()

                    if delete_book_Barra(book_id):
                    
                        self.tableBarras.removeRow(row)


    def remove_book_portico(self):
        selected_row = self.tablePorticos.selectedItems()
        print("SELECT ROWWWWW: "+str(selected_row))
        if len(selected_row)!=0:
            respuesta=msg_boxes.alert_msgbox("Corfirmar Eliminar","¿Estas seguro de eliminar el registro?")
            if respuesta== QMessageBox.Yes:
                if selected_row:
                    book_id = str(selected_row[1].text())
                    row = selected_row[1].row()

                    if delete_book_Portico(book_id):
                    
                        self.tablePorticos.removeRow(row)

    def remove_book_transformador(self):
        selected_row = self.tableTransformador.selectedItems()
        print("SELECT ROWWWWW: "+str(selected_row))
        if len(selected_row)!=0:
            respuesta=msg_boxes.alert_msgbox("Corfirmar Eliminar","¿Estas seguro de eliminar el registro?")
            if respuesta== QMessageBox.Yes:
                if selected_row:
                    book_id = str(selected_row[1].text())
                    row = selected_row[1].row()

                    if delete_book_Transformador_Potencia(book_id):
                    
                        self.tableTransformador.removeRow(row)

    def remove_book_pararrayo(self):
        selected_row = self.tablePararrayo.selectedItems()
        print("SELECT ROWWWWW: "+str(selected_row))
        if len(selected_row)!=0:
            respuesta=msg_boxes.alert_msgbox("Corfirmar Eliminar","¿Estas seguro de eliminar el registro?")
            if respuesta== QMessageBox.Yes:
                if selected_row:
                    book_id = str(selected_row[1].text())
                    row = selected_row[1].row()

                    if delete_book_Pararrayo(book_id):
                    
                        self.tablePararrayo.removeRow(row)
    
    def remove_book_medicion(self):
        selected_row = self.tableMedicion.selectedItems()
        print("SELECT ROWWWWW: "+str(selected_row))
        if len(selected_row)!=0:
            respuesta=msg_boxes.alert_msgbox("Corfirmar Eliminar","¿Estas seguro de eliminar el registro?")
            if respuesta== QMessageBox.Yes:
                if selected_row:
                    book_id = str(selected_row[1].text())
                    row = selected_row[1].row()

                    if delete_book_Transformador_Medicion(book_id):
                    
                        self.tableMedicion.removeRow(row)

    def remove_book_conductor(self):
        selected_row = self.tableConductor.selectedItems()
        print("SELECT ROWWWWW: "+str(selected_row))
        if len(selected_row)!=0:
            respuesta=msg_boxes.alert_msgbox("Corfirmar Eliminar","¿Estas seguro de eliminar el registro?")
            if respuesta== QMessageBox.Yes:
                if selected_row:
                    book_id = str(selected_row[1].text())
                    row = selected_row[1].row()

                    if delete_book_Conductor(book_id):
                    
                        self.tableConductor.removeRow(row)

    def remove_book_bobina(self):
        selected_row = self.tableBobina.selectedItems()
        print("SELECT ROWWWWW:bobina "+str(selected_row))
        if len(selected_row)!=0:
            respuesta=msg_boxes.alert_msgbox("Corfirmar Eliminar","¿Estas seguro de eliminar el registro?")
            if respuesta== QMessageBox.Yes:
                if selected_row:
                    book_id = str(selected_row[1].text())
                    row = selected_row[1].row()

                    if delete_book_Bobina_Bloqueo(book_id):
                    
                        self.tableBobina.removeRow(row)

    def remove_book_compensador(self):
        selected_row = self.tableCompensador.selectedItems()
        print("SELECT ROWWWWW:bobina "+str(selected_row))
        if len(selected_row)!=0:
            respuesta=msg_boxes.alert_msgbox("Corfirmar Eliminar","¿Estas seguro de eliminar el registro?")
            if respuesta== QMessageBox.Yes:
                if selected_row:
                    book_id = str(selected_row[1].text())
                    row = selected_row[1].row()

                    if delete_book_compensador(book_id):
                    
                        self.tableCompensador.removeRow(row)