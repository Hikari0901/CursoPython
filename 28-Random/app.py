"""
Random: es un modulo, un conjunto de funciones para su uso, que nos permite generar selecciones pseudo-aleatorias entre valores o secuencias
 
 
#from random import *

randint: da un int
uniform: da un float
random: float entre 0 y 1
choice: devuelve un elemento al azar de  una secuencia
shuffle: devuelve secuencia de manera aleatoria
importar un modulo es traer funciones para usar, usa (from)
"""

from random import * #(se llama a los metodods de random que se va a usar y el '*' sirve para llamar a todos los existentes)

#randint (trae valores aleatorios)
aleatorio= randint(1, 50)
print(aleatorio)

#uniform valores en float
aleatorio= round(uniform(1,5),2)
print(aleatorio)


#random
print(random())

#choice
colores=['azul','rojo','verde','negro']
print(choice(colores))
##aleatorio = choice(colores)
##print(choice)


#shuffle
numeros=list(range(5,50,5))
shuffle(numeros)
print(numeros)