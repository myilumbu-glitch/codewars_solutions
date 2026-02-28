def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


history = []   # create history BEFORE loop


while True:
    operation = input("Choose operation (+, -, *, /, h for history, q to quit): ")

    if operation == 'q':
        break

    if operation == 'h':
        print("History:", history)
        continue

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if operation == '+':
        result = add(a, b)
    elif operation == '-':
        result = subtract(a, b)
    elif operation == '*':
        result = multiply(a, b)
    elif operation == '/':
        result = divide(a, b)
    else:
        print("Invalid operation")
        continue

    print(result)
    history.append(result)

