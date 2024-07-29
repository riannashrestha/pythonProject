print("who knows rianna the best?")
print("there will be 5 questions and at the end you will get your score")

points = 0

first_question = input("what is rianna's favorite color?: ")

if first_question == "purple":
    points += 1

second = int(input("how old is she?: "))
if second == 12:
    points += 1

third = input("what is her birth month?: ")
if third == "march":
    points += 1
    
fourth = input("what school does she go to?: ")
if fourth == "carnage":
    points += 1

fifth = input("what is her brother's name?: ")
if fifth == "aviyan":
    points += 1

print("{} {} {}".format("score is: ", points, "out of 5"))






