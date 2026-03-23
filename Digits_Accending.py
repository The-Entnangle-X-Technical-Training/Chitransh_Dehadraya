#CHECK IF DIGITS ARE IN ACCENDING ORDER
a=int(input("Enter a number:  "))
f=a//100
m=(a//10)%10
l=a%10  
if(f<m<l):
    print("Digits are in accending order")
else:
    print("Digits are in descending  order")