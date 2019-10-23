import math
from PIL import Image

def distance(color_1, color_2):
    red_diff = math.pow((color_1[0] - color_2[0]), 2)
    green_diff = math.pow((color_1[1] - color_2[1]), 2)
    blue_diff = math.pow((color_1[2] - color_2[2]), 2)
    return math.sqrt(red_diff + green_diff + blue_diff)

def chromakey(source, bg):
    for x in range(source.width):
        for y in range(source.height):

            cur_pixel = source.getpixel((x,y))
            green = (94, 255, 3)
        print(distance(cur_pixel, green)
        # if (distance(cur_pixel, green) < 250):
        #     source.putpixel((x,y), bg.getpixel((x,y)))
#
#     source.save("images/chromakeyed.png")
#
#
# source = Image.open("images/t1.png")
# bg = Image.open("images/wh.png")
chromakey(source, bg)

#1280 by 780
