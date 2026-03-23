x = float(input("Enter x coordinate: "))
y = float(input("Enter y coordinate: "))
if x > 0 and y > 0:
    print("Point lies in Quadrant I")
elif x < 0 and y > 0:
    print("Point lies in Quadrant II")
elif x < 0 and y < 0:
    print("Point lies in Quadrant III")
elif x > 0 and y < 0:
    print("Point lies in Quadrant IV")
elif x == 0 and y == 0:
    print("Point lies at the Origin")
elif x == 0:
    print("Point lies on the Y-axis")
elif y == 0:
    print("Point lies on the X-axis")