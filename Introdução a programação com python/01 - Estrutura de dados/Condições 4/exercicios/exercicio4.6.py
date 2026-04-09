"""Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km.
 Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km, e R$ 0,45 para viagens mais longas.
"""

distancia = int(input("Distância a percorrer em km: "))

km = 200 # já inicio a variável com o valor 

if distancia > km:    # faço a vericação da distancia com a condição
    preco = distancia * 0.45

else:
    preco = distancia * 0.50  # caso a primeira condição seja falsa

print(f"o preço da viagem é R${preco:.2f} para a distancia de {distancia}Km")    