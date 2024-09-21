#1. Simple Calculator with Match Case
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
operation = str(input("Choose the operation (+, -, *, /): "))
result = 0

#calculations
match operation:
    case "+":
        result = number1 + number2
        print(f"The result is {result}.")
    case "-":
        result = number1 - number2
        print(f"The result is {result}.")
    case "*":
        result = number1 * number2
        print(f"The result is {result}.")
    case "/":
        if number2 == 0:
            print("Cannot divide by zero.")
        else:
            result = number1 / number2
            print(f"The result is {result}.")
    case _:
        print("Wrong operation.")
