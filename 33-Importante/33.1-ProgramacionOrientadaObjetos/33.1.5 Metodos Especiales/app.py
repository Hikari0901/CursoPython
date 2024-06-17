""".
existen una gran cantidad, pueden llamarse metodos magicos o dunder methods, ayudan a sobrescribir metodos incorporados de python sobre las clases

"""

class CD:
    def __init__(self, autor, album, cancion):
        self.autor = autor
        self.album = album
        self.cancion = cancion
        
    #imprimir
    def __str__(self):
        return f"Album: {self.album} de {self.autor}"
    #obtener el tamaño
    def __len__(self):
        return self.cancion
    #eliminar el objeto
    def __del__(self):
        print("se ha eliminado el cd")
        
mi_cd = CD("Pink Floyd","The Wall",24)

print(mi_cd)


