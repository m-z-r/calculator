
# Display the calculator title
print("==============================")
print("      SIMPLE CALCULATOR")
print("==============================")

# Display the available mathematical operations
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

# Ask the user to choose an operation
choice = input("\nChoose an operation (1-4): ")

try:
    # Ask the user to enter two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Perform addition if the user chooses option 1
    if choice == "1":
        result = num1 + num2
        print("Result:", result)

    # Perform subtraction if the user chooses option 2
    elif choice == "2":
        result = num1 - num2
        print("Result:", result)

    # Perform multiplication if the user chooses option 3
    elif choice == "3":
        result = num1 * num2
        print("Result:", result)

    # Perform division if the user chooses option 4
    elif choice == "4":
        # Check whether the second number is zero
        if num2 == 0:
            print("Error: Cannot divide by zero!")
        else:
            result = num1 / num2
            print("Result:", result)

    # Handle an invalid menu choice
    else:
        print("Invalid choice! Please select an option from 1 to 4.")

# Handle inputs that cannot be converted into numbers
except ValueError:
    print("Invalid input! Please enter valid numbers.")

# Display a message when the program finishes
print("\nThank you for using the calculator!")
