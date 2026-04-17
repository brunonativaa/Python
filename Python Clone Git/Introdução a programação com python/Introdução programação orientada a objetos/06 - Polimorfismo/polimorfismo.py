class Passaro:
    def voar(self):
        print("O pássaro está voando.")


class Pardal(Passaro): # classe Pardal herda da classe Passaro e sobrescreve o método voar para fornecer uma implementação específica para pardais.
    def voar(self):
        print("Pardal pode voar.")


class Avestruz(Passaro): # classe Avestruz herda da classe Passaro e sobrescreve o método voar para fornecer uma implementação específica para avestruzes.

    def voar(self):
        print("Avestruz não pode voar.")


def plano_de_voo(obg): # Exemplo de polimorfismo com o método plano_de_voo, que aceita qualquer objeto que tenha o método voar.
    obg.voar() #

plano_de_voo(Pardal())
plano_de_voo(Avestruz())


            