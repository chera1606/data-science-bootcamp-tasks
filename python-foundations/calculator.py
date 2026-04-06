# Python Foundations Assignment
# Level 3 Task: CLI-based Calculator

# function to add two numbers
def add(a, b):
    return a + b

# function to subtract two numbers
def subtract(a, b):
    return a - b

# function to multiply two numbers
def multiply(a, b):
    return a * b

# function to divide two numbers
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

# main program
def main():
    print("Simple CLI Calculator")
    print("Choose operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1-4): ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == "1":
        print("Result:", add(num1, num2))
    elif choice == "2":
        print("Result:", subtract(num1, num2))
    elif choice == "3":
        print("Result:", multiply(num1, num2))
    elif choice == "4":
        print("Result:", divide(num1, num2))
    else:
        print("Invalid choice")

# run the calculator
if __name__ == "__main__":
    main()