# Controle da utilização de salas de um cinema

lugares_vagos = [10, 2, 1, 3, 0]

while True:
    sala = int(input("Sala (0 para sair): "))
    
    if sala == 0:
        print("Encerrando o programa.")
        break
    if sala > len(lugares_vagos) or sala < 1:
        print("Número de sala inválido. Tente novamente.")
    elif lugares_vagos[sala - 1] == 0:
        print(f"Desculpe, a sala {sala} está lotada.")
    else:
        lugares = int(input(f"Quantidade de lugares solicitados: {lugares_vagos[sala - 1]} disponíveis. "))
        if lugares > lugares_vagos[sala - 1]:
            print(f"Desculpe, não há lugares suficientes na sala {sala}.")
        elif lugares <= 0:
            print("numero de lugares inválido. Tente novamente.")

        else:
            lugares_vagos[sala - 1] -= lugares
            print(f"Venda realizada. Lugares vendidos: {lugares}")

    print(f"Ultilização final das salas:")

    for x , l in enumerate(lugares_vagos):
        print(f"Sala {x + 1}: {l} lugares vagos")