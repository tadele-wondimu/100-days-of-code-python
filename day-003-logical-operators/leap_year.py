print("*******A leap year checker app*******")
year=int(input("Year you want to check?: "))
if year % 4 == 0:
    if year % 100 != 0:
        print(f"{year} is a leap year")
    else:
        if year % 400 == 0:
            print(f"{year} is a leap year")
        else:
            print(f"{year} is NOT a leap year")
            
else:
    print(f"{year} is NOT a leap year")