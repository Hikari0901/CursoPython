""".
Practica herencia extendida 1
Si la clase hija ha heredado de su padre la forma de reir, y de su madre la vocacion, y hoy tienen el mismo
trabajo en la fiscalia, crea la herencia multiple que le permita a esta clase heredar correctamente de padre y madre

completa el codigo suministado a continuacion para lograrlo
"""
class Padre:
    def actitud(self):
        print("jaja")
        
class Madre:
    def vocacion(self):
        print("Fiscal")
        
class Hija(Padre,Madre):
    pass

mi_hija= Hija()
mi_hija.actitud()
mi_hija.vocacion()