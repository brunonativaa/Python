# Escreva um programa que leia uma string e imprima quantas vezes cada caractere aparece nessa string.

string1 = input("Digite a string: ")

resultado = ''

for letra in string1:
    # só conta e imprime se for letra nova
    if letra not in resultado:
       # Conta quantas vezes a letra aparece na palavra inteira 
        quantidade = string1.count(letra)
    

    print(f"{letra}: {quantidade}x")

    # Guarda a letra na memória para não contá-la de novo
    resultado += letra