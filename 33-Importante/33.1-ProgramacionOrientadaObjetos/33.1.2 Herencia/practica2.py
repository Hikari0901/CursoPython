""".
Practica Herencia 2:
Crea una clase llamada mascota, que tenga los siguientes atributos de instancia:
edad, nombre, cantidad_patas. crea otra clase, perro, que herede de la primera sus 
atribuos.
"""
class Mascota:
    def __init__(self,edad,nombre,cantidad_patas):
        self.cantidad_patas=cantidad_patas
        self.nombre = nombre
        self.edad = edad
        
class Perro(Mascota):
    def __init__(self, edad, nombre, cantidad_patas):
        super().__init__(edad, nombre, cantidad_patas)
        
Perro1= Perro(10, 'susi', 4)
print(f"Esta mascota se llama {Perro1.nombre}, tiene {Perro1.edad} years y anda en {Perro1.cantidad_patas} patas.")