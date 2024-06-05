#son ciclos, los loops son secuencias de intrucciones de codigo que se ejecutan repetidas veces
#son iterables
#for item in iterable:
#for es como llamar a cada item del interable

###lista= ['a','b','c','d']

#antes:
#print(lista[0])
#print(lista[1])
#print(lista[2])

#explicacion: for es el loop, el item puede ser cualquiera (y,letra,etc), in es en, lista es el iterable


for item in lista:
    print("Letra" + ' ' + item)
    
for i in lista:
    print("Letra" + ' ' + i)
    
for letra in lista:
    print("Letra" + ' ' + letra)
    
for item in lista:
    numero_letra = lista.index(item) + 1
    print(f"Letra {numero_letra}: {item}")
    

#nos permite leer un caracter en cada palabra .starswitch

lista= ['pablo', 'laura', 'jose','luis','julia']
for item in lista:
    if item.startswith('l'):
        print(item)
    else:
     print('Nombre que no comienza con L')


numeros = [1,2,3,4,5]
mi_valor= 0

for item in numeros:
    mi_valor = mi_valor+item
    print(mi_valor)
    
#directamente
for a,b in [[11,2],[2,3,],[5,6]]:
    print(f"valor {a} - valor {b}")
   
#diccionarios
dic={'clave1':'a', 'clave2':'b', 'clave3':'c'}
for a,b in dic.items():
    print(a,b)