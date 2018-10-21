#!/usr/bin/python3

#num = input('Digite um numero: ')
#num.isnumeric()
#isinstance(num, int)

try:
    num = int(input('Digite um numero: '))
    if num % 2 == 0:
        print('par')
    else:
        print('impar')

except ValueError as e:
    print('Erro {}'.format(e))

except KeyboardInterrupt as e:
    print('Ctrl+C')

except Exception as e:
    print('Erro: {}'.format(e))

finally:
    print('Sempre sera executado')
