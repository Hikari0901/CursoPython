""".
Argumentos:
cuando no se sabe el numero de argumentos para una funcion se usa el *args para referirse a todos los argumentos adicionales luego de los obligatorios
recibe de forma de tupla


"""


#funcion que sume numeros
def sumar_todos(*args):
    suma = 0
    for n in args:
        suma += n
    return suma

print(sumar_todos(1,2,3))
print(sumar_todos(10,20,30,50))
