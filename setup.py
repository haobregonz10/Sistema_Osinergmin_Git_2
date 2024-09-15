import sys
import os
from cx_Freeze import setup, Executable

files = ['assets', 'book_files','books_db.db','pys2_msgboxes','DATABASEAPP.db','DATABASEAPPTEMP.db']

exe = Executable(
    script="app.py",
    base='Win32GUI',
    icon="logo_febanvAnt.ico",
    target_name="Registros OSINERGMIN.exe"
)

setup(
    name="Sistema de Registro de Centrales de Energía Eléctrica",
    version="1.0",
    description="Sistema para ...",
    author="Hoz",
    options={'build_exe': {'include_files': files}},
    executables=[exe]
)
