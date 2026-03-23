print("For a quadratic equation ax^2 + bx + c = 0")
a=float(input("Enter cofficient of a : "))
b=float(input("Enter cofficient of b : "))
c=float(input("Enter cofficient of c : "))
d=(b**2)-(4*a*c)
if(d>0):
    print("The roots are real and Distinct")
elif(d==0):
    print("the roots are real and equal")
else:
    print("The roots are imagnery ")