import math
print("circle area calculator")

pi = math.pi
radius = float(input("please enter the radius of you circle: "))
answer = pi * radius * radius

print(f"the area of you circle is {answer:.2f}")
print(".............")
print()
print()

print("{} {}".format("the area of circle: ", answer))
