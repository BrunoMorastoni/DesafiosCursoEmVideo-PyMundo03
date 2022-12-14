# Maior e menor valores em Tupla #
from random import randint

num = (randint(1, 10), randint(1, 10), randint(
    1, 10), randint(1, 10), randint(1, 10))
num_sort = sorted(num)
print(f'Os valores sorteados foram: {num}')
print(f'O maior valor sorteado foi {num_sort[-1]}')
print(f'O menor valor sorteado foi {num_sort[0]}')
