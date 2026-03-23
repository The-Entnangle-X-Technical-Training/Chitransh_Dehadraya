u=float(input("Enter water Useage: "))
b=0
if u<=500:
    b=u*2
elif u<=10000:
    b=(5000*2)+(u-5000)*3
else:
    b=(5000*2)+(5000*3)+(u-10000)*5
if (u<3000):
    b*=0.85
print("Total Water Bill: ",b)

