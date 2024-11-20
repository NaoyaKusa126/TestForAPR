# buggy_script.py

def divide_numbers(a, b):
    """Divide two numbers with division by zero check."""
    if b == 0:
        return 'Error: Division by zero is not allowed'
    return a / b

# Main function to trigger bugs
if __name__ == "__main__":
    # Bug 1: Division by zero
    print("Testing division function...")
    try:
        print(divide_numbers(10, 0))
    except ZeroDivisionError as e:
        print(f"Caught an error: {e}")

   
