
try:
    print(6/2)
    print(1/0)
except ZeroDivisionError:
    print('Atenção, o número não pode ser dividido por zero!')


try:
    arquivo = open('cursos.txt')
except FileNotFoundError:
    print('Atenção, esse arquivo não existe')


try:
    arquivo = open('cursos2.txt')
    try:
        print(arquivo.readline())
        print(arquivo.readline())
    finally:
        print('final')
        arquivo.close()
except FileNotFoundError:
    print('Atenção, esse arquivo não existe')

'''
o finally tem que ser sempre usado 
para que mesmo que der erro na aplicação,
o arquivo consiga ser fechado e os dados
consigam ser gravados no arquivo.
'''
# o código abaixo dá erro mesmo,
# para explicar o comentário acima
try:
    arquivo = open('cursos2.txt')
    print(arquivo.readline())
    print(arquivo.readline())
    print(1/0)
finally:
    print('final')
    arquivo.close()

