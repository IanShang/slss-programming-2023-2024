# functione et tutle
# author
# 28/11/23

# import turtle

# screen = turtle.Screen()
# screen.setup(10000, 10000)

# el_gato = turtle.Turtle()
# el_gato.color("orange")
# el_gato.shape("turtle")
# el_gato.speed(0)

# # def square(n: float):
# #     # returne quand nn
# #     return n**2

# # def dessiner_carree(l: float):
# #     for n in range(4):
# #         el_gato.forward(l)
# #         el_gato.right(90)

# # dessiner_carree(square(5))
# # dessiner_carree(square(square(5)))
# # dessiner_carree(square(square(square(5))))

# def dessine_arbre(level: int, l: int):
#     # c'est ap comp sci flashbacks (i actually did ok in ap comp sci)
#     # dessiner arbre avec y que est me donne
#     # param =
#     # level que me parler le level de branch
#     # height y de arbres dans pixel

#     if level > 0: #🤔
#         # dessiner les branch
#         el_gato.forward(l)
#         # turner a port
#         el_gato.left(45)
#         # dessiner une arbres petit: level - 1
#         dessine_arbre(level - 1, l / 2)
#         # turner a starboard
#         el_gato.right(90)
#         # dessiner une arbres petit: level - 1
#         dessine_arbre(level - 1, l / 2)
#         # aller a la origin
#         el_gato.left(45)
#         el_gato.back(l)
#     else:
#         # faire level 0 arbre, une leaf desune
#         color_originale = el_gato.color()
#         el_gato.color("green")
#         el_gato.stamp()

# el_gato.setheading(90)
# dessine_arbre(4, 250)

# turtle.done()

import turtle

screen = turtle.Screen()
screen.setup(10000, 10000)

el_gato = turtle.Turtle()
el_gato.color("orange")
el_gato.shape("turtle")
el_gato.speed(0)

def dessine_arbre_beau(level: int, l: int): #c'est une belle arbre, n'est pas bizarre
    # c'est ap comp sci flashbacks (i actually did ok in ap comp sci)
    # dessiner arbre avec y que est me donne
    # param =
    # level que me parler le level de branch
    # height y de arbres dans pixel

    if level > 0: #🤔
        # dessiner les branch
        el_gato.forward(l)
        # turner a port
        el_gato.left(45)
        # dessiner une arbres petit: level - 1
        dessine_arbre_beau(level - 1, l / 2)
        # turner a starboard
        el_gato.right(90)
        # dessiner une arbres petit: level - 1
        dessine_arbre_beau(level - 1, l / 2)
        # aller a la origin
        el_gato.left(45)
        # dessine mid branch desune
        dessine_arbre_beau(level - 1, l / 2)
        el_gato.back(l * 2)
        el_gato.left(90)
        # funny
        dessine_arbre_beau(level - 1, l / 2)
        el_gato.back(l * 2)
        el_gato.left(45)
        # funny
        dessine_arbre_beau(level - 1, l / 2)
        el_gato.back(l * 2)
        el_gato.left(45)
        # funny
        dessine_arbre_beau(level - 1, l / 2)
        el_gato.back(l * 2)
        el_gato.left(45)
        # funny
        dessine_arbre_beau(level - 1, l / 2)
        el_gato.back(l * 1.5)
        el_gato.left(45)
        # funny
        dessine_arbre_beau(level - 1, l / 2)
        el_gato.back(l * 3)

    else:
        # faire level 0 arbre, une leaf desune
        color_originale = el_gato.color()
        el_gato.color("green")
        el_gato.stamp()
        el_gato.color(color_originale[0])

el_gato.setheading(90)
dessine_arbre_beau(5, 75)

turtle.done()