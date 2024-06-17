""".

"""
class Pajaro:
    alas = True
    
    #metodo constructor
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie
    
    #Metodos propios contruidos a parte
    def piar(self):
        print("Pio")
        
    def volar(self,metros):
        print(f"El pajaro ha volado {metros} metros")
    
    #metodo de instancia: acceder y modificar directamente
    def pintar_negro(self):
        self.color = "Negro"
        print(f"Ahora el pajaro es {self.color}")
    #metodo de clase: opera en la clase, usa el @classmethod ''(cls,'parametro'), hace no necesario crear una variable para acceder al metodo
    @classmethod
    def poner_huevos(cls,cantidad):
        print(f"Puso {cantidad} huevos")
        cls.alas = False
        print(Pajaro.alas)
    #metodos estaticos: no depende ni de la intancia ni de la clase ni requieren parametro en especial @statickmethod
    @staticmethod
    def mirar():
        print("El pajaro mira")        
        
#Creacion de objetos

piolin = Pajaro('amarillo','canario')
print(piolin.color)
print(piolin.pintar_negro())

#class method objetos
print(piolin.poner_huevos(5))

#static method:
piolin.mirar()