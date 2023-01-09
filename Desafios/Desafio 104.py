# Validando entrada de dados em Python #
def leiaInt(num):
    """
    --> Verifica se o que foi digitado é um número inteiro.
    :param num: valor a ser recebido.
    :return val: valor inteiro.
    """
    ok = False
    val = 0
    while True:
        n = str(input(num))
        if n.isnumeric():
            val = int(n)
            ok = True
        else:
            print('Erro - Digite um número inteiro')
        if ok:
            break
    return val


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar um número {n}')
