""".
Escribe una funcion que requiera una cantidad indefinida de argumentos.
lo que hara esta funcion es devolver True  si en algun momento se ha
ingresado al numero  cero  repetido dos veces consecutivas.

por ejemplo:
(5,6,1,0,0,9,3,5) True
(6,0,5,1,0,3,0,1) False
"""

def funcion(*args):
    for primero,segundo in zip(args,args[1:]):
        if primero==0 and segundo==0:
            return True
    return False

print(funcion(5,6,1,0,0,9,3,5))
print(funcion(6,0,5,1,0,3,0,1))

