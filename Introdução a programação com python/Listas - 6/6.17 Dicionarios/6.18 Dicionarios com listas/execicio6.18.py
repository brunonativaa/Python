# Escreva um programa que gere um dicionário, onde cada chave seja um caractere, e seu valor seja o número desse caractere encontrado
#  em uma frase lida. Exemplo: O rato -> { “O”:1, “r”:1, “a”:1, “t”:1, “o”:1}



frase_usuario = input("Escreba una frase: ")

dicionario_frase = { }

for frase in frase_usuario:
    if frase_usuario not in dicionario_frase:
     dicionario_frase[frase] = 1
    else:
       dicionario_frase[frase] = dicionario_frase[frase_usuario] + 1

print(dicionario_frase)
