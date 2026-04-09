


total_compra = 0.00

while True:
        codigo = int(input("Digite o codigo: 1,2,3,5,9 (ou 0 para sair) "))
       
        if codigo == 0:
            break
         
        if codigo == 1:
            preco = 0.50

        elif codigo == 2:
            preco = 1.00

        elif codigo == 3:
            preco = 4.00

        elif codigo == 5:
            preco = 7.00

        elif codigo == 9:
            preco = 8.00

        else:
            print("Codigo inválido !")
        continue
    
qtd = int(input("Qual a quantidade? "))



valor_item = preco * qtd
total_compra += valor_item

print(f"Total a pagar: R${total_compra:.2f}")