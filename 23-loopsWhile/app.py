#una estructura condicional que se ejecuta en repeticion hasta que se ejecuta false
#while condicion:
#expreison
#else
#expresion
#continue interrumpe la interaccion 
#pass no altera el programa

monedas= 5

while monedas > 0:
    print(f"Tengo {monedas} monedas")
    monedas = monedas - 1
    
#ejercicio
"""
respuesta = 's'
while respuesta == 's':
    #respuesta= input('Quieres seguir? (s/n)')
    pass
else:
    print('Gracias')
"""
#break
nombre = input("Tu nombre: ")
for letra in nombre:
    if letra == 'r':
        #break #detiene el codigo
        continue #onmite la especificacion y continua el codigo
    print(letra)