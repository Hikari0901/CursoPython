#1propiedad: Son inmutables es decir solo son sting y nada mas, no se puede mutar
nombre = "carina"
#nombre[0] = "K"
print(nombre)

#solucion: (es a unica forma)
nombre = "carina"
nombre = "Karina"
print(nombre)


#2Propiedad: Concatenar
n1 = "Kari"
n2 = "na"
print(n1 + n2)

#3Propiedad: se puede multiplicar los strings
print(n1*3)

#4Popiedad: Se puede buscar (in) valor boleano
#in: en (not in: no en)
poema = "Ecuador pais uno de los mejores paraisos del mundo"
print("mejores" not in poema)

#5propiedad: len: tamaño del string es decir cuantas letras tiene
print(len(poema))
