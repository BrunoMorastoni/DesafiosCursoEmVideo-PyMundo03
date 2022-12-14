# Número por Extenso #
n = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze',
     'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

var = int(input('Digite um número entre 0 e 20: '))
while var < 0 or var > 20:
    var = int(input(f'Tente novamente, digite um número entre 0 e 20: '))
else:
    numero = n[var]
    print(f'Você escreveu o número {numero}')
