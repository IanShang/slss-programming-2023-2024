# biscuits
# ion shanks
# 28378/239723/2938

import turtle

ecran = turtle.Screen()

# Make baker turtle
baker_tutle = turtle.Turtle()
baker_tutle.color("brown")
baker_tutle.fillcolor("black")

l = ecran.window_width()
h = ecran.window_width()

x = int(input("ou est la biscuit sur l'axis de x: ").strip(".,?! "))
y = int(input("ou est la biscuit sur l'axis de y: ").strip(".,?! "))
grand = int(input("comment grande est cette biscuit: ").strip(".,?! "))
if grand <= 0: 
    print("cette biscuit vais disappeare")
if x+grand <= l and y+grand <= h and x-grand>=-l and y-grand>=-h:
    # Draw outline of cookie
    baker_tutle.penup()
    baker_tutle.goto(x, y)
    baker_tutle.pendown()
    baker_tutle.begin_fill()
    baker_tutle.circle(grand)
    baker_tutle.end_fill()
    baker_tutle.penup()
    # Add chips
    baker_tutle.color("black")
    baker_tutle.penup()
    baker_tutle.left(90)
    baker_tutle.forward(20)
    baker_tutle.pendown()
    turtle.done()
else: print("cette biscuit vais disappeare")