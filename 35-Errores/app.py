""".
Manejo de errores: existen estrategias para capturar y gestionar los errores que pueden presentarse al ejecutar un programa
a fines de evitar una falla mayor y controlar la informacion que es mostrada al usuario
--Partes:
try: se ejecuta hasta finalizar o hasta que se presente un error
exect: contiene un manejador de errores atrapando las excepciones que se presentan durante la ejecucion de try
#opcionales
-else: engloba el codigo que se ejecutara unicamente cuando ninguna excepcion haya sido detectada en la ejecucion de try
-finally: contiene codigo que e ejecuta siempre, se hayan presentado o no errores
"""

num1=12
num2=2

try:
    resultado= num2 / num1
except ZeroDivisionError:
    print('Error: Division por cero no permitida.')
except TypeError:
    print('Error: ambos operandos deben ser numeros.')
finally:
    print(f"Operacion de division realizada {resultado}")
#print(resultado)





