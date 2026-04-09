# Faça um programa que percorra duas listas e gere uma terceira sem elementos repetidos.

lista1 = ['a', 'b', 28,  2025, 'c', 'r', 'u']
lista2 = ['r', 'c', 2025, 'd', 'n', 'o']

mylista = []

contador = 0



while contador < len(lista1):
    if lista1[contador] not in mylista:
        mylista.append(lista1[contador])
    contador += 1   


contador1 = 0

while contador1 < len(lista2):
    if lista2[contador1] not in mylista:
        mylista.append(lista2[contador1])
    contador1 += 1

print(mylista)    