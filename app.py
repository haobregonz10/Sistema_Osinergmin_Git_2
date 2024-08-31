from PySide2.QtWidgets import QApplication
from PySide2.QtCore import Qt
from controllers.login_window import LoginWindowForm


# Manejo de escalado de alta resolución
if hasattr(Qt, 'AA_EnableHighDpiScaling'):
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
if hasattr(Qt, 'AA_UseHighDpiPixmaps'):
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)
#ESTE ES EL INICIO DEL PROYECTO22
if __name__ == "__main__":
    app = QApplication()
    window = LoginWindowForm()
    window.show()
    app.exec_()
