""" Nem sempre nossos programas serão tão simples. Muitas vezes, precisaremos aninhar vários if para obter o comportamento desejado
do programa. Aninhar, nesse caso, é utilizar um if dentro de outro. Vejamos o exemplo de calcular a conta de um telefone celular 
da empresa Tchau. Os planos da empresa Tchau são bem interessantes e oferecem preços diferenciados de acordo com a 
quantidade de minutos usados por mês. Abaixo de 200 minutos, a empresa cobra R$ 0,20 por minuto. Entre 200 e 400 minutos,
o preço é de R$ 0,18. Acima de 400 minutos, o preço por minuto é de R$ 0,15. O programa da listagem 4.6 resolve esse problema."""

# Conta de telefone com três faixas de preco

minutos = int(input("Quantos minutos você utilizou este mês: "))

if minutos < 200: # Primeira condição
    preco = 0.20    # atribui o preço  a variavel

else:   # If alinhado dentro do else
    if minutos < 400:  #condição 
        preco = 0.18

    else: # else alinhado com if
     preco = 0.15

total = minutos * preco 


print(f"O valor cobrado foi de R${total}")
print(f"Por minutos usados: {minutos}mi")