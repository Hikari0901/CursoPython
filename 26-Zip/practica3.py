"""
Practica 3

Crea el zip con las traducciones los números del 1 al 5 en español, portugués e inglés (en el mismo orden), y convierte el objeto generado en una lista almacenada en la variable numeros:

uno / um / one

dos / dois / two

tres / três / three

cuatro / quatro / four

cinco / cinco / five

El resultado deberá seguir la estructura:

[(uno, um, one), (dos, dois, two), ... ]
"""

numerosEspañol=['uno','dos','tres','cuatro','cinco']
numerosIngles=['one','two','tree','four','five']
numerosPortugues=['um','dois','três','quatro','cinco']

numeros=list(zip(numerosEspañol,numerosPortugues,numerosIngles))
print(numeros)