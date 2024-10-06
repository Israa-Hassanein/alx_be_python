def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        denom = float(denominator)
        if denom == 0:
            return "Error: Cannot divide by zero."
        return f"The result of the division is {num / denom:.1f}".rstrip('0').rstrip('.')
    except ValueError:
        return "Error: Please enter numeric values only."

if __name__ == "__main__":
    # Example usage for testing
    print(safe_divide(10, 5))
