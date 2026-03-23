a=float(input("enter amount: "))
b=input("Are you member?(Yes/No): ")
d=0
if(a>10000):
    d=20
elif(a>5000):
    d=15
elif(a>2000):
    d=10
else:
    d=0
if b.lower()=="yes":
    d+=5
da=(d/100)*a
fp=a-da
print("Total Discount",d,"%")
print("Price after Discount ₹ ",fp,)