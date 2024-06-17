""".
Practica atributos 1 
crea una clase llamada casa, y asignale atributos: color, cantidad_pisos.

crea una instancia de casa, llamada casa_blanca, de color 'blanco' y cantidad 
de pisos igual a 4
"""

class casa:
    #constructor
    def __init__(self,color,cantidad_pisos):
        #atributos
        self.color = color
        self.cantidad_pisos = cantidad_pisos
        
#creacion de objetos
casa_blanca= casa('blanca', 4)
print(f"la casa es color {casa_blanca.color} y de {casa_blanca.cantidad_pisos} pisos")
