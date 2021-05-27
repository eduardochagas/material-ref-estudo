print('=-'*30 + ' Classe: Orientação a Objetos ' + '-='*30)
print()

#criando classe sem parametro
class Carros:
    def __init__(self):
        self.marca = 'Ferrari'
        self.cor = 'vermelha'

# criando classe com parametros
class Carros1:
    def __init__(self, pmarca, pcor):
        self.marca = pmarca
        self.cor = pcor
