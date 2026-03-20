a = input("Enter numbers separated by space: ")
list = list(map(int, a.split()))
for i in range(a):
    list.append(input("enter number: "))
print(list)