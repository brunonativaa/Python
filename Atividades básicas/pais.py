populacionA = int(input("População do pais A: "))

while populacionA <0:
    populacionA = int(input("População do pais deve ser maior que 0: "))
taxaA = float(input("Taxa de crescimento da cidade A: "))

populacionB = int(input("População do pais B: "))

while populacionB <0:
    populacionB = int(input("População do pais deve ser maior que 0: "))
taxaB = float(input("Taxa de crescimento da cidade B: "))

ano = 0

while populacionA < populacionB:
    ano += 1
    populacionA = int((1 + (taxaA/100) )* populacionA  )
    populacionB = int((1 + (taxaB/100) )* populacionB )  
    print("Ano %d:" % ano)
    print("População A: %d" % populacionA)
    print("População B: %d\n\n" % populacionB)

print("Ultrapassa no ano:" , ano)
