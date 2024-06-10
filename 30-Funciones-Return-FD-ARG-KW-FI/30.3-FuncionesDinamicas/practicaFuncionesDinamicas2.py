
lista_numeros=[1,50,500,5000,750,600]

def suma_menores(lista_numeros):
    suma= 0
    suma_menos= 0
    for n in lista_numeros:
        if n > 0:
            suma+= n
        if n > 1000:
            suma_menos += n
        else:
            print("valores fuera del rango")
    return suma - suma_menos
            
    
print(suma_menores(suma_menores))
