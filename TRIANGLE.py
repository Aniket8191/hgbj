# Function to perform operations
def calculate_operations(a, b):
    # Perform arithmetic operations
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    division = a / b if b != 0 else "Undefined (division by zero)"
    modulus = a % b if b != 0 else "Undefined (modulus by zero)"
    exponentiation = a ** b

    # Return results
    return {
        "Addition": addition,
        "Subtraction": subtraction,
        "Multiplication": multiplication,
        "Division": division,
        "Modulus": modulus,
        "Exponentiation": exponentiation,
    }

# Input numbers
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Calculate results
    results = calculate_operations(num1, num2)

    # Display results
    print("\nResults:")
    for operation, result in results.items():
        print(f"{operation}: {result}")

except ValueError:
    print("Invalid input! Please enter numeric values.")

