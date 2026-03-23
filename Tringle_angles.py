a=int(input("Enter 1st Side: "))
b=int(input("Enter 2nd Side: "))
c=int(input("Enter 3rd Side: "))
if(89>a or 89>b or 89>c):
    print("The tringle is actue")
elif(a==90 or b==90 or c==90):
    print("the tringle is right angle tringle")
elif(90<a or 90<b or 90<c):
    print("The tringle is obtuse angle tringle")