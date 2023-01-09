# Funções aprofundadas em Python #
def leiaInt(num):
    """
    --> Verifica se o que foi digitado é um número inteiro.
    :param num: valor a ser recebido.
    :return val: valor inteiro.
    """
    while True:
        try:
            n = int(input(num))
        except (ValueError, TypeError):
            print('Erro - Digite um número inteiro válido.')
            continue
        except (KeyboardInterrupt):
            print('Erro - Favor digitar algo.')
            return 0
        else:
            return n


def leiaFloat(num):
    """
    --> Verifica se o que foi digitado é um número real.
    :param num: valor a ser recebido.
    :return val: valor real.
    """
    while True:
        try:
            n = float(input(num))
        except (ValueError, TypeError):
            print('Erro - Digite um número inteiro válido.')
            continue
        except (KeyboardInterrupt):
            print('Erro - Favor digitar algo.')
            return 0
        else:
            return n


n1 = leiaInt('Digite um número inteiro: ')
n2 = leiaFloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {n1} e o real foi {n2}')
