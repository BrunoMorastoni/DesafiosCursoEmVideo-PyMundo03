# Tuplas são imútaveis
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[-4])  # Total -4 = hambúrguer
print(lanche[1:3])  # Do elemento 1 ao 3
print(lanche[:2])  # Do início até o elemento 2

# A primeira não enúmera a posição. As 2 ultimas fazem a mesma coisa, apenas de modo diferente
for comida in lanche:
    print(f'Eu vou comer {comida}')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')


# Somando tuplas
a = (2, 5, 4)
b = (5, 8, 1, 2)
# c = a + b é diferente de c = b + a
c = a + b
c = b + a
print(c)
