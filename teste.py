#!/usr/bin/env python

import subprocess
import threading, time


def carrinho(nome):
    x = 0
    while(x<=3):
        print("Carrinho: " + nome + " : "+ str(x))
        x += 1
        time.sleep(1)

def main():
    carrinho1 = threading.Thread(target=carrinho,args=["fastboy1"])
    carrinho2 = threading.Thread(target=carrinho,args=["quiklad2"])
    carrinho3 = threading.Thread(target=carrinho,args=["zoomman3"])


    carrinho1.start()
    time.sleep(1)
    carrinho2.start()
    #time.sleep(3)
    #carrinho3.start()


main()
