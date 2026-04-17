"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

if nome and idade:
    print(f"Seu nome é: {nome}")
    print(f"Seu nome invertido é {nome[::-1]}" ) # fatiamento com o ultimo indice da posição da string[-1] inverte o nome

    if ' ' in nome:    # if para verificar se contém espaços ' ' in nome
        print("Seu nome tem espaços!")
    else:
        print("Seu nome não possui espaços!")    

    print(f"Seu nome possui {len(nome)} letras") # função len para contar as letras no nome
    print(f"A primeira letra do seu nome é: {nome[0]}") # primeiro indice do nome [0]
    print(f"O ultimo letra do seu nome é : {nome[-1]}") # ultimo indice [-1]

else:
    print("Desculpe, você deixou campos vazios")    
