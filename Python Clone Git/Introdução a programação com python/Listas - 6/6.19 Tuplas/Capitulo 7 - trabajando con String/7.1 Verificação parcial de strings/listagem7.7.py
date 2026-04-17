s = "João comprou um carro"

nome = "joão" in s.lower()
print(nome)

nome = "CARRO" in s.upper()
print(nome)

nome = "comprou" not in s.lower()
print(nome)

nome = "barco" not in s.lower()
print(nome)

"""O operador in também pode ser utilizado com listas normais, facilitando, assim,
 a pesquisa de elementos dentro de uma lista.
 """