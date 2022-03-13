import turtle
from turtle import Turtle, Screen
import random

alice_turtle = Turtle()
alice_turtle.shape("turtle")
turtle.colormode(255)

# Draw dashed line
for _ in range(9):
    alice_turtle.forward(10)
    alice_turtle.penup()
    alice_turtle.forward(10)
    alice_turtle.pendown()


# Draw continuous shapes

def draw_shape(sides):
    for _ in range(sides):
        alice_turtle.forward(100)
        alice_turtle.left(calculate_angle(sides))


def calculate_angle(sides):
    return 360 / sides


shapes = {
    "triangle": 3,
    "square": 4,
    "pentagon": 5,
    "hexagon": 6,
    "heptagon": 7,
    "octagon": 8,
    "nonagon": 9,
    "decagon": 10

}


def continuous_shapes():
    for shape in shapes:
        draw_shape(shapes[shape])


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def random_walk():
    directions = [0, 90, 180, 270]
    alice_turtle.pensize(15)
    alice_turtle.speed(10)
    for _ in range(200):
        alice_turtle.pencolor(random_color())
        alice_turtle.forward(30)
        alice_turtle.setheading(random.choice(directions))


def draw_circle():
    alice_turtle.speed(0)
    for _ in range(72):
        alice_turtle.pencolor(random_color())
        alice_turtle.circle(100)
        current_heading = alice_turtle.heading()
        alice_turtle.setheading(current_heading + 5)


#continuous_shapes()
#draw_circle()
#random_walk()
screen = Screen()
screen.exitonclick()
