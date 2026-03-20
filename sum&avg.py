a=int(input("Enter first number"))
b=int(input("Enter second number"))
c=int(input("Enter third number"))
d=input("Enter operation avg or sum")
if d=="avg":
    avg=a+b+c/3
    print("The average of Numbers:",avg)
if d=="sum":
    sum=a+b+c
    print("The sum of numbers:",sum)
