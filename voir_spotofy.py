# ooooof
# Ian for real
# 38473847328432

# voir pour songs by drake

import csv

# drake_songs = []

# with open("./spotify.csv") as f:

#     f.readline()

#     for line in f:

#         chanson_info_maintenant = line.strip().split(",")

#         artist = chanson_info_maintenant[len(chanson_info_maintenant) - 1]

#         if artist == "Drake":

#             drake_songs.append(chanson_info_maintenant[len(chanson_info_maintenant) - 2])

# print(drake_songs)

# faires une function que trouver tout les chanson by une artist

#-------------------------------------------------------------------------------------------------------- ian style coding fr

def trouver_tout_chanson(artist: str) -> list:
    
    # trouve une liste de data et retournes tous le chansons from une artist

    # Returne list de chanson trouve

    with open("./spotify.csv") as f:
        # utilise linear trouve
        # faire une csv lirer obj
        lirer_de_cvs = csv.DictReader(f)

        # prends tout le chanson
        chansons = []

        i = 0

        for ligne in lirer_de_cvs:
            if i == 0:
                i += 1
            else:
                if artist.lower() in ligne["artist"].lower():
                    chansons.append(
                        (ligne["artist"])
                    )
                i += 1

        return chansons

# no wilson songs 😔
wilson_songs = trouver_tout_chanson("wilson")