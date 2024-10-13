class Book:
    def __init__(self, title: str, author: str, year: int):
        """Constructor to initialize a Book instance."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor to print a message when a Book instance is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self) -> str:
        """Return a string representation of the Book."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self) -> str:
        """Return an official string representation of the Book."""
        return f"Book('{self.title}', '{self.author}', {self.year})"

# To test the Book class, create a separate main.py as provided in the task description.
