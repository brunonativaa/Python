from abc import ABC, abstractmethod 
# ABC é a classe base para criar classes abstratas, e abstractmethod é um decorador para indicar que um método é abstrato e deve ser implementado pelas subclasses.
class ControleRemoto(ABC):
        @abstractmethod 
        def ligar(self):
            pass

        @abstractmethod
        def desligar(self):
            pass

        @property
        @abstractmethod
        def marca(self):
            pass


class ControleTV(ControleRemoto):
        def ligar(self):
            print("TV ligada")

        def desligar(self):
            print("TV desligada")

        @property
        def marca(self):
            return "Samsung"
        
class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ar condicionado ligado")

    def desligar(self):
        print("Ar condicionado desligado")

    
    @property
    def marca(self):
            return "Philco"
        

controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca)

controle_ar = ControleArCondicionado()
controle_ar.ligar()
controle_ar.desligar()
print(controle_ar.marca)