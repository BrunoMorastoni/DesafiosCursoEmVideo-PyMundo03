# Funções #
def selo(txt):
    print('='*50)
    print(txt.center(50))
    print('='*50)


def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de {a} + {b} = {s}')


def contador(*n):
    tam = len(n)
    print(f'O tamanho dos valores {n} são {tam}')


def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1


def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'A soma dos valores {valores} é {s}')


valores = [9, 10, 6, 8, 2, 4, 1]
selo('Título')
soma(5, 1)
contador(2, 4, 1)
dobra(valores)
print(valores)
soma(5, 9)
