""".
sirve para identificar el argumento por su nombre independiente de la posicion que pasen a la funcion
lo agrupa en un diccionario
**kwargs

"""

def cantidad_atributos(**kwargs):
    cantidad = 0
    for i in kwargs.items():
        cantidad+= 1
    return cantidad

print(cantidad_atributos(a=1,b=2,c=3,d=4))


def imprimir_kwargs(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")
        
imprimir_kwargs(nombre= 'Jose', edad=30,ciudad = 'Loja')


def configurar_opciones(obligatorio,**kwargs):
    opciones = {
        'opcion1' : 'valor por defecto 1',
        'opcion2' : 'valor por defecto 2'
    }
    opciones.update(kwargs)
    print(f"obligatorio: {obligatorio}")
    for key,value in opciones.items():
        print(f"{key}:{value}")
        
configurar_opciones('necesario',opcion1= 'nuevo valor1',opcion2 = 'nuevo valor2')