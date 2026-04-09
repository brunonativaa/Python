texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto: # Itera sobre cada letra do texto informado pelo usuário.
    if letra.upper() in VOGAIS: # Verifica se a letra, convertida para maiúscula, está presente na string de vogais.
        print(letra, end=" ") 
