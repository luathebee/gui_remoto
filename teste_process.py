#!/usr/bin/env python

import subprocess, threading, time, sys
#para python2.6 pra cima, para usar o end=''
comandox2go = "/usr/bin/x2goclient --session-conf=sessions --session=linux_remoto --close-disconnect --thinclient"
comandoAxsPy = "python3", "teste.py"

### TESTE 1
def AlgumaCoisa():
    print("Abre Janela")
    #popenWindows = subprocess.call("exec " + comandox2go,stdout=subprocess.PIPE,shell=True)
    popenJanela = subprocess.Popen("exec " + comandox2go,stdout=subprocess.PIPE,shell=True) #inicia o processo em plano de fundo

    while(popenJanela.poll()==None): #retorna 1 quando o processo se encerra, NONE enquanto roda
        print("esperando...")
        nextline = popenJanela.stdout.readline()
        print(nextlinepyth)

    #popenJanela.kill()
    print("Mata janela")

#TESTE 2 - Com threading, so printa no final
class MyClass(threading.Thread):
    def __init__(self):
        self.stdout = None
        self.stderr = None
        threading.Thread.__init__(self)

    def run(self):
        p = subprocess.Popen(comandox2go.split(),
                             shell=False,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)

        self.stdout, self.stderr = p.communicate()

#TESTE 3 - Ainda soh printa no final
def execute():
    popen = subprocess.Popen(comandox2go, stdout=subprocess.PIPE, universal_newlines=True)
    for line in popen.stdout: print(line.decode())

    popen.stdout.close()
    return_code = popen.wait()
    if return_code:
        raise subprocess.CalledProcessError(return_code, cmd)

#teste 4 -

# Example


def main():
    #TESTE1 c/ funcao faz alguma coisa
#    print("Comeca as threads")
#    janela1 = threading.Thread(target=AlgumaCoisa)
#    janela1.start()

    #TESTE2 c/ classe MyClass
#    myclass = MyClass()
#    myclass.start()
#    myclass.join()
#    print(myclass.stdout)

    #teste3 s/ threads
#    for path in execute(comandoAxsPy):
#        print(path)

    #teste 4 aquele with estranho
    with subprocess.Popen(comandoAxsPy, stdout=subprocess.PIPE, bufsize=1, universal_newlines=True) as p:
        print("Abriu proceesso")
        for line in p.stdout:
            print(line, end='') # process line here

        if p.returncode != 0:
            print("Terminou essa bagaca")
            #raise CalledProcessError(p.returncode, p.args)


main()
