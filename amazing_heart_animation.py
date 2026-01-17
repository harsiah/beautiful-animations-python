import turtle
import time
import math

screen = turtle.Screen()
screen.bgcolor("black")

heart = turtle.Turtle()
heart.hideturtle()
heart.speed(0)
heart.color("red")
heart.width(2)

def draw_heart(scale):
    heart.penup()
    heart.goto(0, -40 * scale)
    heart.pendown()
    heart.begin_fill()

    heart.setheading(140)
    heart.forward(113 * scale)

    for _ in range(200):
        heart.right(1)
        heart.forward(1 * scale)

    heart.setheading(60)
    for _ in range(200):
        heart.right(1)
        heart.forward(1 * scale)

    heart.forward(113 * scale)
    heart.end_fill()

# Animation loop
while True:
    heart.clear()
    draw_heart(1.0)
    time.sleep(0.15)

    heart.clear()
    draw_heart(1.1)
    time.sleep(0.15)