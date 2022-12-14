# Cadastro de Trabalhador em Python #
from datetime import datetime

dados = dict()
dados['Nome'] = str(input('Nome: '))

nasc = int(input('Ano de nascimento: '))
dados['Idade'] = datetime.now().year - nasc

dados['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['salário'] = float(input('Salário: R$:'))
    dados['aposentadoria'] = dados['Idade'] + \
        (dados['contratação'] + 35) - datetime.now().year
print()
for k, v in dados.items():
    print(f'{k} é {v}')
