# Palpites para a Mega Sena #
from random import randint
from time import sleep
lista = list()
jogos = list()
#
print('='*60)
print('Mega Sena'.center(60))
print('='*60)
#
q = int(input('Quantos jogos você quer sortear? '))
tot = 1
#
while tot <= q:
    cont = 0
    while True:
        num = randint(0, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
#
print()
print(f' Sorteando {q} jogos '.center(60, "-"))
#
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}'.center(60, ' '))
    sleep(1)
#
print(' | Boa Sorte | '.center(60, "-"))
