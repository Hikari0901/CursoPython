"""
Práctica Crear y Escribir Archivos 2
Abre el archivo llamado "mi_archivo1.txt", y añade una línea
 al final del mismo que diga: "Nuevo inicio de sesión".

Imprime el contenido completo de "mi_archivo.txt" al finalizar.
"""
archivos2= open('f:/Ronnald/Documents/Curso Python/32-Archivos/mi_archivo2.txt','a')
archivos2.write('Nuevo inicio de sesion')
archivos2.close()
archivos2= open('f:/Ronnald/Documents/Curso Python/32-Archivos/mi_archivo2.txt','r')
print(archivos2.read())
archivos2.close()