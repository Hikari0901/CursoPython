"""
es una accion que hace de forma diferente lo que queremos hacer
hay como 46 metodos pero se usan los siguientes:

es con el .(el metodo y su config)

"""
#UPPERCASE: hacer todo a mayuscula

texto = "Este es el texto de jose"
resultado = texto.upper()
print(resultado)

#**averiguar** SPLITT: coloca los elementos en una lista y los separa en (,), se puede colocar por que separar en () 
resultado = texto.split("t")
print(resultado)

#hace y une en una lista la lista va en []
a = "Aprender"
b = "Python"
c = "es"
d = "genial"
e = "-".join([a,b,c,d])
"""print(e)"""

#FIND: verifica o busca desde la poscicion que encuentra
resultado = texto.find("t")
print(resultado)
#find encuentra por posciciones y cuando no existe sale en -1 es la dif con el index

#REPLACE: remplaza el texto y va asi .replace(texto, texto a reemplazar) 
resultado=texto.replace("Jose", "Python")
print(resultado)
