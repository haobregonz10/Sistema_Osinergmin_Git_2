from PySide2.QtWidgets import QPushButton, QWidget, QFileDialog,QCompleter
from PySide2.QtCore import Qt, QDate
from PySide2.QtGui import *
from views.new_central_interruptor_plano import Ui_NewBook
#from db.books import EncontrarDni,UpdateAutoriza, EncontrarNombreVisitante,EncontrarAutorizaArea, ExisteDni, ExisteNombreVisitante, insert_book, select_all_personalFeban, select_all_areaTabla, select_all_EntidadTabla,select_all_motivoTabla,select_all_visitantesDNI, select_all_visitantesNombres,insert_NuevoDNI,insert_NuevoAutoriza,insert_NuevoEntidad,insert_NuevoMotivo,insert_NuevoVisita,ExisteAutoriza,ExisteEntidad,ExisteMotivo,ExisteVisita,UpdateVisitante,EncontrarAreasDelBn,EncontrarPisoSeleccionado,EncontrarAreaSeleccionada
from PySide2 import QtCore
from pys2_msgboxes import msg_boxes
from datetime import date, datetime



class NewBookWindow(QWidget,Ui_NewBook):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)

        
        #self.populate_comboboxPiso()
        #self.populate_comboboxEstado()
        #self.populate_inputs()
        #self.config_comboBoxes()
#
    
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

    
    #def check_inputs(self):
    #    autoriza = self.titleLineEdit.text()
    #    autoriza=autoriza.strip()
#
    #    aquienvisita = self.categoryLineEdit.text()
    #    autoriza=autoriza.strip()
#
    #    areavisitada = self.areaVisitadaLineEdit.text()
    #    areavisitada=areavisitada.strip()
    #    #fechanuevo =self.dateEditNuevo.text()
    #    dni = self.dniLineEdit.text()
    #    dni=dni.strip()
#
    #    visitante = self.nombreVisitanteLineEdit.text()
    #    visitante=visitante.strip()
#
    #    entidadempresa = self.categoryLineEditEntidadEmpresa.text()
    #    entidadempresa=entidadempresa.strip()
#
    #    horaingreso = self.horaIngresoLineEdit.text()
    #    horaingreso=horaingreso.strip()
#
    #    horasalida = self.horaSalidaLineEdit.text()
    #    horasalida=horasalida.strip()
#
    #    motivovisita = self.motivoVisitaLineEdit.text()
    #    motivovisita=motivovisita.strip()
    #    
#
    #    errors_count = 0
    #    if autoriza == "":
    #        self.ast_autoriza.show()
    #        self.label_nota_obligatoria.show()
    #        errors_count += 1
    #    else:
    #        self.ast_autoriza.hide()
#
    #    if aquienvisita == "":
    #        self.ast_aquienvisita.show()
    #        self.label_nota_obligatoria.show()
    #        print("El campo aquienvisita es obligatorio")
    #        errors_count +=1
    #    else:
    #        self.ast_aquienvisita.hide()
#
    #    if areavisitada == "":
    #        print("El campo areavisitada es obligatorio")
    #        self.ast_area.show()
    #        self.label_nota_obligatoria.show()
    #        errors_count +=1
    #    else:
    #        self.ast_area.hide()
#
    #    if dni == "":
    #        print("Debe ingresar un DNI")
    #        self.ast_dni.show()
    #        self.label_nota_obligatoria.show()
    #        errors_count +=1
    #    else:
    #        self.ast_dni.hide()
#
    #    
    #    if visitante == "":
    #        print("Debe seleccionar un visitante")
    #        self.ast_visitante.show()
    #        self.label_nota_obligatoria.show()
    #        errors_count +=1
    #    else:
    #        self.ast_visitante.hide()
#
    #    if entidadempresa == "":
    #        print("Debe seleccionar un entidadempresa")
    #        self.ast_entidadempresa.show()
    #        self.label_nota_obligatoria.show()
    #        errors_count +=1
    #    else:
    #        self.ast_entidadempresa.hide()
    #    
    #    if horaingreso == "":
    #        print("Debe seleccionar un horaingreso")
    #        self.ast_horaingreso.show()
    #        self.label_nota_obligatoria.show()
    #        errors_count +=1
    #    else:
    #        self.ast_horaingreso.hide()
    #    
    #    
    #    if motivovisita == "":
    #        print("Debe seleccionar un motivovisita")
    #        self.ast_motivo.show()
    #        self.label_nota_obligatoria.show()
    #        errors_count +=1
    #    else:
    #        self.ast_motivo.hide()
    #    
    #    if errors_count==0:
    #        return (True)
    #        
    #    
    #def add_book(self):
    #    
    #    autoriza = self.titleLineEdit.text()
    #    autoriza=autoriza.strip()
    #    aquienvisita = self.categoryLineEdit.text()
    #    aquienvisita=aquienvisita.strip()
#
    #    areavisitada = self.areaVisitadaLineEdit.text()
    #    areavisitada=areavisitada.strip()
    #    fechanuevo =self.dateEditNuevo.text()
    #    fechanuevo=fechanuevo.strip()
#
    #    dni = self.dniLineEdit.text()
    #    dni=dni.strip()
#
    #    visitante = self.nombreVisitanteLineEdit.text()
    #    visitante=visitante.strip()
#
    #    entidadempresa = self.categoryLineEditEntidadEmpresa.text()
    #    entidadempresa=entidadempresa.strip()
#
    #    horaingreso = self.horaIngresoLineEdit.text()
    #    horaingreso=horaingreso.strip()
#
    #    horasalida = self.horaSalidaLineEdit.text()
    #    horasalida=horasalida.strip()
#
    #    motivovisita = self.motivoVisitaLineEdit.text()
    #    motivovisita=motivovisita.strip()
#
    #    observaciones1 = self.descriptionTextedit.toPlainText()
    #    observaciones= observaciones1.upper()
    #    piso = self.comboBoxPiso.currentText()
    #    estado = self.comboBoxEstado.currentText()
    #    self.label_advertencia_dni.hide()
    #    print("NOMBRE ACTUAL: "+visitante)
    #    self.ast_dni.hide()
    #    self.ActualizarVisitante(dni,visitante)
    #    if self.check_inputs():
    #        #new_path = shutil.copy(path, "book_files")
    #        self.label_nota_obligatoria.hide()
    #        data = (fechanuevo, dni,visitante,entidadempresa,motivovisita,aquienvisita,autoriza,areavisitada, piso,horaingreso,horasalida,observaciones,estado) 
    #        self.AnadirNuevos(dni,visitante,entidadempresa,motivovisita,aquienvisita,autoriza,areavisitada) 
    #        if insert_book(data):
    #            self.clean_inputs()
    #            msg_boxes.correct_msgbox("¡Registro Exitoso!","¡Se registró exitosamente!")
    #            self.parent.refresh_table_from_child_window()
    #            self.close()
    #        else: 
    #            print("ERROR EN EL REGISTRO!")
    #        '''
    #        if(len(dni)!=8):
    #            self.label_advertencia_dni.show()
    #            self.ast_dni.show()
    #        else:
    #        '''    

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

    

    