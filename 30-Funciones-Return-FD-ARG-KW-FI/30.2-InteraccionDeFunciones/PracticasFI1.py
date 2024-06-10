"""
Practica 3
Crea una función (llamada lanzar_moneda) que devuelva el resultado de lanzar 
una moneda (al azar). Dicha función debe poder devolver los resultados "Cara" o "Cruz", 
y no debe recibir argumentos para funcionar.
Crea una segunda función (llamada probar_suerte), que tome dos argumentos: el primero, debe ser el resultado del lanzamiento de la moneda. El segundo argumento, será una lista de números cualquiera (debes crear una lista con valores y llamarla lista_numeros).
Si se le proporciona una "Cara", debe mostrar el mensaje al usuario: "La lista se autodestruirá", y eliminarla (devolverla como lista vacía []).
Si se le proporciona una "Cruz", debe imprimir en pantalla: "La lista fue salvada" y devolver la lista intacta.
"""
import random

lista_numeros=[1,2,15,7,2,8]
def lanzar_moneda():
    resultado=random.choice(['Cara','Cruz'])
    return resultado


def probar_suerte(moneda, lista):
    if moneda == 'Cara':
        print("la lista se autodestruira")
        return []
    elif moneda == 'Cruz':
        print("La lista fue salvada")
        return lista
    
suerte = probar_suerte(lanzar_moneda(),lista_numeros)
print(suerte)

#scope - alcance de variables: significa que cada variable dentro de una funcion, solo funciona dentro de la funcion