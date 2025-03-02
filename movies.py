# COP2500 - Christopher Desrouleaux
# movies.py - this program calculates the cost of movie tickets depending on group size. 

import math

# obtaining the users input (# of tickets)
g = int(input("Enter the number of moviegoers: "))
indv_collect = 9.50
indv = 12.00
lg = 7.25

# this if statement outputs the total cost of tickets
# Discount may be applied if size of group is greater than 25
if g == 1:
    print("Total: $", indv_collect)
elif g <= 25:
    g_size = g-1
    total = indv_collect + (indv * g_size)
    print("Total: $",total)
elif g > 25:
    g_size = g-1
    total = indv_collect + (lg * g_size)
    print("Total: $",total)
else:
    print("invalid input")
