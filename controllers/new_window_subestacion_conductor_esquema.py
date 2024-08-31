from PySide2.QtWidgets import QDialog,QPushButton, QWidget, QFileDialog,QCompleter
from PySide2.QtCore import Qt, QDate
from PySide2.QtGui import *
from views.new_transmision_conductor_esquema import Ui_NewBook
from db.books import insert_book_conductor_ubicacion_esquema,buscar_usuario_acceso
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
        #self.label_advertencia_dni.hide()
        #self.label_nota_obligatoria.hide()
        if _codigo is not None:
            print("----------NO ES EDIT-----------:"+str(_codigo))
            self.populate_inputs(_codigo)
            self.inputCodigo.setText(str(_codigo))
            self.inputCodigo.setEnabled(False)
            self.addButton.setText("GUARDAR")
        self.addButton.clicked.connect(self.add_book)
        #self.btnAddEsquema.clicked.connect(self.open_new_window_coordenadas)
        #self.btnAddPlanta.clicked.connect(self.open_new_window_plano)

        self.inputCodigo.setText(str(_codCentral))
        self.inputCodigo.setEnabled(False)

        self.inputBarra.setText(str(_codCelda))
        self.inputBarra.setEnabled(False)
        
        #self.populate_comboboxPiso()
        #self.populate_comboboxEstado()
        #self.populate_inputs()
        #self.config_comboBoxes()
#
    
        #self.addButton.clicked.connect(self.add_book)
        #self.cancelButton.clicked.connect(self.close)

    def check_inputs(self):


        inputSecuencia = self.inputSecuencia.text()
        inputSecuencia=inputSecuencia.strip()

        inputX = self.inputX.text()
        inputX=inputX.strip()

        inputY = self.inputY.text()
        inputY=inputY.strip()

        
        errors_count = 0
        
        #if inputSecuencia == "":
        #    self.label_advertencia_dni.show()
        #    self.label_advertencia_dni.show()
        #    print("El campo aquienvisita es obligatorio")
        #    errors_count +=1
        #else:
        #    self.label_advertencia_dni.hide()
#
        #if inputX == "":
        #    print("El campo areavisitada es obligatorio")
        #    self.label_advertencia_dni.show()
        #    self.label_advertencia_dni.show()
        #    errors_count +=1
        #else:
        #    self.label_advertencia_dni.hide()

        if errors_count==0:
            return (True)

    def add_book(self):
        

        inputCodigo = self.inputCodigo.text()
        inputCodigo=inputCodigo.strip()
        
        inputBarra = self.inputBarra.text()
        inputBarra=inputBarra.strip()

        inputSecuencia = self.inputSecuencia.text()
        inputSecuencia=inputSecuencia.strip()

        inputX = self.inputX.text()
        inputX=inputX.strip()

        inputY = self.inputY.text()
        inputY=inputY.strip()

        #self.label_advertencia_dni.hide()

        #self.ActualizarVisitante(dni,visitante)
        if self.check_inputs():
            #new_path = shutil.copy(path, "book_files")
            #self.label_nota_obligatoria.hide()
            data = (self.Usuario,inputCodigo,inputBarra,inputSecuencia,inputX,inputY) 
            
            if insert_book_conductor_ubicacion_esquema(data):
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

    

    