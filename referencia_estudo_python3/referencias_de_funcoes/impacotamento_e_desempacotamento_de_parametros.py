
print("=" * 30)
print("desempacotamento de lista")
print("=" * 30)

lista = ['Eduardo', 'Weverton', 'Jeane', 'Anthony']
print(lista)
print()
(nome1, nome2, nome3, nome4) = lista
print('nome1: ',nome1)
print('nome2: ',nome2)
print('nome3: ',nome3)
print('nome4:',nome4)

print()

print("=" * 50)
print("Função soma normal")
print("=" * 50)
def soma(num1, num2):
    print('A soma é: ', (num1+num2))

n1 = 6
n2 = 7
print('parâmetro num1: ', n1)
print('parâmetro num2: ', n2)
soma(6, 7)

print()

print("=" * 50)
print("desempacotamento de lista em uma função definida com 2 parâmetros !!!")
print("=" * 50)

print(" OBS: a quantidade de itens dentro da lista deve ser correspondente a quantidade de parâmetros da função !!!")
print(" OBS2: se a quantidade de itens da lista for maior que a quantidade de parâmetros da função, gerará um erro !!!")
print(" OBS3: a lista deve ser inserida no parâmetro com o sinal de asterisco (*) antes do nome, assim: *lista.")
print(""" OBS4: repare que a função já foi criada com dois parâmetros, por isso que a quantidade de itens dentro da lista deve ser correspondente a quantidade de parâmetros criado na função !!!""")
print()
lista = [6, 9]
print('lista: ',lista)
soma(*lista)

print()

print("=" * 50)
print("Desempacotamento de lista em uma função que recebe uma quantidade ilimitada de elementos como parâmetro")
print("=" * 50)

print(''' OBS: para criar um parâmetro em uma função que recebe uma quantidade ilimitada de elementos, devemos inserir um sinal asterisco (*) antes do nome do parâmetro, assim: *numeros.''')
print(''' OBS2: repare que a função já foi criada com um parâmetro que contêm um asterisco (*) seguido do nome do parâmetro, assim: *numeros. Isso significa que podemos inserir uma lista de qualquer tamanho no parâmetro da função''')
print()
def soma2(*numeros):
    total = 0
    for num in numeros:
        total += num
    print('A soma é: ', total)
    
lista2 = [3, 5, 7, 9, 1, 6, 2]
print('lista2: ',lista2)
soma2(*lista2)

print()

print("=" * 50)
print("Desempacotamento de chaves e de valores de um dicionário")
print("=" * 50)

print("-" * 50)
print("Desempacotamento de chaves de dicionário")
print("-" * 50)
print(""" OBS: repare que em dicionarios, quando passamos a variável que armazena o dicionário no parâmetro da função com somente 1 asterisco (*) antes do nome, assim: *argumentos, descompactaremos as chaves armazenadas no dicionário.""")
print()

def desempacotarKey(a, b, c, d):
    return (a, b, c, d)

argumentos = {'d': 3, 'c': 2, 'b': 6, 'a': 4}
print('dicionario: ',argumentos)

key = desempacotarKey(*argumentos)
print('chaves do dicionário: ',key)

print()
print('-=' * 40)
print()

print("-" * 50)
print("Desempacotamento de valores de dicionário")
print("-" * 50)
print(""" OBS: repare que em dicionarios, quando passamos a variável que
armazena o dicionário no parâmetro da função com somente 2 asteriscos (**)
antes do nome, assim: **argumentos, descompactaremos os valores armazenados no dicionário.""")
print()

argumentos = {'d': 3, 'c': 2, 'b': 6, 'a': 4}
print('dicionario: ',argumentos)

valores = desempacotarKey(**argumentos)
print('valores do dicionário: ',valores)

print()

print("=" * 50)
print("Função mostrando que uma função pode retornar mais de um resultado ao mesmo tempo")
print("=" * 50)
#uma função pode retornar mais de um valor
def func(x, y):
    return x**2, y**2

print("Desempacotando os valores retornados da função nas variáveis: r1 e r2.")
r1, r2 = func(2, 5) #desempacotando os resultados para as variáveis r1 e r2
print('r1, r2 = func(2, 5)')
print()

print("imprimindo na tela os valores descompactados nas variáveis r1 e r2")
print(r1) #retorna o valor de x**2
print(r2) #retorna o valor de y**2

print()
