"""
Funcion: es cada una de las posciones que hay en cada uno de los elementos strings, son valores independientes, se leen desde el posicion o valor 0

p y t h o n
0 1 2 3 4 5

"""
#se representa con [] para deir el valor de la posicion

mi_texto = "esta es una prueba"
resultado = mi_texto[9]
print(resultado)

#metodos:
#se puede tener mas parametros que agregar que seria siguiente  ("palabra", inicio, fin)
"""resultado = mi_texto.index("prueba", 11 , 18)"""

#Metodo rindex permite leer de derecha a izquierda
resultado= mi_texto.rindex("a")
print(resultado)