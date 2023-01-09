# Erros e exceções #

# erros são != de exceções, erro seria algo mais sintatico

# Algumas EXCEPTION/Exceções do PY #
    # NameError
    # ValuaError
    # ZeroDivisionError
    # TypeError
    # IndexError
    # KeyError
    # EOFError

# try: except: else: finally: #
    # try:
        # operação
    # except:
        # falhou
    # else:
        # deu certo
    # finally: | opcional |
        # certo/falha

# Exemplos:
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a/b
# except Exception as erro:
    #print(f'!!!Infelizmente ocorreu um problema!!!')
    #print(f'Problema encontrado... {erro.__class__}')
except (ValueError, TypeError):
    print('Erro com os tipos de dados digitados')
except ZeroDivisionError:
    print('Não é possivel dividir o número por zero.')
else:
    print(f'O resultado de {a} dividido por {b} é {r}.')
finally:
    print('FIM')
