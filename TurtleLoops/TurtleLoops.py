#Lilly Hewitt
import turtle
wn = turtle.Screen()
wn.bgcolor("white")
bot = turtle.Turtle()
bot.shape("triangle")
bot.speed(5)

#Turtle Olympics
def drawLogo():
    bot.up()
    bot.goto(-190,40)
    bot.down()
    count = 0;
    for j in range(3):
        if count == 0:
            bot.color("blue")
        if count == 1:
            bot.color("black")
        if count == 2:
            bot.color("red")
        bot.circle(150)
        bot.up()
        bot.forward(205)
        bot.down()
        count += 1
    bot.up()
    bot.goto(-125,-150)
    bot.down()
    count = 0
    for i in range(2):
        if count == 0:
            bot.color("yellow")
        if count == 1:
            bot.color("green")
        bot.circle(155)
        bot.up()
        bot.forward(245)
        bot.down()
        count += 1
      
drawLogo()
#Source: https://www.w3schools.com/python/python_conditions.asp 

#Turtle Clock
bot.shape("turtle")
bot.up()
bot.goto(250,0)
bot.down

def drawTurtle():
    bot.up()
    bot.forward(100)
    bot.down()
    bot.forward(50)
    bot.stamp()
    bot.up()
    bot.goto(250,0)
    bot.down()

def drawClock():
    for i in range(12):
        drawTurtle()
        bot.right(30)
      
drawClock()

#Initials
bot.shape("square")
bot.up()
bot.goto(-400,350)
bot.down()
bot.right(90)
bot.forward(600)
bot.left(90)
bot.forward(300)
bot.up()
bot.forward(175)
bot.down()
bot.left(90)
bot.forward(600)
bot.left(180)
bot.forward(300)
bot.left(90)
bot.forward(300)
bot.left(90)
bot.forward(300)
bot.left(180)
bot.forward(600)

#Draw Shape
n = int(input("Enter amount of sides: "))
angle = 360 / n
bot.goto(100,20)
for i in range(n):
    bot.down()
    bot.forward(150)
    bot.left(angle)

#TriForce
bot.up()
bot.goto(-100,20)
bot.down()
for i in range(2):
    for i in range(3):
        bot.forward(150)
        bot.left(120)
    bot.forward(150)
bot.left(120)
bot.forward(150)
for i in range(3):
    bot.forward(150)
    bot.left(120)
