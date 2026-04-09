""" Quando há problemas, como a mensagem do carro velho (Listagem 4.3), onde a segunda condição é simplesmente o inverso da primeira, 
podemos usar outra forma de if para simplificar os programas. Essa forma é a cláusula else para especificar o que fazer caso o resultado
 da avaliação da condição seja falso, sem precisarmos de um novo if. 
 Vejamos como ficaria o programa reescrito para usar else na listagem 4.5. """


idade = int(input("Digite a idade do seu carro: "))

if idade <= 3:
    print("O carro é novo")
else:
    print(f"O carro é velho {idade} anos de idade!")    