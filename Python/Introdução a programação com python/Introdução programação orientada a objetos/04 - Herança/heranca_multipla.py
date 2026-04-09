class Animal:
    def __init__(self,nro_patas):
        self.nro_patas = nro_patas


    def __str__(self):
        return f"{self.__class__.__name__}: {", ".join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"        

class Mamifero(Animal):
    """**kwargs** é usado para permitir que a classe Mamifero aceite argumentos adicionais que serão passados para o construtor da
classe pai (Animal) usando super(). Isso é útil para garantir que os atributos definidos na classe Animal sejam corretamente 
inicializados, mesmo quando a classe Mamifero tem seus próprios atributos específicos. """
    def __init__(self, cor_pelo, **kwargs): 
        super().__init__(**kwargs)
        self.cor_pelo = cor_pelo
    pass
                    # A herança múltipla deixa o codigo muito complexo, e deve ser evitada. 
                    # mas é importante conhecer o conceito para entender como funciona a hierarquia de classes em Python.
class Ave(Animal):
    def __init__(self, cor_bico, **kwargs):
        super().__init__(**kwargs)
        self.cor_bico = cor_bico

    pass

  

class gato(Mamifero):
    pass


class ornitorrinco(Mamifero, Ave): # Exemplo de herança múltipla, onde a classe ornitorrinco herda de ambas as classes Mamifero e Ave
    pass


gato = gato(nro_patas=4, cor_pelo="cinza")
print(gato)


ornitorrinco = ornitorrinco(nro_patas=2, cor_pelo="vermelho", cor_bico="laranja")
print(ornitorrinco)