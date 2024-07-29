print("have a conversation with bob")
hi = input("say hi!: ")

if hi == "hi" or hi == "hello":
    print("hi there! how are you?")
    good = input()

    if good == "good" or good == "good how about you" or good == "im good" or good == "pretty good":
        print("that's nice to hear! I didn't catch your name. What is your name?")
    else:
        print("aww. I'm sorry to hear that. What is your name?")

name = input("enter your name: ")
print((name),"is such a nice name! well, i've got to go now! see you later!")