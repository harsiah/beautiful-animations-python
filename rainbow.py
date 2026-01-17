import turtle as t
import colorsys
t.bgcolor("black")
t.speed(0)
t.width(2)
t.hideturtle()
h=0
for i in range(360):
    c = colorsys.hsv_to_rgb(h, 1, 1)
    t.pencolor(c)
    t.circle(150)
    t.right(10)
    h+=0.01
t.done()