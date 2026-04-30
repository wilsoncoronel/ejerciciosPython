palabra = "polimorfismo"
lista = ["Clases", "POO", "Polimorfismo"]
tupla = (1, 2, 3, 80)
objetos = [palabra, lista,tupla]
for item in objetos:
        print(len(item))

class Mago():
    def atacar(self):
        print("Ataque mágico")

class Arquero():
    def atacar(self):
        print("Lanzamiento de flecha")

class Samurai():
    def atacar(self):
        print("Ataque con katana")

mago1 = Mago()
arquero1 = Arquero()
samurai1 = Samurai()

personajes = [arquero1, mago1, samurai1]
for personaje in personajes:
     personaje.atacar()

class Mago():
    def defender(self):
        print("Escudo mágico")

class Arquero():
    def defender(self):
        print("Esconderse")

class Samurai():
    def defender(self):
        print("Bloqueo")

mago1 = Mago()
arquero1 = Arquero()
samurai1 = Samurai()


def personaje_defender(objeto):
    objeto.defender()

personaje_defender(mago1)