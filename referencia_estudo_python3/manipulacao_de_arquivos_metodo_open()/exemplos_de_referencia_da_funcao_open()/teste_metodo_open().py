'''
# a forma mais comum de abrir um arquivo com a função open().
# nesse modo de abrir o arquivo, é necessário fechar o arquivo com .close().

f = open('test0.txt', 'r')

print(f.name)

f.close() #fechando o arquivo com .close().
'''

'''
# existe uma outra forma de abrir um arquivo, mas que não precisa de usar o .close() pq
# nessa sintaxe já é fechado automaticamente, confira abaixo:

# o comando abaixo significa: com o arquivo 'test.txt' aberto na variável 'f'. 
# obs: o arquivo já é fechado sem utilizar o .close()
with open('test1.txt', 'r') as f:
    pass # aqui dentro do bloco, você define 
         # as manipulações/comportamento do arquivo, 
	 # lembrando: o arquivo já é fechado automaticamente ao
         # sair desse bloco (sem utilizar o .close())
	 

# imprime True se o arquivo foi fechado, e False se não foi fechado.
print(f.closed)
'''

'''
with open('test2.txt', 'r') as f:
    f_contents = f.readlines() # retorna o texto dividido em strings a cada quebra de linha encontrada no arquivo, dentro de um array. 
    print(f_contents)
'''

'''
with open('test3.txt', 'r') as f:
    f_contents = f.readline() #lê a primeira linha do arquivo,
    print(f_contents, end='') #o end='' elimina/retira a quebra de linha embutida do print().

    #e a cada vez que o f.readline() for chamado novamente no código abaixo, lerá a lina seguinte, e assim por diante...  
    f_contents = f.readline()
    print(f_contents, end='') #o end='' elimina/retira a quebra de linha embutida do print().
'''
'''
# iterando as linhas de um arquivo
with open('test3.txt', 'r') as f:
    for line in f: #para cada linha no arquivo
        print(line, end='') #imprima cada linha do arquivo SEM a QUEBRA DE LINHA (que já é acionada/embutida do proprio print()).
'''

'''
# lendo os 100 primeiros caracteres e imprimindo. 
with open('test3.txt', 'r') as f:
    f_contents = f.read(100) #faz a leitura dos 100 primeiros carateres do arquivo.
    print(f_contents, end='') #imprima cada linha do arquivo SEM a QUEBRA DE LINHA (que já é acionada/embutida do proprio print()).
'''

'''
# visualizando o comportamento do loop while
with open('test3.txt', 'r') as f:

    size_to_read = 10 #quantos caracteres serão lidos

    f_contents = f.read(size_to_read) #leia 10 caracteres do arquivo armazenado em 'f'.
    while len(f_contents) > 0: #enquanto o tamanho de f_contents for maior que 0.
        print(f_contents, end='*') #imprima o tamanho de f_contents e insira o caractere de '*'.
        f_contents = f.read(size_to_read) #volta pra condição do loop while e procura por mais 10 caracteres.
'''

'''
# entendendo o funcionamento do metodo seek(0)
with open('test3.txt', 'r') as f:

    size_to_read = 10
    
    f_contents = f.read(size_to_read)
    print(f_contents, end='')

    f.seek(0)

    f_contents = f.read(size_to_read)
    print(f_contents)
'''

'''
# entendendo o metodo seek(0) com arquivos em modo escrita ('w').
with open('test4.txt', 'w') as f:
    f.write('Test') #escreve a palavra 'Test' no arquivo 'f'.
    f.seek(0) #zera o ponteiro de leitura para o inicio como se a leitura do programa começasse aqui.
    f.write('Rest') # e escreve a palavra 'Rest' no arquivo 'f' por cima da escrita(s) anteriore(s).
'''

'''
# copiando de um arquivo para outro
with open('test5.txt', 'r') as readFile: # abre 'test5.txt' em modo 'r' (leitura) dentro da variavel 'readFile'.
    with open('test5_copy.txt', 'w') as writeFile: # abre 'test5_copy.txt' em modo 'w' (escrita) dentro da variavel 'writeFile'.
        for line in readFile: # para cada linha em 'test5.txt'.
            writeFile.write(line) # escreva as linhas no arquivo test5_copy.txt.
'''

'''
# cópia (dos bytes) de imagem com metodo open() em modo 'b' (byte).
with open('bronx.jpg', 'rb') as readFile: # abre a imagem 'bronx.jpg' em modo 'r' (leitura) dentro da variavel 'readFile'.
    with open('bronx_copy.jpg', 'wb') as writeFile: # abre a imagem 'bronx_copy.jpg.txt' em modo 'w' (escrita) dentro da variavel 'writeFile'.
        for line in readFile: # para cada byte em 'bronx.jpg'.
            writeFile.write(line) # escreva os bytes no arquivo bronx_copy.jpg (o arquivo copiado ficará no diretório atual).
'''


# fazendo a mesma coisa do código acima, porém com loop while
with open('bronx.jpg', 'rb') as rf: # o 'rb' significa: (leitura em byte)
    with open('bronx_copy.jpg', 'wb') as wf: # o 'wb' significa: (escreva em byte)
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size) #refaz a leitura de onde parou no arquivo.
