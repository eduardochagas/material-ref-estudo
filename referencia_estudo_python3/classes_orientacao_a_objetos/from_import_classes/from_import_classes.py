print('=-'*30 + ' Classe: Orientação a Objetos ' + '-='*30)
print()
#a partir do arquivo 'classes' importe a classe 'Carros1' 
from classes import Carros1

#definindo os parametros 'marca' e 'cor' da classe 'Carros1'
camaro = Carros1('Chevrolet', 'Amarelo')
print(camaro.marca)
print(camaro.cor)

