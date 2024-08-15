from turtle import Turtle, Screen

rianna = Turtle()
rianna.shape("turtle")
rianna.color("blue")
# rianna.forward(300)
# rianna.backward(500)
# rianna.color("orange")
# rianna.right(45)
# rianna.forward(100)
# rianna.circle(50)
# rianna.color("maroon")
# rianna.circle(60)
# rianna.fillcolor("yellow")

# for steps in range(100):
#     for c in ('red', 'purple'):
#         rianna.color(c)
for size in range(1,101,10):
    rianna.circle(size)
    rianna.shape("circle")

















my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()





