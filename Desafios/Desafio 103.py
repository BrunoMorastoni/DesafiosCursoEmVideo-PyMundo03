# Ficha do Jogador #

def ficha(j='<Desconhecido>', g=0):
    print(f'O jogador {j} fez {g} gol.')


nome = str(input('Qual o nome do jogador? '))
gols = str(input('Quantos gols foram marcados? '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(g=gols)
else:
    ficha(nome, gols)
