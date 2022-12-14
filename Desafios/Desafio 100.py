# Funções para sortear e somar #
from random import randint
from time import sleep


def sorteia(lista):
    print(f'Sorteando 5 valores da lista', end=' ')
    for cont in range(0, 5):
        val = randint(0, 10)
        lista.append(val)
        print(f'{val}', end=' ', flush=True)
        sleep(0.3)
    print('FIM')


def somaPar(lista):
    s = 0
    for num in lista:
        if num % 2 == 0:
            s += num
    print(f'Somando os valores pares de {lista}, temos {s}')


n = list()
sorteia(n)
somaPar(n)
