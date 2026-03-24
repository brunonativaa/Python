""" Escreva um programa que leia duas strings e gere uma terceira com os caracteres comuns às duas strings lidas. 
1ª string: AAACTBF 2ª string: CBT Resultado: CBT A ordem dos caracteres da string gerada não é importante, 
mas deve conter todas as letras comuns a ambas. """

string1 = input("Digite a primeira string: ")
string2 = input("Digite a segunda string: ")

resultado = '' 

# Percorrendo cada letra da primeira string1
for letra in string1:
    # Se a letra estiver em string2 e ainda não estiver em resultado
    if letra in string2 and letra not in resultado:
        resultado += letra # Concatenando a letra no resultado

print(f"Resultado: {resultado}")