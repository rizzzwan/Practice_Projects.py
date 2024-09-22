import matplotlib.pyplot as plt

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

def visualize_operation(operation, num1, num2, result):
    plt.figure(figsize=(6, 4))
    labels = ['First Number', 'Second Number', 'Result']
    values = [num1, num2, result]
    
    plt.bar(labels, values, color=['blue', 'green', 'orange'])
    plt.title(f'{operation.capitalize()} Operation')
    plt.ylabel('Values')
    plt.show()

def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    choice = input("Enter choice (1/2/3/4): ")
    
    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if choice == '1':
            result = add(num1, num2)
            operation = 'add'
        elif choice == '2':
            result = subtract(num1, num2)
            operation = 'subtract'
        elif choice == '3':
            result = multiply(num1, num2)
            operation = 'multiply'
        elif choice == '4':
            result = divide(num1, num2)
            if result == "Error! Division by zero.":
                print(result)
                return
            operation = 'divide'
        
        print(f"The result of {operation} operation is: {result}")
        visualize_operation(operation, num1, num2, result)
    else:
        print("Invalid input")

# Run the calculator
calculator()
