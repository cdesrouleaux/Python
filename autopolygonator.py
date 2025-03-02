# COP2500 - Christopher Desrouleaux
# autopolygonator.py - This program uses the turtle library to draw a polygon 
# with any number of sides and lenght entered by the user.

import turtle

tortoise = turtle.getscreen()
tortoise = turtle.Turtle()

def autopolygonator(turtleturd, sides, totlenght):
    # calculates the interior angle 
    int_angles = (sides - 2)* 180

    # calculates angle for turtle to turn (polygon = equal angle sides)
    a1 = 180 - int_angles / sides

    # calculates lenght of a single sides
    s1 = totlenght / sides

    # accepts the number of sides as range parameter
    for i in range (sides):
        turtleturd.forward(s1)
        turtleturd.right(a1)
    

# here starts main

print("Welcome to the AUTOPOLYGONATOR!!")
s = int(input("Enter the number of sides in your polygon: "))
l = int(input("Enter the total lenght of your polygon: "))

autopolygonator(tortoise,s,l)
