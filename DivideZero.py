# buggy_script.py

    "Divide two numbers, returning None if division by zero is attempted."
    if b == 0:
        return None  # Handle division by zero
    return a / b

# Main function to trigger bugs
if __name__ == "__main__":
    # Bug 1: Division by zero
    print("Testing division function...")
    try:
        print(divide_numbers(10, 0))
    except ZeroDivisionError as e:
        print(f"Caught an error: {e}")

   
