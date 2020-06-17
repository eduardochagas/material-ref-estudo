print('--------- Metodos de Array ---------')
print('-=' * 50)
print()


print('Um array comum.')
alfabeto = ['a', 'b', 'c']
print(alfabeto)
print()


# usando os operadores +=
print('O mesmo array acima incrementando mais itens á lista com os operadores +=')
alfabeto = ['a', 'b', 'c']
alfabeto += 'defg'
print(alfabeto)
print()


# usando o metodo extend()
print('estende a lista com a string inserida no parametro do metodo extend() como ')
print(' cada caractere sendo um item da lista de forma individual. ')
alfabeto = ['a', 'b', 'c']
alfabeto.extend('hijkl')
print(alfabeto)
print()


# usando o metodo append()
print('adiciona um item á lista com o metodo append()')
nomes = ['Neri', 'Selvino', 'Romilda']
nomes.append('Eduardo')
print(nomes)
print()


# usando o metodo insert()
print('insere uma string no array com o metodo insert() definindo o indice no')
print('primeiro parâmetro, e definindo a string a ser inserida, no segundo parâmetro')
nomes = ['Neri', 'Selvino', 'Romilda']
nomes.insert(1,'Weverton')
print(nomes)
print()


# usando o metodo pop()
print('retira o último elemento do array com o metodo pop()')
alfabeto = ['a', 'b', 'c', 'd', 'e']
alfabeto.pop()
print(alfabeto)
print('Obs: voce pode remover o item que quiser do array com o pop(), basta')
print('inserir o indice do item a ser removido do array como parametro do pop()')
alfabeto2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
alfabeto2.pop(1)
print(alfabeto2)
print()


print('deleta um item de um array pelo indice com o comando del alfabeto[2]')
alfabeto = ['a', 'b', 'c', 'd', 'e']
del alfabeto[2]
print(alfabeto)
print()


print('remove os indices definidos nos colchetes menos o último indice ')
print('após os dois pontos dentro dos colchetes')
alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
del alfabeto[2:4]
print(alfabeto)
print()


# usando o metodo remove()
print('remove o item do array inserindo o item desejado a ser removido no ')
print('parametro do metodo remove()')
alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
alfabeto.remove('b')
print(alfabeto)
print('')


print('Fazendo a copia de uma lista em outra variável, mas mantendo o mesmo endereço de memória,')
print('ou seja, o que for alterado em uma lista, a mesma coisa será alterada na outra.')
lista1 = ['weverton', 'ana', 'erica', 'dri']
lista2 = lista1 # Faz a cópia da lista MANTENDO O MESMO ENDEREÇO DE MEMÓRIA da lista anterior.
lista2.remove('erica')
print(lista2)
print(lista1)
print()


print('Fazendo a copia de uma lista em outra variável, mas TENDO UM ENDEREÇO DE MEMÓRIA DIFERENTE da lista anterior.')
print('ou seja, o que for alterado em uma lista, a mesma coisa NÃO SERÁ ALTERADA na outra.')
lista1 = ['weverton', 'ana', 'erica', 'dri']
lista2 = lista1[:] # Faz a cópia da lista TENDO UM ENDEREÇO DE MEMÓRIA DIFERENTE da lista anterior.
lista2.remove('dri')
print(lista2)
print(lista1)
print()


# usando o metodo count()
print('retorna quantas vezes o item inserido no parametro de cont() apareceu no array com o metodo count()')
cursos = ['python', 'java','android', 'python', 'java', 'python']
print(cursos)
print('O curso apareceu: ', cursos.count('python'), 'vezez no array')
print('O curso apareceu: ', cursos.count('java'), 'vezez no array')
print('O curso apareceu: ', cursos.count('html'), 'vezes no array') # Retorna 0 pq não tem nenhum item com esse nome no array.
print()


# usando o metodo reverse()
print('')
cursos = ['python', 'java', 'android', 'delphi', 'html', 'clipper']
print(cursos)
cursos.reverse() # NÃO FAÇA assim: print(cursos.reverse()), senão dará erro, primeiro faça array.reverse(), depois use o print(), dessa forma os dados funcionarão corretamente.
print(cursos)
print()


# usando o metodo index()
print('retorna o número do indice do elemento no array iserido como parametro no metodo index()')
cursos = ['python', 'java', 'android', 'delphi', 'html', 'clipper']
print(cursos)
print('O indice do item da lista é:', cursos.index('clipper'))
print()


# usando o metodo sort()
print('ordena os itens da lista em ordem alfabética com o metodo sort()')
listanomes = ['neri', 'lisiane', 'giulia', 'gustavo']
print(listanomes)
listanomes.sort()
print(listanomes)
print()


print()
listanomes = ['neri', 'lisiane', 'giulia', 'gustavo']
print(listanomes)
for i, nomeslista in enumerate(listanomes):
    print('Item: ', i+1, 'nome: ', nomeslista)

#print(nomeslista[2:])
print(listanomes[2:])
print()


print()
print('o metodo clear() limpa/remove todos os itens do array deixando ')
print('um array vazio, ex:')
array1 = ['eduardo', 'weverton', 'alex']
print(array1)
array1.clear()# NÃO FAÇA assim: print(cursos.clear()), senão dará erro, primeiro faça array.clear(), depois use o print(), dessa forma os dados funcionarão corretamente.
print('array depois de usar o clear()')
print(array1)
print()


print()
print('O metodo extend() é usado para inserir vários itens em uma lista extendendo-a')
array2 = ['edu', 'we', 'dri']
print(array2)
array2.extend(['alex', 'nego', 'ana', 'alexandre'])# NÃO FAÇA assim: print(cursos.extend()), senão dará erro, primeiro faça array.extend(), depois use o print(), dessa forma os dados funcionarão corretamente, e lembre-se de inserir os colchetes no parametro do extend([]) e inserir os dados dentro dos colchetes.
print('depois de usado o metodo extend(), o array ficará assim:')
print(array2)
print()


print()
print('O metodo append() é usado para adicionar um item ao final de uma array')
array3 = ['nego', 'ana', 'rafael']
print(array3)
array3.append('Inês')
print('array depois de inserir um item ao array com o metodo append()')
print(array3)
print()


"""
fatiamento de arrays
array[2:] - fatia o array a partir do indice 2 até o final da lista.
array[:5] - fatia o array do começo dele até (mas não inclusive) o indice 5.
array[::2] - fatia o array do inicio ao fim de 2 em 2 itens.
array[::-1] - exibe os valores do array de trás pra frente.  


linkando uma lista com a outra
A = [2, 3, 4, 7]
B = a[] # Ao fazer isso, vc não está copiando a lista A em B, vc está atribuindo a mesma 
lista em outra variável (no caso, na variével B), ou seja, O DADO QUE FOR ALTERADO 
EM UMA LISTA (na lista A, por exemplo), TBM SERÁ ALTERADO NA OUTRA LISTA (no caso, na lista B).
print('Lista A: {}'.format(A))
print('Lista B: {}'.format(B))


fazendo cópia de um array
A = [2, 3, 4, 7]
B = a[:] #aqui significa: COPIE TODOS OS ITENS do começo ao final da lista de A e insira em B.
Isso faz com que o valor B RECEBA UMA CÓPIA da lista A, tornando as listas com valores iguais, mas 
sendo listas independentes (a alteração de valores de uma lista, não altera o valor da outra lista).
print('Lista A: {}'.format(A))
print('Lista B: {}'.format(B))



desempacotamento de lista (array)
lista = [1, 2, 3, 4]

a, b, c = lista
print(a)
print(b)
print(c)


imprimindo na tela os valores de uma lista de forma desempacotada
lista = [1, 2, 3, 4, 5]

print(*lista) #o sinal de * antes do nome da lista indica que os valores devem ser imprimidos de forma desempacotada.

	OBS:podemos imprimir na tela os valores de uma lista de forma DESEMPACOTADA COM O CARACTER (-) COMO SEPARADOR.

		ex:			
			lista = [1, 2, 3, 4, 5]

			print(*lista, sep='-') #o sinal de * antes do nome da lista indica que os valores devem ser imprimidos de forma desempacotada e o parametro sep='-'imprime os números com o caractere traço (-) entre cada número.

	
desempacotando somente os valores que eu quiser
lista = [1, 2, 3, 4, 5]

a, b, _, d, _ = lista

print(a)
print(b)
print(d)


desempacotando os primeiros valores de uma lista, e o restante dos valores mantendo na mesma lista
lista = [1, 2, 3, 4, 5]
n1, n2, *n = lista  #a variável *n é a variável que mantém o restante dos valores da lista, na lista.
print(n1, n2, n)


para imprimir valores de uma tupla (lista imutável) que contém tipos de dados diferentes, 
utilize o loop for com range(), com o método len() dentro do segundo parâmetro do range(), ex:

listagem = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90,
            'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99,
            'Mochila', 120.00, 'Canetas', 22.30, 'Livro', 34.90)

#loop for com range() e com o método len() dentro do segundo parâmetro.
for i in range(0, len(listagem), 2):
    print(listagem[i], listagem[i+1])
    
OBS: Nesse caso, como a string aparece a cada dois itens do array em sequência,
utilizamos o terceito parâmetro com valor 2, para que o loop pule a cada dois itens
do array (começando do indice 0, como definido no primeiro parametro do range(), onde 
o indice 0 contêm a primeira string da tupla, e assim pegando cada string a cada dois indices), 
usando o listagem[i] no print), e imprimimos os valores de cada item (utilizando o listagem[i+1] no print). 
OBS2: Essa forma de imprimir dados com tipos diferentes funciona tanto para 
listas quanto para tuplas, lembrando que há formas melhores e mais eficientes de se fazer isso, esse
é só um exemplo de uma das formas de se fazer.




Metodos estudados:

clear()
count()
index()
insert()
pop()
remove()
sort()
reverse()
extend()
append()


'''
