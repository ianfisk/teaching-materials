from turtle import *

# Run this program here: https://pythonandturtle.com/turtle/
space = Screen()
alex = Turtle()

# Possible student code
for i in range(5):
    alex.forward(50)
    alex.right(72)

for j in range(6):
    alex.forward(50)
    alex.right(60)
    j += 1
# ...

# Generalized solution (no input checks)
def draw_shape(turt, num_sides, side_length = 50):
    # What is missing right here?
    turn_angle = 360 / num_sides

    for i in range(num_sides):
        turt.forward(side_length)
        turt.right(turn_angle)


for k in range(3, 9):
    draw_shape(alex, k)

num_sides = int(input('enter the number of sides for your polygon: '))
draw_shape(alex, num_sides)
