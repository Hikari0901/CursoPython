"""
Descripción:
Crea un programa que pida al usuario dos números y una operación (suma, resta, multiplicación, división).
Utiliza match-case para realizar la operación correspondiente y muestra el resultado.

"""

numero1=round(float(input('Dime un primero numero:\n\t ')),2)
numero2=round(float(input('Dime un segundo numero:\n\t ')),2)
operacion=input('Dime la operacion matematica que deseas realizar: ')
respuesta=()
match operacion:
    case 'suma':
        print(f" {numero1} + {numero2} = {numero1 + numero2}")
    case 'resta':
        print(f" {numero1} - {numero2} = {numero1 - numero2}")
    case 'multiplicacion':
        print(f" {numero1} * {numero2} = {numero1 * numero2}")
    case 'division':
        print(f" {numero1} / {numero2} = {numero1 / numero2}")
    case _:
        print('intente denuevo')