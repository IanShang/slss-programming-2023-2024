# biscuits
# ion shanks
# 28378/239723/2938

import turtle

# Make baker turtle
baker_tutle = turtle.Turtle()
baker_tutle.color("brown")
baker_tutle.fillcolor("black")

# Draw outline of cookie
baker_tutle.penup()
baker_tutle.goto(-5, -30)
baker_tutle.pendown()
baker_tutle.begin_fill()
baker_tutle.circle(30)
baker_tutle.end_fill()
baker_tutle.penup()

# Add chips
baker_tutle.color("black")
baker_tutle.penup()
baker_tutle.left(90)
baker_tutle.forward(20)
baker_tutle.pendown()
turtle.done()