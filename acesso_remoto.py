#!/usr/bin/env python

import pygtk, gtk, subprocess, threading
pygtk.require('2.0')

class Base:


    ## ------------------------------------------
    ##  *Destroy*
    ## ------------------------------------------

    def destroy(self, widget, data=None):
        ## Fecha o processo inteiro quando chamada.
        gtk.main_quit()


    ## ------------------------------------------
    ##  *fazAcessoWindows*
    ## ------------------------------------------
    def fazAcessoWindows(self, widget):
        #Usa o remmina com o arquivo .rpd com as configs desejadas
        args = ("/usr/bin/remmina -c terminal_windows.rdp ")
        print("Iniciando sessao Remmina")
        popen = subprocess.call(args,stdout=subprocess.PIPE,shell=True)


    ## ------------------------------------------
    ##  *fazAcessoLinux*
    ## ------------------------------------------

    def fazAcessoLinux(self, widget):
        #Ativar opcao de login por ssh no x2go e --hide e --thinclient p/ ocultar a interface
        #uma vez que as confs seja ddefinidas, --no-session-edit bloqueia o acesso a as configs
        args = ("/usr/bin/x2goclient --session-conf=sessions --session=linux_remoto")
        print("Iniciando sessao X2Go")
        subprocess.call(args,stdout=subprocess.PIPE,shell=True)

    ## ------------------------------------------
    ##  *instanciaLinux*
    ## ------------------------------------------

    def instanciaLinux(self, widget):
        #Defince a criacao da thread que instancia o acesso ao servidor
        acessoLinux = threading.Thread(target=self.fazAcessoLinux,args=[self])
        acessoLinux.start()

    ## ------------------------------------------
    ##  *instanciaWindows*
    ## ------------------------------------------

    def instanciaWindows(self, widget):
        #Defince a criacao da thread que instancia o acesso ao servidor
        acessoWindows = threading.Thread(target=self.fazAcessoWindows,args=[self])
        acessoWindows.start()





    ## ------------------------------------------
    ##  *CONSTRUTOR*
    ## ------------------------------------------

    def __init__(self):
            self.window =  gtk.Window(gtk.WINDOW_TOPLEVEL)
            self.window.set_position(gtk.WIN_POS_CENTER)
            self.window.set_size_request(350,200)


            self.button1 = gtk.Button("Fechar Janela")
            self.button2 = gtk.Button("Acesso Windows")
            self.button3 = gtk.Button("Acesso Linux")


            self.vbox = gtk.VBox() #container vertical para os elementos
            self.hbox = gtk.HBox() #container horizontal para os elementos


         ##Posicionamento por container vertical/horizontal
         ##Adiciona os elementos no container horizontal, depois no vertical
            self.hbox.pack_start(self.button2)
            self.hbox.pack_start(self.button3)
            self.vbox.pack_start(self.hbox)
            self.vbox.pack_start(self.button1)

            self.window.add(self.vbox)
            self.window.show_all()


            self.window.connect("destroy", self.destroy)
            self.button1.connect_object("clicked", self.destroy, self.window)
            self.button2.connect_object("clicked", self.instanciaWindows, self.window)
            self.button3.connect_object("clicked", self.instanciaLinux, self.window)

    def main (self):
        gtk.main()

if __name__ == "__main__":
    base = Base()
    base.main()
