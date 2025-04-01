import turtle

alex = turtle.Turtle('turtle')
alex.speed(10)

# I
alex.right(90)
alex.forward(20)

# Space
alex.color('red')
alex.left(90)
alex.forward(10)

# A
alex.color('black')
alex.left(60)
alex.forward(20)
alex.right(120)
alex.forward(20)

# Space
alex.color('red')
alex.left(60)
alex.forward(10)

# N
alex.color('black')
alex.left(90)
alex.forward(20)
alex.right(150)
alex.forward(23)
alex.left(150)
alex.forward(20)


alex.hideturtle()
turtle.done()
