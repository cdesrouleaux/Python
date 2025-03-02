# Quadratic lists 
#didnt finish

def quadratic(a,b,c,x):
    y = a * x**2 + b * x + c
    return y


def quadraticlist(a,b,c,xlist):
    ylist = []

    for x in xlist:
        y = quadratic(a,b,c,x)
        ylist.append(y)

    return ylist


def outputQuadratic(x,y):
    print("f(", x, ") = ", y)
    ylist = []

    for l in xlist:
        y = quadratic(a,b,c,l)
        ylist.append(y)




# here begins main

a = int(input("Enter a value for a : "))
b = int(input("Enter a value for b : "))
c = int(input("Enter a value for c : "))

listof_x = [0,1,2,3,4,5]
listof_y = quadratic(a,b,c,listof_x)
print(listof_x)
print(listof_y)



outputQuadratic(x,y)