#!/usr/bin/python3

'''
GUI DE INICIO DE SESSÃO PARA RASPBERRY PIs DO LABUFSC

Rodando no magnífico PyQt.
Requisitos de instalação: Python 3.X, PyQt5

'''

#--------------------
# IMPORTS
#--------------------

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QImage, QPalette, QBrush
from PyQt5.QtCore import QSize


import subprocess, sys


class MainWindow(QWidget):
    def __init__(self, widthMain, heightMain):
        QWidget.__init__(self)
        self.setGeometry(widthMain, widthMain, heightMain, heightMain)

        ## ------------ background ---------
        oImage = QImage("resources/bkgd.png")
        sImage = oImage.scaled(QSize(400, 700))
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))
        self.setPalette(palette)

        ## ------------ elementos ----------
        ## ------ botao 1
        button1 = QPushButton()
        button1.setGeometry(250, 250, 300, 300)
        icon1 = QIcon('resources/ubuntu_button.png')
        button1.setIcon(icon1)
        button1.setIconSize(QSize(200, 250))

        ## ------ botao 2
        button2 = QPushButton()
        button2.setGeometry(250, 250, 300, 300)
        icon2 = QIcon('resources/windows_button.png')
        button2.setIcon(icon2)
        button2.setIconSize(QSize(200, 250))

        ## ------ botao 3 (not yet)
        #button3 = QPushButton()


        ## ----------- layout ----------
        layoutbuttons = QHBoxLayout()
        layoutbuttons.addWidget(button1)
        layoutbuttons.addWidget(button2)
        self.setLayout(layoutbuttons)

        ## ----------- voila ----------
        self.show()


if __name__ == "__main__":

    app = QApplication(sys.argv)
    mainwindow = MainWindow(400,700)
    sys.exit(app.exec_())



