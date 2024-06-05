"""
Si la cuenta fue de $1500, repartida entre 5 personas, con 12% de propina
Cada persona deberá pagar (150.00 / 5) * 1.12
Formatear el resultado con 2 decimales = 33.60
Por lo tanto, la parte de la factura total que corresponda a todos es $30.00 más una propina de $3,60.
"""

print('¡Bienvenido a la calculadora de propinas!')
facturaTotal= float(input('¿Cuál fue la factura total?\n\t $'))
propuestaPropina= float(input('¿Cuánta propina te gustaría dar? ¿10, 12 o 15?\n\t%'))
divisionPersonas= float(input('¿Cuántas personas para dividir la cuenta?\n\t'))
TotalPago= round((facturaTotal/divisionPersonas),2)
PropinaPago= round(((propuestaPropina*TotalPago)/100),2)
print('Cada persona debe pagar: $', TotalPago, 'Mas una propina de: $', PropinaPago, '\n\tTotal: $', round((TotalPago + PropinaPago),2))