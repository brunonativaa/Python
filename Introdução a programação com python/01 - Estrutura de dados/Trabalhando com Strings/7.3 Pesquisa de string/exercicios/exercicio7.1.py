""" Escreva um programa que leia duas strings. Verifique se a segunda ocorre dentro da primeira e imprima a posição de início. 
1ª string: AABBEFAATT 2ª string: BE Resultado: BE encontrado na posição 3 de AABBEFAATT
"""

string1 = input("Digite a primeira string: ")
string2 = input("Digite a segunda string: ")


resultado = string1.find(string2)

if resultado >= 0:
    print(f"Resultado: {string2} encontrado na posição: {resultado} de {string1}")
else:
    print(f"Resultado: {string2} não foi encontrada em {string1}")    