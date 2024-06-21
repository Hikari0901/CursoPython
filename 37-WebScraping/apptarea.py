""".
https://books.toscrape.com/catalogue/page-2.html
https://datademia.es/blog/que-es-web-scraping leer info

"""

import requests
import bs4

resultado = requests.get('https://books.toscrape.com/catalogue/page-2.html')

ordenado_html= bs4.BeautifulSoup(resultado.text, 'html.parser')

#rating_Libros = ordenado_html.select('p.star-rating.Five')
#for r in rating_Libros:
#    print(r)

#titulos_Libros = ordenado_html.select('h3')
#for t in titulos_Libros:
#    print(t.getText())
"""   
def busqueda():
    li= ordenado_html.select('li')
    if ordenado_html.select('p.star-rating.Five') in li: 
        titulo = ordenado_html.select('h3')
        print(f"{li} {titulo}")
        
busqueda()
"""

def busqueda():
    # Suponiendo que 'ordenado_html' es tu objeto BeautifulSoup con el HTML cargado
    items = ordenado_html.select('li')
    for item in items:
        if item.select_one('p.star-rating.Five'):
            titulo = item.select_one('h3')
            if titulo:
                print(titulo.get_text())
                
busqueda()