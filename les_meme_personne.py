# trouve si une personne aimes les meme films preferee
# ion shanks
# 9/11/2023

a_film_preferee = ["among us", "freddy fazbear? au au au", "bollywood", "ching cheng han ji opera"]
b_film_preferee = ["nerd emoji", "erm actually", "fixing good"]
match = 0
for film in a_film_preferee:
    if film in b_film_preferee:
        match +=1
print("tu et elle aimont " + str(match) + " meme film preferee")