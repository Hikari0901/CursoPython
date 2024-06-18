""".
Practica manejo de errores 1
Hemos visto en la leccion de que manera se implementa el manejo de errores
habitualmente en python. en el caso de este ejercicio, sin embargo,
necesitare que lo hagamos de una forma ligeramente distinta para que pueda ser evaluado:
deberas implementarlo Dentro de la funcion. en forma de comentario,
veras un ejemplo de resolucion. Ten presente, sin embargo,
que la forma preferida es la que hemos visto en clase.

"""
def division(a,b):
    try:
        division = a / b
        print(division)
    except ZeroDivisionError:
        print('Error: tipo de dato incorrecto')
    except TypeError:
        print('Error: tipo de dato incorrecto')

        
division(12,0)