import turtle

alex = turtle.Turtle('turtle')

# Square
alex.right(90)
alex.forward(100)

alex.color('red')
alex.right(90)
alex.forward(100)

alex.color('blue')
alex.right(90)
alex.forward(100)

alex.color('green')
alex.right(90)
alex.forward(100)

alex.hideturtle()

# Equilateral triangle
jeff = turtle.Turtle('circle')
jeff.right(90)
jeff.forward(100)
jeff.left(120)
jeff.forward(100)
jeff.left(120)
jeff.forward(100)

jeff.hideturtle()

# Right Triangle
marv = turtle.Turtle('arrow')
marv.right(90)
marv.forward(100)

marv.left(90)
marv.forward(100)

marv.left(135)
marv.forward(141)

marv.hideturtle()


turtle.done()
