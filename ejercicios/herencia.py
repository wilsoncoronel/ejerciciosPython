class Personaje:
    def __init__(self, nombre, herramienta):
        self.nombre = nombre
        self.herramienta = herramienta
    
    def nacer(self):
        print("EL hechicero ha nacido")

    def hablar(self):
        print("Hechicero habla")


class Mago(Personaje):
    def __init__(self,nombre, herramienta , altura_vuelo):
        self.edad = nombre
        self.herramienta = herramienta
        self.altura_vuelo = altura_vuelo

    def hablar(self):
        print("Hechicero dice espoliarmmus")

hechicero = Personaje("Merlin", "Caldero")

hechicero2 = Mago("Angelius","Baston", 100)
hechicero2.hablar()
hechicero.nacer()

