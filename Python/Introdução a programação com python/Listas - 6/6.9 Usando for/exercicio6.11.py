
# Modifique o programa da listagem 6.15 usando for.
#  Explique por que nem todos os while podem ser transformados em for.



lista = []

num = int(input("Digite um número (0 para sair): "))


for executa in lista:
    if executa == num:
        print(f"✅ Sucesso! O número {num} foi encontrado na lista.")
        break
else:
    print(f"❌ O número {num} não foi encontrado na lista.")

# a lista está ficando vazia, pois não estamos adicionando os números digitados nela. O programa não tem como encontrar o número, 
# pois a lista está vazia. Para corrigir isso, precisamos adicionar os números digitados à lista antes de realizar a busca.

# 0Nem todo while pode ser transformado em for porque o for exige algo para ser percorrido (uma lista, uma string, um range).