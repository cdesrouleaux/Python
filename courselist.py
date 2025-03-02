# COP2500 - Christopher Desrouleaux
# courselist.py - This program allows the user to enter up to 5 classes for their 
# upcomming samester. Also checks and corrects if the user entered too many.



# deletecourse() function has the user delete a course from the list if there are too many. Only runs
# if the user enters 6 courses or more. Parameter(s): courselist[] the list of user courses (self explanatory).
# No returns, Only accepts numerals up to 6.
def deletecourse(courselist):    
        i = int(input("Max courses allowed per samester is 5. Enter the course number (1-6) you would like to remove: "))
        remove = i - 1
        del courselist[remove]

    
# the usercourses() function accepts an empty list courselist[] and has the user fill 
# the list with classes. No returns, No bad inputs.
def usercourses(courselist):
    
    i = 0
    print("Below enter the courses you are taking this samester")

    # accepts the users input and breaks the loop if user asks to    
    while i != "EXIT" and i != "exit":
        i = input("Enter a course or type EXIT when complete: ")
        
        # this if statement prevents the input of "exit" or "EXIT" to
        # be added to the list and printed unnecessarily
        if i != "EXIT" and i != "exit":
            courselist.append(i)
            # this loop prints the users input
            j = 1
            for i in (courselist):
                print(j,".",i)
                j = j + 1
        
        if len(courselist) > 5:
            deletecourse(courselist)

    # this loop prints the users input after modification/deletion
    print("Here are your courses for this samester:")
    j = 1
    for i in (courselist):
        print(j,".",i)
        j = j + 1
    print("Done!")



## here starts main
emptycourselist = []

# function call 
usercourses(emptycourselist)

