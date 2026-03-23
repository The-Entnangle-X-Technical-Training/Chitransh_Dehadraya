#Write a program that takes a number N and calculates its factorial (N! = 1×2×3×...×N)
N = int(input("Enter a number: "))

def factorial(n):
    if n < 0:
        return "Factorial not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

result = factorial(N)
print("The factorial of", N, "is:", result)