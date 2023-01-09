import moeda

p = float(input('Digite um preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(
    f'A taxa de 25% adicionada sobre o {moeda.moeda(p)} é de {moeda.aumentar(p,25, True)}')
print(
    f'A taxa de 10% diminuida sobre o {moeda.moeda(p)} é de {moeda.diminuir(p,10, True)}')
