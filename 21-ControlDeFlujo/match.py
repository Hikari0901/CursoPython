""" 
match valor: 
   case patron1:
     #codigo a ejecutar, si el valor coincide con el patron 1
    case patron2:
     #codigo a ejecutar, si el valor coincide con el patron 2
     case _:# 'caso': valor default
     #codigo a ejecutar si el valor no coincide con ningun patron
     
     

"""

#Comparacion de numeros:
number = 1

match number:
    case 1:
        print("Uno")
    case 2:
        print("Dos")
    case 3:
        print("Tres")
    case _:
        print("otro numero")

#Comparacion de tipos
value={'a': 1,'b':2}

match value:
    case int():
        print('Es un entero')
    case str():
        print('es una cadena')
    case list():
        print('es una lista')
    case _:
        print('es un tipo desconocido')
        
#desempaquetado de tuplas
coord=(0,5)
match coord:
    case (0,0):
        print('Punto de origen')
    case (x,0):
        print(f"Eje x en {x}")
    case(0,y):
        print(f"Eje y en {y}")
    case(x,y):
        print(f"Punto en {x} y {y}")
    case _:
        print("Coordenadas desconocidas")
        
