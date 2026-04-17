contador = 0 

while contador <= 100:
    contador += 1

    if contador == 6:
       print("BUUuuM")
       continue  # Vai pular o laço quando a expressão for verdadeira 
                  # Pode ter mais continue dentro do laço  

    if contador >= 12 and contador <= 22:
        print("Não vou mostrar .... Buuumm")  
        continue             


    print(contador)

print("Acabou")