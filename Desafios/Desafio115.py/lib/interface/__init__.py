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


def linha(tam=50):
    return '=' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(50))
    print(linha())


def menu(lista):
    cabecalho('Menu Principal')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    opc = leiaInt('Sua opção: ')
    return opc
