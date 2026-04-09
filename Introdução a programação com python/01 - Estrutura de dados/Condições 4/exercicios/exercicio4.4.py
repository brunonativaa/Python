# Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento.
#  Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, de 15%.
aumento = 0 

salario = float(input("Digite o seu salario: "))

base = 1250

if salario > base:
    aumento =  salario * 0.10

if salario <= base:
    aumento =  salario * 0.15

novo_salario = aumento + salario

 

    

print(f"O valor do seu aumento foi de R${aumento:.2f}") 
print(f"Novo Salario R${novo_salario:.2f}")      