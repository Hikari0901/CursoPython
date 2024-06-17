""".
HM: se pueden usar varias clases para heredar
"""
class Padre:
    def hablar(self):
        print("Hola")
        
class Madre:
    def reir(self):
        print("Jaja")
        
class Hijo(Padre, Madre):
    pass

class nieto(Hijo):
    pass

mi_nieto= nieto()
mi_nieto.hablar()
mi_nieto.reir()