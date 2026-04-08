from abc import ABC, abstractmethod, abstractproperty
from datetime import datetime
import textwrap # módulo para formatar texto, permitindo a quebra automática de linhas e a remoção de espaços em branco desnecessários, facilitando a exibição de mensagens formatadas no console.

class Cliente: # Classe base para clientes
    def __init__(self, endereco):
        self._endereco = endereco
        self.contas = [] # lista para armazenar as contas do cliente vazia inicialmente


    def realizar_transacao(self, conta, transaocao): # recebe a conta e a transação a ser realizada
        transaocao.registrar(conta) # chama o método rgistrar da transação, passando a conta como argumento para realizar a transação

    def adicionar_conta(self, conta): # método para adicionar uma conta à lista de contas do cliente
        self.contas.append(conta)    


class PessoaFisica(Cliente): # Estende a classe Cliente para representar um cliente pessoa física
        def __init__(self, nome, cpf, endereco, data_nascimento): # recebe os atributos específicos de uma pessoa física, além dos atributos da classe Cliente
            super().__init__(endereco) # chama o construtor da classe Cliente para inicializar o atributo endereco
            self.nome = nome
            self.cpf = cpf
            self.data_nascimento = data_nascimento


class Conta: # Classe base para contas bancárias, definindo os atributos e métodos comuns a todas as contas
   
    def __init__(self, saldo, numero, cliente): # metodo construtor para inicializar os atributos de uma conta, incluindo o saldo inicial, número da conta e cliente associado à conta
        self._saldo = saldo
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod # método de classe para criar uma nova conta

    def nova_conta(cls, cliente, numero): # mapear nova conta que retorna uma nova instância da classe Conta, recebendo o cliente e o número da conta como argumentos
        return cls(numero, cliente)
    

    @property
    def saldo(self): # propriedade para acessar o saldo da conta protegido, retornando o valor armazenado no atributo _saldo
        return self._saldo
    
    @property # propriedade para acessar o número da conta
    def numero(self):
        return self._numero
    
    @property # propriedade para acessar a agência da conta
    def agencia(self):
        return self._agencia
    
    @property # propriedade para acessar o cliente associado à conta
    def cliente(self):
        return self._cliente

    @property # propriedade para acessar o histórico de transações da conta
    def historico(self):
        return self._historico
    

    def sacar(self, valor):
        saldo = self._saldo
        excedeu_saldo = valor > saldo # verifica se o valor do saque excede o saldo disponível na conta

        if excedeu_saldo: # caso o valor do saque execeda o saldo.
            print("Saldo insuficiente para saque.")

        elif valor > 0: # verifica se o valor do saque é positivo
            self._saldo -= valor # debita o valor do saque do saldo da conta
            print("\nSaque realizado com sucesso! ")
            return True # retorna True para indicar que o saque foi realizado com sucesso
        
        else: # caso o valor do saque seja negativo ou zero, exibe uma mensagem de erro e retorna False para indicar que o saque não foi realizado
            print("Valor de saque deve ser positivo.")
        return False 
        

    def depositar(self, valor):
        if valor > 0: # verifica se o valor do depósito é positivo
            self._saldo += valor # credita o valor do depósito ao saldo da conta
            print("\nDepósito realizado com sucesso! ")
            return True
        
        else: # caso o valor do depósito seja negativo ou zero, exibe uma mensagem de erro e retorna False para indicar que o depósito não foi realizado
            print("Valor de depósito deve ser positivo.")
            return False

class ContaCorrente(Conta): # Estende da classe Conta para representar uma conta corrente, adicionando atributos e métodos específicos para esse tipo de conta
     
    def __init__(self, numero, cliente, limite=500, limite_saques=3):   # recebe os atributos específicos de uma conta corrente, além dos atributos da classe Conta
    
            super().__init__(0, numero, cliente) # chama o construtor da classe Conta para inicializar os atributos numero e cliente
            self.limite = limite # define atributo limite com o valor padrão de 500
            self.limite_saques = limite_saques # define atributo limite_saques com o valor padrão de 3, indicando o número máximo de saques permitidos por dia
            self.cpf = cliente.cpf # define atributo cpf para armazenar o CPF do cliente associado à conta corrente, acessando o atributo cpf do cliente usando a propriedade cliente da classe Conta
    def sacar(self, valor):
        numero_saques = len([transacao for transacao in self.historico.transacoes if transacao['tipo'] == Saque.__name__])
# usando a compreensão de lista para contar o número de transações do tipo Saque no histórico de transações da conta, armazenando o resultado na variável numero_saques
        excedeu_limite = valor > self.limite # verifica se o valor do saque excede o limite permitido para a conta corrente
        excedeu_saques = numero_saques >= self.limite_saques # verifica se o número de saques realizados no dia excede o limite de saques permitido para a conta corrente
        
        if excedeu_limite: # mensagem de erro caso o valor do saque exceda o limite permitido.
            print("Valor de saque excede o limite permitido.")

        elif excedeu_saques: # mensagem de erro caso o número de saques realizados exeda o limite de saques permitido.
            print("Número máximo de saques diários excedido.")

        else:
             return super().sacar(valor) # chama o método sacar da classe base Conta para realizar o saque, caso o valor do saque esteja dentro do limite e o número de saques diários não tenha sido excedido. 
        
        return False

    def __str__(self): # metodo para obter a representação em string da conta corrente, exibindo informações relevantes como agência, número da conta, nome do titular e saldo formatado com duas casas decimais
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
            Saldo:\t\tR$ {self.saldo:.2f}
        """


    def _str__(self): # representação da classe  conta corrente, exibindo informações relevantes como agência, número da conta, nome do titular e saldo formatado com duas casas decimais
        return f"""\ Agencia: {self.agencia} \nNúmero: {self.numero} \nTitular: {self.cliente.nome} \nSaldo: R${self.saldo:.2f}"""
    
class Historico: 
    def __init__(self):
        self._transacoes = [] # lista para armazenar as transações realizadas na conta, inicialmente vazia
    @property
    def transacoes(self):
        return self._transacoes # pega a lista de transações armazenada no atributo _transacoes e a retorna para quem acessar a propriedade transacoes
    
    def adicionar_transacao(self, transacao):
        self._transacoes.append({  # armazena as informações da transação em um dicionário, incluindo o tipo da transação (Saque ou Depósito), o valor da transação e a data e hora em que a transação foi realizada. O dicionário é adicionado à lista de transações armazenada no atributo _transacoes.
            "tipo": transacao.__class__.__name__, # obtém o nome da classe da transação (Saque ou Depósito) usando a função __class__.__name__ e armazena esse valor no campo "tipo" do dicionário
            "valor": transacao.valor, # acessa o valor da transação usando a propriedade valor da classe Transacao e armazena esse valor no campo "valor" do dicionário
            "data" : datetime.now().strftime("%Y-%m-%d %H:%M:%S") # obtém a data e hora atual usando a função datetime.now() 
        })

class Transacao(ABC): # classe abstrata para representar uma transação bancária, definindo a estrutura
    @property
    @abstractmethod
    def valor(self): # acessa o valor da transação.
        pass


    @abstractmethod
    def registrar(self, conta):     
        pass        

class Saque(Transacao): # Estende a classe Transacao para representar uma transação de saque, implementando os métodos abstratos definidos na classe base
    def __init__(self, valor):
        self._valor = valor

    @property # obrigado implementar a propriedade valor, retornando o valor do saque armazenado no atributo _valor
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso = conta.sacar(self.valor) # chama o sacar da conta, passando o valor do saque como argumento, e armazena o resultado (True ou False) na variável sucesso

        if sucesso:
            conta.historico.adicionar_transacao(self) # adiciona a transação de saque ao histórico da conta usando o método adicionar_transacao da classe Historico, passando a instância atual da transação (self) como argumento para registrar os detalhes do saque no histórico de transações da conta. """"

class Deposito(Transacao): # Estende a classe Transacao para representar uma transação de depósito, implementando os métodos abstratos definidos na classe base

    def __init__(self, valor): # recebe o valor do depósito e armazena esse valor no atributo protegido _valor
        self._valor = valor  # define o método construtor para inicializar o valor do depósito.

    @property
    def valor(self):
        return self._valor # implementa a propriedade valor, retornando o valor do depósito armazenado no atributo _valor
    
    def registrar(self, conta):
        sucesso = conta.depositar(self.valor) # chama o método depositar da conta, passando o valor do depósito como argumento, e armazena o resultado (True ou False) na variável sucesso

        if sucesso:
            conta.historico.adicionar_transacao(self) # adiciona a transação de depósito ao histórico da conta usando o método adicionar_transacao da classe Historico, passando a instância atual da transação (self) como argumento para registrar os detalhes do depósito no histórico de transações da conta.   

def menu(): # função para exibir o menu de opções para o usuário e solicitar a escolha da opção desejada, retornando a opção escolhida como um número inteiro
    menu_text = """
    [1] - Depositar
    [2] - Sacar
    [3] - Extrato
    [4] - Novo Cliente
    [5] - Criar Conta
    [6] - Listar Contas
    [0] - Sair

    => """
    return int(input(textwrap.dedent(menu_text)))


def filtrar_cliente(cpf, clientes): # função para filtrar um cliente com base no CPF fornecido, verificando se o CPF do cliente corresponde ao CPF fornecido e retornando o cliente correspondente ou None se nenhum cliente for encontrado
    clientes_filtrados = [cliente for cliente in clientes  if cliente.cpf == cpf] # usando a compreensão de lista para criar uma nova lista clientes_filtrados que contém apenas os clientes cujo CPF corresponde ao CPF fornecido como argumento para a função

    return clientes_filtrados[0] if clientes_filtrados else None # retorna o primeiro cliente da lista clientes_filtrados se a lista não estiver vazia, ou None se a lista estiver vazia, indicando que nenhum cliente com o CPF fornecido foi encontrado.

def recuperar_conta_cliente(cliente): # função para recuperar a conta associada a um cliente, fazendo a verificação se o cliente possui contas.
    if not cliente.contas: # verifica se a lista de contas do cliente está vazia, indicando que o cliente não possui contas associadas
        print("\n@@@ Cliente não possui conta! @@@")
        return None # retorna None para indicar que o cliente não possui conta
    
    # FIXME: não funciona para clientes com mais de uma conta
    return cliente.contas[0] # retorna a primeira conta da lista de contas do cliente 

def depositar(clientes): # função para realizar um depósito em uma conta associada a um cliente.
    cpf = input("Informe o CPF do cliente: ") # solicita ao usuário que informe o CPF do cliente para identificar a conta associada a esse cliente
    cliente = filtrar_cliente(cpf, clientes) # chama a função filtrar_cliente para obter o cliente correspondente ao CPF fornecido, passando a lista de clientes como argumento para a função

    if not cliente: # verifica se o cliente foi encontrado, ou seja, se a variável cliente é None
        print("\n@@@ Cliente não encontrado! @@@")
        return # retorna None para indicar que o cliente não foi encontrado e encerra a função
    

    valor = float(input("Informe o valor do depósito: ")) # solicita ao usuário que informe o valor do depósito e converte a entrada para um número de ponto flutuante (float) para ser usado posteriormente na transação de depósito
    transacao = Deposito(valor) # cria uma instância da classe Deposito, passando o valor do depósito como argumento para o construtor da classe, e armazena essa instância na variável transacao


    conta = recuperar_conta_cliente(cliente) # chama a função recuperar_conta_cliente para obter a conta associada ao cliente, passando o cliente como argumento para a função, e armazena a conta retornada na variável conta
    if not conta: # verifica se a conta foi encontrada, ou seja, se a variável conta é None
        return # retorna None para indicar que a conta não foi encontrada e encerra a função
    

    cliente.realizar_transacao(conta, transacao) # chama o método realizar_transacao do cliente, passando a conta e a transação de depósito como argumentos para realizar a transação de depósito na conta associada ao cliente.



def sacar(clientes): # função para realizar um saque em uma conta associada a um cliente, seguindo uma lógica semelhante à função depositar, mas utilizando a classe Saque para criar a transação de saque e chamando o método sacar da conta para realizar a transação de saque.
    cpf = input("Informe o CPF do cliente:")
    cliente = filtrar_cliente(cpf, clientes) # chama a função filtrar_cliente para obter o cliente correspondente ao CPF fornecido, passando a lista de clientes como argumento para a função

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return
    
    valor = float(input("Informe o valor do saque: "))
    transacao = Saque(valor) # cria uma instância da classe Saque, passando o valor do saque como argumento para o construtor da classe, e armazena essa instância na variável transacao

    conta = recuperar_conta_cliente(cliente) # chama a função recuperar_conta_cliente para obter a conta associada ao cliente, passando o cliente como argumento para a função, e armazena a conta retornada na variável conta
    if not conta: # verifica se a conta foi encontrada, ou seja, se a variável conta é None
        print("\n@@@ Conta não encontrada! @@@")
        return 
    
    cliente.realizar_transacao(conta, transacao) # chama o método realizar_transacao do cliente, passando a conta e a transação de saque como argumentos para realizar a transação de saque na conta associada ao cliente.


def exibir_extrato(clientes): # função para exibir o extrato de uma conta associada a um cliente, solicitando o CPF do cliente, filtrando o cliente correspondente, recuperando a conta associada ao cliente e exibindo as transações registradas no histórico da conta.
    cpf = input("Informe o CPF do cliente: ") # solicita ao usuário que informe o CPF do cliente para identificar a conta associada a esse cliente
    cliente = filtrar_cliente(cpf, clientes) # chama a função filtrar_cliente para obter o cliente correspondente ao CPF fornecido, passando a lista de clientes como argumento para a função

    if not cliente: # verifica se o cliente foi encontrado, ou seja, se a variável cliente é None
        print("\n@@@ Cliente não encontrado! @@@")
        return # retorna None para indicar que o cliente não foi encontrado e encerra a função
    
    conta = recuperar_conta_cliente(cliente) # chama a função recuperar_conta_cliente para obter a conta associada ao cliente, passando o cliente como argumento para a função, e armazena a conta retornada na variável conta
    if not conta: # verifica se a conta foi encontrada, ou seja, se a variável conta é None
        return # retorna None para indicar que a conta não foi encontrada e encerra a função
    
    print("\n========== EXTRATO ==========")
    transacoes = conta.historico.transacoes # acessa a lista de transações registradas no histórico da conta usando a propriedade historico da conta e

    extrato = "" # inicializa uma string vazia para armazenar o extrato formatado

    if not transacoes: # verifica se a lista de transações está vazia, indicando que não foram registrada transações na conta
        extrato = "Não foram realizadas transações."
    
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}:\n \tR$ {transacao['valor']:.2f}"
    
    print(extrato)

    print(f"\nSaldo atual: \tR$ {conta.saldo:.2f}") # exibe o saldo atual da conta formatado com duas casas decimais usando a propriedade saldo da conta.
    print("============================")


def criar_cliente(clientes): # função para criar um novo cliente, solicitando as informações necessárias, criando uma instância da classe PessoaFisica e adicionando o cliente à lista de clientes.
        cpf = input("Informe o CPF do cliente: ") # solicita ao usuário que informe o CPF do cliente para identificar o cliente a ser criado
        cliente = filtrar_cliente(cpf, clientes) # chama a função filtrar_cliente para

        if cliente: # verifica se o cliente já existe, ou seja, se a variável cliente não é None
            print("\n@@@ Já existe cliente com esse CPF! @@@")
            return # retorna None para indicar que o cliente já existe e encerra a função
        

        nome = input("Informe o nome do cliente: ") # solicita ao usuário que informe o nome do cliente
        data_nascimento = input("Informe a data de nascimento do cliente (dd-mm-aaaa): ") # solicita ao usuário que informe a data de nascimento do cliente no formato dd-mm-aaaa
        endereco = input("Informe o endereço do cliente: ") # solicita ao usuário que informe o

        cliente = PessoaFisica(nome=nome, cpf=cpf, endereco=endereco, data_nascimento=data_nascimento) # cria uma instância da classe PessoaFisica, passando as informações do cliente como argumentos para o construtor da classe, e armazena essa instância na variável cliente
        clientes.append(cliente) # adiciona o cliente criado à lista de clientes usando o método append da lista.

        print("\n@@@ Cliente criado com sucesso! @@@") # exibe uma mensagem de sucesso indicando que o cliente foi criado com sucesso.


def criar_conta(numero_conta, clientes, contas): # função para criar uma nova conta, solicitando o número da conta e o CPF do cliente associado, verificando se o cliente existe, criando uma instância da classe ContaCorrente e adicionando a conta à lista de contas do cliente e à lista de contas do sistema.
        cpf = input("Informe o CPF do cliente: ") # solicita ao usuário que informe o CPF do cliente para identificar o cliente associado à conta a ser criada
        cliente = filtrar_cliente(cpf, clientes) # chama a função filtrar_cliente para obter o cliente correspondente ao CPF fornecido, passando a lista de clientes como argumento para a função

        if not cliente: # verifica se o cliente foi encontrado, ou seja, se a variável cliente é None
            print("\n@@@ Cliente não encontrado! Fluxo de criação de conta interrompido. @@@")
            return # retorna None para indicar que o cliente não foi encontrado e encerra a função
        
        conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta) # chama o método de classe nova_conta da classe ContaCorrente para criar uma nova conta corrente associada ao cliente encontrado, passando o cliente e o número da conta como argumentos para o método, e armazena a conta criada na variável conta
        contas.append(conta) # adiciona a conta criada à lista de contas do sistema usando o método append da lista
        cliente.adicionar_conta(conta) # chama o método adicionar_conta do cliente para adicionar a conta criada à lista de contas do cliente, passando a conta como argumento para o método

        print("\n@@@ Conta criada com sucesso! @@@") # exibe uma mensagem de sucesso indicando que a conta foi criada com sucesso.

def listar_contas(contas): # função para listar as contas existentes, exibindo informações relevantes como agência, número da conta, nome do titular e saldo formatado com duas casas decimais para cada conta na lista de contas do sistema.
        for conta in contas: # itera sobre cada conta na lista de contas do sistema usando um loop for
            print("=" * 100)
            print(textwrap.dedent(str(conta))) # exibe as informações da conta formatadas usando a função textwrap.dedent para remover a indentação e a função str para obter a representação em string da conta, que é definida no método __str__ da classe ContaCorrente

def main(): # função principal para executar o programa, inicializando as listas de clientes e contas, exibindo o menu de opções e chamando as funções correspondentes com base na escolha do usuário
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == 0:
            print("\n@@@ Obrigado por usar nosso sistema bancário! @@@")
            break

        if opcao == 1:
            depositar(clientes)

        elif opcao == 2:
            sacar(clientes)

        elif opcao == 3:
            exibir_extrato(clientes)

        elif opcao == 4:
            criar_cliente(clientes)

        elif opcao == 5:
            numero_conta = len(contas) + 1 # gera um número de conta sequencial com base no número de contas já existentes na lista de contas do sistema, adicionando 1 para garantir que o número da nova conta seja único
            criar_conta(numero_conta, clientes, contas)

        elif opcao == 6:
            listar_contas(contas)

        else:
            print("\n@@@ Opção inválida! @@@")

if __name__ == "__main__":
    main()
