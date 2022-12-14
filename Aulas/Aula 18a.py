# Listas Compostas #
print('='*100)
print('Teste 01'.center(100))
print('='*100)
# 1
teste = list()
teste.append('Bruno')
teste.append(19)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)
print('='*100)

#
print('Teste 02'.center(100))
# 2
print('='*100)
galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')

#
print('Teste 03'.center(100))
# 3
galera2 = list()
dado = list()
for c in range(0, 2):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera2.append(dado[:])
    dado.clear()
print(galera2)
