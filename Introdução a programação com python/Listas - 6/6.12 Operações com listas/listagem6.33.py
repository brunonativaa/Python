# Podemos percorrer uma lista de forma a verificar o menor e o maior valor (Listagem 6.33).
# Verificação do maior valor


lista = [1, 7, 2, 4]

maximo = lista[0]

for e in lista:
    if e > maximo:
        maximo = e

print(maximo)