import turtle
import colorsys
from tkinter import Button
import math

screen = turtle.Screen()
screen.bgcolor("black")
screen.tracer(0)

root = screen.getcanvas().winfo_toplevel()
start_button = Button(root, text="start Drawing")
start_button.pack(side="bottom")

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.pensize(2)
t.penup()
t.goto(0, -20)
t.pencolor('white')
t.write("Press 'Start Drawing' to begin", align="center", font=("Arial", 24, "normal"))
screen.update()

def draw_heart():
    start_button.config(state="disabled")
    t.clear()
    h = 0.0
    for i in range (1, 100):
        scale = i * 0.4

        first_point = True
        for a in range(360) :
            angle = math.radians(a)
            x = 16 * math.sin(angle) ** 3
            y = ( 13 * math.cos(angle) - 5 * math.cos(2 * angle)- 2 * math.cos(3 * angle) - math.cos(4 * angle))
            r, g, b = colorsys.hsv_to_rgb(h, 1, 1)
            t.pencolor(r, g, b)
            if first_point :
                t.penup()
                t.goto(x *scale, y * scale)
                t.pendown()
                first_point = False 
            else:
                t.goto(x *scale, y * scale)
        h += 0.015
        screen.update()

start_button.config(command=draw_heart)
turtle.done()



