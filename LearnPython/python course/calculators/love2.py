print("This is a love calculator")

name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")

combined_names = (name1 + name2).lower()
print(f"Combined names: {combined_names}")

lower_names = list(combined_names)
print(f"List of characters: {lower_names}")

# Calculate the first score
first_score = lower_names.count("t") + lower_names.count("r") + lower_names.count("u") + lower_names.count("e")

# Calculate the second score
second_score = lower_names.count("l") + lower_names.count("o") + lower_names.count("v") + lower_names.count("e")

total_score = first_score * 10 + second_score

if total_score < 10 or total_score > 90:
    print(f"Your score is {total_score}, you go together like coke and mentos!")
elif 40 <= total_score <= 50:
    print(f"Your score is {total_score}, you are alright together.")
else:
    print(f"Your score is {total_score}.")
