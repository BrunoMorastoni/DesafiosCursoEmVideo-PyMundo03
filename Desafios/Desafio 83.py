# Validando expressões matemáticas #
lista = []
e = str(input('Digite uma expressão: '))

for s in e:
    if s == '(':
        lista.append('(')
    elif s == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break

if len(lista) == 0:
    print('Sua expressão está valida')
else:
    print('Sua expressão está invalida')
