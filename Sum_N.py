a=int(input("Enter a number: "))
sum=0
for i in range(1, a+1):
    sum+=i
    print("after adding", i, "the sum is:", sum)
print("The sum of first", a, "natural numbers is:", sum)