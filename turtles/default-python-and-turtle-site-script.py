import turtle

# Turtle script example
alex = turtle.Turtle('turtle')

alex.width(5)
alex.color('red')

for _ in range(4):
    alex.forward(100)
    alex.left(90)

alex.penup()
alex.goto(-80, 150)
alex.color('green')

message = "Welcome to Python and Turtle!"
alex.write(message, font=("Arial", 16, "normal"))
print(message)

turtle.done()
# - OR -
# input("Press enter to exit...")
