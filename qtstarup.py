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
from PyQt5.QtCore import QSize , Qt


import subprocess, sys , threading, time


class MainWindow(QWidget):

    def button1clicked():
        alert = QMessageBox()
        alert.setIcon(QMessageBox.Warning)
        alert.setText('Verificando conexão ao Terminal Acadêmico. \n Aguarde...')
        alert.exec_()

        if subprocess.call("ping -c 3 acadmico.terminal.ufsc.br", stdout=subprocess.PIPE, shell=True) == 0 :
            alert.setText('Conexão bem sucedida')
            #args = ("/usr/bin/remmina -c /home/rubenszanatta/Projetos/gui_remoto/terminal_windows.rdp")
            #popen = subprocess.call(args, stdout=subprocess.PIPE, shell=True)
            thread1 = threading.Thread(target=MainWindow.remminaThread, args=[])
            thread1.start()
            alert.destroy(alert)
            # popen.wait()
        else:
            alert.setText('Não foi possível se conectar com o servidor remoto. \n'
                          'tente novamente mais tarde')
        alert.exec_()



    def remminaThread():
        args = ("/usr/bin/remmina -c /home/rubenszanatta/Projetos/gui_remoto/terminal_windows.rdp")
        popen = subprocess.Popen(args, stdout=subprocess.PIPE, shell=True)

    def __init__(self, widthMain, heightMain):
        QWidget.__init__(self)
        self.setGeometry(widthMain, widthMain, heightMain, heightMain)
        self.setMinimumSize(QSize(700,700))

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
        button1.clicked.connect(MainWindow.button1clicked)

        ## ------ botao 2
        button2 = QPushButton()
        button2.setFixedSize(QSize(300,250))
        icon2 = QIcon('resources/windows_button.png')
        button2.setIcon(icon2)
        button2.setIconSize(QSize(250, 300))

        ## ------ button 3
        button3 = QPushButton('Fechar')
        button3.setFixedSize(QSize(75,50))
        button3.setStyleSheet('color: black; font-size: 15px')
        button3.clicked.connect(qApp.quit)



        ## ------ header 1
        header1 = QLabel('Seja bem vindo! \n Escolha uma das opções abaixo para acessar o sistema:')
        header1.setAlignment(Qt.AlignCenter)
        header1.setStyleSheet('color: white; font-size: 25px')


        ## ----------- layout ----------
        layoutbuttons = QHBoxLayout()
        #layoutbuttons.setContentsMargins(50,50,50,50)
        layoutbuttons.setSpacing(25)
        layoutbuttons.addWidget(button1, 100)
        layoutbuttons.addWidget(button2, 100)

        layoutquit = QHBoxLayout()
        layoutquit.addWidget(button3)
        layoutquit.setSpacing(25)


        layoutcoluna1 = QVBoxLayout()
        layoutcoluna1.setContentsMargins(50, 200, 50, 200)
        layoutcoluna1.setSpacing(20)
        layoutcoluna1.addWidget(header1)
        layoutcoluna1.addLayout(layoutbuttons)
        layoutcoluna1.addLayout(layoutquit)


        # ----- Layout final
        self.setLayout(layoutcoluna1)

        ## ----------- voila ----------
        self.show()


if __name__ == "__main__":

    app = QApplication(sys.argv)
    mainwindow = MainWindow(1920,1080)
    sys.exit(app.exec_())



