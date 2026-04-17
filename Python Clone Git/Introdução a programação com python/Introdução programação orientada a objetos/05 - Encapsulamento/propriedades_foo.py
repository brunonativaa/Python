class Foo:
    def __init__(self, x = None):
        self._x = x  # Atributo protegido
        pass

    @property # Decorador para criar um método getter
    def x (self):
        return self._x  or 0  # Método getter para acessar o valor de x
    
    @x.setter # Decorador para criar um método setter
    def x(self, value):
       self._x += value  # Método setter para modificar o valor de x
    
    @x.deleter # Decorador para criar um método deleter
    def x(self):
        self._x = -1  # Método deleter para deletar o valor de x (definindo como -1 para indicar que foi deletado)
    
foo = Foo(10)
print(foo.x)  # Acessando o valor de x usando o método getter
del foo.x  # Deletando o valor de x usando o método deleter
print(foo.x)  # Acessando o valor de x usando o método getter após deletar (deve retornar -1)
foo.x = 10
print(foo.x)  # Acessando o valor de x usando o método getter após delet