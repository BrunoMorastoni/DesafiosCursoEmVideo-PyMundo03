# Funções P2 (atividade) #
def fatorial(nun=1):
    f = 1
    for c in range(nun, 0, -1):
        f *= c
    return f
#n = int(input('Digite um número: '))
#print(f'O fatorial de {n} é {fatorial(n)}')
##
#f1 = fatorial(5)
#f2 = fatorial(4)
#f3 = fatorial()
#print(f'Os resultados respectivamente são {f1}, {f2}, {f3}')


def par(n=1):
    if n % 2 == 0:
        return True
    else:
        return False
#num = int(input('Digite um número: '))
# if par(num):
#    print('O número é par')
# else:
#    print('O número é Impar')
