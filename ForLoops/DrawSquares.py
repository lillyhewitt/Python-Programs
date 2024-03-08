import random
import turtle
wn = turtle.Screen()
wn.bgcolor("blue")
bot = turtle.Turtle()
bot.shape("triangle")

#2.1.1 DrawSquare
def drawSquare(myTurtle, squareSize):
    for i in range(4):
        myTurtle.forward(squareSize)
        myTurtle.left(90)
      
drawSquare(bot, 50)

#2.1.2 Drawing a Row of Squares
def drawRow(myTurtle, length, squareSize):
    for i in range(length):
        drawSquare(myTurtle, squareSize)
        myTurtle.forward(squareSize)
      
drawRow(bot, 5, 50)

#2.1.3 Drawing a Grid
def drawGrid(myTurtle, size, squareSize):
    for i in range(size):
        myTurtle.right(90)
        myTurtle.forward(squareSize)
        myTurtle.left(90)
        drawRow(myTurtle, size, squareSize)
        myTurtle.left(180)
        myTurtle.forward(250)
        myTurtle.left(180)
      
drawGrid(bot, 5, 50)

#2.1.4 Drawing a Stair of Squares
def drawSquareStairs(myTurtle, height, squareSize):
    for i in range(1, height+1):
        myTurtle.right(180)
        myTurtle.forward(squareSize * (i-1))
        myTurtle.left(90)
        myTurtle.forward(squareSize)
        myTurtle.left(90)
        drawRow(myTurtle, i, squareSize)
      
drawSquareStairs(bot, 5, 50)

#2.2.1 N Sided Polygon
colors = ["purple", "cyan", "green", "pink"]
def drawNgon(myTurtle, numSides, sideLength):
    angle = 360 / numSides
    for i in range(numSides):
        myTurtle.color(random.choice(colors))
        myTurtle.forward(sideLength)
        myTurtle.left(angle)
      
drawNgon(bot, 6, 100)

#2.2.2 Super Spiral
def drawNgonSpiral(myTurtle, numSides, sideLength, numShapes):
    myTurtle.speed(15)
    angle = 720 / numShapes
    for i in range(numShapes):
        drawNgon(myTurtle, numSides, sideLength)
        myTurtle.left(angle)
      
drawNgonSpiral(bot, 6, 100, 35)
