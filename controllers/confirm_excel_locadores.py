from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Qt
from views.confirm_excel_locadores import ConfirmExcelLocadores
from PySide2 import QtCore
from pys2_msgboxes import msg_boxes
from db.books import generar_data_excel_fechas_locadores, generar_data_excel_hoy, generar_data_excel_fechas, generar_data_excel_hoy_locadores

from datetime import date
from PySide2.QtGui import *

class ConfirmExcel(QWidget,ConfirmExcelLocadores):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)
        #self.setMaximumSize(QtCore.QSize(902, 408))
        self.populate_inputs()
        self.generarExcelHoyButton.clicked.connect(self.generarExcelHoy)
        self.generarExcelHoyButton.setDefault(True)
        self.generarExcelFechasButton.clicked.connect(self.generarExcelFechas)
        self.generarExcelFechasButton.setDefault(True)
        self.horaSalidaLineEdit.returnPressed.connect(self.generarExcelFechasButton.click)
        self.fechaHoyLineEdit.returnPressed.connect(self.generarExcelHoyButton.click)
        self.cancelButton.clicked.connect(self.close)
        self.cancelButton.setDefault(True)
        


    def populate_inputs(self):

        #self.titleLineEdit.setText(data[1])
        #elf.categoryLineEdit.setText(data[2])
        #self.pageQtySpinBox.setValue(data[3])
        #self.pageReadQtySpinBox_2.setValue(data[4])
        #self.filePathLineEdit.setText(data[5])
        #self.descriptionTextedit.setText(data[6])
        today = date.today()
        fechaHoy = today.strftime("%d/%m/%Y")
        self.fechaHoyLineEdit.setText(fechaHoy)
    
    def generarExcelHoy(self):
        fechabusqueda=self.fechaHoyLineEdit.text()
        fechabusqueda=fechabusqueda.strip()
        print("LA FECHA DE HOY ES EN EXCEL: "+fechabusqueda)
        generar_data_excel_hoy_locadores(fechabusqueda)
        msg_boxes.correct_msgbox("Generación de Excel","Se ha generado el archivo Excel exitosamente. Puede encontrarlo en la carpeta 'Reportes'")
        self.close()
    
    def generarExcelFechas(self):
        HoraInicio=self.horaIngresoLineEdit.text()
        HoraInicio=HoraInicio.strip()
        HoraFin=self.horaSalidaLineEdit.text()
        HoraFin=HoraFin.strip()
        print("HORA INICIO: "+HoraInicio+" HORA FIN: "+HoraFin)
        if HoraInicio=="" or HoraFin=="":
            msg_boxes.error_msgbox("Complete ambos campos", "Debe ingresar una fecha inicial y final")
        else:
            generar_data_excel_fechas_locadores(HoraInicio,HoraFin)
            msg_boxes.correct_msgbox("Generación de Excel","Se ha generado el archivo Excel exitosamente. Puede encontrarlo en la carpeta 'Reportes'")
            self.close()

        