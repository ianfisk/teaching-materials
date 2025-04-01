import turtle

# Turtle script example
t = turtle.Turtle('turtle')

t.width(5)

t.color('red')

for _ in range(4):
    t.forward(100)
    t.left(90)

t.penup()

t.goto(-80, 150)
t.color('green')

message = "Welcome to Python and Turtle!"

t.write(message, font=("Arial", 20, "normal"))

print(message)

turtle.done()
