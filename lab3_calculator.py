
x = float(input("Enter a value for x"))
y = float(input("Enter a value for a y"))

op = input("Do you want to add, sub, mult, or div? ")

if op == "add":
    z = x + y 
    # print("The result is:", z)

elif op == "sub":
    z = x - y
    # print("The result is:", z)

elif op == "mult":
    z = x * y
    # print("The result is:", z)

elif op == "div":
    z = x / y
    # print("The result is:", z)

else:
    print("Invalid command")

print("The result is:", z)
