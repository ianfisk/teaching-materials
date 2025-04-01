# Drawing with Turtles Mini-Lab 🐢

In this lab you will explore
- Writing a computer programing using the Python programming language
- Using a Python Turtle to draw something
- Using some mathematical thinking to solve a problem
- Having fun with code!

## Explore Drawing with Turtles

**Load the website https://pythonandturtle.com/turtle/ and write a program that uses Turtles to draw some shapes!**

### Some ideas of what to draw

Polygons:
1. Triangle (done in class)
1. Square (done in class)
1. Pentagon: 5 sides
1. Hexagon: 6 sides
1. Heptagon: 7 sides
1. Octagon: 8 sides

Miscellaneous:
1. Draw a cat
1. Draw a dog
1. Draw any animal
1. Draw a face
1. Draw overlapping shapes (like some of the fancy star examples)
1. Write out some text


## Turtle cheatsheet

**All programs must have the line `import turtle` at the top, and end with the line `turtle.done()`. For example, here is the general structure:**

```python
import turtle

# WRITE YOUR CODE HERE

turtle.done()
```

### Initializing a turtle

```python
alex = turtle.Turtle('turtle')
```

### Moving the turtle

```python
alex.forward(100) # Move forward
alex.left(90) # Rotate left 90 degrees
alex.right(120) # Rotate right 120 degrees
```

### Change the turtle's color, speed, and pen size

```python
alex.color('red')
alex.speed(10)
alex.pensize(2)
```

### Picking up the turtle and moving it without leaving a mark

```python
alex.penup()
alex.goto(-80, 150)
```

### Turning and moving in a loop (doing something over, and over, and over...)

```python
for i in range(100):
    alex.forward(200)
    alex.right(161)
```




([full Python docs](https://docs.python.org/3/library/turtle.html))
