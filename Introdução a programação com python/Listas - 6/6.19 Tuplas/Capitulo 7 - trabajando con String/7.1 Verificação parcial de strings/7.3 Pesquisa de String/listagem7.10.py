s = "Um dia de sol"

encontrada = s.rfind("d")
print(encontrada)

encontrada = s.find("d")
print(encontrada)

""" Tanto find quanto rfind suportam duas opções adicionais: início (start) e fim (end). Se você especificar início, 
a pesquisa começará a partir dessa posição. Se você especificar o fim, a pesquisa utilizará essa posição como último caractere
 a considerar na pesquisa. Veja os exemplos na listagem 7.11.
 """