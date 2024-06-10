""".
son la integracion de diferentes herramientas de contol de flujo
crea funciones dinamicas y flexibles


"""

#calcular el area de un cuadrado y un rectangulo
def calcular_area_forma(lado1,lado2=None):
    if lado2 is None:
        return lado1**2 #nos da el area del cuadrado
    else:
        return lado1 * lado2 #calcular el area del rectangulo

print(calcular_area_forma(5))
print(calcular_area_forma(3 , 4))

#una funcion que me sume los numeros pares

def suma_pares_hasta(n):
    suma= 0
    for i in range(2,n+1,2):
        suma += i
    return suma

print(suma_pares_hasta(10)) #(2+4+6+8+10) = 30

#crear una funcion que permita la sumatoria de los cubos y cuadrados

def suma_cuadrados_cubos(n):
    suma_cuadrados= 0
    suma_cubos= 0
    for i in range(1,n+1):
        if i % 2 == 0:
            suma_cuadrados+= i**2
        else:
            suma_cubos += i **3
    return suma_cuadrados, suma_cubos

cuadrados, cubos= suma_cuadrados_cubos(5)
print("Suma de cuadrados: ", cuadrados)# 2^2 + 4^2 =20
print("Suma de cubos: ", cubos)# 1^3 + 3^3 + 5^3 = 153

        