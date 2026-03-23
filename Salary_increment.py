b=int(input("enter your rating 1-5: "))
a=int(input("Enter Your salary: "))
c=int(input("Enter years of exp: "))
if(b==5):
    print("you got 5 rating you will be getting 20% pr increment",a*1.2)
elif(b==4):
    print("you got 4 rating you will be getting 15% pr increment",a*1.15)
elif(b==3):
    print("you got 3 rating you will be getting 10% pr increment",a*1.1)
elif(b==2):
    print("you got 2 rating you will be getting 5% pr increment",a*1.05)
else:
    print("you got 1 rating you will be getting 0% increment",a)


