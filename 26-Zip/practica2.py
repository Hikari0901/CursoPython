"""
Practica 2

Crea un objeto zip formado a partir de listas, de un 
conjunto de marcas y productos que tú prefieras, dentro de la variable mi_zip.
"""
marcas=['Samsung', 'Apple', 'Gigabite', 'Vans',]
productos=['SmartPhones', 'Vision Pro','Monitores Gaming','Zapatillas']

mi_zip = list(zip(marcas,productos))
for marcas,productos in mi_zip:
    print(f"De la marca {marcas} mi producto favorito es: {productos}")