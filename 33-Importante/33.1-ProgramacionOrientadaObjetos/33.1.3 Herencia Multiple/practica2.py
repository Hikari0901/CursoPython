""".
practica herencia extendida 3
un hijo ha heredado de su padre todas sus caracteristicas, sin embargo, tienen diferentes hobbies.
logra que la clase Hijo herede de padre todos sus metodos y atributos, sobrescribiendo el metodo hobby()
para que se devuelva[1]: "Juego videojuegos en mi tiempo libre"

"""
class Padre:
    def __init__(self,simpatico,alto,positivo):
        self.simpatico=simpatico
        self.alto= alto
        self.positivo = positivo
class Hijo(Padre):
    def __init__(self, simpatico, alto, positivo):
        super().__init__(simpatico, alto, positivo)
    def hobbie(self):
        print("Juego videojuegos en mi tiempo libre")
        
hijo1= Hijo("simpatico","alto","positivo")

hijo1.hobbie()
        