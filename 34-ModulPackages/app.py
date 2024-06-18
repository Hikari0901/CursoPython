""".
Paquetes: se pueden desarrollar nosotros mismo y tambien hay algunos en python, son poricones de codigo o librerias predefinidas que se las puede llamar una vez instaladas usando el pip
para importar un modulo se usa: 
Import --- as ---
"""
#la libreria cv2 sirve para modificar imagenes, se suele utilizar para reconocimiento facial
import cv2

imagen = cv2.imread('computadora-gamer.jpg')

##cv2.imshow('compu',imagen)
#cambiar esala a color gris
griss= cv2.cvtColor(imagen, cv2.COLOR_BGRA2GRAY)

cv2.imshow('Imagen en escalas grises', griss)
cv2.waitKey(0)


import turtle as t
import random

tim= t.Turtle()
t.colormode(255)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color

#dibujar un elemento
def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)
    
draw_spirograph(5)