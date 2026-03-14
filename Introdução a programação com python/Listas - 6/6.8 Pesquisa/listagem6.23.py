lista = [15, 7, 27, 39]

print("--- Sistema de Busca ---")

while True:

    entrada = input("Digite um número para buscar na lista (ou 's' para encerrar): ")

    if entrada.upper() == 'S':
        print("Encerrando o sistema de busca. Até mais!")
        break   # Encerra o loop principal se o usuário digitar 'sair'

    procura = int(entrada)
    achou = False
    contador = 0 

    #loop de busca (While Filho)

    while contador < len(lista):
        if lista[contador] == procura:
            achou = True
            break   # quebra o loop quando encontrar o número
        contador += 1

    if achou:
        print(f"✅Sucesso! O número {procura} foi encontrado na posição {contador}.")    
    
    else:
        print(f" ❌ Falha! O número {procura} não foi encontrado na lista.")

    