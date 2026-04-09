# Pesquisa usando for

lista = [7, 9, 10, 12]

procurar = int(input("Digite um número para buscar na lista: "))

for encontrado in lista:
    if encontrado == procurar:
        print(f"✅ Sucesso! O número {procurar} foi encontrado na lista.")
        break
else:
    print(f"❌ O número {procurar} não foi encontrado na lista.")


    """Utilizamos a instrução break para interromper a busca depois de encontrarmos o primeiro elemento em ❶.
      Em ❷ utilizamos um else, parecido com o da instrução if, para imprimir a mensagem informando que o elemento não foi encontrado.
        O else deve ser escrito na mesma coluna de for e só será executado se todos os elementos da lista forem visitados,
          ou seja, se não utilizarmos a instrução break, deixando for terminar normalmente."""