"""Escreva um programa que leia duas strings e gere uma terceira apenas com os caracteres que aparecem em uma delas.
 1ª string: CTA 2ª string: ABC 3ª string: BT A ordem dos caracteres da terceira string não é importante. """


string1 = input("Digite a primeira string: ")
string2 = input("Digite a segunda string: ")

string3 = ''

for letra in string1:
    if letra in string2 and letra not in string3:
        string3 += letra  
print(f"Terceira palavra: {string3}")        