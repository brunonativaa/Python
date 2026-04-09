#Escreva um programa que verifique se um número é palíndromo. 
# Um número é palíndromo se continua o mesmo caso seus dígitos sejam invertidos.
#  Exemplos: 454, 10501

numero_texto = input("Digite um número para verificar: ")

numero_invertido = numero_texto[::-1]

if numero_texto == numero_invertido:
    print(f"O número {numero_texto} é um Palindromo! 🚀")

else:
    print(f"O número {numero_texto} Nâo é  Palindromo. 👎")