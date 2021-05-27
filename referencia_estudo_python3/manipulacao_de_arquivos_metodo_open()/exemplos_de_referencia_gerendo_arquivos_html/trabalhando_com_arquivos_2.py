'''
.close() - fecha o arquivo.
.readlines() -
.readline() -
.center() - imprime o(s) dado(s) entre o número de caracteres definidos no
parametro, (ex: se o número definido no parametro é 80, os dados serão inseridos
no centro desses 80 caracteres.)
.ljust() - imprime os dados com um espaçamento de caracteres vazios a
esquerda da string.
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
arquivo.write('*Lisiane\n')
arquivo.write('*Giulia\n')
arquivo.write('%Isso não deve ser impresso\n')
arquivo.write('*Gustavo\n')
#arquivo.flush()
arquivo.close()


arquivo = open('texto.txt', 'r') # r= leitura
for linha in arquivo.readlines():
    if linha[0] == '#':
        print(linha[1:].center(80))
    elif linha[0] == '*':
        print(linha[1:].rjust(80))

