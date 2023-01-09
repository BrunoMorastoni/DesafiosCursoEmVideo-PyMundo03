# Função para Fatorial #
def fatorial(nun=1, show=False):
    """
    --> Calcula a Fatorial de um número.
    :param nun: número a ser calculado.
    :param show: Mostra ou não a conta com o comando [True, False, nada] (Opcional)
    :return: O valor do Fatorial de um número nun
    """
    f = 1
    for c in range(nun, 0, -1):
        if show:
            print(c, end=' ')
            if c > 1:
                print('x', end=' ')
            else:
                print('=', end=' ')
        f *= c
    return f


print(fatorial(5, False))
