num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")
if operation == "+":
    sum = num1 + num2
    print("The result is", sum)
elif operation == "-":
    subtraction = num1 - num2
    print("The result is", subtraction)
elif operation == "*":
    product = num1 * num2
    print("The result is ",product)
elif operation == "/":
    if num2 == 0:
        print("Cannot divide by zero.")
    elif num2 != 0:
        division = num1 / num2
        print("The result is ",division)