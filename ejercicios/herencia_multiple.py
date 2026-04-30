class Padre:
    def hablar(self):
        print("Hola")
class Madre:
    def reir(self):
        print("ja ja ja")

    def hablar(self):
        print("Que tal")

class Hijo(Padre, Madre):
    pass
class Nieto(Hijo):
    pass

hijo = Hijo()
hijo.hablar()
mi_nieta = Nieto()
mi_nieta.reir()
mi_nieta.hablar()