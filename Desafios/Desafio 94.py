# Unindo dicionários e listas #
dado = dict()
galera = list()
soma = 0
media = 0
mulher = list()

while True:
    dado['nome'] = str(input('Nome: '))

    while True:
        dado['sexo'] = str(input('Sexo: [M|F] ')).upper()[0]
        if dado['sexo'] in 'MF':
            break
        else:
            print('Error - Favor digitar apenas M ou F')

    dado['idade'] = int(input('Idade: '))
    soma += dado['idade']

    galera.append(dado.copy())

    while True:
        cont = str(input('Você quer continuar? [S|N] ')).upper()[0]
        if cont in 'SN':
            break
        else:
            print('Erro - Favor digitar apenas S ou N ')
    if cont == 'N':
        break

print('='*50)
print(f'Ao todo temos {len(galera)} pessoas cadastradas.')

media = (soma / len(galera))
print(f'A média das idades são {media:.2f} anos.')

print(f'As mulheres cadastradas foram ', end='---> ')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}', end=' ')

print()
print(f'Lista das pessoas com a idade acima da média: ')
for p in galera:
    if p['idade'] >= media:
        print('-'.center(50))
        for k, v in p.items():
            print(f'{k} = {v}')
        print()

print('FIM')
