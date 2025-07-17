"""
Class for programming languages
Estimated: 20 mins
Actual: 30 mins
"""

class ProgrammingLanguage:
    """Class for programming languages."""
    def __init__(self, name="", typing ="", reflection="", year=0):
        """Create programming language from values"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Determine language is Dynamic."""
        return self.typing == "Dynamic"

    def __str__(self):
        """Return string representation of programming language."""
        return (f"{self.name}, {self.typing} Typing, "
                f"Reflection={self.reflection}, First appeared in {self.year}")
