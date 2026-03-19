""" Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. 
O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar. 
O valor da prestação mensal não pode ser superior a 30% do salário. 
Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo número de meses a pagar.
"""
# Usando float() para dinheiro é mais seguro do que int()

valor_imovel = float(input("Valor do imóvel: "))
salario = float(input("Digite o seu salário: "))
anos = int(input("Quantidade de anos a pagar: "))


meses = anos * 12 #  Converte a quantidade de anos em meses

valor_prestacao = valor_imovel / meses # Calcula o valor real da prestação mensal

limite_salario = salario * 30 / 100 #  Calcula qual é o limite de 30% do salário

if valor_prestacao > limite_salario: #  Compara se a prestação ultrapassa o limite permitido
    print(f"O valor da prestação comsome mais de 30% do salario. REPROVADO! {valor_prestacao:.2f}")

else: # se a primeira condição for falsa ela cai aqui
     print(f"O emprestimo bancário foi aprovado! Valor mensal: R${valor_prestacao:.2f}")

