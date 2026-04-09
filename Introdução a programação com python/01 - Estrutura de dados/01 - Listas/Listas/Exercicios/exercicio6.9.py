# Modifique o exemplo para pesquisar dois valores. Em vez de apenas p, leia outro valor v que também será procurado.
#  Na impressão, indique qual dos dois valores foi achado primeiro.


lista = [15, 7, 27, 39,10, 20, 30]



print("--- Sistema de Busca ---")

while True:

    p_raw = input("Digite um número para buscar na lista (p) (ou 's' para encerrar): ")
    v_raw = input("Digite outro número para buscar na lista (v)(ou 's' para encerrar): ")


    if p_raw.upper() == 'S':
        print("Encerrando o sistema de busca. Até mais!")
        break   # Encerra o loop principal se o usuário digitar 'sair'

    if v_raw.upper() == 'S':
        print("Encerrando o sistema de busca. Até mais!")
        break   # Encerra o loop principal se o usuário digitar 'sair'

    procura = int(p_raw)
    valor = int(v_raw)
    

    contador = 0 

    #loop de busca (While Filho)

    while contador < len(lista):
     if lista[contador] == procura or lista[contador] == valor:
        break   # quebra o loop quando encontrar o número
     contador += 1   
        
     
        

    if contador < len(lista):

        achado = lista[contador]
        if achado == procura and achado == valor:
            print(f"BINGO Ambos ({procura} e {valor} foram encontrados simultaneamente na posição {contador}).")

        elif achado == procura:    
            print(f"✅Sucesso! O número {procura} foi encontrado na posição {contador}.")

        else:
                print(f"✅Sucesso! O número {valor} foi encontrado na posição {contador}.")    
    else:
        print(f" ❌ Falha! Nenhum dos números {procura} ou {valor} foi encontrado na lista.")

    