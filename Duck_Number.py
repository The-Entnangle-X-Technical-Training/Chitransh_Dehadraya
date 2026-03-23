#CHECK DUCK NUMBER IN 4 DIGITS
a=int(input("Enter a number:  "))
f=a//1000
m=(a//100)%10
s=(a//10)%10
l=a%10
if( m==0 or s==0 or l==0):
    print("Duck number")
elif(f!=0):
    print("Not Duck number")
else:  
    print("Not Duck number")