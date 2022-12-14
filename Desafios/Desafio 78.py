# Maior e Menor valores na Lista #
lnum = []
for cont in range(1, 6):
    lnum.append(int(input(f'Digite um {cont}º valor: ')))


print(f'Você digitou esse valores: {lnum}')

lnum.sort()
print(
    f'O maior valor digitado foi {lnum[4]}')

print(
    f'O menor valor digitado foi {lnum[0]}')
