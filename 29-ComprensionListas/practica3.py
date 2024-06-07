"""
Para realizar el ejercicio a continuación, puedes optar por diferentes caminos. 
Si bien en programación el camino correcto es el que devuelve el resultado correcto, 
te animo a que intentes aplicar los conceptos de comprensión de listas para comenzar 
a afianzarlos para el futuro. ¡Pueden resultarte muy útiles en tu práctica profesional!

Para la siguiente lista de temperaturas en grados Fahrenheit, expresa estos mismos 
valores en una nueva lista de valores de temperatura en grados Celsius. La conversión 
entre tipo de unidades es la siguiente:

°C = (°F - 32) * (5/9)

o expresado de otro modo:

(grados_fahrenheit-32)*(5/9)

La lista de temperaturas es la siguiente:

temperatura_fahrenheit = [32, 212, 275] 
Almacena esta nueva lista en una variable llamada grados_celsius
"""


Nueva_temperatura=(float(input("Ingrese la nueva temperatura a convertir: \n\t °F  ")))
if Nueva_temperatura <=32<=212:
    temperatura_fahrenheit = [32, 212, 275] 
    temperatura_fahrenheit.append(Nueva_temperatura)
    grados_celsius=[round(((x-32)*(5/9)),1) for x in temperatura_fahrenheit]
    print(f"La temperatura {temperatura_fahrenheit} °F equivale a {grados_celsius} °C")
else:
    print('Agregue un valor valido de temperatura Fahrenheit')
