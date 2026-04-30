class Vaca:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print("muuu")

class Oveja:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        for n in range(0,3):
            print(f"Bee {n + 1}")

vaca1 = Vaca("Aurora")
oveja1 = Oveja("Nube")


animales_granja = [vaca1,oveja1]

'''for animal in animales_granja:
    animal.hablar()'''

def animal_habla(animal):
    animal.hablar()

animal_habla(oveja1)

