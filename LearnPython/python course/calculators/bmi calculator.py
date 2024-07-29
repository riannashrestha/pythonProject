print("bmi calculator")
h = float(input("enter your height in m: "))
w = float(input("enter your weight in kilograms: "))
bmi = w/h**2

if bmi < 18.5:
    print(f"your bmi is {bmi}, you are underweight")