#es otro tipo de estructura de datos, son una coneccion mutable de elementos inmutables, no ordenados y sin datos repetidos

"""
existen 2 formas de declarar un set
myset=set()
{datos,1,2,3}
"""
#Primera forma de declarar un set

mi_set= set([1,2,3,4])
print(type(mi_set))
print(mi_set)

#Segunda fomra de declarar un set
otro_set={1,2,3}
print(type(otro_set))
print(otro_set)

#Errores en sets:
#1.- se quiere acceder a la posicion de los elementos
#2.- se quiere cambiar el valor de la posicion
"""
print(mi_set[0])
mi_set[0] = 5
print(mi_Set)
"""

#Elementos unicos: el set automaticamente elimina elementos repetidos
mi_set=set((1,2,3,4,5,1,1,1,1,2,2,2,2))
print(mi_set)

#No permite la convinacion de elementos entre listas o valores fijos
"""
mi_set=set((1,2,3,4,5,[2,1],1,1,1,1,2,2,2,2))
print(mi_set)
"""

#Permite validar si existe un elemento y nos verifica en booleano
mi_set= set((1,2,3,4,5))
print(10 in mi_set)

#Union de los sets, se usa el metodo .union, no se repiten los valores por lo que si hay numeros repetidos los onmite

s1={1,2,3}
s2={3,4,5}
s3=s1.union(s2)
print(s3)

#Agregar elementos, se usa el metodo .add
s1={1,2,3,5,6}
s1.add(4)
print(s1)

#Eliminando sets, se usa el metodo .remove
s1.remove(3)
print(s1)

#Descartar elementos, se usa el metodo .discard *no los elimina* solo los descarta pero aun existe

s1.discard(6)
print(s1)

#Eliminar el primer elemento, se usa el metodo .pop
s1.pop()
print(s1)