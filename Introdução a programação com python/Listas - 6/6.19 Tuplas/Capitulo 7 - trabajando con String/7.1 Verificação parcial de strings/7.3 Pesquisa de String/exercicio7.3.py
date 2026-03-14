"""Escreva um programa que leia duas strings e gere uma terceira apenas com os caracteres que aparecem em uma delas.
 1ª string: CTA 2ª string: ABC 3ª string: BT A ordem dos caracteres da terceira string não é importante.
 """

string1 = "CTA"
string2 = "ABC"

resultado = ""

for letra in string1: # Procurar as letras da string1 que não estão na string2
    if letra not in string2 and letra not in resultado:
        resultado += letra

for letra in string2: # Procurar as letras da string2 que não estão na string1
    if letra not in string1  and letra not in resultado:
        resultado += letra

print(f"O resultado: {resultado}")              