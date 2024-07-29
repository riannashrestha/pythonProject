import random

# a guessing game - asking friend to guess a number from 1 to 5

randomNumber = random.randint(1, 5)

while True:
    guessNum = input("Guess a number from 1 to 5, if you win - you get $5: ")

    try:
        userguess = int(guessNum)
    except ValueError:
        print("You must enter a valid number")
        continue

    if userguess < 1 or userguess > 5:
        print("Please enter a number between 1 and 5")
        continue
    if userguess == randomNumber:
        print("You got it!")
        print("You won $5!")
        break
    else:
        print("Sorry, you guessed wrong.")
        print("You do dishes, have fun!")
        break
print("Goodbye!")
