day = int(input("Enter day (1-31): "))
month = int(input("Enter month (1-12): "))

valid = False

if month in [1, 3, 5, 7, 8, 10, 12]:
    if 1 <= day <= 31:
        valid = True
elif month in [4, 6, 9, 11]:
    if 1 <= day <= 30:
        valid = True
elif month == 2:
    if 1 <= day <= 29:
       valid = True

if valid:
    print("Valid")
else:
    print("Invalid")