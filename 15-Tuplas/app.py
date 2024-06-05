#son estructuras de datos que almacenan multiples elementos en una unica variable, son ordenadas, inmutables(trabaja menos la memoria), mas eficiente en memoria y a prueba de daños
#se las conoce con (datos,1,2,(5.0,6)) 'tuple'

#son inmutables - no se puede editar

mi_tupla=(1,2,(10,20),4)
print(type(mi_tupla))

print(mi_tupla[2][0])

#conversion de types

mi_tupla = list(mi_tupla)#convertir a una lista
print(type(mi_tupla))

#asignar a diferentes variables: pero debe tener el mismo tamaño de datos en la tupla y en la conversion
t = (1,2,3)
x,y,z = t
print(x,y,z)

#solo se pueden aplicar 2 metodos (count() y index() )

t= (1,2,3,1)
print(t.count(2))#cantidad de elementos
print(t.index(1))#la posicion del elemento


