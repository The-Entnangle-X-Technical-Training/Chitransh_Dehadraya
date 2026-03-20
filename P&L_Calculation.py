s=float(input("Enter sellprice"))
b=float(input("Enter price"))
p=s-b
if p>0:
    print("Profit:",p)
elif p<0:
    print("loss",p)    