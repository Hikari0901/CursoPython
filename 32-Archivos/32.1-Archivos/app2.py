#reescribir archivos

###archivo=open('f:/Ronnald/Documents/Curso Python/32-Archivos/32.1-Archivos/prueba.txt','w')#la w: significa que se va a escribir sobre el archivo
###archivo.write('Hola\n')
###archivo.write('mundo')

#modificar archivo
archivo=open('f:/Ronnald/Documents/Curso Python/32-Archivos/32.1-Archivos/prueba2.txt','a')
lista=['hola', 'mundo','aqui','estoy']
for p in lista:
    archivo.writelines(p + '\n')

archivo.write("bienvenidos")
archivo.close()