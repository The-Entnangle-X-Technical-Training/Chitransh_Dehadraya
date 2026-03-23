num = int(input("Enter a number: "))
if 1 <= num <= 10:
    print("Range: 1-10")
elif 11 <= num <= 50:
    print("Range: 11-50")
elif 51 <= num <= 100:
    print("Range: 51-100")
elif 101 <= num <= 500:
    print("Range: 101-500")
elif 501 <= num <= 1000:
    print("Range: 501-1000")
elif num > 1000:
    print("Range: Above 1000")
else:
    print("Number is less than 1")