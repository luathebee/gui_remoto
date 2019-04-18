#!/usr/bin/python3

'''
GUI DE INICIO DE SESSÃO PARA RASPBERRY PIs DO LABUFSC

Rodando no magnífico PyQt.
Requisitos de instalação: Python 3.X, PyQt5

'''

#--------------------
# IMPORTS
#--------------------

from PyQt5.QtWidgets  import *
from PyQt5.QtGui import QIcon, QImage, QPalette, QBrush
from PyQt5.QtCore import QSize


import subprocess, sys


class MainWindow(QWidget):
    def __init__(self, widthMain, heightMain):
        QWidget.__init__(self)
        self.setGeometry(widthMain, widthMain, heightMain, heightMain)



if __name__ == "__main__":

    app = QApplication(sys.argv)
    mainwindow = MainWindow(400,700)
    sys.exit(app.exec_())



