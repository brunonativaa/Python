"""
Exercício 7.9 Modifique o programa para utilizar listas de strings para desenhar o boneco da forca. 
Você pode utilizar uma lista para cada linha e organizá-las em uma lista de listas.
Em vez de controlar quando imprimir cada parte, desenhe nessas listas, substituindo o elemento a desenhar.
Exemplo: >>> linha = list("X------") >>> linha ['X', '-', '-', '-', '-', '-', '-'] >>> linha[6] = "|" 
>> linha ['X', '-', '-', '-', '-', '-', '|'] >>> "".join(linha) 'X-----|'
"""



palavra = input("Digite a palavra secreta: ").lower().strip()
# input para chamar os métodos de string lower e strip.


for x in range(100):
    print() # Pulando várias linhas para que o jogador não veja o que foi digitado como palavra

digitadas = []
acertos = []

erros = 0

while True:
    senha = ""

    for letra in palavra:
        senha += letra if letra in acertos else "." # O else não tem : e indica o resultado caso a condição seja falsa.

    print(senha)

    if senha == palavra:
        print("Você acertou!")
        break
    
    tentativa = input("\nDigite uma letra: ").lower().strip()

    if tentativa in digitadas:
        print("Você já tentou essa letras!")
        continue

    else:
        digitadas += tentativa
        
        if tentativa in palavra:
            acertos += tentativa

        else:
            erros += 1 
            print("Você errou!")

    forca = [
        list("X==:=="),    # Linha 0 (Colunas vão de 0 a 5)
        list("X  :  "),    # Linha 1 (Colunas vão de 0 a 5)
        list("X     "),    # Linha 2 (Colunas vão de 0 a 5)
        list("X     "),    # Linha 3 (Colunas vão de 0 a 5)
        list("X     "),    # Linha 4 (Colunas vão de 0 a 5)
        list("X     "),    # Linha 5 (Colunas vão de 0 a 5)
        list("===========")  # Linha 6 
    ]
  
  
  
    if erros >= 1:
        forca[1][2] = "O"   # Cabeça (Linha 2, embaixo da corda na coluna 3)

    if erros >= 2:
        forca[2] = "|"   # Tronco (Linha 3, exatamente embaixo da cabeça)

    if erros >= 3:
        forca[2][1] = "\\"  # Braço esquerdo (Linha 3, à esquerda do tronco)

    if erros >= 4:
        forca[2][4] = "/"   # Braço direito (Linha 3, à direita do tronco)

    if erros >= 5:
        forca[4][1] = "/"   # Perna esquerda (Linha 4, embaixo do braço esquerdo)

    if erros >= 6:
        forca[4] = "\\"  # Perna direita (Linha 4, embaixo do braço direito)

    for linha in forca:
        print("".join(linha))


   # =============================================


    if erros == 6:
        print("Enforcado!")
        print(f"A palavra é: {palavra}")
        print("Game Over👾")
        break