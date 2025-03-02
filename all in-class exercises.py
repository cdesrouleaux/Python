# all in-class code.py - all coding assignments 
# Christopher Desrouleaux, COP2500

###################################################################
# Takaway notes for COP2500 
# take Matt Gurber for Descrete programming!!
####################################################################
# 02/14
# How to use for loops

######

# for n in range (1,100,1):
#     if n % 3 == 0:
#         print(n)


# print("\nnext\n")

# for n in range (3, 100, 3):
#     print(n)
    
######

# 02/16
# Write a function that accepts a prompt string as a parameter, 
# prompts the user with that string, accepts a float as user input, 
# and returns it *as* a float without the need for caller to re-cast it

######

# def wow_sting(input):
#     x = float(input(input))
#     return x

######

# 02/18

# Write a function that returns the are of a circle  give the radius.

# import math 

# #circle area: given the radius of a circle, returns the area. Causes an error
# if radius isn't a number 
# a = pir^2

# def area_circle(radius):
#     a = math.pi * pow(radius,2)
#     return a 

# # Here starts main

# r = float(input("Enter the radius of a circle: "))
# result = area_circle(r)
# print(" The area of the circle is: ",result)

# # Write a function  that returns the lenght of a right triangle's 
# # hypoteneuse given its adjacent and opposite side lenghts.

# #a^2 + b^2 = c^2
# import math 

# # gimme_lenght: accepts the adjacent and opposite lenghts of a right triangle and
# # returns the hypotenuse lenght. Will cause an error if the adj and opp lenghts aren't numbers.

# def gimme_lenght(adjacent, opposite):
#     hypoteneuse = math.sqrt(adjacent**2 + opposite**2)
#     return hypoteneuse

# ## here starts main

# adj = int(input("Enter the adjacent side of the right triangle: "))
# opp = int(input("Enter the opposide side of the right triangle: "))


# result = gimme_lenght(adj, opp)

# print("The hypotenuse is:", result)

######

# Write a functino that accepts a *turtle* and set of x/y coordinates, 
# and moves the turtle to thoes without drawing anything in the process

# import turtle
# screen = turtle.getscreen()
# tortiouse = turtle.Turtle()

# # alter_turtle: move turtle t to coordinates (x,y) without drawing a line.
# # Returns nothing. Cause an error if x and y aren't numbers, or if ti isn't
# # a turtle.
# def alter_turtle(t,x,y):
#     t.penup
#     t.goto(x,x)
#     t.pendown

# ## here starts main

# print("Enter coordinates that you would like your turtle to move to")

# # x = int(input("Enter x coordinate: "))
# # y = int(input("Enter y coordinate: "))

# alter_turtle(tortiouse,100,300)

# 02/21

# Write a function that returns rthe area of a right 
# triangle given its adj and opp lenghts

# import math 

# # areatri: accepts the adj adn opp lenghts of a right triangle and returns
# # the are. Will cause an error if the adjacent and opposite lenghts aren't numbers. 

# def areatir(adjacent, opposite):
#     area = (adjacent * opposite) / 2
#     return area

# ## here starts main

# result = areatri(5, 6)

# Write a functino that returns the volume of an ordinary cylinder 
# given its raduis and height

# import math

# def volumevylinder1(radius, height):
#     volume = math.pi * radius**2 * height
#     return volume

# ## her starts main

# # print(volumevylinder1(5, 10))

# # Write a function that returns the volume of an ordinary cylinder 
# # given its raduis and height. You can't directly use pi, whether 
# # from the math library or as your own constant


# def volumecylinder2(radius, height):
#     volume = volumevylinder1(radius, height)
#     return volume

# # here starts main

# print(volumecylinder2(5, 10))

# ## 02/25
# # Write a function that, given an n, sums the numbers from 1 to n 
# # inclusive and returns a sum.

# def gimmesum(n):
#     sum = 0
#     for i in range(1, n+1, 1):
#         sum = i + 1 
#     return sum

# # here starts main

# print(gimmesum(5))

########################

### 03/21
## Write a function that accepts a list of numbers and returns their
## sum. Use a FOR loop to optain the sum.

# def firstlist(conceptlist):
#     sum = 0
#     for i in conceptlist:
#         sum = sum + i
#     return sum
        


# # here starts main

# int(input(sciencelist = [1,2,3,4,5,6,7,8,9,10]))

# print("The sum =",firstlist(sciencelist))

## 03/23
# Write a function




##########################

##04/06
# Write a funtion that accepts two monster dictionaries and prints out the
# name of the more monstery monster

#monster1 = {
#"name": "spaceduckmon",
#"type": "rubberduck",
#"weight": 0.007,
#"monsteriness": 2.0
#}
#
#monster2 = {
#"name": "spinmon",
#"type": "electricscooter",
#"weight": 14.0
#"monsteriness": 10.0
#}

#monsteriness.sort

# Final Exam

s = "the quick brown fox jumps over the lazy dog"

print ("Uppercase:", s.upper())
print ("Lowercase:", s.lower())
print ("Capitalized:", s.capitalize())
print ("Title case:", s.title())

s.replace("dog","cat")
print(s)

print("\n")
s = "I want a dog"
s = s.replace("dog","cat")
print(s)

print("\n")
c = 14.23745628904
print(f"{c:4.5f}")


print("\n")
n = ["boat","horse","car","fence","aligator","Alex","Fart","Cum"]

n.sort()
print("n = ",n)

