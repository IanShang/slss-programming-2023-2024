# functione et tutle
# author
# 28/11/23

import turtle

screen = turtle.Screen()
screen.setup(10000, 10000)

el_gato = turtle.Turtle()
el_gato.color("orange")
el_gato.shape("turtle")
el_gato.speed(0)

def square(n: float):
    # returne quand nn
    return n**2

def dessiner_carree(l: float):
    for n in range(4):
        el_gato.forward(l)
        el_gato.right(90)

dessiner_carree(square(5))
dessiner_carree(square(square(5)))
dessiner_carree(square(square(square(5))))

turtle.done()