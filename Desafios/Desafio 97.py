# Um print especial #
def escreva(txt):
    print('='*(len(txt)+4))
    print(txt.center(len(txt)+4))
    print('='*(len(txt)+4))


f = str(input(f'Escreva um algo: '))
escreva(f)
