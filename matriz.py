#!/usr/bin/python3

'''Dado uma matriz
m=  [
    [6,2,6]
    [7,3,6]
    [10,2,1]
]
Calcular a  soma das diagonais
exempo: 6+3+1+6+3+10'''

matriz =  [
    [6,2,6],
    [7,3,6],
    [10,2,1]
]

a = 0
cont = 0

'''for x, y  in enumerate(matriz):
    a += y[x]
    print(x, y)
'''

for x in matriz:
    a += x[cont]
    cont += 1
    a += x[-cont]
    # a += y[x]
    # b += y[-(x+1)]

    print(a)