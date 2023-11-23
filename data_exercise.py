# File Exercises
# Author:
#

"""Instructions:

Put this file in your programming folder.
Download the data-example.csv file and put it in this same folder.
For each problem, design a solution.
Each part builds on the previous step, so don't skip any.
You can refer to the work that we did last day for any hints.
Do not use any generative AI for the solutions."""

# Since our file has some symbols in it, this is the most
# effective way at opening up the file.

with open("./data_example.csv", encoding="utf-8") as f:
    f.readline()

# Note that I've set the encoding parameter to "utf-8"

# --- Problems


# Problem 1:
# Open the file and print the contents of the second line in the file.

    print(f.readline())

# Problem 2:
# Good! Now that you've done that, open the file, and print out every line of data.

    # for line in f:
    #     print(f.readline().strip())

# Problem 3:
# If you've made it this far, well done. Next task:
# Convert that line of data into a list.

    # for line in f:
    #     activite = line.strip().split(",")
    #     print(activite)

# Problem 4:
# Give yourself a pat on the back.
# See if you can count how many people like "Chicken Adobo" as their
# favourite food.

    # aime_chicken_adobo = 0
    # for line in f:
    #     activite = line.strip().split(",")
    #     for info in activite:
    #         if info == "Chicken Adobo":
    #             aime_chicken_adobo +=1
    # print("il y a " + str(aime_chicken_adobo) + " personne qui aimes chicken adobo")

# Problem 5:
# You should have gotten four people for the last problem. If not,
# see if why your code doesn't work.
# Else, you can move on to this part, which is, find out how many
# people have the first letter of their first name start with "A".

    # nom_commence_avec_a = 0
    # for line in f:
    #     activite = line.strip().split(",")
    #     #  si le character premiere est a
    #     if activite[0][0] == "A":
    #         nom_commence_avec_a +=1
    # print("il y a " + str(nom_commence_avec_a) + " qui a un nom qui commence avec un a")

# Problem 6:
# 19 people! Excellent. How many people come from Guangzhou?

    # nom_commence_avec_a = 0
    # for line in f:
    #     activite = line.strip().split(",")
    #     #  si la place est guangzhou #ching cheng han ji
    #     if activite[4] == "Guangzhou":
    #         nom_commence_avec_a +=1
    # print("il y a " + str(nom_commence_avec_a) + " personnes qui habiter dans Guangzhou")

# Problem 7:
# Just one is from Guangzhou! Alright, last one. How many people have a credit card
# number that is even. There are a couple of ways to solve this.
# You can either do this with the string or with the int.

    # carde_divisible_by_2 = 0
    # for line in f:
    #     activite = line.strip().split(",")
    #     if int(activite[3]) % 2 == 0:
    #         carde_divisible_by_2 +=1
    # print("j'ai le credit card numero de " + str(carde_divisible_by_2) + " personnes")

# Problem 8:
# Sorry, no answer for the above one. This one is a challenge question.
# Can you design a way to find the most popular food?

    carde_divisible_by_2 = 0
    for line in f:
        activite = line.strip().split(",")
        for nourriture in activite:
            if int(activite[3]) % 2 == 0:
                carde_divisible_by_2 +=1
    print("j'ai le credit card numero de " + str(carde_divisible_by_2) + " personnes")