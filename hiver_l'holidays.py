# hiver weekend passe
# ian innit
# 1/24

# faire une functione que prends une parameter (str)
# retourne une summary d'event a weekend passe

import random

bonne = ["didnt get shanked in the uk", "went to museum", "chem review for real", "ireland looked good", "nourriture est interessant"]
mauvais = ["first uk hotel kinda very dirty", "tired ahh", "forgor to bring adaptor bc european outlets r cringe"]

def hiver_passe(event: str) -> str:
    if event == "bonne":
        return bonne[random.randint(0, len(bonne)-1)]
    elif event == "mauvais":
        return mauvais[random.randint(0, len(mauvais)-1)]
    
print(hiver_passe("bonne"))
print(hiver_passe("mauvais"))