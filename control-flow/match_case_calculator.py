num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operator = input("Choose the operation (+, -, *, /): ")
if operator == "+":
    sum = num1 + num2
    print("The result is", sum)
elif operator == "-":
    subtraction = num1 - num2
    print("The result is", subtraction)
elif operator == "*":
    product = num1 * num2
    print("The result is ",product)
elif operator == "/":
    if num2 == 0:
        print("Cannot divide by zero.")
    elif num2 != 0:
        division = num1 / num2
        print("The result is ",division)