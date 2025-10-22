height= float(input("Enter height in meters: "))
weight= int(input("Enter weight in kilograms "))
bmi= round(weight/(height**2), 2)
print(f"BMI is {bmi}")