""".
Herencia: son atributos que se heredan de las clasesPadre (SuperClass), permite la duplicidad de codigo, solo esta definida en POO
"""

class Animal:
    
    def __init__(self, edad, color):
        self.edad = edad
        self.color = color
        
    def nacer(self):
        print("Este animal a nacido")
    
    def hablar(self):
        print("Este animal emite un sonido")

class Pajaro(Animal):
    def __init__(self, edad, color, altura_vuelo):
        super().__init__(edad, color)
        self.altura_vuelo = altura_vuelo
        
    def hablar(self):
        return super().hablar()
    
    def volar(self,metros):
        print(f"El pajaro vuela {metros} metros")
        
#crear objetos

piolin = Pajaro(10, "Amarillo", 3)
piolin.nacer()
piolin.hablar()