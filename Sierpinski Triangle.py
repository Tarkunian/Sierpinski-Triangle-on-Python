import turtle

myWindow = turtle.Screen()                      # create background
myWindow.bgcolor("white")                       # set background color to red
myWindow.setworldcoordinates(0, 1000, 1000, 0)  # changing coordinate system
myTurtle = turtle.Turtle()                      # init
myTurtle.speed(10)                              # speed = 1 to slow turtle down
myTurtle.color("red")                           # set color
myTurtle.shape("circle")                        # set shape to a turtle
myTurtle.shapesize(0.5, 0.5, 1)                 # resizing the turtle


def drawTriangle(x, y, length, turtle):
    """ Function for drawing a filled triangle
        x,y - coordinates of triangle's leftmost vertice
        length - triangle side's length
        turtle - turtle used
    """
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.fill(True)
    turtle.goto(x+length, y)
    turtle.goto(x+length/2, y-length)
    turtle.goto(x, y)
    turtle.fill(False)


def generateFractal(x, y, length, turtle, deg):
    """ Function for generating Sierpinski Triangle
        x,y - coordinates of triangle's leftmost vertice
        length - triangle side's length
        turtle - turtle used
        deg - degree of a fractal
    """
    if deg > 0:
        generateFractal(x+length/2, y, length/2, turtle, deg-1)
        generateFractal(x+length/4, y-length/2, length/2, turtle, deg-1)
        generateFractal(x, y, length/2, turtle, deg-1)
    if deg == 0:
        drawTriangle(x, y, length, turtle)

generateFractal(300, 1000, 500, myTurtle, 5)

myWindow.exitonclick()                          # exit on click
