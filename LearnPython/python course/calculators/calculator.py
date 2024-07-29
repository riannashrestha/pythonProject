#calculator

#asking the numbers
num1 = float(input("whats the first number?: "))
num2 = float(input("whats the second number?: "))

#add
def add(n1, n2):
    return n1 + n2

#subtract
def subtract(n1, n2):
    return n1 - n2

#multiply
def multiply(n1, n2):
    return n1 * n2

# divide
def divide(n1, n2):
    return n1 / n2

operations = {"+": add(n1=num1, n2=num2),
              "-": subtract(n1=num1, n2=num2),
              "*": multiply(n1=num1, n2=num2),
              "/": divide(n1=num1, n2=num2)
              }

def calculator():
    for operation in operations:
        print(operation)
    operation_symbol = input("pick an operation from above: ")

    if operation_symbol == "+":
        answer = add(n1=num1, n2=num2)
    elif operation_symbol == "-":
        answer = subtract(n1=num1, n2=num2)
    elif operation_symbol == "*":
        answer = multiply(n1=num1, n2=num2)
    elif operation_symbol == "/":
        answer = divide(n1=num1, n2=num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
            num1 = answer
        else:
            should_continue = False
            clear()
            calculator()

calculator()