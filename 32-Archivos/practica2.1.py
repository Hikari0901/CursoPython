"""

Práctica Crear y Escribir Archivos 1
Abre el archivo llamado "mi_archivo.txt", y cambia su contenido por el texto "Nuevo texto".

Imprime el contenido completo de "mi_archivo.txt" al finalizar.
"""

Archivos1=open('f:/Ronnald/Documents/Curso Python/32-Archivos/mi_archivo1.txt','w')
Archivos1.write('Nuevo Texto')
Archivos1.close()

Archivos1=open('f:/Ronnald/Documents/Curso Python/32-Archivos/mi_archivo1.txt','r')
print(Archivos1.readline())
Archivos1.close()