class Pajaro:
    alas = True
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie
 
    def piar(self):
        print("pio")
    
    def volar(self, metros):
        print(f"El pájaro vuela {metros} metros.")
        self.piar()
    
    def pintar_negro(self):
        self.color = "negro"
        print(f"El pajaro ahora es {self.color}")

    @classmethod
    def poner_huevos(cls, cantidad):
        print(f"Ponemos {cantidad} huevos")
    
    @staticmethod
    def mirar():
        print("El pajaro mira")
    
Pajaro.mirar()

Pajaro.poner_huevos(10)

mi_pajaro = Pajaro("blanco", "paloma")

mi_pajaro.volar(40)

mi_pajaro.alas = False
print(mi_pajaro.alas)
