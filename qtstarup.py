#!/usr/bin/python3

'''
GUI DE INICIO DE SESSÃO PARA RASPBERRY PIs DO LABUFSC

Rodando no magnífico PyQt.
Requisitos de instalação: Python 3.X, PyQt5

'''

# --------------------
# IMPORTS
# --------------------

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QImage, QPalette, QBrush, QPixmap
from PyQt5.QtCore import QSize , Qt

import subprocess, sys , threading, time

# outra janela
import windows_info

class MainWindow(QWidget):


    def button1clicked(self):
        info1 = windows_info.WindowsInfo()
        info1.exec_()

    def button2clicked(self):
        alert = QMessageBox()
        alert.setIcon(QMessageBox.Warning)
        alert.setText('Verificando conexão ao Terminal Acadêmico. \n Aguarde...')
        alert.exec_()

        if subprocess.call("ping -c 3 acadmico.terminal.ufsc.br", stdout=subprocess.PIPE, shell=True) == 0 :
            alert.setText('Conexão bem sucedida')
            #args = ("/usr/bin/remmina -c /home/rubenszanatta/Projetos/gui_remoto/terminal_windows.rdp")
            #popen = subprocess.call(args, stdout=subprocess.PIPE, shell=True)
            thread1 = threading.Thread(target=MainWindow.remminathread, args=[])
            thread1.start()
            alert.destroy(alert)
            # popen.wait()
        else:
            alert.setText('Não foi possível se conectar com o servidor remoto. \n'
                          'tente novamente mais tarde')
        alert.exec_()


    def centerWindow(self):
        box = self.frameGeometry()
        center = QDesktopWidget().availableGeometry().center()
        box.moveCenter(center)
        self.move(box.topLeft())


#    def button1clicked(self):


    def remminathread():
        args = ("/usr/bin/remmina -c /home/rubenszanatta/Projetos/gui_remoto/terminal_windows.rdp")
        popen = subprocess.Popen(args, stdout=subprocess.PIPE, shell=True)

    def __init__(self, widthMain, heightMain):
        QWidget.__init__(self)
        #self.setGeometry(widthMain, widthMain, heightMain, heightMain)
        self.setFixedSize(QSize(widthMain,heightMain))

        ## ------------ background ---------
        oImage = QImage("resources/bkgd.png")
        sImage = oImage.scaled(QSize(1920, 1080))
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))
        self.setPalette(palette)

        ## ------------ elementos ----------
        ## ------ botao 1
        button1 = QPushButton()
        button1.setMaximumSize(QSize(300,250))
        icon1 = QIcon('resources/ubuntu_button.png')
        button1.setIcon(icon1)
        button1.setIconSize(QSize(250, 300))
        button1.clicked.connect(MainWindow.button1clicked)

        ## ------ label botao1
        labelbutton1 = QLabel('GNU/Linux')
        labelbutton1.setAlignment(Qt.AlignCenter)
        labelbutton1.setStyleSheet('color: white; font-size: 25px')

        ## ------ botao 2
        button2 = QPushButton()
        button2.setFixedSize(QSize(300,250))
        icon2 = QIcon('resources/windows_button.png')
        button2.setIcon(icon2)
        button2.setIconSize(QSize(250, 300))
        button2.clicked.connect(MainWindow.button2clicked)

        # ------ labelbotao2
        labelbutton2 = QLabel('Windows 10')
        labelbutton2.setAlignment(Qt.AlignCenter)
        labelbutton2.setStyleSheet('color: white; font-size: 25px')



        ## ------ button 3
        button3 = QPushButton('Fechar')
        button3.setFixedSize(QSize(75,50))
        button3.setStyleSheet('color: black; font-size: 15px')
        button3.clicked.connect(qApp.quit)



        ## ------ header 1
        header1 = QLabel('Seja bem vindo! \n Escolha uma das opções abaixo para acessar o sistema:')
        header1.setAlignment(Qt.AlignCenter)
        header1.setStyleSheet('color: white; font-size: 25px')


        ## ------- imagemUFSC
        imagemufsc = QLabel(self)
        pixmapufsc = QPixmap('resources/ufsc.png')
        pixmapufsc.scaled(150, 225, Qt.KeepAspectRatio)
        imagemufsc.setPixmap(pixmapufsc)


        ## ----------- layout ----------
        layoutVbuttons1 = QVBoxLayout()
        layoutVbuttons1.addWidget(button1)
        layoutVbuttons1.addWidget(labelbutton1)
        layoutVbuttons1.setAlignment(Qt.AlignCenter)


        layoutVbuttons2 = QVBoxLayout()
        layoutVbuttons2.addWidget(button2, 100)
        layoutVbuttons2.addWidget(labelbutton2)
        layoutVbuttons2.setAlignment(Qt.AlignCenter)


        layoutbuttons = QHBoxLayout()
        #layoutbuttons.setContentsMargins(50,50,50,50)
        layoutbuttons.setSpacing(25)
        layoutbuttons.addLayout(layoutVbuttons1)
        layoutbuttons.addLayout(layoutVbuttons2)

        layoutquit = QHBoxLayout()
        layoutquit.addWidget(button3)
        #layoutquit.setSpacing(25)


        layoutcoluna1 = QVBoxLayout()
        layoutcoluna1.setSpacing(40)
        layoutcoluna1.addWidget(header1)
        layoutcoluna1.addLayout(layoutbuttons)
        layoutcoluna1.addLayout(layoutquit)

        # --- layout main
        layoutcoluna2 = QVBoxLayout()
        layoutcoluna2.setAlignment(Qt.AlignCenter)
        layoutcoluna2.addWidget(imagemufsc)

        # --- layout main
        layoutmain = QHBoxLayout()
        layoutmain.addLayout(layoutcoluna1)
        layoutmain.addLayout(layoutcoluna2)
        layoutmain.setContentsMargins(50, 200, 50, 200)



        # ----- Layout final
        self.setLayout(layoutmain)


        ## ----------- voila ----------
        self.show()
        self.centerWindow()


if __name__ == "__main__":

    app = QApplication(sys.argv)
    mainwindow = MainWindow(1200,900)
    sys.exit(app.exec_())



