# Dicionário em Python #
aluno = dict()
l = list()

aluno['Nome'] = str(input('Nome: '))
aluno['Média'] = float(input(f'Média do {aluno["Nome"]}: '))
l.append(aluno.copy())
print('='*50)

print(f'O nome é igual a {aluno["Nome"]}')
print(f'A média é igual a {aluno["Média"]}')

if aluno["Média"] < 7 and aluno["Média"] >= 5:
    print(f'A situação é igual a RECUPERAÇÃO')
elif aluno["Média"] < 5:
    print(f'A situação é igual a REPROVADO')
else:
    print(f'A situação é igual a APROVADO')
