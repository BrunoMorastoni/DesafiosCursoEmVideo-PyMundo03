# Dicionários #
pessoas = {'Nome': 'Bruno', 'Sexo': 'Masculino', 'Idade': 19}
print(f'O {pessoas["Nome"]} tem {pessoas["Idade"]} anos de idade.')
print()

# Keys
print(pessoas.keys())  # <--- Mostra os grupos
for k in pessoas.keys():
    print(k)
print()

# Values
print(pessoas.values())  # <--- Mostra os valores
for v in pessoas.values():
    print(v)
print()

# Items
print(pessoas.items())  # <--- Mostra os grupos e seus valores
for i in pessoas.items():
    print(i)
print()

# Teste 01
for k, v in pessoas.items():
    print(f'{k} = {v}')
print()

# Adicionando um elemento novo sem append
pessoas['Peso'] = 80.0
for k, v in pessoas.items():
    print(f'{k} = {v}')
print()

# Trocando nome / modificando
pessoas['Nome'] = 'Leandro'
for k, v in pessoas.items():
    print(f'{k} = {v}')
print()

# Deletando
del pessoas['Sexo']
for k, v in pessoas.items():
    print(f'{k} = {v}')
print()
