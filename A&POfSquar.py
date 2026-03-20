s=int(input("Enter Side"))
c=input("chose area or peri")
if c=="area":
    area=s*s
    print("Area of squar",area)
elif c=="peri":
    peri=4*s
    print("Peri of squar",peri)