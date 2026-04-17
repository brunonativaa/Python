"""
Repetições
While (enquanto)

"""

qtd_linhas = 5
qtd_colunas = 5


linha = 1 # variavel contadora do primeiro While

while linha <= qtd_linhas:
    coluna = 1  # Variavel contadora do while interna
    
    while coluna <= qtd_colunas:
        print(f"{linha=} {coluna=}")
        coluna += 1 # Atribuição da variavel contadora interna
    
    linha += 1 # Variavel contadora do while inicial

print("Acabou")   