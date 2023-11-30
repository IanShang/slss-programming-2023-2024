# aoc une jour
# "ubilal"
# ok lol

elves_inventoire = []
J_maintenant = 0

with open("./aoc2022_1.txt") as f:

    for line in f:
        #si il y a une item dans le ligne
        if(line.strip()):
            J_maintenant += int(line.strip())
    
print(J_maintenant)