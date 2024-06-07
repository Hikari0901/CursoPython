"""
zip()
es una funcion que crea un interador formado por los elementos agrupados del mismo indice
solo agarra hasta el numero de elementos que alcance en comparacion con la lista de menor cantidad 



"""
nombre=['Ana', 'Hugo', 'Valeria']
edades = [65,29,45,23]

combinados= list(zip(nombre, edades))
print(combinados)

#agregar ciudades
ciudades=['Lima', 'Madrid', 'Mexico', 'Ecuador']
combinados= list(zip(nombre, edades,ciudades))
print(combinados)

#crear un loop
for nombre,edades,ciudad in combinados:
    print(f"{nombre} tiene {edades} years y vive en {ciudad}")