#!/usr/bin/python3
class Classe():
    def __init__(self):
        self.atributo= 'atributo' #pode ser acessado de outras classes
        print('metodo construtor! ')

    def metodo(self):
        print('metodo comum!')
        print(self.atributo)

a = Classe()
a.metodo() #so executa quando é chamado
print (a.atributo)