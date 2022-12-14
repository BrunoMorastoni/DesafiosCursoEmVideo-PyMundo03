# Valores únicos em uma Lista #
lista = []

while True:
    n = int(input('Digite um valor: '))
    if n in lista:
        print('Valor já existente na lista! Tente outro valor...')
    else:
        lista.append(n)
        print('Valor adicionado com sucesso.')
    resp = str(input('Você quer continuar? [S|N] ')).upper()
    if resp == 'N':
        print('='*50)
        print(f'Voce digitou os seguintes valores {lista}')
        break
