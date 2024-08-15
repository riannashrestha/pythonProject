
print("welcome to the roller coaster!")
height = int(input("what is your height in cm?: "))

if height >=120:
    print("you can ride the roller coaster!")
    age = int(input("how old ore you?: "))
    if age >= 18:
        bill = 12
        print("your ticket costs $12")
    elif age >= 12:
        bill = 7
        print("your ticket cost $7")
    else:
        bill = 5
        print("the ticket costs $5")

    photo = input("would you like a photo for $3 (yes or no): ")
    if photo == "yes":
        bill +=3
    print(f"your final cost is ${bill}")

else:
    print("sorry, you have to grow "
          ""
          "taller before you can ride")