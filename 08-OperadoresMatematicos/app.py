x = 6
y = 2
z = 7

#operaciones basicas en python

print(f"{x} + {y} es igual a {x+y}")
print(f"{x} - {y} es igual a {x-y}")
print(f"{x} * {y} es igual a {x*y}")
print(f"{x} / {y} es igual a {x/y}")

#divicion entera y div por modulo:

print(f"{z} // {y} es igual a {z//y}") #// es para entera

print(f"{z} % {y} es igual a {z%y}") # % es para modulo

#fomra de hacer elevado

print(f"{x} elevado a la {y} es igual a {x**y}") # se usa **

print(f"{x} elevado a la {3} es igual a {x**3}")

#Raiz cuadrada (todo elevado a 0.5 es raiz cuadrada)

print(f"la raiz cuadrada de {x} es {x**0.5}")

#redondeo se usa ("round" que es propio de python + , (el numero de decimales))
resultado = 97/7
redondeo = round(resultado, 4)
print(redondeo)
