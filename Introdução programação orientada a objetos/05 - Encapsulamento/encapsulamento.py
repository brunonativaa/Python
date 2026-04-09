class Conta:
    def __init__(self,nro_agencia, saldo = 0):
        self._saldo = saldo # Atributo protegido
        self.nro_agencia = nro_agencia # Atributo público

    def depositar(self, valor):
        self._saldo += valor # Modificando o saldo usando um método público

    def sacar(self, valor):
        self._saldo -= valor # Modificando o saldo usando um método público

    def mostrar_saldo(self):
        return self._saldo    

conta = Conta("0458",100)  
#conta._saldo += 100  # Modificando o saldo diretamente (não recomendado)
# #print(conta._saldo)  # Acesso direto ao atributo protegido (não recomendado)
conta.depositar(100)  # Usando o método para modificar o saldo (recomendado)
print(conta.nro_agencia)  # Acesso ao atributo público
print(conta.mostrar_saldo())  # Acesso ao método para mostrar o saldo (recomendado  )