# Lista composta e análise de dados #
galera = list()
dado = list()
menor = 0
maior = 0
cont = 0

while True:
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Peso: ')))
    if len(galera) == 0:
        maior = menor = dado[1]
    else:
        if dado[1] > maior:
            maior = dado[1]
        if dado[1] < menor:
            menor = dado[1]
    cont += 1
    galera.append(dado[:])
    dado.clear()
    cont += 1
    resp = str(input('Quer continuar? [S|N] ')).upper()
    if resp == 'N':
        print('='*100)
        print(f'Ao todo, você cadastrou {cont} pessoas.')
        print(f'O maior peso foi {maior}Kg. De ', end='')
        for p in galera:
            if p[1] == maior:
                print(f'{p[0]}', end=' ')
        print()
        print(f'O menor peso foi {menor}Kg. De ', end='')
        for p in galera:
            if p[1] == menor:
                print(f'{p[0]}', end=' ')
        break
