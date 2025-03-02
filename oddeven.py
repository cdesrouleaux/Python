# COP2500 - Christopher Desrouleaux
# oddeven.py - Guessing Game - guess if the random number generated is even or odd

import random 

user_string = input("I'm thinking of a number... guess if its even or odd: ")

n = random.randint(1,256)

# even case - compares the user input with the value of the random generated number. 
while n % 2 == 0:
    if user_string == "even":
        print("Great guess!")
    elif user_string == "odd":
        print("Sorry bad guess.")
    else:
        print("You didn't enter odd or even.  You forfeit!  (My number was", n, "if you're wondering.)")
    break

# odd case - compares the user input with the value of the random generated number. 
while n % 2 != 0: 
    if user_string == "odd":
        print("Great guess")
    elif user_string == "even":
        print("Sorry bad guess.")
    else:
        print("You didn't enter odd or even.  You forfeit!  (My number was", n, "if you're wondering.)")
    break
