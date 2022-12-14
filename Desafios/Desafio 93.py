# Cadastro de Jogador de Futebol #
dados = dict()
gols = list()

dados['Nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {dados["Nome"]} jogou? '))
print()

if partidas != 0:
    for g in range(0, partidas):
        gols.append(int(input(f'Quantos gols na {g+1}º partida: ')))
dados['Gols'] = gols[:]
dados['Total'] = sum(gols)

print('='*50)
print(dados)

print('='*50)
for k, v in dados.items():
    print(f'O campo {k} tem o valor de {v}')

print('='*50)
print(f'O jogador {dados["Nome"]} jogou {partidas} partidas.')
for i, v in enumerate(dados['Gols']):
    print(f' Na partida {i+1}, fez {v} gols')
print(f'Fez um total de {dados["Total"]} gols')
