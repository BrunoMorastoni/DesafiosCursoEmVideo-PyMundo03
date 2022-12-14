# Matriz em Python #
m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        m[l][c] = int(input(f'Digite um valor para a posição [{l}, {c}]: '))

print('-'*50)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{m[l][c]}]', end=' '.center(2))
    print()
