#!/usr/bin/python3

#with open ('texto.txt', 'r') as arq:
#    print(arq.read())


#with open ('texto.txt', 'r') as arq:
#    print(arq.readlines())


#with open ('texto.txt', 'r') as arq:
#    print(arq.readlines(), end='')
#    print(arq.readlines(), end='')
#    arq.seek(0)
#    print(arq.readlines(), end='')

#conteudo = 5*['linha']

#conteudo = ['%s\n'%(x) for x in conteudo]
with open ('texto.txt', 'r') as arq:
    conteudo = arq.readlines()
    
aux = []
cont = 1
for linha in conteudo:
    if linha != '\n':
        aux.append('{} - {}'.format(cont, linha))
        cont += 1

with open ('texto.txt', 'w') as arq:
    arq.writelines(aux)

# conteudo = ['{}- {}'.format(y+1,x for y,x in enumerate(conteudo)]