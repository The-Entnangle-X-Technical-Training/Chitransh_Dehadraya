a = int(input("Enter the password length: "))
b = int(input("Enter the count of uppercase letters: "))
c = int(input("Enter the count of lowercase letters: "))
d = int(input("Enter the count of digits: "))
e = 0
if b > 0:
    e += 1
if c > 0:
    e += 1
if d > 0:
    e += 1

if a >= 8 and e >= 3:
    print("Strong")
elif a >= 6 and e >= 2:
    print("Medium")
else:
    print("Weak")
    
