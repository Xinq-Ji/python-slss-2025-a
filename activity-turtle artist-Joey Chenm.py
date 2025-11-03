# Turtle Artist
# Author: Joey Chen
# 28 October

import turtle
import math

# Setup
wn = turtle.Screen()
t = turtle.Turtle()
wn.bgcolor("white")

# Draw a black circle as the background
t.penup()
t.goto(0, -150)
t.pendown()
t.pensize(5)
t.color("black", "red")
t.begin_fill()
t.circle(150)
t.end_fill()


# Recursive ellipse
def draw_ellipse(angle: float, increase_rate: float, rotation: float = 0):
    """
    Draws one ellipse relative to a rotation angle (so they can face different directions).
    """
    # Horizontal and vertical radius
    a = 150
    b = 70

    # stop after full rotation
    if angle >= 360:
        return

    rad = math.radians(angle)
    rot = math.radians(rotation)

    # rotated ellipse formula
    x = a * math.cos(rad) * math.cos(rot) - b * math.sin(rad) * math.sin(rot)
    y = a * math.cos(rad) * math.sin(rot) + b * math.sin(rad) * math.cos(rot)

    # Move turtle
    if angle == 0:
        t.penup()
        t.goto(x, y)
        t.pendown()
    else:
        t.goto(x, y)

    # recursive call
    draw_ellipse(angle + increase_rate, increase_rate, rotation)


# Draw multiple ellipses
def draw_eyes(num_ellipses: int, rotated_angle: float):
    for i in range(num_ellipses):
        rotation = i * rotated_angle
        draw_ellipse(0, 2, rotation)


# Main
t.speed(0)
t.color("black")
t.penup()
t.goto(0, 0)
t.pendown()

draw_eyes(2, 120)  # Try 4 ellipses, each rotated 45°

wn.exitonclick()
