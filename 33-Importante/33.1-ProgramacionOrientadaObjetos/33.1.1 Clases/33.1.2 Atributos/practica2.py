""".
practica atributos 2
crea una clase llamada personaje y asignale el siguiente atributo de clase:
real = False

Crea una instancia llamada harry_potter con los siguientes atributos de instancia:
especie = 'Humano'
magico = True
edad = 17
"""

class personaje:
    real = False
    def __init__(self,especie,magico,edad):
        self.especie = especie
        self.magico = magico
        self.edad= edad
        
#objetos
harry_potter = personaje('humano',True,17)
harry_potter.real = True
print(f"el personaje es {harry_potter.especie}, tiene {harry_potter.edad} y su estado de magia es {harry_potter.magico} ")