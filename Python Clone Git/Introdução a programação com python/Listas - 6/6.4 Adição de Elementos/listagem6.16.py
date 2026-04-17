lista = []

lista = lista + [1]  # Isso não é recomendado, pois cria uma nova lista a cada iteração

print(lista)

lista += [2]  # Isso é recomendado, pois modifica a lista existente

print(lista)

lista += [3, 4, 5]  # Você pode adicionar vários elementos de uma vez

print(lista)