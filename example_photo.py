from PIL import Image
# ouvrir le photo

def pixele_a_nom(pixele: tuple) -> str:
    rouge, vert, bleu = pixele
    if rouge < 150 and bleu < 150 and vert > 150:
        return "vert"

with Image.open("./images/kid-green.jpg") as photo:
    bg_im = Image.open("./images/beach.jpg")

# # me donne sur guahce/droit pixele
#     pixele = photo.getpixel((0,0))
#     print(pixele)

#     mid_coord = photo.width // 2
#     print(mid_coord)
#     pixele = photo.getpixel((mid_coord, mid_coord))

# # commence a la sur et allais gauche a droite
# # faire variable au prendre dy et dx
    # photo_dx = photo.width
    # photo_dy = photo.height
    # for y in range(photo_dy):
    #     for x in range(photo_dx):
    #         # photocopier les information de cette pixele
    #         pixele = photo.getpixel((x, y))
    #         print(pixele)

    photo_dx = photo.width
    photo_dy = photo.height
    for y in range(photo_dy):
        for x in range(photo_dx):
            # photocopier les information de cette pixele
            pixele = photo.getpixel((x, y))
            if pixele_a_nom(pixele)  == "vert":
                bg_pixel = bg_im.getpixel((x, y))
                photo.putpixel((x, y), bg_pixel)  

    bg_im.close()
    photo.save("./images/output.jpg")