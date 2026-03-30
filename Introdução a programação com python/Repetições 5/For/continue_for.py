for numero in range(100):

    if numero == 10:
        print( "saindo do loop.")
        continue # A instrução continue é usada para pular a iteração atual do loop for quando o número 10 é encontrado.

    print(numero, end=" ") # Imprime os números de 0 a 99, exceto o número 10, separados por espaço.