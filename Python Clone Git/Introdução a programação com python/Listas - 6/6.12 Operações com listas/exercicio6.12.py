
# Altere o programa da listagem 6.33 de forma a imprimir o menor elemento da lista.



lista = [1, 7, 2, 4]
minimo = lista[0]

for e in lista:
    if e < minimo:
        minimo = e

print(minimo)