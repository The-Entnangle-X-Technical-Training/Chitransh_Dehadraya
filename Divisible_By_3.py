#Write a program that prints all numbers from 1 to N that are divisible by 3.
N = int(input("Enter a number: "))
print("Numbers from 1 to", N, "that are divisible by 3:")
for i in range(1, N + 1):
    if i % 3 == 0:
        print(i)
