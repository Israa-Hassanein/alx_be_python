class Book:
  """
  A class representing a book with title, author, and publication year.
  """

  def __init__(self, title, author, year):
    """
    Initializes a Book instance with title, author, and year.

    Args:
      title (str): The title of the book.
      author (str): The author of the book.
      year (int): The publication year of the book.
    """
    self.title = title
    self.author = author
    self.year = year

  def __del__(self):
    """
    Prints a message when the Book instance is deleted.
    """
    print(f"Deleting {self.title}")

  def __str__(self):
    """
    Returns a string representation of the book in a human-readable format.

    Returns:
      str: A string in the format "(title) by (author), published in (year)".
    """
    return f"{self.title} by {self.author}, published in {self.year}"

  def __repr__(self):
    """
    Returns a string representation of the Book instance for recreation.

    Returns:
      str: A string that can be used to create a new Book instance.
    """
    return f"Book('{self.title}', '{self.author}', {self.year})"

# Test the Book class (optional, can be removed)
if __name__ == "__main__":
  my_book = Book("1984", "George Orwell", 1949)
  print(my_book)  # Output: 1984 by George Orwell, published in 1949
  print(repr(my_book))  # Output: Book('1984', 'George Orwell', 1949)
  del my_book  # Triggers __del__ and prints "Deleting 1984"
