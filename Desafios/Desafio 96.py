# Função que calcula área #
def area(l, c):
    a = l * c
    print(f'A área de um terreno de {l}m por {c}m é de {a}m².')


def linha():
    print('='*50)


linha()
print(f'Controle de Terrenos'.center(50))
linha()
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l, c)
