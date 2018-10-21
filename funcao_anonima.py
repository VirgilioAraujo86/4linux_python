#!/usr/bin/python3
'''a= lambda x, y: x + y

a(1,6)

print((lambda x, y: x + y)(5,4))'''

'''Criar uma lista com o quadrado perfeito de 2 a 10'''

quadrado = [(lambda y: y**2)(x) for x in range(2,11)]
print(quadrado)