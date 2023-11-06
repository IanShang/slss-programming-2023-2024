# combien de continents as tu allais
# Airbus pilot ian shanks
# 4/11/2023

travelled = 0
Conts = ["NA", "SA", "EU", "AS", "AF", "Arctic", "Antarctica"]
for cont in Conts:
    q = input("allais tu " + cont + ": ").strip(",.?!").lower()
    if q == "yes":
        travelled +=1
print("tu es allais " + str(travelled) + "/7 continents")