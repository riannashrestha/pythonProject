name = "Elaine"

print(name.isalpha())
print(name[1])
print(len(name))
print(name[2:])
print(name[-2])
print(name[:3])
print(name + ' Haight')
print('-' * 50)

# name[0] = 'e' cannot do it because string is immutable
print(name.upper())
print(name.lower())
print(name)


# string format
print("Your birthday is on: %s/%s/%s" % ('01', '15', '2002'))
print("I will see you on date: %s - %s - %s" % ('09','19','2023'))
print("Our friend group are: %s & %s & %s & %s" % ('rianna', 'chetna', 'visha', 'nandana'))
print("your class starts on: %i-%i-%i" % (8, 28, 2023))
print("you and your friends weighs as: %f & %f & %f & %f" % (90.2, 85.6, 87.1, 95.0))