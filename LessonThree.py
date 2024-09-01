#Pygame is a special tool that helps people to make fun and exciting video games using the Python.

import pgzrun
from random import randint

WIDTH= 300
HEIGHT= 300

def draw():
    

    r= 255
    g= 0
    b= randint(0,255)

    width= WIDTH
    height=HEIGHT-200
    for i in range(10):
        rect= Rect((150,150),(width,height))
        rect.center= 150,150
        screen.draw.rect(rect, (r,g,b))

        r-= 10
        g+= 10


        width -= 10
        height += 10


pgzrun.go()