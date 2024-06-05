#permiten tomar decisiones basadas en multiples condiciones,son importantes con las condicionales*otro tema*, los que existen son: 
#and: devuelve true si todas las condiciones son verdaderas
#or: devuelve true si almenos una condicion es verdadera
#not: devuelve true si el valor boleano es false y false si es true (lo niega y revierte)
"""
AND:
falso falso falso
falso true falso
true false false
--true true true--

Or:

false false false
--falso true true--
--true false true--
--true true true--

Not:

true false
false true

"""
#se utiliza para hacer concatenaciones logicas mas largas.

mi_bool= 4 < 5 > 5

#ejercicio
mi_bool= 4<5 and 5>6

#and
mi_bool = (55==55) and ('perro' == 'perro')

#or
mi_bool = 10 == 10 or 3==7
###print(mi_bool)

texto= "esta frase es breve, python" 
mi_bool= ('frase' in texto) and ('python' in texto)
print(mi_bool)

#diferente
mi_bool = not(False)
print(mi_bool)