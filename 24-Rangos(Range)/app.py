"""
devuelve una secuencia de numeros en 3 pareametros, se usa para controlar el numero de ejecuciones de un loop o para crear rapidamente una serie de valores
range(valor_inicio, valor_final, paso)
    
"""
#forma tradicional
lista= [1,2,3,4]
for num in lista:
    print(num)
    
#codigo optimizado
for num in range(1,5):
    print(num)
    
#creacion de listas en una linea
lista= list(range(1,101,2))
print(lista)