def calculator():
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    operation = input("choose the operation (+, -, *, /): ")
    match operation:
        case "+":
            result = number1 + number2
            print(f"The result is {result}")
        case "-":
            result = number1 - number2
            print(f"The result is {result}")
        case "*":
            result = number1 * number2
            print(f"The result is {result}")
        case "/" :
            if number2 == 0:
                print("Cannot divide by zero.")
            else:
                result = number1 / number2
                print(f"The result is {result}")
        case _:
            print("Invalid operation. Please choose +, -, *, or /.")
    
if __name__ == "__main__":
    calculator()