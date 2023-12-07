# quest'que ce une functione?
# une functione est une square de programme que tu peux utilise multiple fois
# nous pouvons referee les data a parametre
# nous utilisons "arguments" au describe data

# def photocopier_area_de_square(s: float) -> None:
#     print("l'area de square est " + str(s*2) + " sqaured")

# def area_de_square(s: float) -> float:
#     area = s ** 2
#     return area

# photocopier_area_de_square(2)
# area_de_square(2)

# plus_de_area = area_de_square(1) + area_de_square(1)

# # function que retourne
# def plus(x: int, y:int) -> int:
#     sum = x+y
#     return sum # arrete le function, si il y a une val apres, il donne le val ou le function a telephone

# plus(1, 1)

def trouver_linear(l: list, item: any) -> int:
    for n in range(len(l)):
        if item == l[n]:
            return n
    return -100000

print("je trouve ton drugs a la numero " + str(trouver_linear(["doragusu", "drugs"], "drugs")) + " place")