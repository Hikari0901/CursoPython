#Solicitar informacion al cliente (comentario en pyton #)
#input("Dime tu nombre: ")
#input("Dime tu apellido: ")

""" 
Creacion de imputs 
y 
Usando el print
"""

#print(input("Dime tu nombre: "))
#print(input("Nombres completos: " + input("Dime tu nombre: ") + " " + input("Dime tu apellido: ")))

#Forma correcta (lo que hace es separar por parentesis, lo que hace que el comando termine sin necesidad de dar un enter al final)
print("Nombres completos: " + (input("Dime tu nombre: ") + " " + (input("Dime tu apellido: "))))