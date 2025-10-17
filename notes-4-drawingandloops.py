import turtle
import random

wn = turtle.Screen()  # Set up the window and its attributes
wn.bgcolor("light green")

# TMNT - turtles
mikey = turtle.Turtle()
# size
mikey.turtlesize(1)
# color
mikey.color("orange")
# shape
# mikey.shape("turtle")

mikey.speed(5)

# mikey.forward(500)
# mikey.left(90)

# mikey.color("lightblue")
# mikey.pencolor("lightblue")
# mikey.fillcolor("lightblue")
# mikey.turtlesize(1)
# mikey.width(5)
# mikey.seth(0)
# mikey.goto(0, 0)

# mikey.begin_fill()
# mikey.circle(100)
# mikey.end_fill()
# mikey.penup()
# mikey.goto(0, 200)
# mikey.pd()
# mikey.begin_fill()
# mikey.circle(80)
# mikey.end_fill()
# mikey.penup()
# mikey.goto(0, 360)
# mikey.pd()
# mikey.begin_fill()
# mikey.circle(60)
# mikey.end_fill()

# Make sure that turtlee is pointing east
# cahnge the cookie color
mikey.color("brown")
# draw a circle
# put a chocolate chip on the top leeft side
mikey.pu()
mikey.goto(-5, -30)
mikey.pendown()
mikey.circle(30)

# chocolate chip on the top left side
mikey.pu()
mikey.goto(-10, 10)
mikey.stamp()
# chocolate chip on the top right
mikey.goto(10, 10)
mikey.stamp()
# choco chip go to the bottom right
mikey.goto(10, -10)
mikey.stamp()
# bottom left
mikey.goto(-10, -10)
mikey.stamp()
# choco in the middle
mikey.goto(0, 0)
mikey.stamp()


# Create a function that mkaes a cookie
# at (x, y)
def make_cookie(x: int, y: int):
    # Make sure that turtlee is pointing east
    mikey.seth(0)
    mikey.speed(0)
    # cahnge the cookie color
    mikey.color("brown")
    # draw a circle
    mikey.goto(-5 + x, -30 + y)
    # put a chocolate chip on the top leeft side
    mikey.pu()
    mikey.goto(-5 + x, -30 + y)
    mikey.pd()
    mikey.circle(30)

    # chocolate chip on the top left side
    mikey.pu()
    mikey.goto(-10 + x, 10 + y)
    mikey.stamp()
    # chocolate chip on the top right
    mikey.goto(10 + x, 10 + y)
    mikey.stamp()
    # choco chip go to the bottom right
    mikey.goto(10 + x, -10 + y)
    mikey.stamp()
    # bottom left
    mikey.goto(-10 + x, -10 + y)
    mikey.stamp()
    # choco in the middle
    mikey.goto(0 + x, 0 + y)
    mikey.stamp()


# make_cookie(0, 0)
# make_cookie(-150, -150)
# make_cookie(-150, 150)
# make_cookie(150, -150)
# make_cookie(150, 150)

# for i in range(0, 451, 50):
#     make_cookie(-i, i)
#     make_cookie(-i, -i)
#     make_cookie(i, -i)
#     make_cookie(i, i)

# Make cokies in random locations
# Make 1000 cookies

for i in range(1000):
    position = (random.randint(-450, 450), random.randint(-450, 450))
    make_cookie(*position)

wn.exitonclick()
