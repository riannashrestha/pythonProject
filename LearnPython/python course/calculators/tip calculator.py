print("this is a tip calculator")
bill = float(input("what was the total cost?: "))
tip = float(input("how much percentage do you want to give? 10,12,15: "))
people = float(input("how many people will split the bill?: "))

first = bill * (tip/100)
second = bill + first
third = second/people
roundednum = round(third, 2)

print(f"each person wil pay ${roundednum} dollars")