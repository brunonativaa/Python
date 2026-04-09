# Execute o programa (Listagem 5.14) para os seguintes valores: 501, 745, 384, 2, 7 e 1.

soma = 0
quantidade = 0



while True:
    nume = int(input("Digite um número 501,745,384,2,7,100 (0 para sair:) "))
    if nume == 0:
       
        break

    soma = soma + nume
    quantidade = quantidade + 1

    media = soma / quantidade

print(f"quantida de números {quantidade:02d},Valores {soma:.2f}, Média {media:.2f}")    
