""" Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar. 
Você deve poder calcular a soma (+), subtração (-), multiplicação (*) e divisão (/). 
Exiba o resultado da operação solicitada."""

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
operador = input("Escolha as opções: (+, -, *, /)")

if operador == "+": 
    resultado = num1 + num2
    print(f"O resultado do calculo é: {resultado}")

elif operador == "-":
    resultado = num1 - num2
    print(f"O resultado do calculo é: {resultado}")

elif operador == "*":
    resultado = num1 * num2
    print(f"O resultado do calculo é: {resultado}")

elif operador == "/":
    resultado = num1 / num2 
    print(f"O resultado do calculo é: {resultado}")


else: 
    print("Operador inválido tente novamente!")   



