# parents de ben sullivan bot
# ian shanks
# 19/11/2025

activites = ["faires les devoirs", "mange petit dejeuner", "cuisine dejeuner", "allais a l'ecole", "ching cheng han ji"]
oui_counter = 0
for activite in activites:
    ans = input("as tu " + activite + "? ").lower().strip(".,?!")
    if ans == "oui":
        oui_counter += 1
if oui_counter <5:
    print("il y a une grande problems")
else: print("okay")