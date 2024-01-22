# ooooof
# Ian for real
# 38473847328432

# voir pour songs by drake

import csv

drake_songs = []

with open("./spotify.csv") as f:

    f.readline()

    for line in f:

        chanson_info_maintenant = line.strip().split(",")

        artist = chanson_info_maintenant[len(chanson_info_maintenant) - 1]

        if artist == "Drake":

            drake_songs.append(chanson_info_maintenant[len(chanson_info_maintenant) - 2])

print(drake_songs)