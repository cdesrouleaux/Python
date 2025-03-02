# COP2500 - Christopher Desrouleaux
# quad.py - This program asks the user to enter values for ax^2 + bx + c = 0 
# and returns the results of a the quadrartic equation

import math

# The gimmedeterminant() funtion accepts inputs of the quadratic equation and outputs the 
# determenent. This function only accepts numerals.
def gimmedeterminant(a,b,c):
    d = b**2 - (4*a*c)
    return d

# The onerootoutput() funtion accepts the a,b. This funtion returns the value of the quadratic formula 
# when the determinant is zero. This function only accepts numerals and variable "a" cannot accept zero as input.
def onerootoutput(a,b):
    oneroot = -b / (2*a)
    return oneroot

# The positivequadratic() funcion accpets the a,b, and det (determinant calculated in gimmedeterminant()).
# This function returns the positive result of quadratic equation. This function only accepts numerals and 
# variable "a" cannot accept zero as input.
def positivequadratic(a,b,det):
    positive = ((-b) + (math.sqrt(det))) / (2*a)
    return positive

# The negativequadratic() funcion accpets the a,b, and det (determinant calculated in gimmedeterminant()).
# This function returns the negative result of quadratic equation. This function only accepts numerals and 
# variable "a" cannot accept zero as input.
def negativequadratic(a,b,det):
    negative = ((-b) - (math.sqrt(det))) / (2*a)
    return negative



## here starts main

# accepts user input for quadratic equation
am = float(input("Input coefficient a: "))
bm = float(input("Input coefficient b: "))
cm = float(input("Input coefficient c: "))

determinant = gimmedeterminant(am,bm,cm)
detzero = onerootoutput(am,bm,)

print(determinant)

if determinant == 0:
    print("That quadratic has one root:", detzero)
elif determinant > 0:
    pos = positivequadratic(am,bm,determinant)
    neg = negativequadratic(am,bm,determinant)
    print("That quadratic has two roots:",pos,"and",neg)
elif determinant < 0:
    print("Sorry, that quadratic has complex roots.")
