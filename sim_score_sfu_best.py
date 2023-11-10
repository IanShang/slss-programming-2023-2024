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
        sim_score_maintenant = 0

        # sim score algorithm
        for item in profile:
            if item in aimes_maintenant:
                sim_score_maintenant +=1

        # print results from cette ligne de data
        print(nom_maintenant + "-" + str(sim_score_maintenant))