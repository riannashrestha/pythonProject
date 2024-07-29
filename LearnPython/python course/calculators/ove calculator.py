print("this is a love calculator")
name1 = input("Enter a name: ")
name2 = input("Enter a name again:  ")
combinednames = name1 + name2
str = combinednames.lower()
print(str)
lowernames = list(str)
print(lowernames)
t = lowernames.count("t")
r = lowernames.count("r")
u = lowernames.count("u")
e = lowernames.count("e")
first = t + r + u + e

l = lowernames.count("l")
o = lowernames.count("o")
v = lowernames.count("v")
e = lowernames.count("e")
second = l + o + v + e

score = first*10 + second
if (score >= 10) or (score>90):
    print(f"your score is {score}, you go together like coke and mentos")
elif (score >=40) and (score <= 50):
    print(f"your score is {score}, you are alright together")
else:
    print(f"your score is {score}")