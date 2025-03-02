# COP2500 - Christopher Desrouleaux
# courselist2.py - prompts the user to enter exactly 5 courses for the upcomming
# samester.




#addcourse - adds users input to their list of courses. Parameters: add
#inserts post formated input into the list of courses, emptylist temporarly
#holds each courses name, list3 is the raw user input pre format. Returns
#a formated list of courses. No issues, any input.
def addcourse(add, emptylist, list3):
    pos = 0
    for x in list3:
        emptylist = x.strip().title()
        add.insert(pos,emptylist)
        pos = pos + 1
    return add

#dropcourses- drops is triggered when user inputs more than 5 courses. It
#prompts user to deletes any extra courses over 5. Parameters: list4 is an unformated
#list of courses the user would like to delete from the list, drop_it is the
#list of courses needing to be modified. Returns a formated list less than
#or equal to 5 courses. No issues, any input.
def dropcourse(drop_it, list4):
    z = 0
    for z in list4:
        kill = z.strip().title()
        if kill in drop_it:
            drop_it.remove(kill)
        else:
            break
    return drop_it

#coursecompiler - prompts the user to enter exactly 5 courses for the upcomming
#samester. If there are to few or to many courses, the user is prompted to add
#to list or delete the extra course(s). Parameters: courselist is the list of
#the users courses. Returns nothing. No issues, any input.
def coursecompiler(courselist):

    k = 0
    y = 0
    x = 0

    print("You aren't currently taking any courses.\n")
    while len(courselist) != 5:

        while len(courselist) < 5:
            usecase1 = input("What courses would you like to take? ")
            list1 = usecase1.split(",")
            
            print("You are currently taking these courses:")
            courselist = addcourse(addition, emlist, list1)
            
            j = 1
            for x in courselist:
                print(j,".",x)
                j = j + 1

        while len(courselist) > 5:
            drop = input("What courses would you like to drop? ")
            list2 = drop.split(",")

            print("You are currently taking these courses:")
            courselist = dropcourse(courselist, list2)
            
            i = 1
            for y in courselist:
                print(i,".",y)
                i = i + 1

                
    print("Yay you picked all your classes, you'll have so much fun!")

       

# here starts main

#declares lists
listofcourses = []
emlist = []
addition = []

#calls master function
coursecompiler(listofcourses)


