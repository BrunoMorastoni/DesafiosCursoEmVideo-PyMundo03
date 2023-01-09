# Analisando e gerando Dicionários #
def notas(*n, sit=False):
    """
    --> Calcula média dos alunos e mostra a situação
    :param n: Nota(s) tirada(s)
    :param sit: mostra ou não a situação do aluno
    :return n: retorna o dicionario com total, maio, menor, media e a situaçao caso solicitado
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situação'] = 'Boa'
        elif r['media'] <= 6.5:
            r['situação'] = 'Razoável'
        else:
            r['situação'] = 'Ruim'
    return r


resposta = notas(5.5, 9.5, 7.5, sit=True)
print(resposta)
