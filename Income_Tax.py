a=float(input("Enter the amount: "))
if(0<=a<=250000):
    print("The percent on this amount will be 0%",a)
elif(250000<=a<=500000):
    print("The percent on this amount will be 5%",a)
elif(500000<=a<=1000000):
    print("The percent on this amount will be 10%",a)
else:
    print("The percent on this amount will be 30%",a)