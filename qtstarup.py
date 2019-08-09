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

#endereço da diretorio de trabalho
import os 

resPath = os.getcwd() + '/resources'


class MainWindow(QWidget):


    def button1clicked(self):
        confirma = QMessageBox.question(self, 'PyQt5 message', "Deseja acessar diretamente o rasp?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if confirma == QMessageBox.No:
            alert1 = QMessageBox.information('PyQt5 message', "Obrigado por usar o rasp")
            qApp.quit()


    def button2clicked(self):
        alert2 = QMessageBox()
        alert2.setIcon(QMessageBox.Warning)
        alert2.setText('Verificando conexão ao Terminal Acadêmico. \n Aguarde...')
        alert2.exec_()

        if True:
        #if subprocess.call("ping -c 3 acadmico.terminal.ufsc.br", stdout=subprocess.PIPE, shell=True) == 0 :
            alert.setText('Conexão bem sucedida')
            #args = ("/usr/bin/remmina -c /home/rubenszanatta/Projetos/gui_remoto/terminal_windows.rdp")
            #popen = subprocess.call(args, stdout=subprocess.PIPE, shell=True)
            thread1 = threading.Thread(target=MainWindow.remminathread, args=[])
            thread1.start()
            alert.destroy(alert)
            # popen.wait()
        #else:
         #   alert.setText('Não foi possível se conectar com o servidor remoto. \n'
          #                'tente novamente mais tarde')
        alert.exec_()

    def button4clicked(self):
        print('lel')

    def button5clicked(self):
        info1 = windows_info.WindowsInfo()
        info1.show()

    def centerWindow(self):
        box = self.frameGeometry()
        center = QDesktopWidget().availableGeometry().center()
        box.moveCenter(center)
        self.move(box.topLeft())



    def remminathread():
        args = ("/usr/bin/remmina -c /opt/gui_remoto/terminal_windows.rdp")
        popen = subprocess.Popen(args, stdout=subprocess.PIPE, shell=True)

    def __init__(self, widthMain, heightMain):
        QWidget.__init__(self)
        #self.setGeometry(widthMain, widthMain, heightMain, heightMain)
        self.setFixedSize(QSize(widthMain,heightMain))

        ## ------------ background ---------
        oImage = QImage(resPath + "/bkgd.png")
        sImage = oImage.scaled(QSize(1920, 1080))
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))
        self.setPalette(palette)


        ## ------------ elementos ----------

        ## ------ botao 1
        button1 = QPushButton()
        button1.setMaximumSize(QSize(300,250))
        icon1 = QIcon(resPath +'/ubuntu.png')
        button1.setIcon(icon1)
        button1.setStyleSheet('background-color: #FFFFFF')
        button1.setIconSize(QSize(250, 300))
        button1.clicked.connect(MainWindow.button1clicked)

        ## ------ label botao1
        labelbutton1 = QLabel('GNU/Linux')
        labelbutton1.setAlignment(Qt.AlignCenter)
        labelbutton1.setStyleSheet('color: white; font-size: 25px')

        ## ------ botao 2
        button2 = QPushButton()
        button2.setMaximumSize(QSize(300,250))
        icon2 = QIcon(resPath + '/windows.png')
        button2.setIcon(icon2)
        button2.setStyleSheet('background-color: #ffffff')
        button2.setIconSize(QSize(250, 300))
        button2.clicked.connect(MainWindow.button2clicked)

        # ------ labelbotao2
        labelbutton2 = QLabel('Windows 10')
        labelbutton2.setAlignment(Qt.AlignCenter)
        labelbutton2.setStyleSheet('color: white; font-size: 25px')



        ## ------ button 3
        button3 = QPushButton('Fechar')
        button3.setFixedSize(QSize(75,50))
        button3.setStyleSheet('color: black; font-size: 20px;background-color: #30179c ')
        button3.clicked.connect(qApp.quit)


        ## ------ button 4
        button4 = QPushButton('Informações \nsobre Raspberry')
        button4.setFixedSize(QSize(170,50))
        button4.setIcon(icon1)
        button4.setStyleSheet('color: black; font-size: 14px;background-color: #30179c ')
        button4.setIconSize(QSize(30,30))
        button4.clicked.connect(MainWindow.button4clicked)

        ## ------ button 5
        button5 = QPushButton('Informações \nsobre Windows')
        button5.setFixedSize(QSize(170, 50))
        button5.setIcon(icon2)
        button5.setStyleSheet('color: black; font-size: 14px;background-color: #30179c ')
        button5.setIconSize(QSize(30, 30))
        button5.clicked.connect(MainWindow.button5clicked)


        ## ------ header 1
        header1 = QLabel('Seja bem vindo! \n Escolha uma das opções abaixo para acessar o sistema:')
        header1.setAlignment(Qt.AlignCenter)
        header1.setStyleSheet('color: white; font-size: 25px')


        ## ------- imagemUFSC
        imagemufsc = QLabel(self)
        pixmapufsc = QPixmap('/opt/gui_remoto/resources/ufsc.png')
        pixmapufsc.scaled(150, 225, Qt.KeepAspectRatio)
        imagemufsc.setPixmap(pixmapufsc)


        ## ----------- layout ----------
        layoutVbuttons1 = QVBoxLayout()
        layoutVbuttons1.addWidget(button1)
        layoutVbuttons1.addWidget(labelbutton1)
        layoutVbuttons1.setAlignment(Qt.AlignCenter)


        layoutVbuttons2 = QVBoxLayout()
        layoutVbuttons2.addWidget(button2)
        layoutVbuttons2.addWidget(labelbutton2)
        layoutVbuttons2.setAlignment(Qt.AlignCenter)


        layoutbuttons = QHBoxLayout()
        #layoutbuttons.setContentsMargins(50,50,50,50)
        layoutbuttons.setSpacing(25)
        layoutbuttons.addLayout(layoutVbuttons1)
        layoutbuttons.addLayout(layoutVbuttons2)

        layouthelp = QHBoxLayout()
        layouthelp.addWidget(button4)
        layouthelp.addWidget(button5)
        #layoutquit.setSpacing(25)

        layoutquit = QHBoxLayout()
        layoutquit.addWidget(button3)

        layoutcoluna1 = QVBoxLayout()
        layoutcoluna1.setSpacing(40)
        layoutcoluna1.setAlignment(Qt.AlignCenter)
        layoutcoluna1.addWidget(header1)
        layoutcoluna1.addLayout(layoutbuttons)
        layoutcoluna1.addLayout(layouthelp)
        layoutcoluna1.addLayout(layoutquit)



        # --- layout main
        layoutcoluna2 = QVBoxLayout()
        layoutcoluna2.setAlignment(Qt.AlignCenter)
        layoutcoluna2.addWidget(imagemufsc)

        # --- layout main
        layoutmain = QHBoxLayout()
        layoutmain.addLayout(layoutcoluna1)
        layoutmain.addLayout(layoutcoluna2)
        layoutmain.setContentsMargins(50, 50, 50, 50)



        # ----- Layout final
        self.setLayout(layoutmain)


        ## ----------- voila ----------
        self.show()
        self.centerWindow()


if __name__ == "__main__":

    app = QApplication(sys.argv)
    mainwindow = MainWindow(1200,900)
    sys.exit(app.exec_())



