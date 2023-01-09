# Funções para votação #

def voto(ano):
    """
    --> Calcula a idade e mostra se o voto é obrigatorio, opcional ou ainda não vota.
    :param ano: ano em que nasceu.
    """
    from datetime import date
    ano_agora = date.today().year
    idade = ano_agora - ano
    if idade >= 16 and idade < 18 or idade > 70:
        print(f'Com {idade} anos o seu voto é Opcional.')
    if idade >= 18 and idade < 70:
        print(f'Com {idade} anos o seu voto é Obrigatório.')
    if idade < 16:
        print(f'Com {idade} anos você não vota.')


ano_nascimento = int(input('Em que ano você nasceu? '))
print(voto(ano_nascimento))
