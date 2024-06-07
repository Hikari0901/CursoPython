"""
Practica 1

Implementa la función randint() de la librería random que 
te permita obtener un número entero del 1 al 10, y almacena dicho 
valor en una variable llamada aleatorio
"""

from random import randint
aleatorio=randint(1,10)
print(aleatorio)

while aleatorio >=0:
    print(randint(-5,10))
else:
    print('fin')