#!/usr/bin/python3


from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QImage, QPalette, QBrush, QPixmap
from PyQt5.QtCore import QSize, Qt, QCoreApplication
import sys, os
resPath = os.getcwd() + '/resources'


class WindowsInfo(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.setMaximumSize(500, 500)
#        self.setStyleSheet('background-color: #30179c')


        ## ---------- Textos ----------

        infoheader = QLabel('Terminal Academico Remoto')
        infoheader.setStyleSheet('color: white ;font-size: 25px')
        infoheader.setAlignment(Qt.AlignCenter)

        infotext = QLabel('Ao acessar o termianal acadêmico da UFSC é possível acessar programas \n'
                          'como Photoshop, Autocad, entre outros.\n')
        infotext.setStyleSheet('color: white; font-size: 14px')

        infowarning = QLabel('Aviso: Audio indisponível.')
        infowarning.setStyleSheet('color: red; font-size 20px')
        infowarning.setAlignment(Qt.AlignCenter)

        infolist = QTextEdit('* Sujeito a alteração de acordo com disponibilidade de licenças.'
                            '3ds Max 2016; \n'
                            'Acrobat Reader DC; \n'
                            'Adobe Acrobat Distiller X; \n'
                            'Adobe Acrobat X Pro; \n'
                            'Adobe After Effects CS6; \n'
                            'Adobe Audition CS6; \n'
                            'Adobe Content Viewer; \n'
                            'Adobe Creative Cloud; \n'
                            'Adobe Dreamweaver CS6; \n'
                            'Adobe Encore CS6; \n'
                            'Adobe Fireworks CS6; \n'
                            'Adobe Flash Builder 4.6; \n'
                            'Adobe Flash Professional CS6; \n'
                            'Adobe Illustrator CS6 (64 Bit); \n'
                            'Adobe InDesign CS6; \n'
                            'Adobe LiveCycle ES2; \n'
                            'Adobe Master Collection CS6; \n'
                            'Adobe Photoshop CS6 (64 Bit); \n'
                            'Adobe Prelude CS6; \n'
                            'Adobe Premiere Pro CS6; \n'
                            'Adobe SpeedGrade CS6; \n'
                            'ANAREDE 9.7.5; \n'
                            'Applied Biosystems; \n'
                            'AutoCAD 2016 - English; \n'
                            'AutoCAD Map 3D 2016 - English; \n'
                            'BEASTv1.8.2; \n'
                            'BioEdit; \n'
                            'CEPEL; \n'
                            'ChemSep; \n'
                            'CorelDRAW Graphics Suite X6 (64-Bit); \n'
                            'ECONOMATICA; \n'
                            'eDrawings 2015 x64 Edition; \n'
                            'Enterprise Architect; \n'
                            'FontForge; \n'
                            'IM Data Editor 2016; \n'
                            'Image Lab; \n'
                            'Infrastructure Admin 2016; \n'
                            'LAS AF Lite; \n'
                            'Leica LAS AF Lite; \n'
                            'LibreOffice 5.0; \n'
                            'Maintenance; \n'
                            'MATLAB; \n'
                            'Matlab CAPE-OPEN Thermo Import; \n'
                            'Matlab CAPE-OPEN Unit Operation; \n'
                            'MATLAB R2013a; \n'
                            'Microsoft Office 2013; \n'
                            'Mozilla Firefox; \n'
                            'Multiflash 6.0; \n'
                            'Notepad++; \n'
                            'novaPDF 7; \n'
                            'R - Online; \n'
                            'R i386 3.2.2; \n'
                            'R x64 3.2.2; \n'
                            'Raster Design 2016 on AutoCAD 2016 - English; \n'
                            'SDS 2.4; \n'
                            'SOLIDWORKS 2015; \n'
                            'Start CCM; \n'
                            'STATISTICA; \n'
                            'TreeSize Free; \n')
        infolist.setMaximumSize(200,300)
        #infolist.setReadOnly(True)


        #------------------------------

        # --------- Imagem ------------

        ## ------------ background ---------
        oImage = QImage(resPath + "/bkgd.png")
        sImage = oImage.scaled(QSize(1920, 1080))
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))
        self.setPalette(palette)

        image = QLabel(self)
        pixmap = QPixmap( resPath + '/softwarelist.png')
        image.setPixmap(pixmap)

        #---------- Botoes ------------

        closeButton = QPushButton('Fechar')
        closeButton.clicked.connect(self.close)
        closeButton.setMaximumSize(170, 30)


        #------------------------------


        #---------- Layout ------------

        infolayout = QVBoxLayout()
        infolayout.setAlignment(Qt.AlignCenter)
        infolayout.addWidget(infoheader)

        infocolumn1 = QVBoxLayout()
        infocolumn1.addWidget(infotext)
        infocolumn1.addWidget(infolist)

        infomidlayout = QHBoxLayout()
        infomidlayout.addLayout(infocolumn1)
        infomidlayout.addWidget(image)

        infolayout.addLayout(infomidlayout)
        infolayout.addWidget(infotext)
        infolayout.addWidget(infowarning)

        bottomlayout = QHBoxLayout()
        bottomlayout.addStretch()
        bottomlayout.addWidget(closeButton)
        bottomlayout.addStretch()

        infolayout.addLayout(bottomlayout)
        self.setLayout(infolayout)
        self.show()

        #------------------------------

if __name__ == "__main__":
    app = QApplication(sys.argv)
    infoWindow = WindowsInfo()
    sys.exit(app.exec_())

