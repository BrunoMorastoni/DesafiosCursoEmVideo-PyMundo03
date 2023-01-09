# módulo #

def aumentar(n=0, taxa=0, formato=False):
    res = n + (n * taxa/100)
    return res if formato is False else moeda(res)


def diminuir(n=0, taxa=0, formato=False):
    res = n - (n * taxa/100)
    return res if formato is False else moeda(res)


def dobro(n=0, formato=False):
    res = n*2
    return res if formato is False else moeda(res)


def metade(n=0, formato=False):
    res = n/2
    return res if formato is False else moeda(res)


def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')


def resumo(n=0, taxa=10, tx=5):
    print('='*50)
    print('Resumo Do Valor'.center(50))
    print('='*50)
    print(f'Preço analisado: \t\t\t{moeda(n)}')
    print(f'Dobro do preço: \t\t\t{dobro(n,True)}')
    print(f'Metade do preço: \t\t\t{metade(n,True)}')
    print(f'{taxa}% de aumento: \t\t\t{aumentar(n,20,True)}')
    print(f'{tx}% de redução: \t\t\t{diminuir(n,12,True)}')
    print('='*50)
