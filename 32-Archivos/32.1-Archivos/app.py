""".
Archivos de texto en python: permite leer archivos, editar y sobrescribirlos a archivos .txt donde antes no habia una base de datos
abrir: open

"""
mi_archivo= open('./32-Archivos/32.1-Archivos/prueba.txt')#me salio un error y me toco poner la ruta completa del archivo

#leer todo el texto
###print(mi_archivo.read())

#leer linea por linea del texto
###print(mi_archivo.readline())
###print(mi_archivo.readline())

#utilizando un loop for

for l in mi_archivo:
    print("Aqui dice: " + l )

mi_archivo.close()
