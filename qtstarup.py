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
        sImage = oImage.scaled(QSize(1920, 1080))
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))
        self.setPalette(palette)

        ## ------------ elementos ----------
        ## ------ botao 1
        button1 = QPushButton()
        button1.setFixedSize(QSize(300,250))
        icon1 = QIcon('resources/ubuntu_button.png')
        button1.setIcon(icon1)
        button1.setIconSize(QSize(250, 300))

        ## ------ botao 2
        button2 = QPushButton()
        button2.setFixedSize(QSize(300,250))
        icon2 = QIcon('resources/windows_button.png')
        button2.setIcon(icon2)
        button2.setIconSize(QSize(250, 300))

        ## ------ botao 3 (not yet)
        #button3 = QPushButton()


        ## ----------- layout ----------
        layoutbuttons = QHBoxLayout()
        layoutbuttons.setContentsMargins(50,50,50,50)
        layoutbuttons.setSpacing(25)
        layoutbuttons.addWidget(button1, 100)
        layoutbuttons.addWidget(button2, 100)
        self.setLayout(layoutbuttons)

        ## ----------- voila ----------
        self.show()


if __name__ == "__main__":

    app = QApplication(sys.argv)
    mainwindow = MainWindow(1920,1080)
    sys.exit(app.exec_())



