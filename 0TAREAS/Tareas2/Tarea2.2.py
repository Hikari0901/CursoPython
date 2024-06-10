""".
Escribe una funcion (puedes ponerle cualquier nombre que quieras) que reciba cualquier palabra como parametro
y que devuelva todas sus letras unicas(sin repetir) pero en orden alfabetico

Por ejemplo si al invocar esta funcion pasamos la parabra "entretenido"
deberia devolver ['d','e','i','n','o','r','t']
"""
letras='entretenido'

def fun_letras(letras):
    letras_sin_suplicados= list(set(letras))
    letras_sin_suplicados.sort()
    print(letras_sin_suplicados)
    
fun_letras(letras)
