import turtle

# https://pythonandturtle.com/turtle/

alex = turtle.Turtle()
alex.speed(10)

# Star showing it draws over itself:
for i in range(18):
    alex.forward(200)
    alex.right(160)

# Cooler star
for i in range(100):
    alex.forward(200)
    alex.right(161)

# Always need to end program with the following line:
turtle.done()
