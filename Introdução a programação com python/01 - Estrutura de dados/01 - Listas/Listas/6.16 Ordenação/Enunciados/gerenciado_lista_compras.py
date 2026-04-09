compras = []

compras.append("arroz")
compras.append("feijão")
compras.append("leite")

compras.insert(0, "pão")  # insere o elemento "pão" na posição 0 da lista de compras

compras.remove("leite") # remove o elemento "leite" da lista de compras

print("---- CONFERINDO A LISTA DE COMPRAS ----")    


for e in compras: # para cada elemento e na lista de compras
    print(f"Preciso comprar: {e}")


print("\n---- CONFERINDO A LISTA DE COMPRAS ORDENADA ----")
compras.sort()
print(f"lista de compras: {compras}" )