""" Escreva um programa que leia duas strings e gere uma terceira, na qual os caracteres da segunda foram retirados da primeira.
 1ª string: AATTGGAA 2ª string: TG 3ª string: AAAA  """

string1 = input("Digite a primeira string: ")
string2 = input("Digite a segunda string: ")

string3 = ''

for letra in string1: # Percorre cada letra da string1
    if letra not in string2: # verifica se letra não esta em string2
     
     string3 += letra # armazena as letras que não estao na string2 

print(f"Letras retiradas: {string2}" )
print(f"String :{string3}")


