import turtle

# https://allinpython.com/top-5-awesome-python-turtle-graphics/

def draw_attractive_design1():
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    pen = turtle.Turtle()
    pen.speed(10)
    turtle.bgcolor("black")
    pen.pensize(2)

    for i in range(180):
        pen.color(colors[i % 6])
        pen.forward(200)
        pen.right(61)
        pen.forward(100)
        pen.right(120)
        pen.forward(100)
        pen.right(61)
        pen.forward(200)
        pen.right(181)

    pen.hideturtle()

def draw_attractive_design2():
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    pen = turtle.Turtle()
    pen.speed(10)
    turtle.bgcolor("black")
    pen.pensize(2)

    initial_size = 30

    for i in range(200):
        pen.color(colors[i % 6])
        pen.forward(initial_size + i)
        pen.left(59)

    pen.hideturtle()

def draw_attractive_design3():
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    pen = turtle.Turtle()
    pen.speed(10)
    turtle.bgcolor("black")
    pen.pensize(2)

    for i in range(180):
        pen.color(colors[i % 6])
        pen.forward(100)
        pen.left(59)
        pen.forward(50)
        pen.left(91)
        pen.forward(50)
        pen.left(59)
        pen.forward(100)
        pen.right(121)

    pen.hideturtle()

def draw_attractive_design4():
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    pen = turtle.Turtle()
    pen.speed(10)
    turtle.bgcolor("black")
    pen.pensize(2)

    size = 20

    for i in range(300):
        pen.color(colors[i % 6])
        pen.forward(size)
        pen.left(59)
        pen.forward(size)
        pen.left(59)
        pen.forward(size)
        pen.left(59)
        pen.forward(size)
        pen.left(121)
        size += 2

    pen.hideturtle()

def draw_attractive_design5():
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    pen = turtle.Turtle()
    pen.speed(10)
    turtle.bgcolor("black")
    pen.pensize(2)

    initial_size = 100

    for i in range(300):
        pen.color(colors[i % 6])
        pen.forward(initial_size + i)
        pen.left(150)

    pen.hideturtle()

def draw_attractive_design6():
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    pen = turtle.Turtle()
    pen.speed(10)
    turtle.bgcolor("black")
    pen.pensize(2)

    for i in range(35):
        pen.color(colors[i % 6])
        pen.circle(100)
        pen.left(25)

    pen.hideturtle()

draw_attractive_design6()

turtle.done()
