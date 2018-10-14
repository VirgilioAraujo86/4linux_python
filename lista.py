#!/usr/bin/python3
'''
Criar uma lista de numerica de 0 até 100 com numeros pares.
'''

for x in range(0, 102, 2):
    print(x, end=' ')
print()


numeros = [1,5,2,6,8,1002, 3041,762]
#par = [x for x in numeros if x % 2 == 0]# igual ao for abaixo
#For igual a variavel par abaixo

par = []
for x in numeros:
    if x % 2 == 0:
        par.append(x)