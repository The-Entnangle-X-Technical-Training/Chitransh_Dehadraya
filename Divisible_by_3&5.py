a=int(input("Enter numbers: "))
if(a%3==0 and a%5==0):
    print("The Number is Divisible By 3&5")
elif(a%3==0):
    print("The Number is Divisible by 3")
elif(a%5==0):
    print("The Number is divisible by 5")
else:
    print("The Number is not Divisible by any 3&5")
