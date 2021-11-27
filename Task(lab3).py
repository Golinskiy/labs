from PIL import Image, ImageColor
from PIL import ImageDraw
from math import *


CONST_A = radians(-80)


file = open("DS7.txt", "r")

image = Image.new("RGB", (960, 960))
draw = ImageDraw.Draw(image)

for str in file:
    str = str[:-1].split(" ")
    str[0] = int(str[0]) - 480
    str[1] = int(str[1]) - 480
    coords = [str[0] * cos(CONST_A) - str[1] * sin(CONST_A) + 480, str[0] * sin(CONST_A) + str[1] * cos(CONST_A) + 480]
    draw.point((int(coords[0]), int(coords[1])), fill=ImageColor.getrgb("blue"))

file.close()

image.save("result.png", "PNG")
