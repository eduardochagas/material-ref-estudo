'''
.close() - fecha o arquivo.
.readlines() -
.readline() -
.flush() - força a gravação dos dados no arquivo

.mode - é uma propriedade que retorna o modo como o arquivo foi
aberto, ou seja, se o modo foi um desses: (r, w, a, w+, a+).
.name - é uma propriedade que retorna o nome do arquivo.

.closed - é uma propriedade que retorna um boleano (True ou False) para dizer se
o arquivo foi fechado.
'''


arquivo = open('texto.txt', 'w') # w= escrita
arquivo.write('#Lista de pessoas da familia do Neri:\n\n ')
arquivo.write('*Neri\n')
arquivo.write('Lisiane\n')
arquivo.write('Giulia\n')
arquivo.write('%Isso não deve ser impresso\n')
arquivo.write('Gustavo\n')
#arquivo.flush()
arquivo.close()
print('O modo ao qual o seu arquivo foi aberto é: ', arquivo.mode)
print('O arquivo está Fechado?: ',arquivo.closed)

arquivo = open('familia.txt', 'r') # r= leitura
for linha in arquivo.readlines():
    print(linha)
arquivo.close()
