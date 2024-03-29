# Colour Helper
# Author: Ubial
# 13 December 2023

PIXELE_NOIR = (0, 0, 0)
PIXELE_DARK_GRAY = (127, 127, 127)
PIXELE_LIGHT_GRAY = (128, 128, 128)
PIXELE_BLANC = (255, 255, 255)
PIXELE_ROUGE = (255, 0, 0)

def pixel_to_string(pixel: tuple) -> str:
    """Take a rgb 3-tuple and "interpret it"
    as a colour and return that colour's name

    Params:
        pixel - 3-tuple of (red, green, blue)

    Return:
        String representing the colour
    """
    r, g, b = pixel

    if g > 220 and r < 120 and b < 120:
        return "green"
    if g < 25 and b < 25 and r > 150:
        return "red"


print(pixel_to_string((160, 0, 4)))  # red
print(pixel_to_string(PIXELE_BLANC))


def is_light(pixel: tuple) -> bool:
    """Returns true if given pixel is "light"

    Params:
        pixel - 3-tuple of values red, green, blue

    Returns:
        True if pixel is light false if not
    """
    return pixel >= (128, 128, 128)


def pixel_to_grayscale(pixel: tuple) -> tuple:
    """Returns a grayscale version of the given pixel"""
    gray = int(pixel[0] * 0.3 + pixel[1] * 0.59 + pixel[2] * 0.11)

    return (gray, gray, gray)