""" Comprension de listas:
ofrece una sintaxis mas leve en la creacion de una lista basada en valores disponibles en otra secuencia, vale la pena mencionar que la  brevedad se logra a costo de una menor interpretabilidad


                    elemento interable              parte logica
nueva_lista=[expresion] for item in interable if condicion ==True]
        formula matematica           tupla,set,otra lista
        
con else: 
nueva_lista=[expresion if condicion ==True else otra_expresion for item in iterable]


"""

#Forma tradicional
palabra = 'phyton'
lista=[]

for item in palabra:
        lista.append(item)
###print(lista)

lista=[item for item in 'python']
###print(lista)

#comprension de listas con numeros
lista= [item/2 for item in range(0,21,2)]
print(lista)

#usando if

lista=[item if item**2>10 else 'no' for item in range(0,21,2)]
print(lista)

lista = [item**2 if item > 10 else 'no' for item in range(0, 21, 2)]
print(lista)


#parte complicada:

numero= [1,2,3,4,5,6,7,8,9,10]
resultado=['par' if numero % 2 == 0 else 'impar' for numero in numero]
print(resultado)


#convertir de pies a metros
metros=[10,20,30,40,50]
pies=[p*3.281 for p in metros]
print(pies)
