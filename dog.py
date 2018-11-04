#!/usr/bin/python3


class Dog():
    '''Tentando abstrair um cachorro'''
    def __init__(self, nome, raca, idade):
        self.nome = nome
        self.raca = raca
        self.idade = idade
        self.energia = 5

    def latir(self):
        print('latindo...')

dog1 = Dog('bilu', 'pitbull', 2)
dog2 = Dog('rex', 'poodle', 1)

print(dog1.nome, dog1.raca, dog1.idade)
dog1.latir()