#Write a program that takes a number and calculates the sum of its digits
number = input("Enter a number: ")
digits = sum(int(digit) for digit in number)
print("The sum of the digits in the number", number, "is:", digits)
