# Jogo de Dados em Python #
from random import randint
from operator import itemgetter

print('Valores Sorteados:'.center(50))
jogo = {'1º jogador': randint(1, 6), '2º jogador': randint(
    1, 6), '3º jogador': randint(1, 6), '4º jogador': randint(1, 6)}
print('='*50)
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.'.center(50))

print('='*50)
print('<=> Ranking de Jogadores <=>'.center(50))

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: Tirou {v[1]} = {v[0]}'.center(50))
print('='*50)
