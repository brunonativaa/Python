# Escreva um programa que calcule o resto da divisão inteira entre dois números. Utilize apenas as operações de soma e subtração para calcular o resultado.

dividendo = int(input("Digite um número: "))
divisor = int(input("Digite outro número: "))

quociente = 0 
resto = dividendo

if divisor == 0:
    print("Erro: Divisão por zero não permitida! ")
else:    

    while resto >= divisor:
        resto = resto - divisor
        quociente = quociente =+ 1
        

print(f"Resultado da divisão:  {quociente}")  

print(f"Resto: {resto}")