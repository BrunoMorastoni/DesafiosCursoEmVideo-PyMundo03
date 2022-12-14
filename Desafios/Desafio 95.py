# Aprimorando os Dicionários #
dados = dict()
gols = list()
jogadores = list()

while True:
    dados.clear()
    dados['Nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {dados["Nome"]} jogou? '))
    print()

    if partidas != 0:
        for g in range(0, partidas):
            gols.append(int(input(f'Quantos gols na {g+1}º partida: ')))
    dados['Gols'] = gols[:]
    dados['Total'] = sum(gols)

    jogadores.append(dados.copy())

    while True:
        cont = str(input('Você quer continuar? [S|N] ')).upper()[0]
        if cont in 'SN':
            break
        else:
            print('Erro - Favor digitar apenas S ou N ')
    if cont == 'N':
        break


print('='*50)
print(f'{"Nº":<8}{"Nome":<8}{"Gols":<8}{"Total":<8}')
print('-'*50)
for k, v in enumerate(jogadores):
    print(f'{k:<8}', end='')
    for d in v.values():
        print(f'{str(d):<8}', end='')
    print()

while True:
    print('='*50)
    NA = int(input('Mostrar as dados de qual jogador? (999 para encerrar) '))
    if NA == 999:
        break
    if NA >= len(jogadores):
        print(f'Não existe jogador com o código {NA}')
    else:
        print(f'{jogadores[NA]["Nome"]}'.center(50))
        for i, g in enumerate(jogadores[NA]['Gols']):
            print(f' No jogo {i+1} fez {g} gols'.center(50))
print('fim')
