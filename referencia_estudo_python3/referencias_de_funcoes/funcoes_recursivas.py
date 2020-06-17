
def fatorialRecursividade(numero):
    print('Fatorial com recursividade do número %d: ' % numero)
    if numero == 0 or numero == 1:
        print('O fatorial de %d é = 1' % numero)
        return 1
    else:
        f = numero*fatorialRecursividade(numero-1)
        print('O fatorial de %d = %d' % (numero, f))
    return f

fatorialRecursividade(5)
