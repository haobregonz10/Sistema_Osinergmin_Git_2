from PySide2.QtWidgets import QMessageBox
from PySide2.QtGui import QIcon,QFont


class MsgBox(QMessageBox):
    def __init__(self, titulo,text):
        super().__init__()
        self.setWindowTitle(titulo)
        self.setText(text)
        
    
    def set_custom_icon(self,icon,iconWindow):
        self.setIconPixmap(icon)
        q_icon= QIcon(iconWindow)
        self.setWindowIcon(q_icon)
    
    def set_yes_no_buttons(self):
        self.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        buttonY = self.button(QMessageBox.Yes)
        buttonY.setText('Si')
        buttonN = self.button(QMessageBox.No)
        buttonN.setText('No')
    
    def set_ok_button(self):
        self.setStandardButtons(QMessageBox.Ok)
        buttonOk = self.button(QMessageBox.Ok)
        buttonOk.setText('Aceptar')

def correct_msgbox(titulo, text):
    icon= 'pys2_msgboxes/icons/exitoso.png'
    iconBanco= 'pys2_msgboxes/icons/banco_icon.png'
    font = QFont()
    font.setPointSize(12)
    msg_box = QMessageBox()
    msg_box = MsgBox(titulo,text)
    msg_box.set_custom_icon(icon,iconBanco)
    msg_box.setFont(font)
    msg_box.exec_()

def marc_salida_msgbox(titulo, text):
    icon= 'pys2_msgboxes/icons/icon_marcar.png'
    iconBanco= 'pys2_msgboxes/icons/banco_icon.png'
    font = QFont()
    font.setPointSize(12)
    msg_box = QMessageBox()
    msg_box = MsgBox(titulo,text)
    msg_box.set_custom_icon(icon,iconBanco)
    msg_box.setFont(font)
    msg_box.exec_()

def error_msgbox(titulo, text):
    icon= 'pys2_msgboxes/icons/warning_icon.png'
    iconBanco= 'pys2_msgboxes/icons/banco_icon.png'
    font = QFont()
    font.setPointSize(12)
    msg_box = QMessageBox()
    msg_box = MsgBox(titulo,text)
    msg_box.set_custom_icon(icon,iconBanco)
    msg_box.setFont(font)
    msg_box.exec_()

def alert_msgbox(titulo, text):
    icon= 'pys2_msgboxes/icons/warning_icon.png'
    iconBanco= 'pys2_msgboxes/icons/banco_icon.png'
    font = QFont()
    font.setPointSize(12)
    msg_box = QMessageBox()
    msg_box = MsgBox(titulo,text)
    msg_box.set_custom_icon(icon,iconBanco)
    msg_box.setFont(font)
    msg_box.set_yes_no_buttons() 
    resp= msg_box.exec_()
    return resp

def alert_msgbox_2(titulo, text):
    icon= 'pys2_msgboxes/icons/warning_icon.png'
    iconBanco= 'pys2_msgboxes/icons/banco_icon.png'
    font = QFont()
    font.setPointSize(12)
    msg_box = QMessageBox()
    msg_box = MsgBox(titulo,text)
    msg_box.set_custom_icon(icon,iconBanco)
    msg_box.setFont(font)
    msg_box.set_ok_button() 
    resp= msg_box.exec_()
    return resp