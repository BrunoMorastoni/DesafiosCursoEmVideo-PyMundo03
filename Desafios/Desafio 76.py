# Lista de Preços com Tupla #
lista = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Penal', 25.00, 'Transferidor',
         4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)

print('='*60)
print('Lista de Preços'.center(60, '-'))
print('='*60)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]}'.ljust(50, '.'), end='R$: ')
    else:
        print(f'{lista[pos]}')
print('='*60)
