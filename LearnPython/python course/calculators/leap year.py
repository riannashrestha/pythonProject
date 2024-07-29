print("is it a leap year?")
four = input("is it divisible by four? (yes or no): ")
if four == "yes":
    hundred = input("is it divisible by a hundred (yes or no): ")
    if hundred == "no":
        print("its a leap year")
    else:
        fh = input("is it divisible by four hundred? (yes or no): ")
        if fh == "yes":
            print("its a leap year")
        else:
            print("its not a leap year")
else:
    print("it is not a leap year")