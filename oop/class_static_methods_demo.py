class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a: float, b: float) -> float:
        """Static method to add two numbers."""
        return a + b

    @classmethod
    def multiply(cls, a: float, b: float) -> float:
        """Class method to multiply two numbers."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b

# Example usage (optional)
if __name__ == "__main__":
    # Testing the static method
    result_add = Calculator.add(5, 3)
    print(f"Addition result: {result_add}")

    # Testing the class method
    result_multiply = Calculator.multiply(5, 3)
    print(f"Multiplication result: {result_multiply}")
