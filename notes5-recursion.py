# We are going to draw trees
import turtle
import random

t = turtle.Turtle()
wn = turtle.Screen()
wn.bgcolor("white")


def draw_tree(level: int, branch_length: float):
    """A recursive funtion to draw trees
    Level - thee levels of branches
    brach_length - length of brach to draw
    """
    # Base case is when level is 0
    if level == 0:
        # Create a leaf
        t.color("darkgreen")
        t.stamp()
        t.color("brown")
    # For all other levels
    else:
        # 1. Go forward brach_length pixels
        t.forward(branch_length)
        # 2. Turn to the left and draw a -1 tree
        t.left(59)
        draw_tree(level - 1, branch_length * 0.8)
        # 3. Turn to the right and draw a -1 level tree
        t.right(118)
        draw_tree(level - 1, branch_length * 0.8)
        # 4. Go back to where we started
        t.left(59)
        t.backward(branch_length)


def draw_beautiful_tree(level: int, branch_length: float):
    """A recursive funtion to draw trees
    Level - thee levels of branches
    brach_length - length of brach to draw
    """
    # Base case is when level is 0
    if level == 0:
        # Create a leaf
        t.color(random.choice(["green", "yellowgreen", "gold", "orange", "red"]))
        t.stamp()
        t.color("saddlebrown")
    # For all other levels
    else:
        # 1. Go forward brach_length pixels
        # t.forward(branch_length)
        # 2. Turn to the left and draw a -1 tree
        # angle = random.randint(15, 50)

        # t.left(angle)
        # t.color(random.choice(["green", "yellowgreen", "gold", "orange", "red"]))
        # draw_beautiful_tree(level - 1, branch_length * random.uniform(0.6, 0.8))
        # # 3. Turn to the right and draw a -1 level tree
        # braches = random.randint(1, 4)

        t.forward(branch_length)

        # Main left branch
        angle_left = random.randint(15, 40)
        t.left(angle_left)
        draw_beautiful_tree(level - 1, branch_length * random.uniform(0.6, 0.8))
        t.right(angle_left)

        # Main right branch
        angle_right = random.randint(15, 40)
        t.right(angle_right)
        draw_beautiful_tree(level - 1, branch_length * random.uniform(0.6, 0.8))
        t.left(angle_right)

        # Extra branches
        extra_branches = random.randint(0, 3)
        for _ in range(extra_branches):
            random_angle = random.randint(-37, 37)
            t.left(random_angle)
            draw_beautiful_tree(level - 1, branch_length * random.uniform(0.5, 0.8))
            t.right(random_angle)

        # 4. Go back to where we started

        t.backward(branch_length)


# Set up the turtle
# point the turtle up
# Set turtle's colour to brown
# Set the turtle's ize to 5
# Set the turtlle's ahpe to turtle
# Move the turtle lower
t.left(90)
t.color("brown")
t.pensize(5)
t.shape("turtle")
t.penup()
t.goto(0, -250)
t.speed(0)
t.pd()

draw_beautiful_tree(5, 100)

wn.exitonclick()
