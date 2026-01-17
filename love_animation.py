import turtle
import time

t = turtle.Turtle()
t.speed(0)
t.width(3)

screen = turtle.Screen()
screen.bgcolor('black')

def draw_heart(color):
    t.color(color)
    t.begin_fill()
    t.left(140)
    t.forward(180)
    t.circle(-90, 200)
    t.left(120)
    t.circle(-90, 200)
    t.forward(180)
    t.end_fill()
    t.setheading(0)

colors = ['red', 'hotpink', 'magenta', 'purple', 'deeppink']

for c in colors:
        t.clear()
        t.penup()
        t.goto(0, -80)
        t.pendown()
        draw_heart(c)
        time.sleep(0.4)

t.penup()
t.goto(-230, -220)
t.color('white')
t.pendown()
t.write('i love you Zsolt', font=('Arial', 36, 'bold'))
                
t.hideturtle()
turtle.done()

            

               