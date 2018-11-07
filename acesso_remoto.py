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
        #--close-disconnect fecha o x2go em caso desconectado
        #uma vez que as confs seja ddefinidas, --no-session-edit bloqueia o acesso a as configs
        args = ("/usr/bin/x2goclient --session-conf=sessions --session=linux_remoto --close-disconnect --thinclient")
        print("Iniciando sessao X2Go")
        subprocess.call(args,stdout=subprocess.PIPE,shell=True)

    ## ------------------------------------------
    ##  *instanciaLinux*
    ## ------------------------------------------

    def instanciaLinux(self, widget):
        #Defince a criacao da thread que instancia o acesso ao servidor
        self.botaoAcesso2.set_sensitive(False)
        acessoLinux = threading.Thread(target=self.fazAcessoLinux,args=[self])
        acessoLinux.start()
        acessoLinux.wait()
        self.botaoAcesso2.set_sensitive(True)


    ## ------------------------------------------
    ##  *instanciaWindows*
    ## ------------------------------------------

    def instanciaWindows(self, widget):
        #Defince a criacao da thread que instancia o acesso ao servidor
        self.botaoAcesso1.set_sensitive(False)
        acessoWindows = threading.Thread(target=self.fazAcessoWindows,args=[self])
        acessoWindows.start()
        acessoWindows.wait()
        self.botaoAcesso1.set_sensitive(True)



    ## ------------------------------------------
    ##  *CONSTRUTOR*
    ## ------------------------------------------

    def __init__(self):
            self.window =  gtk.Window(gtk.WINDOW_TOPLEVEL)
            self.window.set_position(gtk.WIN_POS_CENTER)
            self.window.set_size_request(350,200)


            self.botaoFechar = gtk.Button("Fechar Janela")
            self.botaoAcesso1 = gtk.Button("Acesso Windows")
            self.botaoAcesso2 = gtk.Button("Acesso Linux")
            self.botaoFecha1 = gtk.Button("Interrompe Windows")
            self.botaoFecha2 = gtk.Button("Interrompe Linux")



            self.vbox = gtk.VBox() #container vertical para os elementos
            self.hbox1 = gtk.HBox() #container horizontal para os elementos
            self.hbox2 = gtk.HBox()

         ##Posicionamento por container vertical/horizontal
         ##Adiciona os elementos no container horizontal, depois no vertical
            self.hbox1.pack_start(self.botaoAcesso1)
            self.hbox1.pack_start(self.botaoFecha1)
            self.vbox.pack_start(self.hbox1)
            self.hbox2.pack_start(self.botaoAcesso2)
            self.hbox2.pack_start(self.botaoFecha2)
            self.vbox.pack_start(self.hbox2)
            self.vbox.pack_start(self.botaoFechar)

            self.window.add(self.vbox)
            self.window.show_all()


            self.window.connect("destroy", self.destroy)
            self.botaoFechar.connect_object("clicked", self.destroy, self.window)
            self.botaoAcesso1.connect_object("clicked", self.instanciaWindows, self.window)
            self.botaoAcesso2.connect_object("clicked", self.instanciaLinux, self.window)

    def main (self):
        gtk.main()

if __name__ == "__main__":
    base = Base()
    base.main()
