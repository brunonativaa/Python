word1 = "AABBEFAATT"
word2 = "BE"

# O find procura word2 dentro de word1 e devolve o número da posição
posicao = word1.find(word2)

# Se posição for maior ou igual a zero, significa que achou!
if posicao >= 0:
    print(f"{word2} encontrado na posição {posicao} de {word1} ")
else:
    print(f"{word2} não foi encontrado na {word1}")