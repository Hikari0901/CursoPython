""".
interaccion entre funciones: las salidas de una funcion pueden convertise en entradas de otras funciones, de esa manera cada funcion realiza una tarea definida y el programa se construye a partir de la interaccion entre funciones

"""
#
lista_numeros = [1,2,15,7,2,8,15]

def reducir_lista(lista):
    lista = list(set(lista))#quitar elementos repetidos
    lista.pop(-1)#elimina el ultimo elemento de la lista
    return lista

def promedio(lista):
    valor_medio = sum(lista) / len(lista)#hace una suma el sum(), len() cuenta cuantos elementos hay en lista
    return valor_medio

resultado = promedio(reducir_lista(lista_numeros))
print(resultado)
  