#CHECK IF Harshad/Niven NUMBER
a=int(input("Enter a number:  "))
f=a//100
m=(a//10)%10
l=a%10
if(a%(f+m+l)==0):
    print("Harshad/Niven number")
else:
    print("Not Harshad/Niven number")
    