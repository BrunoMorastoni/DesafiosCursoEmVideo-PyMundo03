# Listas com pares e ímpares #
impar = list()
par = list()

for c in range(0, 7):
    n = int(input(f'Digite o {c+1}º valor: '))
    if n % 2 == 0:
        par.append(n)
        par.sort()
    else:
        impar.append(n)
        impar.sort()

print('-'*50)
print(f'Os valores pares digitados foram: {par}')
print(f'Os valores impares digitados foram: {impar}')
