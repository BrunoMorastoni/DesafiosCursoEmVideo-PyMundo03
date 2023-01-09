# Funções P2 #

def contador(i, f, p):  # Interactive help #
    """
    ---> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c}', end=' ')
        c += p
    print('fim')
# help(contador)


def soma(a=0, b=0, c=0):  # Parêmetros opcionais #
    """
    ---> Faz a soma de três valores e mostra na tela.
    :param a: 1º valor
    :param b: 2º valor
    :param c: 3º valor
    """
    s = a + b + c
    print(f'A soma de {a} + {b} + {c} = {s}')
# soma(8, 4)


def teste(b):  # Escopo de vairáveis #
    global a
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')
#a = 5
# teste(a)
#print(f'A fora vale {a}')


def somar(a=0, b=0, c=0):  # Retorno de valores #
    """
    ---> Faz a soma de três valores e mostra na tela.
    :param a: 1º valor
    :param b: 2º valor
    :param c: 3º valor
    """
    s = a + b + c
    return s

############################### Programa principal#####################################


r1 = somar(3, 2, 5)
r2 = somar(1, 7)
r3 = somar(4)
print(f'Meus cálculos deram respectivamente {r1}, {r2}, {r3}.')
