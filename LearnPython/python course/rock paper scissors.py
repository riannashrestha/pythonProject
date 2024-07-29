print("rock, paper, scissors, shoot!")
print("type '0' for rock, '1' for paper, and '2' for scissors")
choice = int(input(""))
if choice == 0:
    print("you chose rock")
elif choice == 1:
    print("you chose paper")
else:
    print("you chose scissors")

import random
computerchoice = random.randint(0, 3)
if computerchoice == 0:
    print("the computer chose rock")
elif computerchoice == 1:
    print("the computer chose paper")
else:
    print("the computer chose scissors")

if choice == 0 and computerchoice == 0:
    print("its a tie")
elif choice == 0 and computerchoice == 1:
    print("you lose")
elif choice == 0 and computerchoice == 2:
    print("you win")
elif choice == 1 and computerchoice == 0:
    print("you win")
elif choice == 1 and computerchoice == 1:
    print("its a tie")
elif choice == 1 and computerchoice == 2:
    print("you lose")
elif choice == 2 and computerchoice == 0:
    print("you lose")
elif choice == 2 and computerchoice == 1:
    print("you win")
elif choice == 2 and computerchoice == 2:
    print("its a tie")