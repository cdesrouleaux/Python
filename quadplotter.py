# COP2500 - Christopher Desouleaux
# quadplotter.py -

import math

# The calculatequadratic() funcition accepts a, b, c, and x. It then uses the quadratic function y = ax^2 + bx + c 
# and returns the resulting y. This function can only accepts numerals.
def calculatequadratic(a,b,c,x):
    y = a*(x**2) + b*x + c
    return y

# The plotpoints() function accepts a, b, c as parameters and calls calculatequadratic() to obtain (x,y) coordinates 
# of our porabola. This function only accepts numerals. No values are returned. 
def plotpoints(a,b,c):
    x1 = 0
    # retrieves and prints (x,y) coordinates 0-9.
    for x1 in range(0,10,1):
        r1 = calculatequadratic(a,b,c,x1)
        print("At x =",x1, ", y =", r1)
        x1 = x1 + 1 
    
    x2 = 10
    # retrieves and prints (x,y) coordinates 10-10000000, counts by tens.
    while x2 <= 10000000:
        r2 = calculatequadratic(a,b,c,x2)
        print("At x =",x2, ", y =", r2)
        x2 = x2 * 10 




## here starts main


# accepts user input for the quadratic function
am = float(input("Input coefficient a: "))
bm = float(input("Input coefficient b: "))
cm = float(input("Input coefficient c: "))
print("Porabola y =",am,"x^2 +",bm, "x +",cm)

plotpoints(am,bm,cm)
