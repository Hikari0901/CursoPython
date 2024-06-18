""".

"""
def cociente(num1,num2):
    try:
        resultado=num2/num1
        print(resultado)
    except ZeroDivisionError:
        print('El segundo argumento no debe ser cero')
    except TypeError:
        print('Los argumentos a ingresar deben ser numeros')
    
n1 = 0
n2 = 12
cociente(n1,n2)

n1 = 'a'
n2 = 12
cociente(n1,n2)

n1= 2
n2= 12
cociente(n1,n2)
