a=int(input("Enter a number:  "))
f=a//1000
m=(a//100)%10
s=(a//10)%10
l=a%10
if(f>=m and f>=s and f>=l):
    print("Largest digit is",f)
elif(m>=f and m>=s and m>=l):
    print("Largest digit is",m)
elif(s>=f and s>=m and s>=l):
    print("Largest digit is",s)
else:
    print("Largest digit is",l)