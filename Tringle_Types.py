a=int(input("Enter 1st side: "))
b=int(input("Enter 2nd side: "))
c=int(input("Enter 3rd side: "))
if (a==b==c):
    print("Equilateral tringle ")
elif (a==b or b==c or a==c):
    print("Its isosceles Tringle")
else:
    print("scalenec")