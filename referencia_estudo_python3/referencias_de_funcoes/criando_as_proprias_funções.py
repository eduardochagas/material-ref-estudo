print('=-'*20+' Criando as proprias funções'+20*'-=')

print('Sem usar funções, a soma é:', (5+6))
print()
print(''' As funções NÃO PODEM ser chamadas antes
da linha onde ela foi criada.''')

def soma(num1, num2):
    print('Usando funções (DEF), a soma é: ', (num1+num2))

def subtração(num1, num2):
    print('Usando funções (DEF), a soma é: ', (num1-num2))

soma(5, 6)
soma(75, 6)
soma(5, 96)
soma(56, 46)
soma(15, 16)
subtração(44, 23)

# usando comando return
def soma1(num1, num2):
    return num1+num2

print('Usando funções (DEF) com return, a soma é: ',soma1(8,7))

valor1 = 70
valor2 = 80
print('Usando funções (DEF) com variáveis, a soma é: ', soma1(valor1, valor2))

def numeropar(numero):
    return (numero % 2 == 0)

print('O numero 4 é par ?: ', numeropar(4))
print('O numero 5 é par ?: ', numeropar(5))

def parouimpar(numero1):
    if numeropar(numero1):
        return 'par'
    else:
        return 'impar'

print('O número 7 é :', parouimpar(7))
print('O número 8 é :', parouimpar(8))

"""
#####################################################
#
#  Criando uma função com um valor padrão no parâmetro
#
#####################################################

	Funções podem ser definidas criando parâmetros com valores padrão, ou seja, caso não seja inserido nenhum valor no parâmetro, é utilizado o valor padrão do parâmetro.

		ex:

			def func(n1, n2, nome='eduardo'):
				print(n1,n2, nome)


			func(5, 10) # será imprimido os valores: 5, 10 e 'eduardo', pq 'eduardo' é o valor padrão definido no parâmetro nome. 

			func(5, 10, weverton) # será imprimido os valores: 5, 10 e 'weverton', pq o valor 'weverton' sobreescreve o valor definido por padrão no parâmetro (que é: nome='eduardo').


				OBS: a partir do momento que eu crio um parâmetro com valor padrão em uma função, todos os parâmetros seguintes obrigatóriamente devem tbm ser definidos com valor padrão, ou seja, parâmetros definidos com valor padrão devem sempre ser definidos como os últimos parâmetros de uma função, pq NÃO É PERMITIDO INTERCALAR parâmetros normais com parâmetros que contêm valor padrão.
				

############################################
#
#  Funções com parâmetros *args e **kwargs
#
############################################

	OBS1: o nome args (SOMENTE O args, O SINAL DE * É OBRIGATÓRIO) é uma convenção do python para utilização dos parâmetros de função que recebem uma quantidade não-fixa de valores. 

	OBS2: o nome kwargs (SOMENTE O kwargs, O SINAL DE ** É OBRIGATÓRIO) é uma convenção do python para definir parâmetros com valor na função no momento em que a função é chamada,por exemplo:

		ex:
			def func(**kwargs):
				print(kwargs)


			func(nome='eduardo', idade=31)

	Não é necessário definir os parâmetros exatamente com esses nomes (args e kwargs), mas é a forma como todos os programadores python utilizam por convenção da comunidade Python.


	-------------------------------------------
	Funções em python com parâmetros *args
	-------------------------------------------

		OBS: funções com parâmetro *args retornam valores DENTRO DE UMA TUPLA.

		OBS2: as tuplas são imutáveis, ou seja, vc não pode mudar os valores dentro de uma tupla como mudamos valores em uma lista.

			ex:					
				def func(*args): 
					print(args)


				func(1, 2, 3, 4, 5) #retorna os valores dentro de uma tupla. 


		Podemos acessar os indices da tupla, como se fosse uma lista.

			def func(*args):
				print(args[0])
				print(args[1])
				print(args[-1])
				print(len(args))


			func(1, 2, 3, 4, 5) 


		Podemos inserir uma lista no parâmetro *args, e inserir mais valores no parâmetro *args tbm.

			def func(*args):
				print(args)


			lista = [1, 2, 3, 4, 5]

			func(lista, '6', '7') #imprime dentro da tupla uma lista NO PRIMEIRO INDICE o valor 6 NO SEGUNDO INDICE da tupla, e o valor 7 NO TERCEIRO INDICE da tupla.


		Podemos adicionar uma lista para ser desempacotada no parâmetro *args, e atribuir mais valores para *args, assim, todos os valores de dentro da lista e os valores de fora da lista serão inseridos dentro da tupla (lembrando que OS VALORES RETORNADOS PELO PARÂMETRO *args são retornados DENTRO DE UMA TUPLA).

			ex:

			    func(*args):
			        print(args)


			    lista = [1, 2, 3, 4, 5]

			    func(*lista, 10, 20, 30, 40, 50) #retorna todos os valores dentro de uma tupla.


				o mesmo acontece se vc inserir duas listas para ser desempacotadas no parâmetro *args.

					ex:

						func(*args):
			        		print(args)


			    		lista = [1, 2, 3, 4, 5]
			    		lista2 = [10, 20, 30, 40, 50]

			    		func(*lista, *lista2) #desempacota as duas listas e exibe todos os valores dentro de uma tupla.



	-------------------------------------------
	Funções em python com parâmetros *kwargs
	-------------------------------------------

	O parâmetro **kwargs é usado em funções que vc queira inserir o nome de um parâmetro com um valor no momento em que vc for chamar a função.

	OBS: funções com parâmetro **kwargs retornam valores DENTRO DE UM DICIONÁRIO (com {chave:valor}).
	
	
		ex1:
			def func(**kwargs):
				print(kwargs)


			lista = [1, 2, 3, 4, 5]

			func(nome='eduardo', idade=31) # inserindo em cada parâmetro o nome dos parâmetros com seus respectivos valores.



		ex2:
			def func(*args, **kwargs):
				print(args)
				print(kwargs)


			lista1 = [1, 2, 3, 4, 5]
    		lista2 = [10, 20, 30, 40, 50]

			func(*lista, *lista2, nome='eduardo', idade=31)


		imprimindo os valores de cada parâmetro definido na chamada da função.

		ex3:

			def func(*args, **kwargs):
				print(args)
				print(kwargs[nome], kwargs[idade])


			lista1 = [1, 2, 3, 4, 5]
    		lista2 = [10, 20, 30, 40, 50]

			func(*lista, *lista2, nome='eduardo', idade=31)












"""
