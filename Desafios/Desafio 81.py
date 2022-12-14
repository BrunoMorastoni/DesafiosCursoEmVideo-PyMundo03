# Extraindo dados de uma Lista #
lista = []

while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    lista.sort(reverse=True)

    resp = str(input(('Você quer continuar? [S|N] '))).upper()

    if resp == 'N':
        print(f'Você digitou {len(lista)} elementos.')
        print(f'Os valores em ordem decresecente são {lista}')
        if lista.index(5) == True:
            print('O valor 5 faz parte da lista')
        else:
            print('O valor 5 não faz parte da lista')
        break
