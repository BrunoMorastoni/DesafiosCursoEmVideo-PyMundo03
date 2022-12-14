# Contando vogais em Tupla #
lista = ('enfrente', 'problemas', 'leve', 'melhor', 'presentes',
         'cada', 'dia', 'mais', 'bom', 'sua', 'vida')

for pos in lista:
    print(f'\nNa palavra {pos.upper()} temos: ', end='')
    for letra in pos:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
            