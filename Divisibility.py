#Divisibility by 3
a=int(input("Enter a number:  "))
f=a//100
m=(a//10)%10
l=a%10
if((f+m+l)%3==0):
    print("Divisible by 3")
else:
    print("Not Divisible by 3")
    