"""
Practica 2.

Verifica si las palabras almacenadas en las siguientes variables:

palabra1 = "éxito", y
palabra2 = "tecnología"

no se encuentran en la frase a continuación, y almacena 
el resultado de esta comprobación (un booleano) en una variable llamada mi_bool:

"Cuando algo es lo suficientemente importante, lo haces incluso 
si las probabilidades de que salga bien no te acompañan"

Elon Musk
"""
texto="Cuando algo es lo suficientemente importante, lo haces incluso si las probabilidades de que salga bien no te acompañan"
palabra1= "exito"
palabra2= "tecnología"

mi_bool= (palabra1 not in texto) and (palabra2 not in texto) 
print(mi_bool)
