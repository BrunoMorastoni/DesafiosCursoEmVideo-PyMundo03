# Criando Dicionário dentro de uma lista #
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}

brasil.append(estado1)
brasil.append(estado2)

print(brasil[0])
print(brasil[1])
print()

print(brasil[0]['uf'])
