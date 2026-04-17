""" Escreva um programa que leia duas strings e gere uma terceira com os caracteres comuns às duas strings lidas. 
1ª string: AAACTBF 2ª string: CBT Resultado: CBT A ordem dos caracteres da string gerada não é importante, mas deve conter 
todas as letras comuns a ambas.

"""

word1 = "AAACTBF"
word2 = "CBT"

resultado = ""

# Percorre cada caractere da primeira string
for letra in word1:
    if letra in word2 and letra not in resultado:  # Verifica se a letra está na string2 E se ainda não está no resultado
        resultado += letra  # Adiciona a letra comum na terceira string
print(f"Resultado: {resultado}")


