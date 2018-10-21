def teste(*args): #transforma em tupla
    print(args)

def teste2(**kwargs): #transforma em dicionario
    print(kwargs)

teste('daniel', 2, 5, 6, 'prata')

teste2(nome='virgilio', sobrenome='araujo', idade=31, altura='1,87' )