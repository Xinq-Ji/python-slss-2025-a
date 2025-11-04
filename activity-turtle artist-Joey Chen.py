# Turtle Artist - Perfect Tangent Ellipses (continuous)
# Author:
# 28 October

import random
import turtle
import math

# Setup
wn = turtle.Screen()
wn.bgcolor("white")

t = turtle.Turtle()
t.speed(0)
t.pensize(6)

# Circle parameters
# R = radius
R = 180
t.penup()
t.goto(0, -R)
t.pendown()
t.color("black", "#F72C25")
t.begin_fill()
t.circle(R)
t.end_fill()
t.color("black")
t.penup()
t.goto(0, 0)
t.pendown()


# A recursive function to draw a perfect ellipses
# angle --> how smooth the ellipses is
# increase_rate --> finish drawing the ellipses
# rotation --> the next ellipse
# a , b --> vertices
#
def draw_ellipse(angle: float, increase_rate: float, rotation: float, a, b, start=None):
    # Convert to radians
    rad = math.radians(angle)
    rot = math.radians(rotation)

    # Parametric rotated ellipse
    x = a * math.cos(rad) * math.cos(rot) - b * math.sin(rad) * math.sin(rot)
    y = a * math.cos(rad) * math.sin(rot) + b * math.sin(rad) * math.cos(rot)

    color = ["#FFFD77", "#26C485", "#F7F06D", "#F26419", "#8DE969", "#B1CF5F"]
    # Record the start point
    if start is None:
        start = (x, y)
        t.penup()
        t.color(random.choice(color))
        t.goto(start)
        t.pendown()
    else:
        t.goto(x, y)

    # Stop when finished one full loop
    if angle >= 360:
        # close shape exactly
        t.goto(start)
        return

    # Recursive step
    draw_ellipse(angle + increase_rate, increase_rate, rotation, a, b, start)


# Call the recursive function to draw multiple ellipses
def draw_tangent_ellipses():
    t.pensize(4)
    num_ellipses = 3
    rotated_angle = 120
    # first ellipse vertical
    start_rotation = 90

    # Set up the vertices
    a = R * 0.55
    b = R

    for i in range(num_ellipses):
        rotation = start_rotation + i * rotated_angle
        draw_ellipse(0, 2, rotation, a, b)

    return a


# Main
inner_radius = draw_tangent_ellipses()

# Draw the eyeball --> Two Circle
t.pu()
t.goto(0, -inner_radius)
t.setheading(0)
t.pd()
t.pensize(11)
t.color("black", "black")
t.circle(inner_radius)

t.pu()
t.goto(0, -(inner_radius / 2.5))
t.setheading(0)
t.begin_fill()
t.color("black", "black")
t.circle(inner_radius / 2.5)
t.end_fill()

# End
t.hideturtle()
wn.exitonclick()
