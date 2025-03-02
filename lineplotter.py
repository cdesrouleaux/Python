# COP2500 - Christopher Desrouleaux
# lineplotter.py - the purpose of this program is to accept a slope and an intercept 
# and print out the points of that line.


import math

def plotter(slope, intercept):

    # prints points on the line between 0-9
    for x in range(0,10,1):
        y = slope*x + intercept
        print("At x=",x,", y=",y)

    # prints points on the line between 10-100000.
    # Counts by multiplying answer by 10
    x = 10
    while x <= 100000:
        y = slope*x + intercept
        print("At x=",x,", y=",y)
        x = x * 10


# here starts main

m = float(input("Please enter your slope: "))
int = float(input("Please enter your x-intercept: "))

print("Line y =",m, "x +",int)
plotter(m, int)