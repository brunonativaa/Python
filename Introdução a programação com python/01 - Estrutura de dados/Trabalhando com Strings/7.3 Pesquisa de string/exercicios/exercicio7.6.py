""" Escreva um programa que leia três strings. Imprima o resultado da substituição na primeira, 
 dos caracteres da segunda pelos da terceira."""

string1 = input("Digite a primeira string: ")
string2 = input("Digite a segunda string: ")
string3 = input("Digite a terceira string: ")

resultado = ''

 
for letra in string1 :
    posicao = string2.find(letra)# Procura em qual posiçaõ a letra atual está na string2
    
    if posicao >= 0: # Se achou (>= 0), pega a letra na MESMA posição da string3
        resultado += string3[posicao]
    else: # Se não achou (-1), mantém a letra original
        resultado += letra

print(f"Resultado {resultado}")        
