# Criando um menu #
from lib.interface import *
from time import sleep

cabecalho('Sistema com menu')
while True:
    resp = menu(['Ver Pessoas Cadastradas',
                'Cadastro de Nova Pessoas', 'Encerrar sistema'])
    if resp == 1:
        print('op01')
    elif resp == 2:
        print('op02')
    elif resp == 3:
        print('Encerrando sistema')
        print('.', end='')
        sleep(1)
        print('.', end='')
        sleep(1)
        print('.', end='')
        break
    else:
        print(f'!!!ERRO!!! - Digite uma opção válida')
