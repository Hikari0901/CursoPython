""".
directorio: es un tipo exclusivo de archivo que solo contiene la informacion necesaria
"""
import os
"""
ruta= os.getcwd()#ir a la ruta del archivo que se esta editando
print(ruta)

ruta= os.chdir('F:\\Ronnald\\Documents\\Curso Python\\32-archivos')
print(ruta)

#crea una carpeta
ruta= os.makedirs('F:\\Ronnald\\Documents\\Curso Python\\32-archivos\\otra carpeta')
print(ruta)
"""

ruta= 'F:\\Ronnald\\Documents\\Curso Python'
elemento= os.path.split(ruta) #me trae en tupla mi ruta
print(elemento)

#eliminar carpeta rm:remove dir:directorio
os.rmdir('F:\\Ronnald\\Documents\\Curso Python\\32-archivos\\otra carpeta')

