
# Modifique o programa de forma a escrever a palavra secreta caso o jogador perca.


palavra = input("Digite a palavra secreta: ").lower().strip()
# input para chamar os métodos de string lower e strip.


for x in range(100):
    print() # Pulando várias linhas para que o jogador não veja o que foi digitado como palavra

digitadas = []
acertos = []

erros =0

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

    print("X==:==\nX :  ")
    print("X  0 " if erros >= 1 else "X")

    linha2 = ""   

    if erros == 2:
        linha2 = "  |  "

    elif erros == 3:
        linha2 = " \|  "

    elif erros == 4:
        linha2 = "\|/"

    print(f"X{linha2}")

    linha3 = ""

    if erros == 5:
        linha3 += " /   "

    elif erros >= 6:
        linha3 += " / \ "

    print(f"X{linha3}")
    print("X\n========")

    if erros == 6:
        print("Enforcado!")
        print(f"A palavra é: {palavra}")
        print("Game Over👾")
        break # O break encerra o jogo quando o jogador perder!