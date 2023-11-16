# combien de meme activite entres deux personnes
# an-ion (badum tss)
# japan does NOT like the gregorian calendar 🗣️🗣️🗣️🔥🔥🔥💀💀💀

liste_un = input("quest'ce que as tu fais dans ton libre temp: ").lower().split()
liste_deux = input("quest'ce que as tu fais dans ton libre temp: ").lower().split()
memes_nots = 0
for activite in liste_un:
    for activitee in liste_deux:
        if activite == activitee:
            memes_nots += 1
print("vous avez " + str(memes_nots) + " acitivite dans meme")