class Produto:
    def __init__(self, nome, preco):
        self.__nome = nome
        self.preco = preco

    @property
    def nome(self):
        return self.__nome
    
    @property
    def preco(self):
        return self.__preco

    def __str__(self):
        return  (
            f"Nome: {self.nome} "
            f"Preço: {self.preco}"
        )

p1 = Produto("Caderno", 25.0)
print(p1)