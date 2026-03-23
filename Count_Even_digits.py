#Even digits in a number
a=int(input("Enter a number:  "))
f=a//1000
m=(a//100)%10
s=(a//10)%10
l=a%10
print("First",f)
print("Second",m)
print("Third",s)
print("Last",l)
if(f%2==0):
    print("Even digit is",f)
if(m%2==0):
    print("Even digit is",m)
if(s%2==0):
    print("Even digit is",s)
if(l%2==0):
    print("Even digit is",l)
if not (f%2==0 or m%2==0 or s%2==0 or l%2==0):
    print("No even digit")