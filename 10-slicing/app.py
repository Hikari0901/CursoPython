"""
slicing usa []
[valor de inicio : valor de pare o stop : valor de stip o paso]
[inicio : pare : paso]
[inicio : stop : step]
[es en numeros de las posiciones y siempre para uno menos de el final]
step: significa que se salte de 2 en 2 , etc
"""
texto = "ABCDEFGHIJKLM"
fragmento = texto[2:5]

fragmento = texto[:5]
fragmento = texto[2:10:2]
#-1 para invertir strings
fragmento = texto[::-1]
print(fragmento)