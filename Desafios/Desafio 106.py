# Interactive helping system in Python #
c = ('\033[m', '\033[0;30;41m', )


def ajuda(com):
    help(com)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print('='*tam)
    print(msg.center(tam))
    print('='*tam)


cmd = ''
while True:
    titulo('Sistema de Ajuda com o PyHelp')
    cmd = str(input('Função ou Biblioteca? '))
    if cmd.upper() == 'FIM':
        break
    else:
        ajuda(cmd)
titulo('Tchau')
