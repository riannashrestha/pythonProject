print("thank you for choosing python pizza deliveries!")
size = input("what size pizza do you want? S, M, or L: ")
if size == "s":
    bill = 15
elif size == "m":
    bill = 20
else:
    bill = 25
pepperoni = input("do you want pepperoni? Y or N: ")
if pepperoni == "y":
    if size == "s":
        bill += 2
    else:
        bill += 3
cheese = input("do you wat extra cheese? Y or N: ")
if cheese == "y":
    bill += 1

print(f"thank you for choosing python pizza! your total is ${bill}")