import requests

letras = requests.get ('https://www.letras.mus.br/')

print(letras.text)