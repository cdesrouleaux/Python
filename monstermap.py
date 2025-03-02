# COP2500 - Christopher Desrouleaux
# monstermap.py - the purpose of this function is to find the regions where the "small monsters"
# concentrated in using the turtle library

import turtle
    
# the drawMap() function draws a map of circles with different radii, the only vaiable inputed 
# is the turtle library renamed tortoise. This function can only accept numerals.
def drawMap(tortoise):

    # accepting user input to customize the "map"
    horizontal_multiplier = float(input("input value for the horizontal multiplier: "))
    vertical_multiplier = float(input("input value for the vertical multiplier: "))
    constant = float(input("input value for the constant: "))

    tortoise.fillcolor("yellow")
    
    # moves the turtle across the "map" and draws a 10x8 grid of yellow circles, with different radii
    for h_cell in range(0,10,1):
        for v_cell in range(0,8,1):
            tortoise.penup()
            tortoise.goto(25*h_cell,-25*v_cell)
            tortoise.pendown()

            tortoise.begin_fill()

            radius = (horizontal_multiplier * h_cell) + (vertical_multiplier * v_cell) + constant
            tortoise.circle(radius)

            tortoise.end_fill()
    


## here starts main

my_screen = turtle.getscreen()
my_tortoise = turtle.Turtle()


drawMap(my_tortoise)
