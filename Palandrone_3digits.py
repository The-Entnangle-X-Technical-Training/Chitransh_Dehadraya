a=int(input("enter a number:  "))
f=a//100
m=(a//10)%10
l=a%10
if(f==m==l):
    print("Palindrome")
else:
    print("Not Palindrome")