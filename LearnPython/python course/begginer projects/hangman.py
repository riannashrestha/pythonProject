
word_list = ["aardvark", "baboon", "camel"]
import random
chosen_word = random.choice(word_list)

display = []
word_lenth = len(chosen_word)
for _ in range(word_lenth):
    display += "_"

guess = input("guess a letter: ").lower()

for position in range(word_lenth):
    letter = chosen_word[position]

if letter == guess:
    display[position] = letter

print(display)
