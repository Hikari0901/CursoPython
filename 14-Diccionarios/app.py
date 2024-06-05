"""
DICCIONARIOS 'dict': son estructuras de datos que almacenan informacion en pares es decir tienen una clave y valor, son utiles para guardar y recuperar informacion, estos no utilizan indices(index)
usa {clave:valor}
se puede agrear cualquier dato
"""
#caracteristicas: son mutables, no son ordenados, no admiten valores duplicados en el valor {-:valor}
#{'nombre':'jose'}
cliente = {'nombre':'Jose','Apellido':'Diaz','Peso':88,'Talla':1.75}
print(type(cliente))

#atrapar o pintar un valor ():una tupla se usa [] para ver el resultado

consulta = (cliente['Apellido'])
print(consulta)

#otro ejemplo (obtener informacion a travez de las claves) un dic puede ser un archivo ccv
dic = {'c1':55, 'c2':[30,40,50],'c3':{'s1':100,'s2':200}}
print(dic['c3']['s2'])

#mostrar las propiedades y agregar el metodo
dic2 = {'c1':['a','b','c'],'c2':['d','f','g']}
print(dic2['c1'][0].upper())

#agregar elementos a un diccionario
dic3= {1:'a',2:'b'}
print(dic3)

dic3[3]='c'
print(dic3)

#modificar es la [clave]
dic3[2] = 'B'
print(dic3)

print(dic3.keys())#llaves
print(dic3.values())#valores
print(dic3.items())#los muestra de manera separada 

