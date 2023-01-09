# Site está acessível? #
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://github.com/BrunoMorastoni')
except (urllib.error.URLError):
    print('!!!Erro!!! - O Site não está acessivel')
else:
    print(f'Tudo certo site está acessível')
