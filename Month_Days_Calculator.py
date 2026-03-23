a=int(input("Enter month number (1-12): "))
if a in [1, 3, 5, 7, 8, 10, 12]:
   print("Number of days: 31")
elif a in [4, 6, 9, 11]:
    print("Number of days: 30")
elif a == 2:
    print("Number of days: 28 or 29 (leap year)")
else:
    print("Invalid month number. Please enter a number between 1 and 12.")