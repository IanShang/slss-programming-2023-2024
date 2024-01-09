# yes
# no
# mayhaps

# visitez tous pixele
# est ce-que cette piexele rouge?

rouge_pixeles = []

jelly_bean_img = Image.open("./Images/Jelly Beans.jpg")

for y in range(jelly_bean_img.height()):
    for x in range(jelly_bean_img.width()):
        pixele_maintenant = jelly_bean_img.getpixel((x, y))

        if colour_helper.pixel_to_name(pixele_maintenant) == "red":
            rouge_pixeles.append((x, y))

print(rouge_pixeles)