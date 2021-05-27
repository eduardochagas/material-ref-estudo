print('=-'*30 + ' Classe: Orientação a Objetos ' + '-='*30)
print()

class ContaBanco:
    def __init__(self, cliente, numeroconta, saldo=0):
        self.saldo = saldo
        self.cliente = cliente
        self.numeroconta = numeroconta

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        self.saldo -= valor

    def relatorio(self):
        print('Cliente: %s, conta número: %s, saldo %8.2f' % (self.cliente, self.numeroconta, self.saldo))

contaBanco = ContaBanco('Neri Neitzke', 9876-98, 500)
contaBanco.relatorio()
contaBanco.deposito(300)
contaBanco.relatorio()
contaBanco.saque(450)
contaBanco.relatorio()
