#Write a program that calculates sum of all even numbers from 1 to N
n=int(input("Enter a number: "))
sum=0
for i in range(1, n+1):
    if i % 2 == 0:
        print(i)
        sum += i
print("The sum of even numbers from 1 to", n, "is:", sum)   