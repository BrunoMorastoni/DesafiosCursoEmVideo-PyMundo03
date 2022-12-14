# Dividindo valores em várias listas #
lista = []
impar = []
par = []

while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)

    resp = str(input(('Você quer continuar? [S|N] '))).upper()
    if resp == 'N':
        print('='*50)
        print(f'A lista completa é {lista}')
        print(f'A lista de pares é {par}')
        print(f'A lista de impares é {impar}')
        break
