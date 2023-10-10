# je mange les nourriture
# niece and nephews ian shanks (Real)
# dec 7 1941

# c'est une robob qui demander les personnes quest'que ce votre nourriture preferre
# cette robob donne une funny textos pour cette personne
# le robob vais dire je m'appelle

cn_food = ["noodles", "dumplings", "sticky rice", "moon cake"]
jp_food = ["sushi", "miso soup", "ramen", "takoyaki"]
fr_food = ["baguette", "champagne"]
ru_food = ["vodka"]
gb_food = ["tea", "biscuits", "beans", "toast"]

print("HELLO, IM EMU OTORI")
fav_food = input("quest'que c'est ton nourriture preferre: ")

cn_count = 0
while(cn_count <= len(cn_food) -1):
    if fav_food.lower().strip(" .?!") == cn_food[cn_count]:
        print("Ching cheng Hanji. Can't touch me at all. The kitchen in the dungeon. I swear I'll beat Paul the fool. *** ******** ***. my mom doesn't love me. I swear I'll hit Paul")
    cn_count = cn_count +1

jp_count = 0
while(jp_count <= len(jp_food) -1):
    if fav_food.lower().strip(" .?!") == jp_food[jp_count]:
        print("o mai gado")
    jp_count = jp_count +1

fr_count = 0
while(fr_count <= len(fr_food) -1):
    if fav_food.lower().strip(" .?!") == fr_food[fr_count]:
        print("mes amis, vais tu preferre un peu de champagne ou baguette")
    fr_count = fr_count +1

ru_count = 0
while(ru_count <= len(ru_food) -1):
    if fav_food.lower().strip(" .?!") == ru_food[ru_count]:
        print("in soviet russia, you don't drink vodka, vodka drinks you")
    ru_count = ru_count +1

gb_count = 0
while(gb_count <= len(gb_food) -1):
    if fav_food.lower().strip(" .?!") == gb_food[gb_count]:
        print("beans.")
    gb_count = gb_count +1