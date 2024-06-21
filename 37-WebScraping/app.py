""".
entornos irtuales en python: son distintos tipos de entornos donde cada uno por distinto puede albergar distintas librerias instaladas
crear entorno: python.exe -m venv entorno
activar entorno:cd .\entorno\Scripts\ .\activate
pip list: ver los paquetes
desactivar: deactivate
(
html: es un lenguaje de etiquetas de hyper texto para crear un sitio web
css: permite hacer estilos al sitio web(se hace con etiquetas de html)

    
    
)
"""
import requests 
import bs4 # type: ignore

resultado = requests.get('https://primerreporte.com/2024/06/18/estudiantes-de-arquitectura-uide-loja-en-gira-nacional/')

#trae todo el codigo fuente del sitio
###print(resultado.text)

sopa = bs4.BeautifulSoup(resultado.text, 'html.parser')

#titulo del sitio web

##print(sopa.select('title')[0].getText())

#Traer el numero de etiquetas p de parrafo
##print(len(sopa.select('p')))

#taer el texto de p
parrafo= sopa.select('p')[2].getText()
###print(parrafo)

columna_lateral= sopa.select('.widget-title')
for p in columna_lateral:
    print(p.getText())
    
#extraer imagenes

imagenes = sopa.select('.custom-logo')[0]['src']
##print(imagenes)

#print imagenes
logo_empresa= requests.get(imagenes)
##print(logo_empresa.content)

#guardar las imagenes
f = open('logo.png', 'wb')#wb: write binari
f.write(logo_empresa.content)
f.close()
