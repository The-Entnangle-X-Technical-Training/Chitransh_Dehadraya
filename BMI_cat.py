bmi = float(input("Enter your BMI value: "))
if bmi < 18.5:
    print("Category: Underweight")
elif 18.5 <= bmi <= 24.9:
    print("Category: Normal")
elif 25 <= bmi <= 29.9:
    print("Category: Overweight")
else:
    print("Category: Obese")