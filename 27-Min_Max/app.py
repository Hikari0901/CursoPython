"""
min, max: 
min():la funcion min: retorna el item con el valor mas bajo dentro del interable
max():el item con valor mas alto
si son 'str' los compara alfabeticamente
    
"""
menor=min(58,72,96,32,11)
mayor=max(58,72,96,32,11)
print(menor)
print(mayor)

#en una lista
lista=[110,112,114,256,399]
print(f"El menor es {min(lista)} y El mayor es {max(lista)}")


#utilizando un diccionario

dic={'c1':45,'c2':11,'c3':5}
print(min(dic.values()))