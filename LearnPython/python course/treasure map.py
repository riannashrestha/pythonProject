line1 = [" ", " ", " "]
line2 = [" ", " ", " "]
line3 = [" ", " ", " "]
map = [line1, line2, line3]
print("hiding your treasure! x marks the spot")
position = input("where do you want to put the treasure")
letter = position[0].lower()
abc = ["a", "b", "c",]
letterindex = abc.index(letter)
numberindex = int(position[1]) - 1
map[numberindex][letterindex] = "x"
print(f"(line1)\n(line2)\n(line3)")