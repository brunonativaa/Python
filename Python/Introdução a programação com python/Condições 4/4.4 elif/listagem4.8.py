"""Python apresenta uma solução muito interessante ao problema de múltiplos ifs aninhados. A cláusula elif substitui um par else if,
mas sem criar outro nível de estrutura, evitando problemas de deslocamentos desnecessários à direita."""

# Vamos revisitar o problema da listagem 4.7, dessa vez usando elif.

 
#Categoria x preco, usando elif 

categoria = int(input("Digite a categoria do produto: ")) 

if categoria == 1:
    preco = 10

elif categoria == 2:
    preco = 18

elif categoria == 3:
    preco = 23

elif categoria == 4:
    preco = 26

elif categoria == 5:
    preco = 31

else:
    print("Opção invalida, digite uma valor entre 1 e 5!")
    preco = 0

print(f"O preço do produto escolhido é: R${preco:.2f}")