print("the riddle game")
play = input("do you want to play?: ")
if play == "yes":
    print("first riddle")
    print("A prisoner is told that if he tells a lie he will get hanged, but if he tells the truth he will get shot")
    ques = input("what did the prisoner say to save himself?: ")
    if ques == 'i will get hanged':
        print("correct")
else:
    print("bye bye")

