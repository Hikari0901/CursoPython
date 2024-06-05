""" """
lista= ['a','b','c']
indice=0
for item in lista:
    print(indice,item)
    #operadores de asignacion '+='
    indice += 1 # indice + 1
    
#con enumerate
lista= ['a','b','c']
for i,item in enumerate(lista):
    print(i, item)
    
#convinacion enumerate y range


for i, item in enumerate(range(50,55)):
    print(f"{i} - {item}")
    
lista= ['a','b','c']
mis_tuplas=list(enumerate(lista))
print(mis_tuplas)
print(mis_tuplas[1][0])