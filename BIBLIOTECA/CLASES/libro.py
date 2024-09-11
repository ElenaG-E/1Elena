class Libro:
    def __init__(self, ISBN, titulo, autor, año):
        self.ISBN = ISBN
        self.titulo = titulo
        self.autor = autor
        self.año = año

    def encontrar_ISBN(self):
        return self.ISBN
    
    def titulo_libro(self):
        return self.titulo
    
    def autor_libro(self):
        return self.autor
    
    def año_libro(self):
        return self.año