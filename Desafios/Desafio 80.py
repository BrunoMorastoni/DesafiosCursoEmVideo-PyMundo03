# Lista ordenada sem repetições #
lista = []
for cont in range(0, 5):
    n = int(input('Digite um valor: '))
    if cont == 0 or n > lista[len(lista)-1]:
        lista.append(n)
        print('Adicionado no fim da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print(f'Os valores digitados foram {lista}')
