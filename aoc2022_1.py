# aoc une jour
# "ubilal"
# ok lol

elves_inventoire = []
J_maintenant = 0

with open("./aoc2022_1.txt") as f:

    for line in f:
        # si il y a une item dans le ligne
        if(line.strip()):
            J_maintenant += int(line.strip())
        else:
            # si il n'y a pas une numero
            # plus le numero
            elves_inventoire.append(J_maintenant)
            # changer J_maintenant a 0
            J_maintenant = 0
    
    grande = 0
    i = 1
    # for J in range(len(elves_inventoire)):
    while i < len(elves_inventoire):
        # this is a certified java coder moment
        if elves_inventoire[i] > grande:
            grande = elves_inventoire[i]
        i+=1

print(elves_inventoire)
print(grande)
# print(str(sum(sorted(elves_inventoire[-3:]))))