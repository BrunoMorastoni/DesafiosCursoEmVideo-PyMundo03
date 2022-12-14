# Análise de dados em uma Tupla #
n1 = int(input('Digite um número: '))
n2 = int(input('Digite mais um número: '))
n3 = int(input('Digite outro número: '))
n4 = int(input('Digite um ultimo número: '))

num = (n1, n2, n3, n4)


print(f'Você digitou esses valores: {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes.')
if 3 in num:
    print(
        f'O valor 3 apareceu pela primeira vez na {num.index(3)+1}ª posição.')
else:
    print('O valor 3 não apareceu na tupla')
print(f'Os valores pares digitados foram: ', end=' ')
for par in num:
    if par % 2 == 0:
        print(par, end=' ')
