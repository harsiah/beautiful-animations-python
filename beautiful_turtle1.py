import turtle
import colorsys
t = turtle.Turtle()
t.speed(0)
turtle.bgcolor('black')
h = 0
for i in range(1000):
    c = colorsys.hsv_to_rgb(h, 1, 1)
    t.color(c)
    t.forward(i)
    t.left(91)
    h+= 0.005
turtle.done()
# file change