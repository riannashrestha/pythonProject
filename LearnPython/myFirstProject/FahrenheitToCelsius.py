# This program converts the temperature from
# Fahrenheit to Celsius

ftemp = float(input("hey! Enter the temperature in Fahrenheit: "))

ctemp = (ftemp - 32) * 5/9

print(f"The converted temperature in Celcius is: {ctemp:.2f}")
