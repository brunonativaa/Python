carros = ["gol", "celta", "palio"]

for carro in carros: # iterando sobre a lista de carros
    print(carro)


for indice, carro in enumerate(carros): # iterando sobre a lista de carros com o índice usando a função enumerate()
    print(f"{indice}: {carro}")
