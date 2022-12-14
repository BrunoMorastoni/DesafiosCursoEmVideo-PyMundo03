# Mais sobre Matriz em Python #
m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somap = tcoluna = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        m[l][c] = int(input(f'Digite um valor para a posição [{l}, {c}]: '))

print('-'*50)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{m[l][c]}]', end=' '.center(2))
        if m[l][c] % 2 == 0:
            somap += m[l][c]
    print()
print('-'*50)

for l in range(0, 3):
    tcoluna += m[l][2]

for c in range(0, 3):
    if c == 0:
        maior = m[1][c]
    elif m[1][c] > maior:
        maior = m[1][c]

print(f'A soma dos valores pares é {somap}')
print(f'A soma dos valores da terceira coluna é {tcoluna}')
print(f'O maior valor da segunda linha é {maior}')
