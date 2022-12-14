# Boletim com listas compostas #
dado = list()
NM = list()
#
while True:
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    dado.append([nome, [n1, n2], media])

    conti = str(input('Quer continuar? [S|N] ')).upper()
    if conti == 'N':
        print('='*50)
        print(f'{"Nº":<4}{"Nome":<10}{"Média":>8}')
        print('-'*30)
        for i, p in enumerate(dado):
            print(f'{i:<4}{p[0]:<10}{p[2]:>8.1f}')
        break
while True:
    print('='*50)
    NA = int(input('Mostar as notas de qual aluno? (999 para encerrar) '))
    if NA == 999:
        break
    if NA <= len(dado) - 1:
        print(f'Notas de {dado[NA][0]} são {dado[NA][1]}')
