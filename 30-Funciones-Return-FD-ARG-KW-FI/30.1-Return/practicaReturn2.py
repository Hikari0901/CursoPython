"""
Practica 2
Crea una función llamada usd_a_eur que tome como único parámetro un 
valor numérico (un monto en dólares estadounidenses), y devuelva como 
resultado el monto equivalente en euros. A fines de este ejemplo, tomaremos 
la conversión 1 USD = 0.90 EUR.

Crea una variable llamada dolares y almacena en ella un monto cualquiera 
para entregárselo a tu función y evaluar su resultado.
"""

dolares=10
def usd_a_eur(dolares):
    return print(f" El monto: $ {dolares} equivale a: '{round(dolares * 0.9),2}' EUR ")

usd_a_eur(10)
usd_a_eur(100)
usd_a_eur(150)
usd_a_eur(290)


