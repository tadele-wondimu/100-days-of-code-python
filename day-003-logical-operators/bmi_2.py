height= float(input("Enter height in meters: "))
weight= int(input("Enter weight in kilograms "))
bmi= round(weight/(height**2), 2)
print(f"BMI is {bmi}")
if bmi < 18.5:
    print("you are under weight")
elif bmi <25:
    print("you are normal weight")
elif bmi < 30:
    print("you are slightly overweight")
elif bmi <35:
    print("Your are obese")
else: 
    print("you are clinically obese")
