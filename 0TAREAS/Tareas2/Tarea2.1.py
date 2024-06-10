""".
Crea una funcion llamada devolver_distintos() que reciba 3 integers como parametros

si la suma de los 3 numeros es mayor a 15, va a devolver el numero mayor.

si la suma de los 3 numeros es menos a 10, va a devolver el numero menor.

si la suma de los 3 numeros es un valor entre 10 y 15(incluidos) va a devolver el numero de valor intermedio

"""
lista = [1,3,1]
lista.sort()

def devolver_distintos(lista):
    suma=0
    for n in lista:
        suma += n
    if suma>15:
       print(f"El numero mayor es: {(lista[::-1])[0]}")
    elif suma<10:
        print(f"El numero menor es {lista[0]}")
    else:
        print(f"El numero intermedio es: {lista[1]}")
            
devolver_distintos(lista)