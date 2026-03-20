def sistema_matematico():
    # 1. Funções "Filhas" (Definições internas)
    def tabuada(n):
        res = []
        for i in range(1, 11):
            res.append(f"{n} x {i} = {n * i}")
        return res

    def raiz_quadrada(a):
        return a ** 0.5 if a >= 0 else "Erro: Raiz negativa"
    
    def potencia(a, b):
        return a ** b
    
    def adicao(a, b):
        return a + b
    
    def subtracao(a, b):
        return a - b
    
    def multiplicacao(a, b):
        return a * b
    
    def divisao(a, b):
        return a / b if b != 0 else "Erro: Divisão por zero"

    # ... você pode manter as outras funções (adicao, subtracao) aqui dentro ...

    # 2. Comando e Entrada de Dados (A lógica da Função Pai)
    
    while opcao := input("Deseja usar o sistema matemático? (s/n): ").lower() != 's':
       
        print("Encerrando o sistema. Até a próxima!")
        return "Sistema encerrado"
    
    print("--- MENU MATEMÁTICO ---")
    opcao = input("Escolha: (1) Tabuada (2) Raiz Quadrada (3) Potência (4) Adição (5) Subtração (6) Multiplicação (7) Divisão: ")
    num = float(input("Digite o número: "))

    
    


     

    if opcao == '1':
        return tabuada(int(num)) # Chama a filha e retorna o resultado
    elif opcao == '2':
        return raiz_quadrada(num)
    elif opcao == '3':
        return potencia(num, float(input("Digite o expoente: ")))
    elif opcao == '4':
        return adicao(num, float(input("Digite o segundo número: ")))
    elif opcao == '5':
        return subtracao(num, float(input("Digite o segundo número: ")))
    elif opcao == '6':
        return multiplicacao(num, float(input("Digite o segundo número: ")))
    elif opcao == '7':
        return divisao(num, float(input("Digite o segundo número: ")))  
    

    else:
        return "Opção inválida"

# Executando a função pai
resultado_final = sistema_matematico()
print(resultado_final)