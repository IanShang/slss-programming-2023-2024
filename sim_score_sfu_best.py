# sfu's best similarity scores
# ian shanks from the engineering faculty
# 1949/7/90 🤔🤔🤔

# load data from file
# lire les files
# connecteur notre sim score algo au data

# ouvrir le file
with open("./data.csv") as f:

# lire le premiere ligne de file 🤔
    print(f.readline())
    print(f.readline())

# faire profile d'aimes dans SFU
profile = ["ian shanks", "Starbucks", "Ichibankan Express", "Pizza Hut", "Guadalupe (MBC)", "Subway"]

# commence not bien and votre nom
bien_meme_nots = 0
bien_meme_nom = ""
mauvais_meme_nots = 1
mauvais_meme_nom = ""

with open("./data.csv") as f:

    # lancer header
    header = f.readline()

    # pour tous ligne dans csv file
    for line in f:

        # change le string allais une list
        aimes_maintenant = line.split(",")

        # store le nom de personne
        nom_maintenant = aimes_maintenant[1]

        # commence le score maintenant
        meme_nots_maintenant = 0

        # sim score algorithm
        for item in profile:
            if item in aimes_maintenant:
                meme_nots_maintenant +=1

        # print results from cette ligne de data
        print(nom_maintenant + "-" + str(meme_nots_maintenant))

        # surjour les personne meme
        if meme_nots_maintenant > bien_meme_nots:
            bien_meme_nots = meme_nots_maintenant
            bien_meme_nom = nom_maintenant
        
        if mauvais_meme_nots > meme_nots_maintenant:
            mauvais_meme_nots = meme_nots_maintenant
            mauvais_meme_nom = nom_maintenant

print(bien_meme_nom + " est tres meme au toi avec une nots de " + str(bien_meme_nots))
print(mauvais_meme_nom + " est tres mauvais meme au toi avec une nots de " + str(mauvais_meme_nots))