"""
File.
"""


class ProgrammingLanguage:
    """Represent a Programming Language object."""
    def __init__(self,name, typing, reflection, year):
        """Initialise a ProgrammingLanguage instance."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return a string representation of ProgrammingLanguage instance."""
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(self.name,
                                                                           self.typing, self.reflection, self.year)

    def is_dynamic(self):
        """Return whether the ProgrammingLanguage typing is dynamic."""
        return self.typing.lower() == "dynamic"
