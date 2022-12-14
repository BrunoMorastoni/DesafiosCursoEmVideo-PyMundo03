# Função que descobre o maior #
from time import sleep


def linha(n):
    print('='*n)


def maior(*num):
    cont = maior = 0

    linha(75)

    print('Analizando os valores passados...')

    for valor in num:
        print(f'{valor}', end=' ', flush=True)
        sleep(0.3)

        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont = 1

    print(f'Foram informados {len(num)} valores ao todo')
    print(f'O maior valor inforamdo foi {maior}')

    linha(75)


maior(0, 7, 4, 51, 7, 91)
