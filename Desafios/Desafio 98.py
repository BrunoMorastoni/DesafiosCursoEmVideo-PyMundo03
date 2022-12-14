# Função de Contador #
from time import sleep


def contador(i, f, p):
    print(f'Contagem de {i} até {f} pulando de {p} em {p}')

    if i < f:
        cont = 1
        while cont <= f:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.3)
            cont += p
        print('Fim')
    else:
        cont = 1
        while cont >= f:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.3)
            cont -= p
        print('Fim')


contador(1, 10, 1)
contador(10, 0, 2)
