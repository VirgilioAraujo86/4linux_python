#!/usr/bin/python3

var = 10# variavel global

def escopo(): #define funcao
    #var = 5 #variavel local
    global var #muda pra variavel global
    var = 5
    print(var)
 
escopo()
print(var)