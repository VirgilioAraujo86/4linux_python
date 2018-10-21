#!/usr/bin/python3

def ler_arquivo(nome:str)->list:
    """Funçao para ler conteudo do arquivo
    params -> nome:str
    return -> list
    """
    try:
        with open(nome, 'r' ) as arq:
            return arq.readlines()
    except FileNotFoundError:
        #return ['Erro: Arquivo nao encontrado']
        return []

    

def escrever_arquivo(nome, conteudo):
    """Função paar escrever, arquivo
    params -> nome:str conteudo:list
    return -> bool
    """
    with open(nome, 'a') as arq:
        try:
            conteudo = ['{}\n'.format(x) for x in conteudo if x != '\n' ]
            arq.writelines(conteudo)
            return True
        except Exception:
            return False
letras = [ chr(x) for x in range(97, +97+26)]
ler_arquivo('texto.txt')
ler_arquivo('texto1.txt')
ler_arquivo('texto2.txt')
ler_arquivo('texto3.txt')
escrever_arquivo('letras.txt', letras)