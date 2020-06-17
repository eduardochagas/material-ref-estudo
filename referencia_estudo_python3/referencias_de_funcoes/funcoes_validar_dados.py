# sem função
'''
while True:
    nota = int(input('Digite a nota do aluno entre 0 e 10: '))
    if nota < 0 or nota > 10:
        print('Atenção, a nota é inválida, tem que ser entre 0 e 10')
    else:
        print('Nota válida.')
        break
'''
#Com função
def validar(pergunta, notaMin, notaMax):
    while True:
        nota = int(input(pergunta))
        if nota < notaMin or nota > notaMax:
            print('Atenção, a nota é inválida, tem que ser entre %d e %d' % (nota, notaMin, notaMax))
        else:
            print('Nota válida.')
            return True

validar('Digite a nota do aluno: ', 2, 8)
