from turtle import *
from colorsys import *

tracer(50)
bgcolor("black")
pensize(1)
h = 0

for i in range(990):
    color(hsv_to_rgb(h, 1, 1))
    h = (h + 0.005) % 1
    for j in range(6):
        forward(50 + i / 10)
        right(60)
    right(1)
done()