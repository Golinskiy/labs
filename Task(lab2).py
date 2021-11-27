from PIL import Image, ImageColor
from PIL import ImageDraw


file = open("DS7.txt", "r")

image = Image.new("RGB", (540, 960))
draw = ImageDraw.Draw(image)

for coords in file:
    coords = coords[:-1].split(" ")
    draw.point((int(coords[0]), int(coords[1])), fill=ImageColor.getrgb("blue"))
file.close()

image.save("result.png", "PNG")
