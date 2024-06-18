""".
Practica metodos especiales 1
Dada la clase Libro, implementa el metodo especial __str__ para que cada vez que se imprima el objeto, devuelva "{Titulo}", de {autor}
(atencion: el titulo debe estar encerrado entre comillas dobles)
"""

class Libro:
    def __init__(self,titulo,autor):
        self.titulo = titulo
        self.autor= autor
        
    def __str__(self):
        return f"{self.titulo}, de {self.autor}"
        
libro1= Libro('habitos atomicos','James Clear')
print(libro1)