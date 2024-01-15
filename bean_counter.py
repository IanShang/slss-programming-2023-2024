# yes
# no
# mayhaps

# visitez tous pixele
# est ce-que cette piexele rouge?

from PIL import Image

import aide_de_color

PIXELE_ROUGE = [255, 0, 0]
PIXELE_VERT = [0, 255, 0]
PIXELE_BLEU = [0, 0, 255]

jelly_bean_img = Image.open("./Images/Jelly Beans.jpg")

pixeles_rouge = []

# Visit every pixel in the image
for y in range(jelly_bean_img.height):
    for x in range(jelly_bean_img.width):
        # Get the pixel information
        pixele_maintenant = jelly_bean_img.getpixel((x, y))

        # If this pixel is red
        if aide_de_color.pixel_to_name(pixele_maintenant) == "rouge":
            # Store its location somewhere
            pixeles_rouge.append((x, y))

orig_photo_h = jelly_bean_img.height()
orig_photo_l = jelly_bean_img.width()
# faire carte que avoir tous pixele rouge
# pour le location de tous les pixeles
carte_de_pixeles_rouge = Image.new("RGB", (orig_photo_l, orig_photo_h))
for pixel_loc in pixeles_rouge:
    carte_de_pixeles_rouge.putpixel(pixel_loc, PIXELE_ROUGE)

carte_de_pixeles_rouge.save("carte_de_pixeles_rouge.jpg")

# Count all the locations of red pixels
mathe_rouge_pixeles = len(pixeles_rouge)
tous_le_pixeles = jelly_bean_img.width * jelly_bean_img.height

# Divide by the total pixels in the image
percent_de_rouge_pixeles = mathe_rouge_pixeles / tous_le_pixeles * 100

# Generate the report
print(f"Red Jelly Beans: {round(percent_de_rouge_pixeles, 2)}%")

jelly_bean_img.close()