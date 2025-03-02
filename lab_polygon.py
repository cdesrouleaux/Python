# COP2500 LAB - Christopher Desoruleaux

import turtle


def drawPolygon(theTortise, x, y, numSides, perimeter):

    theTortise.penup()
    theTortise.goto(x,y)
    theTortise.pendown()
    
    int_angles = (numSides - 2)* 180
    a1 = 180 - int_angles/numSides
    s1 = perimeter / numSides

    for i in range (numSides):
        theTortise.forward(s1)
        theTortise.right(a1)

        

    

# start of main

myScreen = turtle.getscreen()
tortoiseTurtle = turtle.Turtle()

x = int(input("Enter x coordinate:"))
y = int(input("Enter y coordinate:"))
sides = int(input("Enter number of sides:"))
rim = int(input("Enter perimenter:"))

drawPolygon(tortoiseTurtle, x, y, sides, rim)
