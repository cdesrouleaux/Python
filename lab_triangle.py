# 02/22 COP2500C LAB
# Draws right triangle give n hypotenuse and on angle as input

import math
import turtle

# Get float input form the give nprompt
def getFloat(prompt):
    result = float(input(prompt))
    return result

# Finds opposite side lenght given hypotenuse and angle theta
def findOppFromHypAndTheta(hyp,theta):
    result = math.sin(theta) * hyp
    return result

# Finds adjacent side lenght given hypotenuse and opposite
def findAdjFromHypAndOpp (hyp, opp):
    adj2 = (hyp**2) - (opp**2)
    result = math.sqrt(adj2)
    return result

# Draws triangle given all 3 side lenghts and angle theta
def drawTriangle(opp,adj,hyp,theta):
    turtle.forward(adj)
    turtle.left(90)
    turtle.forward(opp)
    turtle.left(90+theta)
    turtle.forward(hyp)

# Take input for hypootenuse lenght nad angle 
hyp = getFloat("Enter the hypotnuse: ")
theta = getFloat("Enter the angle in degrees: ")

# calculate the opposite and adjacent side lenghts

#math libraries exept radian values.
thetaRad = math.radians(theta)

opp = findOppFromHypAndTheta(hyp,thetaRad)
adj = findAdjFromHypAndOpp(hyp, opp)

# Draw the triangle
drawTriangle(opp,adj,hyp,theta)

