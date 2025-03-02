# COP2500 - Christopher Desrouleaux
# mathfun.py - this program takes the opp,adj,hyp, and adjacent angle for a 
# right triangle and gives the missing parts


import math 

# the adjacent_len() function gives the adjacent lenght by accepting the hypotenuse and adjacent side. Warning: this function
# only accepts numerals, do not enter angles more than 180 degrees
def adjacent_len(hyp,alpha):
    beta = 180-90-alpha
    a = (hyp*math.sin(math.radians(beta)))/(math.sin(math.radians(90)))
    return a
    
# the opposite_len() function gives the opposite lenght by accepting the hypotenuse and adjacent side. Warning: this function
# only accepts numerals, do not enter angles more than 180    
def opposite_len(hyp,alpha):
    b = (hyp*math.sin(math.radians(alpha)))/(math.sin(math.radians(90)))
    return b

# the adjacent_angle1() function gives the adjacent angle by accepting the hypotenuse and opposite side. Warning: this function
# only accepts numerals, the opposite side cannot be greater that the hypotenuse
def adjacent_angle1(hyp,opp):
    alpha = math.asin(opp/hyp)
    alpha = alpha*(180/math.pi)
    return alpha

# the adjacent_angle2() function gives the adjacent angle by accepting the adjacent and opposite sides. Warning: this function
# only accepts numerals
def adjacent_angle2(adj,opp):
    alpha = math.atan(opp/adj)
    alpha = alpha*(180/math.pi)
    return alpha



## here starts main

# accepts user input
opposite = float(input("Enter value of the opposite side: "))
adjacent = float(input("Enter value of the adjacent side: "))
hypotenuse = float(input("Enter vlaue of the hypotnuse: "))
m_alpha = float(input("Enter value of the adjacent angle: "))

# prints output
print("Adjacent Lenght:", adjacent_len(hypotenuse,m_alpha))
print("Opposite Lenght:", opposite_len(hypotenuse,m_alpha))
print("Adjacent Angle:", adjacent_angle1(hypotenuse,opposite))
print("Adjacent Angle:", adjacent_angle2(adjacent,opposite))
