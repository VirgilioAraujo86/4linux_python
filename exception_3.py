#!/usr/bin/python3

ling = input('Qual a melhor linguagem de programacao ? ')

try:
    if ling.strip().lower() == 'python':
        print('acertou!')
    elif ling.strip().lower() == 'golang':
        print('está valendo!')
    else:
        raise ValueError('Linguaguem errada')
except ValueError as e:
    print (e)