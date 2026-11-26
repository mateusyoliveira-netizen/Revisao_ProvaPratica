from Produto import Produto

class Alimento(Produto):
    def __init__(self, nome, preco, validade):
        super().__init__(nome, preco)
        self.__validade = validade
    
    @property
    def validade(self):
        return self.__validade

    def calcular_frete(self):
        return 5
    
a1 = Alimento("Leite", 6.5, "10/12")
print(a1)
print(a1.validade)

