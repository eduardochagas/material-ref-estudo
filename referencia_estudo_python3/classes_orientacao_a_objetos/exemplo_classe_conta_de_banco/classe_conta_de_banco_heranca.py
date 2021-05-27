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

#herança da classe ContaBanco para a classe ContaEspecial
class ContaEspecial(ContaBanco):
    def __init__(self, cliente, numeroconta, saldo=0, limite=0):
        
        #herança de classe sem utilizar o built-in super()
        ContaBanco.__init__(self, cliente, numeroconta, saldo=0)
        self.limite = limite

    def saque(self, valor):
        self.saldo += self.limite
        self.saldo -= valor
        print('Cliente: %s, conta número: %s, saldo %8.2f' % (self.cliente, self.numeroconta, self.saldo))

conta1 = ContaEspecial('Neri',1,500,2000)
conta1.saque(800)
'''
# superclasse - é um nome utilizado por programadores python para dizer  
# que uma classe será usada como herança em uma subclasse.

# subclasse - é um nome utilizado por programadores python para dizer 
# que é a classe que está herdando uma outra classe. 


#-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=--==-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# vamos ao exemplo de herança de classe com essas duas classes abaixo:
#-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=--==-=-=-=-=-=-=-=-=-=-=-=-=-=-=

class Mamifero:
    def __init__(self, corDePelo, genero, andar):
        self.corDePelo = corDePelo
        self.genero = genero
        self.numDePatas = andar

    def falar(self):
        print('Olá, sou um mamifero e eu sei falar')

    def andar(self):
        print('Estou andando sobre {} patas'.format(self.numDePatas))

    def amamentar(self):
        if self.genero.lower()[0] == 'm':
            print('machos não amamentam')
        else:
            print('Amamentando meu filhote')


class Pessoa(Mamifero):
(*) # se herdar parâmetros de uma classe e ainda quiser adicionar mais parâmetros além
    # dos que já foram herdados, adicione normalmente dentro das 
    # aspas do __init__ do construtor da subclasse (nesse caso, da classe Pessoa).
    # No exemplo abaixo, inserimos um parâmetro a mais (o parametro: cabelo) no construtor da classe Pessoa.
    def __init__(self, corDePelo, genero, andar, cabelo):

        # Exemplo de Herança de classe usando o método especial super() para 
        # herdar o (construtor __init__ com os seus parâmetros) da classe Mamífero.

        # No primeiro parametro do metodo built-in do python chamado: super(), vc insere  
        # o NOME DA CLASSE que está herdando (nesse caso, é o nome da classe Pessoa), e no 
        # segundo parâmetro, vc insere o self (esse self é o self da CLASSE QUE RECEBE a herança,
        # no caso, é o self da classe Pessoa) seguido do .__init__ com os parâmetros da
        # classe herdada, que no caso são: corDePelo, genero e andar, que é da classe Mamifero.
        # exemplo do que eu disse acima, na linha abaixo:
        super(Pessoa, self).__init__(corDePelo, genero, andar)

    (*) # Vocẽ pode adicionar mais parâmentros além dos que já foram herdados...
        # adicione normalmente o parametro dentro das aspas do __init__ do construtor da 
        # subclasse (nesse caso, da classe Pessoa) caso queira inserir um valor assim que chamar a classe.
        self.cabelo = cabelo
        
        # ou simplesmente adicione uma propriedade na classe sem inserir um 
        # parametro no construtor, (no caso, da classe Pessoa).
        self.corDosOlhos = 'azul'

    def falar(self):
        # Vc pode usar o built-in super() tbm para herdar um método da superclasse.
        super(Pessoa, self).falar()
        
        OBS: Caso vc herde uma classe para outra classe, e as duas classes contenha metodos de nomes iguais,
        o método da classe que herda (que é a subclasse) irá sobrepor 
        o método da classe herdada (que é a superclasse), CUIDADO!!!
        
        '''
