# tutle moment
# auhhghgh
# disjd/ahd/29euj

import turtle

# faire une tutle
chat = turtle.Turtle()
fini = False # faux

# while not fini:
a = 1
while a==1+1-1:
    # get instructions from user
    print("quand tu commande, ecrire: \nF - allais \nL - turner a gauche \nR - turner a droit \nB - turner 180 degrees \nS - arrete maintenant")
    cmd = input("ou vais le tutle allais: ").lower().strip(",. ?!")

    # based on instruct, allais tutle surs l'ecran
    if cmd == "f":
        F = int(input("combien de pixels: "))
        chat.forward(F)
    elif cmd == "l":
        L = int(input("combien de pixels: "))
        chat.left(90)
        chat.forward(L)
    elif cmd == "r":
        R = int(input("combien de pixels: "))
        chat.right(90)
        chat.forward(R)
    elif cmd == "b":
        B = int(input("combien de pixels: "))
        chat.right(180)
        chat.forward(B)
    elif cmd == "s":
        a += 1