import random

print('=-'*30 + ' Metodos do Módulo random ' + '-='*30)
print()

print('gerando uma sequencia de 0 a 10 SEM metodos random')
for num in range(1, 11): #irá gerar sequencia de 1 a 10
    print(num)
print()

print('random.random() - gera valores aleatórios (não tem parametros)')
for num in range(10): #irá gerar valores aleatórios entre 0 e 1.
    print(random.random())
print()

print('random.randint() - gera valores aleatórios inteiros, do valor definido ')
print('no primeiro parametro, até o valor definido no segundo parametro.')
for num in range(10): #irá gerar valores aleatórios
    print(random.randint(1, 50))
print()


print('random.sample(lista, x) - pega uma determinada quantidade de itens 
print('aleatórios (defina a quantidade inserindo um número (que é a quantidade) em x) dentro de uma lista')
l = [4, 2, 7, 5, 9, 6, 8]
print(l)
random.sample(l, 4)
print(l)
print()

print('random.uniform() - gera valores de ponto flutuante do valor definido no')
print('primeiro parametro, até o valor definido no segundo parametro.')
for num in range(10): #irá gerar valores aleatórios de ponto flutuante
    print(random.uniform(20, 30))
print()

print('random.shuffle() - embaralha os itens da lista inserida no parametro.')
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
print(lista)
random.shuffle(lista) # embaralha os itens da lista
print(lista)
print()

print('random.choice() - escolhe aleatóriamente um item de uma lista.')
lista2 = [10, 2, 5, 67, 3, 98]
print(lista2)
print(random.choice(lista2))
print()

'''
print('random.randrange() - gera números inteiros aleatórios entre 0 e o numero definido)
print('no parametro menos 1')


'''
