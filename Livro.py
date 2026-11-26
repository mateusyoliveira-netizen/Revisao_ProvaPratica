class Livro:
    
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas 

        @property
        def paginas(self):
            return self.__paginas
        @paginas.setter
        def paginas(self, valor):
            if valor <= 0:
                print("Páginas inválidas!")
                valor = 1
            self.__paginas = valor

    def __str__(self):
        return  (
            f"Título: {self.titulo} "
            f"Autor: {self.autor}"
        )

l1 = Livro("Dom Casmurro", "Machado de Assis", 256)
print(l1)

l2 = Livro("Teste", "Ana", 0)
print(l2.paginas)
