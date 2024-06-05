#son secuencias ordenadas de objetos pueden ser datos de cualquier tipo strings,integers,voleanos,floats, listas. son tipos de datos mutables (se pueden editar), son ordenados y admiten duplicados.
#para declarar una lista se suele tener una variable

mi_lista = ["a","b","c"]
print(type(mi_lista))

#tamaño de un string
###print(len(mi_lista))

#unir listas
mi_lista1 = ['a', 'b', 'c']
mi_lista2 = ['s', 'd', 'f']
print(mi_lista1 + mi_lista2)


#slice en listas
resultado = mi_lista[0:] 
print(resultado)

#sobrescribir o editar valores en una lista en el [ponemos el valor en donde va a estar editado]
mi_lista4 = ['z', 'f', 'g']
mi_lista4[2] = 'alfa'
print(mi_lista4)

#-------------metodos
#Metodo de agregar 'el elemeto siempre se va a ir al final'
mi_lista4.append('h')
print(mi_lista4)

#METODO PARA ELIMINAR 'siempre elimina el ultimo de la lista' *se le puede agregar una posicion
mi_lista4.pop(0)
print(mi_lista4)

#METODO DE ORDENAR LISTAS *aveces sale 'none' y se debe reconocer como dato*
mi_lista5 = ['a','x','n','e','o','l']
mi_lista5.sort()
print(mi_lista5)

mi_lista5 = [1,15,3,4,5,6,13,8,9,10,35,86,99]
mi_lista5.sort()
print(mi_lista5)