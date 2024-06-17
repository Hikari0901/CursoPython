""".
Metodo: es el comportamiento, son porsiones de codigo que definen diferentes funcionabilidades

"""
class Pajaro:
    #metodo constructor
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie
    
    #Metodos propios contruidos a parte
    def piar(self):
        print("Pio")
        
    def volar(self,metros):
        print(f"El pajaro ha volado {metros} metros")
        
        
        
#Creacion de objetos

piolin = Pajaro('amarillo', 'canario')
#llamando atributo
print(piolin.especie)
#llamar el metodo piar
piolin.piar()
#llamar el metodo volar con su respectivo atributo
piolin.volar(5)