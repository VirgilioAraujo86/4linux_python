'''atributos titular, n conta e saldo
metodos: sacar, depositar, transferir
'''
class Conta():
    ''' Abstrair conta corrente '''

    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo


    def sacar(self, valor):
        if self.saldo >= valor:
           self.saldo -= valor
           return True
        else:
           return False
    
    def depositar(self, valor):
        self.saldo += valor
        
    def transferir(self, valor, destino):
        try:
            if not self.sacar(valor):
                raise ValueError('Falha na transferencia!')
            try:
                destino.depositar(valor)
            except AttributeError:
                print('Erro: destino nao possui o metodo depositar!')
                self.depositar(valor)
        except Exception as e:
            print("Erro: {}".format(e))

class Poupanca(Conta):
    def __init__(self, titular, saldo):
        super().__init__(titular,saldo)
        self.juros = 0.005

        #self.titular
        #self.saldo
        #self.juros

    def render_juros(self):
        self.saldo += self.saldo * self.juros


#self.sacar(valor)
#destino.depositar(valor)

c1 = Conta('Virgilio', 500)
#c2 = Conta('Manuela', 500)
c2 = Poupanca('Manuela', 500)

c1.transferir(500, c2)
print(c1.titular, c1.saldo)
c2.render_juros()
print(c2.titular, c2.saldo)