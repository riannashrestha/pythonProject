print("welcome to treasure island. your mission is to find the treasure")
road = input("your at a crossroad. where so you want ot go? type 'left' to go left and 'right' to go right: ")
if road == "left":
    lake = input("you come to a lake. there is an island in the middle of the lake. type 'wait' to wait for a boat and"
                 "'swim' to swim across: ")
    if lake == "wait":
        door = input("you arrive at the island unharmed. there is a house with three doors. one red. one yellow, and "
                     "one blue. which do you choose?: ")
        if door == "yellow":
            print("yay! you found the treasure. you win!")
        elif door == "blue":
            print("the room was filled with giant hornets. game over")
        else:
            print("the room was filled with hungry lions. game over")
    else:
        print("swam jumped in the water but it was ice cold and you froze to death. game over")

else:
    print("you came across a bear and died. game over")