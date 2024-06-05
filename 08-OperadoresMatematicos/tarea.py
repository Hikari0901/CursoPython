"""
La situación es esta: tú trabajas en una empresa donde los vendedores reciben comisiones
del 13% por sus ventas totales, y tu jefe quiere que ayudes a los vendedores a calcular sus
comisiones creando un programa que les pregunte su nombre y cuánto han vendido en este
mes. Tu programa le va a responder con una frase que incluya su nombre y el monto que le
corresponde por las comisiones. 
"""

print("--- LooPSell\'s ENTERPRICE ---")
nombre = input("Cual es su nombre: \n\t")
ventas = input("¿Cuanto ha vendido este mes?\n\t$ ")
ventasInt = float(ventas)
porcentaje = round(((ventasInt * 13)/100),2)
print(f"Estimado/a socio {nombre}, usted declara haber vendido un total de \" $ {ventas} \" en este mes.\n Calculando el 13% de sus ventas totales. \n Usted recibe de comision el siguiente valor: $ {porcentaje}. \n  "  "  Muchas gracias por su maravilloso trabajo y aportacion. \n\t --- LooPSell\'s ENTERPRICE ---")
