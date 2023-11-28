# functione et tutle
# author
# 28/11/23

import turtle

el_gato = turtle.Turtle()
el_gato.color("orange")
el_gato.shape("turtle")

def square(n: float):
    # returne quand nn
    return n**2

def dessiner_square(l: float):
    for n in range(4):
        el_gato.forward(l)
        el_gato.right(90)

turtle.done()

dessiner_square(square(5))