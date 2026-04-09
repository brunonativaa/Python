lista = ['a']

lista.append(['b'])
print(lista)

lista.append(['c', 'd'])
print(lista)

print(len(lista))

print(lista[1])  # Isso retorna a sublista ['b']
print(lista[2])  # Isso retorna a sublista ['c', 'd']
print(len(lista[2]) ) # Isso retorna o número de elementos na sublista ['c', 'd'], que é 2
print(lista[2][1])
