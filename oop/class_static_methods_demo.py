class Calculator:
  """
  A class for performing simple arithmetic operations.
  """
  calculation_type = "Arithmetic Operations"  # Class attribute

  @staticmethod
  def add(a, b):
    """
    Static method to perform addition of two numbers.

    Args:
      a (int): The first number.
      b (int): The second number.

    Returns:
      int: The sum of a and b.
    """
    return a + b

  @classmethod
  def multiply(cls, a, b):
    """
    Class method to perform multiplication of two numbers.

    Args:
      cls (class): The Calculator class itself.
      a (int): The first number.
      b (int): The second number.

    Returns:
      int: The product of a and b.
    """
    print(f"Calculation type: {cls.calculation_type}")
    return a * b

# Test the Calculator class (optional, can be removed)
if __name__ == "__main__":
  sum_result = Calculator.add(10, 5)
  print(f"The sum is: {sum_result}")

  product_result = Calculator.multiply(10, 5)
  print(f"The product is: {product_result}")