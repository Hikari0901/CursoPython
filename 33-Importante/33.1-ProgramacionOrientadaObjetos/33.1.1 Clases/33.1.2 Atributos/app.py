""".
son las caracteristicas que cada uno de nuestros objetos peuden tener
se hace el contructor: __init__(self,'atributos')

"""
class Pajaro:
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie
        
#Creacion de objetos
mi_pajaro = Pajaro('negro', 'Tucan')
otro_pajaro= Pajaro('azul', 'loro')

print(f"mi pajaro es un {mi_pajaro.especie} y de color {mi_pajaro.color}")
print(f"mi pajaro es un {otro_pajaro.especie} y de color {otro_pajaro.color}")