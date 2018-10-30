#!/usr/bin/env python 

import pygtk, gtk, subprocess
pygtk.require('2.0')

class Base:

  
    ## ------------------------------------------
    ##  *Destroy*
    ##
    ## Fecha o processo inteiro quando chamada. 
    ## ------------------------------------------

    def destroy(self, widget, data=None): 
        gtk.main_quit()
    

    ## ------------------------------------------
    ##  *acessoWindows*
    ##
    ## Invoca o remmina com o arquivo .rpd contendo as configurações de acesso ao 
    ##  terminal remoto.
    ## ------------------------------------------

    def acessoWindows(self, widget):
        args = ("/usr/bin/remmina -c ~/.config/remmina/terminal_windows.rdp ")
        popen = subprocess.call(args,stdout=subprocess.PIPE,shell=True)
        popen.wait()
    
    ## ------------------------------------------
    ##  *acessoLinux*
    ##
    ## Invoca o x2go com a opção de conexão ao nome da sessão já configurada. 
    ## *Verificar se funciona para o caso de diversos usuários.
    ## Possível habilitar a opção de login automático por SSH, que tenta o log in no anfitrião
    ##  com as mesmas credenciais que o usuário cliente.
    ##  Se funcionar, habilitar opção --thinclient para esconder a interface do X2Go
    ## ------------------------------------------

    def acessoLinux(self, widget):
        #Ativar opcao de login por ssh no x2go e --hide e --thinclient p/ ocultar a interface
        args = ("/usr/bin/x2goclient --session=servidor_remoto")
        subprocess.call(args,stdout=subprocess.PIPE,shell=True)
        popen.wait()


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
            self.button2.connect_object("clicked", self.acessoWindows, self.window)
            self.button3.connect_object("clicked", self.acessoLinux, self.window)
    
    def main (self):
        gtk.main()

if __name__ == "__main__":
    base = Base()
    base.main()

