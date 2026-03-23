a=int(input("Enter total unit: "))
b=5
c=7
d=10
e=15
if(0<=a<=100):
    print("Total Bill is: ",a*b)
elif(101<=a<=200):
    print("Total Bill is: ",a*c)
elif(201<=a<=300):
    print("total bill is: ",a*d)
else:
    print("Its above 300 so Bill is as per 15rs",a*e)