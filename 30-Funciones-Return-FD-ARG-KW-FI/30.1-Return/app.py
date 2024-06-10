""".
return: para almacenar un valor de una funcion en una variable

def mi_funcion():
     return [algo]
     
def nombre_funcion():
     #bloque de codigo
     return valor
     
"""

#crear una funcion de que suma 2 numeros
def sumar(a,b):
     resultado= a + b
     return resultado
     
suma= sumar(5,6)
print(f"Suma = {suma}")

#verificar si un numero es par
def es_par(numero):
     if numero % 2 == 0:
          return True
     else:
          return False
#llamar a la funcion
print(es_par(2))
print(es_par(101))

#calcular el factorial de un numero
def factorial(n):
     if n ==0:
          return 1
     else:
          #aqui se aplica recursividad: factorial que se llama asi mismo
          return n * factorial(n-1)
#llamada a la funcion
print(factorial(5))


# Definir la función recursiva para la cuenta regresiva
def cuenta_regresiva(n):
    if n < 0:  # Condición base: si n es negativo, detenemos la recursión
        return
    else:
        print(n)
        cuenta_regresiva(n - 1)  # Llamada recursiva con n-1

# Ejecutar la función con el ejemplo
cuenta_regresiva(5)

