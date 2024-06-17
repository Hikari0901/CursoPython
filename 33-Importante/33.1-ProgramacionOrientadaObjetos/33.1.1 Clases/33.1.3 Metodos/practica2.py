""".
Practica metodos 3:
crea una instancia de la clase alarma, que tenga un metodo
llamado postergar(cantidad_minutos). el metodo debe imprimir en pantalla el mensaje

"La alarma ha sido pospuesta {cantidad_minutos minutos}"
"""

class alarma:
    def postergar(self,cantidad_minutos):
        print(f"La alarma ha sido pospuesta {cantidad_minutos} minutos")
        
alarma1 = alarma()
alarma1.postergar(1)
        