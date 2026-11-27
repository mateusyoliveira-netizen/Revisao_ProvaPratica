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
    
    @preco.setter
    def preco(self, valor):
        if valor < 0:
            print("Preço inválido!")
            valor = 0
        self.__preco = valor

    def calcular_frete(self):
        return self.preco * 0.1

    def __str__(self):
        return  (
            f"Nome: {self.nome} "
            f"Preço: {self.preco}"
        )
    

p1 = Produto("Caderno", 25.0)
print(p1)

p2 = Produto("Caderno", -5)
print(p2.preco)

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

produtos = [
    Produto("Caderno", 25.0),
    Alimento("Leite", 6.5, "10/12"),
]
for p in produtos:
    print(p.nome, "frete:", p.calcular_frete())

class Estoque:
    def __init__(self):
        self.__produtos = []

    def adicionar(self, produto):
        self.__produtos.append(produto)

    def listar(self):
        for p in self.__produtos:
            print(p)

estoque = Estoque()
estoque.adicionar(Produto("Caderno", 25.0))
estoque.adicionar(Alimento("Leite", 6.5, "10/12"))
estoque.listar()
