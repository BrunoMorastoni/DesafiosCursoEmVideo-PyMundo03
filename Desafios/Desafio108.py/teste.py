import moeda

p = float(input('Digite um preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(
    f'A taxa de 25% adicionada sobre o {moeda.moeda(p)} é de {moeda.moeda(moeda.aumentar(p,25))}')
print(
    f'A taxa de 10% diminuida sobre o {moeda.moeda(p)} é de {moeda.moeda(moeda.diminuir(p,10))}')
