a=int(input("How many numbers you want to add:  "))
n=[]
for i in range(a):
    n.append(int(input("ENter Number")))
print("Remove Last",n[:-1])