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
            
    def tempo_leitura(self):
        return self.paginas * 2


    def __str__(self):
        return  (
            f"Título: {self.titulo} "
            f"Autor: {self.autor}"
        )

l1 = Livro("Dom Casmurro", "Machado de Assis", 256)
print(l1)

l2 = Livro("Teste", "Ana", 0)
print(l2.paginas)

class LivroDigital(Livro):
    def __init__(self, titulo, autor, paginas, tamanho_mb):
        super().__init__(titulo, autor, paginas)
        self.tamanho_mb = tamanho_mb
        
    def tempo_leitura(self):
        return self.paginas * 1.5

d1 = LivroDigital("Python Fácil", "João Silva", 120, 15)
print(d1)

livros = [l1, d1]
for l in livros:
    print(l.titulo, "-", l.tempo_leitura(), "min")

class Biblioteca:
    def __init__(self):
        self.__livros = []

    def adicionar(self, livro):
        self.__livros.append(livro)

    def listar(self):
        for livro in self.__livros:
            print(livro)
            
bib = Biblioteca()
bib.adicionar(l1)
bib.adicionar(d1)
bib.listar()