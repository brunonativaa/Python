"""Você também pode testar se uma string não está contida em outra, utilizando not in (Listagem 7.6). u Listagem 7.6 
 Pesquisa de palavras em uma string usando not in
"""

s = "Todos os caminhos levam a Roma"

word = "levam" not in s

print(word)

word = "Caminhos" not in s

print(word)

word = "AS" not in s

print(word)


"""Veja que aqui também letras maiúsculas e minúsculas são diferentes.
 Você pode combinar lower e upper com in e not in para ignorar esse tipo de diferença, 
 como mostra a listagem 7.7.
 """