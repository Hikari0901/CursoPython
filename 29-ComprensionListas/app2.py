#sintaxis basica de la compresion de listas
#[expresion for elemento in iterable]
#crear una lista de cuadrados de los numeros del 0 al 9

cuadrados=[x**2 for x in range(10)]
print(cuadrados)

#[expresion for elemento in iterable if condicion]
#crear una lista del 0 al 9 que nos devuelva los valores pares
pares= [x for x in range(10) if x % 2 ==0]
print(pares)

#[expresion1 if condicion else expresion2 for elemento in iterable]
#listar numeros pares e inpares pero esto se muestra con un texto
par_impar=['par' if x % 2 == 0 else 'impar' for x in range(10)]
print(par_impar)