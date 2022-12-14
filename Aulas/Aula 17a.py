# Listas / são mutáveis #
lanche = ['hamburger', 'suco', 'pizza', 'picolé']
print(f'{lanche}')

# Comando para adicionar um elemento ao fim da lista #
lanche.append('cookie')
print(f'{lanche} ===> var.append()')

# Comando para adicionar um elemento em um lugar específico da lista #
lanche.insert(0, 'Cachorro quente')
print(f'{lanche} ===> var.insert()')

# Comando para remover/apagar elementos #
del lanche[2]
print(f'{lanche} ===> del var[]')

lanche.pop()
print(f'{lanche} ===> var.pop()')
# Normalmente usado para remover o ultimo parametro, mas é possivel delimitar

lanche.remove('pizza')
print(f'{lanche} ===> var.remove(parametro em str)')

# Criando lista com um range #
valores = list(range(4, 11))
print(valores)

# Organizando com sort() #
val2 = [8, 2, 5, 4, 9, 3, 0]
val2.sort()
print(val2)

# Organizando com sort porém ao contrario #
val2.sort(reverse=True)
print(val2)

# Saber o tamanho com len(var) #
print(len(val2))

# Copiando uma lista com outra
a = [2, 3, 4, 7]
b = a[:]
b[2] = 8

print(f'Lista A: {a}')
print(f'Lista B: {b}')
