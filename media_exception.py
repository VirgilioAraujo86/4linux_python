#!/usr/bin/python3

try:
    nota1 = float(input('Digite sua primeira nota: '))
    nota2 = float(input('Digite sua segunda nota: '))
    
    media=(nota1 + nota2)/2

    if media >= 7:
        print("Passou de ano ", media, end='' )
    elif media >= 3:
        print('Ficou de recuperacao, media ', media, end='' )
    else:
        print('Reprovou de ano, media ', media, end='')
except Exception as e:
    print ('Erro: {}'.format(e))
