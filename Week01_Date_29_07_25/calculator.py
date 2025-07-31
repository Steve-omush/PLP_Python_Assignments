def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def main():
    #List of supported operations
    operations = ['+', '-', '*', '/']

    try:
        #Get user input
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        operation = input("Enter an operation (+, -, *, /): ")

        if operation not in operations:
            raise ValueError("Invalid operation")
        if operation == '/' and num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero")

        result = None

        if operation == '+':
            result = add(num1, num2)
        elif operation == '-':
            result = subtract(num1, num2)
        elif operation == '*':
            result = multiply(num1, num2)
        elif operation == '/':
            result = divide(num1, num2)

        print(f"{num1} {operation} {num2} = {result}")



    except ValueError as ve:
        print(f"ValueError: {ve}")
        exit(1)

    except ZeroDivisionError as zde:
        print(f"ZeroDivisionError: {zde}")
        exit(1)

    except Exception as e:
        print(f"An error occurred: {e}")
        exit(1)


if __name__ == "__main__":
    main()