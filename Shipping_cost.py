w=float(input("Enter Weight in(kg): "))
d=float(input("Enter Distance in(km): "))
c=0
ed=0
ew=0
if(w>5):
    ew=w*10
    c+=ew
if(d>100):
    ed=d*5
    c+=ed
if(w>5 and d>100):
    c=20
print("Total shhipping Cost:₹",c)
