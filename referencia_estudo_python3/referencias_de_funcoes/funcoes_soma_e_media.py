
def soma(num1, num2):
    print('Usando funções (DEF), a soma é: ', soma(num1, num2))


def somarLista(lista):
    totalSoma = 0
    for numeroLista in lista:
        totalSoma += numeroLista
    return totalSoma

def mediaLista(lista):
    return somarLista(listaNumeros) / len(lista)

listaNumeros = [5, 8, 3, 9, 1, 4, 7]
print('A soma da lista é: ', somarLista(listaNumeros))
print('A média da lista é: ', mediaLista(listaNumeros))

def somaeMedia(lista):
    totalSoma = 0
    for numeroLista in lista:
        totalSoma += numeroLista
    return totalSoma / len(lista)

print('A média da lista com a soma junto é: ', somaeMedia(listaNumeros))
