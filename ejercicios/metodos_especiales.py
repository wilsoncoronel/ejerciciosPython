mi_lista = [1,2,3]

class Perro:
    pass

mi_perro = Perro()
print(mi_perro)

class CD:
    def __init__(self, autor, titulo, nro_canciones):
        self.autor = autor
        self.titulo = titulo
        self.nro_canciones = nro_canciones

    def __str__(self):
        return f"CD {self.titulo} de {self.autor}"


cd_1 = CD("Pink Floyd", "The Wall", 24)
print(cd_1)


