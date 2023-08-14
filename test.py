from PIL import Image, ImageDraw
import random

# read the image
# im = Image.open("white.png")
im = Image.new('RGB', (1000, 1000), (255, 255, 255))
# im.putpixel((100, 100), (0, 0, 0))
draw = ImageDraw.Draw(im)


def coordinate(x, y):
    x = 500 + x
    y = 500 - y

    return x, y


def point(c, color=(0, 0, 0), dot_rad=6):
    draw.ellipse((c[0]-dot_rad, c[1]-dot_rad, c[0]+dot_rad, c[1]+dot_rad), fill=color)


def shape_c(coo, rad):
    for c, v in coo:
        point(coordinate(c, v), dot_rad=rad)

#
# def midpoint(p1, p2):
#     return (p1[0]+p2[0])/2, (p1[1]+p2[1])/2

def midpoint(p1, p2):
    return p1[0] +(p2[0]-p1[0]) *2/3, p1[1] +(p2[1]-p1[1]) *2/3


"""
point(coordinate(0,0))
point(coordinate(0, 30))
point(coordinate(30, 30),(255,0,0))
point(coordinate(-50,-100),(0,0,255))

point(coordinate(-50,-200),(0,0,255))
point(coordinate(-50,-50),(0,0,255))
"""
m = 400
pentagon = [(0*m, 1*m), (0.951*m, 0.309*m), (0.587*m, -0.809*m), (-0.587*m, -0.809*m), (-0.951*m, 0.309*m)]

points = []
ress = 3
points.append(midpoint(pentagon[random.randint(0, 4)], pentagon[0]))
print(points)
for i in range(1, ress):
    points.append(midpoint(pentagon[random.randint(0, 4)], points[i-1]))


shape_c(points, 2)
shape_c(pentagon, 2)
# for c, v in pentagon:
#    point(coordinate(c, v))

# show image
im.show()
