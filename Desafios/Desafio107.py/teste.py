import moeda

p = float(input('Digite um preço: R$'))
print(f'A metade de R${p} é R${moeda.metade(p)}')
print(f'O dobro de R${p} é R${moeda.dobro(p)}')
print(f'A taxa de 25% adicionada sobre o R${p} é de {moeda.aumentar(p,25)}')
print(f'A taxa de 10% diminuida sobre o R${p} é de {moeda.diminuir(p,10)}')
