# This program prints the entered starting number to 100

try:
    number = int(input("enter a starting number less than 100: "))
    while number < 101:
        print(number)
        number = number + 1

except ValueError:
    print("Invalid input, Enter only whole numbers")

9


