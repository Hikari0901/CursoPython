""".
Practica Herencia 1
Crea una clase llamada Persona, que tenga los siguientes atributos de instancia:
nombre,edad. crea otra clase, alumno, que herede de la primera persona estos atributos
"""
class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
        
class Alumno(Persona):
    def __init__(self,nombre,edad):
        super().__init__(nombre,edad)
        
persona = Alumno('Ronnald',25)
print(f"{persona.nombre} tiene {persona.edad}")