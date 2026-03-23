a=int(input("enter age: "))
b=int(input("enter your income: "))
c=int(input("Enter Your Credit score: "))
if(21<=a<=60 and b>25000 and c>700):
    print("For Loan You are eligible")
else:
    if not(21<=a<=60):
        print("Failed age must be between 21-60 Plesae enter Correct age ",)
    if not(b>2500):
           print("Failed Income should be >25000")
    if not(c>700):
         print("Failed credit Score should be >700")
