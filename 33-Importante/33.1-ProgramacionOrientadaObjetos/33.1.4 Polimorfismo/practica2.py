""".


"""


class Mago:
    def atacar(self):
        print("Ataque magico")
        
class Arquero:
    def atacar(self):
        print("Lanzamiento de flecha")
        
class Samurai:
    def atacar(self):
        print("Ataque con katana")
        
#creacion de objetos o instancias        
gandalf= Mago()
hwekeye = Arquero()
jack = Samurai()

personajes = [gandalf,hwekeye,jack]

for personaje in personajes:
    personaje.atacar()
    