from PySide2.QtWidgets import  QDialog,QMessageBox, QFileDialog,QTableWidgetItem,QAbstractItemView, QWidget, QFileDialog,QCompleter,QHeaderView
from PySide2.QtCore import Qt, QDate
from PySide2.QtGui import *
import sqlite3
from sqlite3 import Error
from controllers.AlignDelegate import *
from views.new_central import Ui_NewBook
from db.books import buscar_usuario_acceso,delete_book_Conductor_Central_Generacion,delete_book_Transformador_Medicion_Central_Generacion,delete_book_Pararrayo_Central_Generacion,delete_book_Transformador_Central_Generacion,delete_book_Portico_Central_Generacion,delete_book_Barra_Central_Generacion,delete_book_Celda_Central_Generacion,delete_book_Generador_Central_Generacion,insert_book_central_generacion_vertice_plano,insert_book_central_generacion_coordenadas,select_cod_porticos,insert_book,select_cod_generadores,select_cod_celdas,select_cod_barras,select_cod_interruptor,select_cod_transformador,select_cod_seccionador,select_cod_medicion,select_cod_pararrayo,select_cod_conductor
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
        self.inputDatum.setText("WGS84")
        self.inputDatum.setEnabled(False)
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
        
        self.populate_comboboxes()
        self.label_advertencia_dni.hide()
        self.label_nota_obligatoria.hide()
        self.label.setStyleSheet("background-color: #114692;")
        if _codCentral is not None:
            print("----------NO ES EDIT-----------:"+str(_codCentral))
            self.populate_inputs(_codCentral)
            self.refresh_table_from_child_window()
            self.inputCodigo.setEnabled(False)
            self.addButton.setText("GUARDAR")

        self.btnCoordenadas.clicked.connect(self.open_new_window_coordenadas)
        self.btnPlano.clicked.connect(self.open_new_window_plano)

        self.btnAddGeneradores.clicked.connect(self.open_add_generadores)
        self.btnAddCeldas.clicked.connect(self.open_add_celdas)
        self.btnAddBarras.clicked.connect(self.open_add_barras)
        self.btnAddPorticos.clicked.connect(self.open_add_porticos)
        #self.btnAddInterruptor.clicked.connect(self.open_add_interruptor)
        #self.btnAddSeccionador.clicked.connect(self.open_add_seccionador)
        self.btnAddTransformadores.clicked.connect(self.open_add_transformador)
        self.btnAddPararrayo.clicked.connect(self.open_add_pararrayo)
        self.btnAddTransfMed.clicked.connect(self.open_add_transformacion_medicion)
        self.btnAddConductores.clicked.connect(self.open_add_conductor)
        #self.populate_comboboxPiso()
        #self.populate_comboboxEstado()
        #self.populate_inputs()
        #self.config_comboBoxes()
        self.btnDeleteGenerador.clicked.connect(self.remove_book_generador)
        self.btnDeleteCeldas.clicked.connect(self.remove_book_celda)
        self.btnDeleteBarras.clicked.connect(self.remove_book_barra)
        self.btnDeletePorticos.clicked.connect(self.remove_book_portico)
        self.btnDeleteTransformador.clicked.connect(self.remove_book_transformador)
        self.btnDeletePararrayo.clicked.connect(self.remove_book_pararrayo)
        self.btnDeleteTransfMed.clicked.connect(self.remove_book_medicion)
        self.btnDeleteConductor.clicked.connect(self.remove_book_conductor)
        
        idcodCentral= self.inputCodigo.text()           
        self.table_config_generadores()
        self.populate_table_generadores(select_cod_generadores(idcodCentral))
        self.table_config_celdas()
        self.populate_table_celdas(select_cod_celdas(idcodCentral))
        self.table_config_barras()
        self.populate_table_barras(select_cod_barras(idcodCentral))
        self.table_config_porticos()
        self.populate_table_porticos(select_cod_porticos(idcodCentral))
        #self.table_config_interruptor()
        #self.populate_table_interruptor(select_cod_interruptor(idcodCentral))
        self.table_config_transformador()
        self.populate_table_transformador(select_cod_transformador(idcodCentral))
        #self.table_config_seccionador()
        #self.populate_table_seccionador(select_cod_seccionador(idcodCentral))
        self.table_config_medicion()
        self.populate_table_medicion(select_cod_medicion(idcodCentral))
        self.table_config_pararrayo()
        self.populate_table_pararrayo(select_cod_pararrayo(idcodCentral))
        self.table_config_conductor()
        self.populate_table_conductor(select_cod_conductor(idcodCentral))

        self.addButton.clicked.connect(self.add_book)
        self.cancelButton.clicked.connect(self.close)


        self.tableGeneradores.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableGeneradores.verticalHeader().setVisible(False)
        self.tableGeneradores.setColumnWidth(0,19)
        headerVertical = self.tableGeneradores.verticalHeader()
        headerVertical.resizeSections(QHeaderView.ResizeToContents)
        headerVertical.setStretchLastSection(True)
        self.tableGeneradores.doubleClicked.connect(lambda: self.FilaSeleccionadaGeneradores())

        self.tableCeldas.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableCeldas.verticalHeader().setVisible(False)
        self.tableCeldas.setColumnWidth(0,19)
        headerVertical = self.tableCeldas.verticalHeader()
        headerVertical.resizeSections(QHeaderView.ResizeToContents)
        headerVertical.setStretchLastSection(True)
        self.tableCeldas.doubleClicked.connect(lambda: self.FilaSeleccionadaCeldas())

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

        self.tableTransformador.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableTransformador.verticalHeader().setVisible(False)
        self.tableTransformador.setColumnWidth(0,19)
        headerVertical = self.tableTransformador.verticalHeader()
        headerVertical.resizeSections(QHeaderView.ResizeToContents)
        headerVertical.setStretchLastSection(True)
        self.tableTransformador.doubleClicked.connect(lambda: self.FilaSeleccionadaTransformadores())

        self.tableMedicion.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableMedicion.verticalHeader().setVisible(False)
        self.tableMedicion.setColumnWidth(0,19)
        headerVertical = self.tableMedicion.verticalHeader()
        headerVertical.resizeSections(QHeaderView.ResizeToContents)
        headerVertical.setStretchLastSection(True)
        self.tableMedicion.doubleClicked.connect(lambda: self.FilaSeleccionadaTransfMedicion())

        self.tablePararrayo.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tablePararrayo.verticalHeader().setVisible(False)
        self.tablePararrayo.setColumnWidth(0,19)
        headerVertical = self.tablePararrayo.verticalHeader()
        headerVertical.resizeSections(QHeaderView.ResizeToContents)
        headerVertical.setStretchLastSection(True)
        self.tablePararrayo.doubleClicked.connect(lambda: self.FilaSeleccionadaPararrayos())

        self.tableConductor.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableConductor.verticalHeader().setVisible(False)
        self.tableConductor.setColumnWidth(0,19)
        headerVertical = self.tableConductor.verticalHeader()
        headerVertical.resizeSections(QHeaderView.ResizeToContents)
        headerVertical.setStretchLastSection(True)
        self.tableConductor.doubleClicked.connect(lambda: self.FilaSeleccionadaConductores())

    def open_new_window_coordenadas(self,codCentral):
        if(self.inputCodigo.isEnabled()):
            print("DEBE AGREGAR")
            msg_boxes.alert_msgbox_2("¡Error!","¡Primero debe agregar la Central de Generación!")
        else:
            from controllers.new_window_central_generacion_vertice_coordenadas import NewBookWindow
            codCentral= self.inputCodigo.text()
            window= NewBookWindow(self,codCentral)
            window.exec_()

    def open_new_window_plano(self,codCentral):
        if(self.inputCodigo.isEnabled()):
            print("DEBE AGREGAR")
            msg_boxes.alert_msgbox_2("¡Error!","¡Primero debe agregar la Central de Generación!")
        else:        
            from controllers.new_window_central_generacion_vertice_plano import NewBookWindow
            codCentral= self.inputCodigo.text()
            window= NewBookWindow(self,codCentral)
            window.exec_()

    def open_add_generadores(self,codCentral):
        if(self.inputCodigo.isEnabled()):
            print("DEBE AGREGAR")
            msg_boxes.alert_msgbox_2("¡Error!","¡Primero debe agregar la Central de Generación!")
        else:
            from controllers.new_window_central_generador import NewBookWindow
            codCentral= self.inputCodigo.text()
            window= NewBookWindow(self,codCentral)
            window.exec_()

    def open_add_celdas(self,codCentral):
        if(self.inputCodigo.isEnabled()):
            print("DEBE AGREGAR")
            msg_boxes.alert_msgbox_2("¡Error!","¡Primero debe agregar la Central de Generación!")
        else:        
            from controllers.new_window_central_celda import NewBookWindow
            codCentral= self.inputCodigo.text()
            window= NewBookWindow(self,codCentral)
            window.exec_()

    def open_add_barras(self,codCentral):
        if(self.inputCodigo.isEnabled()):
            print("DEBE AGREGAR")
            msg_boxes.alert_msgbox_2("¡Error!","¡Primero debe agregar la Central de Generación!")
        else:        
            from controllers.new_window_central_barra import NewBookWindow
            codCentral= self.inputCodigo.text()
            window= NewBookWindow(self,codCentral)
            window.exec_()

    def open_add_porticos(self,codCentral):
        if(self.inputCodigo.isEnabled()):
            print("DEBE AGREGAR")
            msg_boxes.alert_msgbox_2("¡Error!","¡Primero debe agregar la Central de Generación!")
        else:        
            from controllers.new_window_central_portico import NewBookWindow
            codCentral= self.inputCodigo.text()
            window= NewBookWindow(self,codCentral)
            window.exec_()

    

    def open_add_transformador(self,codCentral):
        if(self.inputCodigo.isEnabled()):
            print("DEBE AGREGAR")
            msg_boxes.alert_msgbox_2("¡Error!","¡Primero debe agregar la Central de Generación!")
        else:        
            from controllers.new_window_central_transformador import NewBookWindow
            codCentral= self.inputCodigo.text()
            window= NewBookWindow(self,codCentral)
            window.exec_()
    
    def open_add_pararrayo(self,codCentral):
        if(self.inputCodigo.isEnabled()):
            print("DEBE AGREGAR")
            msg_boxes.alert_msgbox_2("¡Error!","¡Primero debe agregar la Central de Generación!")
        else:        
            from controllers.new_window_central_pararrayo import NewBookWindow
            codCentral= self.inputCodigo.text()
            window= NewBookWindow(self,codCentral)
            window.exec_()
        
    def open_add_transformacion_medicion(self,codCentral):
        if(self.inputCodigo.isEnabled()):
            print("DEBE AGREGAR")
            msg_boxes.alert_msgbox_2("¡Error!","¡Primero debe agregar la Central de Generación!")
        else:
            from controllers.new_window_central_transformador_medicion import NewBookWindow
            codCentral= self.inputCodigo.text()
            window= NewBookWindow(self,codCentral)
            window.exec_()
    
    def open_add_conductor(self,codCentral):
        if(self.inputCodigo.isEnabled()):
            print("DEBE AGREGAR")
            msg_boxes.alert_msgbox_2("¡Error!","¡Primero debe agregar la Central de Generación!")
        else:        
            from controllers.new_window_central_conductor import NewBookWindow
            codCentral= self.inputCodigo.text()
            window= NewBookWindow(self,codCentral)
            window.exec_()
    #def populate_inputs(self):

        #
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
            
    #    
    def add_book(self):
        
        inputCodigo = self.inputCodigo.text()
        inputCodigo=inputCodigo.strip()

        inputNombre = self.inputNombre.text()
        inputNombre=inputNombre.strip()

        inputAltitud = self.inputAltitud.text()
        inputAltitud=inputAltitud.strip()

        inputCaudalDisenio = self.inputCaudalDisenio.text()
        inputCaudalDisenio=inputCaudalDisenio.strip()

        inputCoefProduccion = self.inputCoefProduccion.text()
        inputCoefProduccion=inputCoefProduccion.strip()

        inputConsumoPropio = self.inputConsumoPropio.text()
        inputConsumoPropio=inputConsumoPropio.strip()

        inputDireccion = self.inputDireccion.text()
        inputDireccion=inputDireccion.strip()

        inputTelefono = self.inputTelefono.text()
        inputTelefono=inputTelefono.strip()

        inputFechaAlta = self.inputFechaAlta.text()

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

        #observaciones1 = self.descriptionTextedit.toPlainText()
        #observaciones= observaciones1.upper()

        cbTipo = self.cbTipo.currentText()
        cbDemanda = self.cbDemanda.currentText()
        cbTipoSistema = self.cbTipoSistema.currentText()
        cbAreaOperativa = self.cbAreaOperativa.currentText()
        cbRegion = self.cbRegion.currentText()
        cbZona = self.cbZona.currentText()
        cbEstado = self.cbEstado.currentText()

        self.label_advertencia_dni.hide()

        self.ast_dni.hide()
        #self.ActualizarVisitante(dni,visitante)
        if self.check_inputs():
            #new_path = shutil.copy(path, "book_files")
            self.label_nota_obligatoria.hide()
            data = (self.Usuario,inputCodigo,inputNombre,cbTipo,cbDemanda,cbTipoSistema,cbAreaOperativa,cbRegion,cbZona,inputAltitud,inputCaudalDisenio,inputCoefProduccion,inputConsumoPropio,inputDireccion,inputTelefono,cbEstado,inputFechaAlta,inputDatum,inputZonaUTM) 
            #self.AnadirNuevos(dni,visitante,entidadempresa,motivovisita,aquienvisita,autoriza,areavisitada) 
            if insert_book(data):
                #self.clean_inputs()
                #data2 = (self.Usuario, inputCodigo, inputSecuencia, inputX,inputY,inputZ )
                #data3 = (self.Usuario, inputCodigo, inputSecuencia_2, inputX_2,inputY_2,inputZ_2 )

                #insert_book_central_generacion_coordenadas(data3)
                #insert_book_central_generacion_vertice_plano(data2)
                msg_boxes.correct_msgbox("¡Registro Exitoso!","¡Se registró exitosamente!")
                self.inputCodigo.setEnabled(False)
                self.addButton.setText("GUARDAR")
                self.parent.refresh_table_from_child_window()
                
                #self.close()
            else: 
                print("ERROR EN EL REGISTRO!")
            '''
            if(len(dni)!=8):
                self.label_advertencia_dni.show()
                self.ast_dni.show()
            else:
            '''    

    def clean_inputs(self):
        self.inputCodigo.clear()
        self.inputNombre.clear()
        self.inputAltitud.clear()
        self.inputCaudalDisenio.clear()
        self.inputCoefProduccion.clear()
        self.inputConsumoPropio.clear()
        self.inputDireccion.clear()
        self.inputTelefono.clear()
        self.inputFechaAlta.clear()
        self.cbTipo.setCurrentText("")
        self.cbDemanda.setCurrentText("")
#
    def select_file(self):
        file_path = QFileDialog.getOpenFileName()[0]
        self.filePathLineEdit.setText(file_path)

    def refresh_table_from_child_window(self):
        print("REFRESH FROM CHILD...")
        print("REFRESH1")
        data = select_cod_generadores(self.inputCodigo.text())
        data2 = select_cod_celdas(self.inputCodigo.text())
        data3 = select_cod_barras(self.inputCodigo.text())
        #data4 = select_cod_interruptor(self.inputCodigo.text())
        data5 = select_cod_transformador(self.inputCodigo.text())
        #data6 = select_cod_seccionador(self.inputCodigo.text())
        data7 = select_cod_medicion(self.inputCodigo.text())
        data8 = select_cod_pararrayo(self.inputCodigo.text())
        data9 = select_cod_conductor(self.inputCodigo.text())
        data10 = select_cod_porticos(self.inputCodigo.text())
        print("REFRESH2")
        self.populate_table_generadores(data)
        self.populate_table_celdas(data2)
        self.populate_table_barras(data3)
        #self.populate_table_porticos(data4)
        self.populate_table_transformador(data5)
        self.populate_table_pararrayo(data8)
        self.populate_table_medicion(data7)
        self.populate_table_conductor(data9)
        self.populate_table_porticos(data10)


    def populate_table_generadores(self,data):
        if data is not None:
            self.tableGeneradores.setRowCount(len(data))
            print("REFRESH4")
            for index_row, row in enumerate(data):
                # Incrementamos el índice de fila en 1 para comenzar con el número de orden en 1
                order_number = index_row + 1
                
                # Establecemos el número de orden en la primera columna
                self.tableGeneradores.setItem(index_row, 0, QTableWidgetItem(str(order_number)))
                
                for index_cell, cell in enumerate(row):
                    # Llenamos los datos de la fila a partir de la segunda columna
                    self.tableGeneradores.setItem(index_row, index_cell + 1, QTableWidgetItem(str(cell)))
                    
                    if index_cell == 13:
                        itemx = self.tableGeneradores.item(index_row, index_cell + 1)  # Se ajusta el índice de la celda
                        print("EL ITEM ACTUAL ES: ", itemx)
                        if itemx.text() == "PENDIENTE":
                            itemx.setForeground(QBrush(QColor(255, 0, 0)))
                        else:
                            itemx.setForeground(QBrush(QColor(0, 0, 255)))

            print("REFRESH5")
            headerVertical = self.tableGeneradores.verticalHeader()
            headerVertical.resizeSections(QHeaderView.ResizeToContents)
            headerVertical.setStretchLastSection(True)

            #self.records_qty()
        else:
            print("¡Error! No se cargaron los datos correctamente.")

    def table_config_generadores(self):
        column_headers = ("#","Código")
        self.tableGeneradores.setColumnCount(len(column_headers))
        self.tableGeneradores.setHorizontalHeaderLabels(column_headers)
        
        stylesheet = "::section{Background-color:#114692;border:1px solid black;color: white;}"
        self.tableGeneradores.horizontalHeader().setStyleSheet(stylesheet)
        self.tableGeneradores.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableGeneradores.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableGeneradores.setStyleSheet("QTableWidget{ gridline-color:black;alternate-background-color: #E2DED0;}")
        self.tableGeneradores.setAlternatingRowColors(True)
        #self.tableGeneradores.color

    def populate_table_celdas(self, data):
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
        #--------------------------------------------------------------------------------
        

    def table_config_celdas(self):
        
        column_headers = ("#", "Código")
        self.tableCeldas.setColumnCount(len(column_headers))
        self.tableCeldas.setHorizontalHeaderLabels(column_headers)
        self.tableCeldas.setSelectionMode(QAbstractItemView.SingleSelection)
        # Puedes agregar configuraciones adicionales aquí, como estilos de encabezado, colores de fondo, etc.
        stylesheet = "::section{Background-color:#114692;border:1px solid black;color: white;}"
        self.tableCeldas.horizontalHeader().setStyleSheet(stylesheet)
        self.tableCeldas.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableCeldas.setStyleSheet("QTableWidget{ gridline-color:black;alternate-background-color: #E2DED0;}")
        self.tableCeldas.setAlternatingRowColors(True)
        #self.tableGeneradores.color

    def populate_table_barras(self, data):
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


    def table_config_barras(self):
        column_headers = ("#", "Código")
        self.tableBarras.setColumnCount(len(column_headers))
        self.tableBarras.setHorizontalHeaderLabels(column_headers)
        self.tableBarras.setSelectionMode(QAbstractItemView.SingleSelection)
        # Puedes agregar configuraciones adicionales aquí, como estilos de encabezado, colores de fondo, etc.
        # Puedes agregar configuraciones adicionales aquí, como estilos de encabezado, colores de fondo, etc.
        stylesheet = "::section{Background-color:#114692;border:1px solid black;color: white;}"
        self.tableBarras.horizontalHeader().setStyleSheet(stylesheet)
        self.tableBarras.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableBarras.setStyleSheet("QTableWidget{ gridline-color:black;alternate-background-color: #E2DED0;}")
        self.tableBarras.setAlternatingRowColors(True)

    def populate_table_porticos(self, data):
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

    def table_config_porticos(self):
        column_headers = ("#", "Código")
        self.tablePorticos.setColumnCount(len(column_headers))
        self.tablePorticos.setHorizontalHeaderLabels(column_headers)
        self.tablePorticos.setSelectionMode(QAbstractItemView.SingleSelection)
        stylesheet = "::section{Background-color:#114692;border:1px solid black;color: white;}"
        self.tablePorticos.horizontalHeader().setStyleSheet(stylesheet)
        self.tablePorticos.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tablePorticos.setStyleSheet("QTableWidget{ gridline-color:black;alternate-background-color: #E2DED0;}")
        self.tablePorticos.setAlternatingRowColors(True)
        # Puedes agregar configuraciones adicionales aquí, como estilos de encabezado, colores de fondo, etc.


    
    def populate_table_transformador(self, data):
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

    def table_config_transformador(self):
        column_headers = ("#", "Código")
        self.tableTransformador.setColumnCount(len(column_headers))
        self.tableTransformador.setHorizontalHeaderLabels(column_headers)
        self.tableTransformador.setSelectionMode(QAbstractItemView.SingleSelection)
        stylesheet = "::section{Background-color:#114692;border:1px solid black;color: white;}"
        self.tableTransformador.horizontalHeader().setStyleSheet(stylesheet)
        self.tableTransformador.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableTransformador.setStyleSheet("QTableWidget{ gridline-color:black;alternate-background-color: #E2DED0;}")
        self.tableTransformador.setAlternatingRowColors(True)
        # Puedes agregar configuraciones adicionales aquí, como estilos de encabezado, colores de fondo, etc.

    def populate_table_seccionador(self, data):
        if data is not None:
            self.tableSeccionador.setRowCount(len(data))
            
            for index_row, row in enumerate(data):
                for index_cell, cell in enumerate(row):
                    self.tableSeccionador.setItem(index_row, index_cell, QTableWidgetItem(str(cell)))

                    # Aquí puedes agregar la lógica para cambiar el color del texto basado en el valor de la celda
                    # Por ejemplo, para cambiar el color de la celda si contiene "ABIERTO" o "CERRADO"
                    if index_cell == 4:  # Supongamos que queremos cambiar el color basado en el valor de la quinta columna
                        item = self.tableSeccionador.item(index_row, index_cell)
                        if item.text() == "ABIERTO":
                            item.setForeground(QBrush(QColor(255, 0, 0)))  # Rojo para "ABIERTO"
                        elif item.text() == "CERRADO":
                            item.setForeground(QBrush(QColor(0, 128, 0)))  # Verde para "CERRADO"

    
    def populate_table_medicion(self, data):
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

    def table_config_medicion(self):
        column_headers = ("#", "Código")
        self.tableMedicion.setColumnCount(len(column_headers))
        self.tableMedicion.setHorizontalHeaderLabels(column_headers)
        self.tableMedicion.setSelectionMode(QAbstractItemView.SingleSelection)
        stylesheet = "::section{Background-color:#114692;border:1px solid black;color: white;}"
        self.tableMedicion.horizontalHeader().setStyleSheet(stylesheet)
        self.tableMedicion.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableMedicion.setStyleSheet("QTableWidget{ gridline-color:black;alternate-background-color: #E2DED0;}")
        self.tableMedicion.setAlternatingRowColors(True)
        # Puedes agregar configuraciones adicionales aquí, como estilos de encabezado, colores de fondo, etc.

    def populate_table_pararrayo(self, data):
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


    def table_config_pararrayo(self):
        column_headers = ("#", "Código")
        self.tablePararrayo.setColumnCount(len(column_headers))
        self.tablePararrayo.setHorizontalHeaderLabels(column_headers)
        self.tablePararrayo.setSelectionMode(QAbstractItemView.SingleSelection)
        stylesheet = "::section{Background-color:#114692;border:1px solid black;color: white;}"
        self.tablePararrayo.horizontalHeader().setStyleSheet(stylesheet)
        self.tablePararrayo.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tablePararrayo.setStyleSheet("QTableWidget{ gridline-color:black;alternate-background-color: #E2DED0;}")
        self.tablePararrayo.setAlternatingRowColors(True)
        # Puedes agregar configuraciones adicionales aquí, como estilos de encabezado, colores de fondo, etc.

    def populate_table_conductor(self, data):
        
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


    def table_config_conductor(self):
        column_headers = ("#", "Código")
        self.tableConductor.setColumnCount(len(column_headers))
        self.tableConductor.setHorizontalHeaderLabels(column_headers)
        self.tableConductor.setSelectionMode(QAbstractItemView.SingleSelection)
        stylesheet = "::section{Background-color:#114692;border:1px solid black;color: white;}"
        self.tableConductor.horizontalHeader().setStyleSheet(stylesheet)
        self.tableConductor.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableConductor.setStyleSheet("QTableWidget{ gridline-color:black;alternate-background-color: #E2DED0;}")
        self.tableConductor.setAlternatingRowColors(True)
        # Puedes agregar configuraciones adicionales aquí, como estilos de encabezado, colores de fondo, etc.

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

    def populate_comboboxes(self):
        cbTipo = ("","Hidroelectrica", "Térmica", "Eólica","Solar")
        self.cbTipo.addItems(cbTipo)

        cbDemanda = ("","cbDemanda 1", "cbDemanda 2", "cbDemanda 3")
        self.cbDemanda.addItems(cbDemanda)

        cbTipoSistema = ("","Interconectado", "Aislado")
        self.cbTipoSistema.addItems(cbTipoSistema)

        cbAreaOperativa = ("","Norte", "Centro", "Sur","Lima")
        self.cbAreaOperativa.addItems(cbAreaOperativa)

        cbRegion = ("","Costa", "Sierra", "Selva")
        self.cbRegion.addItems(cbRegion)

        cbZona = ("","Urbana", "Rural")
        self.cbZona.addItems(cbZona)

        cbEstado = ("","Nuevo", "Existente", "Eliminado","Modificado","Proyectado")
        self.cbEstado.addItems(cbEstado)
    
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
                # Consulta a la tabla Central_Generacion
                sql = f"SELECT * FROM Central_Generacion WHERE COD_CENTRAL = ?"
                cur.execute(sql, (book_id,))
                row = cur.fetchone()
                if row:
                    # Obtener los valores de la fila
                    inputCodEmpresa = row[0]
                    inputCodigo = row[1]
                    inputNombre = row[2]
                    cbTipo = row[3]
                    cbDemanda = row[4]
                    cbTipoSistema = row[5]
                    cbAreaOperativa = row[6]
                    cbRegion = row[7]
                    cbZona = row[8]
                    inputAltitud = str(row[9])
                    inputCaudalDisenio = str(row[10])
                    inputCoefProduccion = str(row[11])
                    inputConsumoPropio = str(row[12])
                    inputDireccion = row[13]
                    inputTelefono = row[14]
                    cbEstado = row[15]
                    inputFechaAlta = row[16]
                    inputDatum = row[17]
                    inputZonaUTM = row[18]

                    # Poblar los campos de entrada de la tabla Central_Generacion
                    self.inputCodEmpresa.setText(inputCodEmpresa)
                    self.inputCodigo.setText(inputCodigo)
                    self.inputNombre.setText(inputNombre)
                    self.inputAltitud.setText(inputAltitud)
                    self.inputCaudalDisenio.setText(inputCaudalDisenio)
                    self.inputCoefProduccion.setText(inputCoefProduccion)
                    self.inputConsumoPropio.setText(inputConsumoPropio)
                    self.inputDireccion.setText(inputDireccion)
                    self.inputTelefono.setText(inputTelefono)
                    self.inputZonaUTM.setText(inputZonaUTM)
                    self.inputDatum.setText(inputDatum)

                    # Poblar las listas desplegables de la tabla Central_Generacion
                    self.cbTipo.setCurrentText(cbTipo)
                    self.cbDemanda.setCurrentText(cbDemanda)
                    self.cbTipoSistema.setCurrentText(cbTipoSistema)
                    self.cbAreaOperativa.setCurrentText(cbAreaOperativa)
                    self.cbRegion.setCurrentText(cbRegion)
                    self.cbZona.setCurrentText(cbZona)
                    self.cbEstado.setCurrentText(cbEstado)

                    # Poblar la fecha alta
                    fecha_alta = QDate.fromString(inputFechaAlta, "yyyy-MM-dd")
                    self.inputFechaAlta.setDate(fecha_alta)

                    ## Consulta a la tabla Central_Generacion_Vertice_Perimetro_Plano_Planta
                    #sql_coord = f"SELECT * FROM Central_Generacion_Vertice_Perimetro_Plano_Planta WHERE COD_CENTRAL = ?"
                    #cur.execute(sql_coord, (book_id,))
                    #row_coord = cur.fetchone()
                    #if row_coord:
                    #    # Obtener los valores de la fila
                    #    inputSecuencia = str(row_coord[2])
                    #    inputX = str(row_coord[3])
                    #    inputY = str(row_coord[4])
                    #    inputZ = str(row_coord[5])
                    #    #print("LOS VALORES DEL PPP: "+inputSecuencia+"; "+inputX+"; "+inputY+"; "+inputZ)
                    #    # Poblar los campos de entrada de la tabla Central_Generacion_Vertice_Perimetro_Plano_Planta
                    #    self.inputSecuencia.setText(inputSecuencia)
                    #    self.inputX.setText(inputX)
                    #    self.inputY.setText(inputY)
                    #    self.inputZ.setText(inputZ)
#
                    ## Consulta a la tabla Central_Generacion_Vertice_Perimetro_Coordenadas_Geograficas
                    #sql_coord_geo = f"SELECT * FROM Central_Generacion_Vertice_Perimetro_Coordenadas_Geograficas WHERE COD_CENTRAL = ?"
                    #cur.execute(sql_coord_geo, (book_id,))
                    #row_coord_geo = cur.fetchone()
                    #if row_coord_geo:
                    #    # Obtener los valores de la fila
                    #    inputSecuencia = str(row_coord_geo[2])
                    #    inputCoordX = str(row_coord_geo[3])
                    #    inputCoordY = str(row_coord_geo[4])
                    #    inputCoordZ = str(row_coord_geo[5])
                    #    #print("LOS VALORES DEL PCG: "+inputSecuencia+"; "+inputCoordX+"; "+inputCoordY+"; "+inputCoordZ)
                    #    # Poblar los campos de entrada de la tabla Central_Generacion_Vertice_Perimetro_Coordenadas_Geograficas
                    #    self.inputSecuencia_2.setText(inputCoordX)
                    #    self.inputX_2.setText(inputCoordX)
                    #    self.inputY_2.setText(inputCoordY)
                    #    self.inputZ_2.setText(inputCoordZ)

            except Error as e:
                print("Error al obtener detalles del libro:", str(e))
            finally:
                if conn:
                    conn.close()
    

    def FilaSeleccionadaGeneradores(self):
        print("ENTRO A DOUBLE CLICK!")
        from controllers.new_window_central_generador import NewBookWindow
        selected_row = self.tableGeneradores.selectedItems()

        if selected_row:
            book_id = str(selected_row[1].text())
            window= NewBookWindow(self,self._codCentral,book_id)
        window.exec_()
        
        self.tableGeneradores.clearSelection()

    def FilaSeleccionadaCeldas(self):
        print("ENTRO A DOUBLE CLICK!")
        from controllers.new_window_central_celda import NewBookWindow
        selected_row = self.tableCeldas.selectedItems()

        if selected_row:
            book_id = str(selected_row[1].text())
            window= NewBookWindow(self,self._codCentral,book_id)
        window.exec_()
        
        self.tableCeldas.clearSelection()
    
    def FilaSeleccionadaBarras(self):
        print("ENTRO A DOUBLE CLICK!")
        from controllers.new_window_central_barra import NewBookWindow
        selected_row = self.tableBarras.selectedItems()

        if selected_row:
            book_id = str(selected_row[1].text())
            window= NewBookWindow(self,self._codCentral,book_id)
        window.exec_()
        
        self.tableBarras.clearSelection()

    def FilaSeleccionadaPorticos(self):
        print("ENTRO A DOUBLE CLICK!")
        from controllers.new_window_central_portico import NewBookWindow
        selected_row = self.tablePorticos.selectedItems()

        if selected_row:
            book_id = str(selected_row[1].text())
            window= NewBookWindow(self,self._codCentral,book_id)
        window.exec_()
        
        self.tablePorticos.clearSelection()
    
    def FilaSeleccionadaTransformadores(self):
        print("ENTRO A DOUBLE CLICK!")
        from controllers.new_window_central_transformador import NewBookWindow
        selected_row = self.tableTransformador.selectedItems()

        if selected_row:
            book_id = str(selected_row[1].text())
            window= NewBookWindow(self,self._codCentral,book_id)
        window.exec_()
        
        self.tableTransformador.clearSelection()
    
    def FilaSeleccionadaPararrayos(self):
        print("ENTRO A DOUBLE CLICK!")
        from controllers.new_window_central_pararrayo import NewBookWindow
        selected_row = self.tablePararrayo.selectedItems()

        if selected_row:
            book_id = str(selected_row[1].text())
            window= NewBookWindow(self,self._codCentral,book_id)
        window.exec_()
        
        self.tablePararrayo.clearSelection()
    
    def FilaSeleccionadaTransfMedicion(self):
        print("ENTRO A DOUBLE CLICK!")
        from controllers.new_window_central_transformador_medicion import NewBookWindow
        selected_row = self.tableMedicion.selectedItems()

        if selected_row:
            book_id = str(selected_row[1].text())
            window= NewBookWindow(self,self._codCentral,book_id)
        window.exec_()
        
        self.tableMedicion.clearSelection()
    
    def FilaSeleccionadaConductores(self):
        print("ENTRO A DOUBLE CLICK!")
        from controllers.new_window_central_conductor import NewBookWindow
        selected_row = self.tableConductor.selectedItems()

        if selected_row:
            book_id = str(selected_row[1].text())
            window= NewBookWindow(self,self._codCentral,book_id)
        window.exec_()
        
        self.tableConductor.clearSelection()
    

    def remove_book_generador(self):
        selected_row = self.tableGeneradores.selectedItems()
        print("SELECT ROWWWWW: "+str(selected_row))
        if len(selected_row)!=0:
            respuesta=msg_boxes.alert_msgbox("Corfirmar Eliminar","¿Estas seguro de eliminar el registro?")
            if respuesta== QMessageBox.Yes:
                if selected_row:
                    book_id = str(selected_row[1].text())
                    row = selected_row[1].row()

                    if delete_book_Generador_Central_Generacion(book_id):
                    
                        self.tableGeneradores.removeRow(row)
                    
    def remove_book_celda(self):
        selected_row = self.tableCeldas.selectedItems()
        print("SELECT ROWWWWW: "+str(selected_row))
        if len(selected_row)!=0:
            respuesta=msg_boxes.alert_msgbox("Corfirmar Eliminar","¿Estas seguro de eliminar el registro?")
            if respuesta== QMessageBox.Yes:
                if selected_row:
                    book_id = str(selected_row[1].text())
                    row = selected_row[1].row()

                    if delete_book_Celda_Central_Generacion(book_id):
                    
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

                    if delete_book_Barra_Central_Generacion(book_id):
                    
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

                    if delete_book_Portico_Central_Generacion(book_id):
                    
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

                    if delete_book_Transformador_Central_Generacion(book_id):
                    
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

                    if delete_book_Pararrayo_Central_Generacion(book_id):
                    
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

                    if delete_book_Transformador_Medicion_Central_Generacion(book_id):
                    
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

                    if delete_book_Conductor_Central_Generacion(book_id):
                    
                        self.tableConductor.removeRow(row)