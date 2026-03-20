a=int(input("Enter the total amount: "))
if(a>=1000):
    c=a*10/100
    d=a-c
    print("10% discount applied ",c)
    print("So your actual amount is ",d)
else:
    print("No Discount allowed")