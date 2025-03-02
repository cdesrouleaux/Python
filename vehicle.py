# COP2500C - Christopher Desrouleaux
# vehicle.py - Drawing ideal small monster search vehicle using Turtle Graphics

import turtle

tortoise_screen = turtle.getscreen()
tortoise = turtle.Turtle()

# This is the boat is the vehicle Small Monsters use to explore the vast islands of Knightrola
tortoise.pencolor("brown")
tortoise_screen.bgcolor("blue")

# this is the ships base
tortoise.fillcolor("brown")
tortoise.begin_fill()

tortoise.begin_fill()
tortoise.pensize(4)
tortoise.goto(-300,0)
tortoise.right(90)
tortoise.circle(300,180)
tortoise.left(90)
tortoise.forward(300)

tortoise.end_fill()

# this is the ships mast
tortoise.pensize(6)
tortoise.right(90)
tortoise.forward(100)

# these are the ships sails
tortoise.fillcolor("white")
tortoise.begin_fill()

tortoise.pensize(4)
tortoise.goto(-300,100)
tortoise.right(60)
tortoise.forward(350)
tortoise.right(60)
tortoise.forward(350)
tortoise.right(150)
tortoise.forward(300)
tortoise.pensize(6)
tortoise.left(90)
tortoise.forward(100)

tortoise.end_fill()

tortoise.right(180)
tortoise.forward(100)
tortoise.pencolor("black")
tortoise.pensize(10)
tortoise.forward(167)








