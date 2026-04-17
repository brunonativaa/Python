# Embora muito útil, a estrutura while só verifica sua condição de parada no iní-cio de cada repetição. 
# Dependendo do problema, a habilidade de terminar while dentro do bloco a repetir pode ser interessante.
#  A instrução break é utilizada para interromper a execução de while independentemente do valor atual de sua condição.
#  Vejamos o exemplo da leitura de valores até que digitemos 0 (zero) no programa da listagem 5.13.


#Escreva um programa que leia números inteiros do teclado. 
# O programa deve ler os números até que o usuário digite 0 (zero). 
# No final da execução, exiba a quantidade de números digitados, assim como a soma e a média aritmética.


soma = 0
quantidade = 0



while True:
    nume = int(input("Digite um número ou 0 para sair: "))
    if nume == 0:
       
        break

    soma = soma + nume
    quantidade = quantidade + 1

    media = soma / quantidade

print(f"quantida de números {quantidade:02d},Valores {soma:.2f}, Média {media:.2f}")    




