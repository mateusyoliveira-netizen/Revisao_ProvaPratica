class Produto:
    
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return  (
            f"Nome: {self.nome} "
            f"Preço: {self.preco}"
        )

p1 = Produto("Caderno", 25.0)
print(p1)