
class Guitar():
    """Represents a guitar object."""

# TODO: Make current_year a class constant.

    def __init__(self, name, year, cost, current_year=2017):
        """Initialize Guitar class."""
        self.name = name
        self.year = year
        self.cost = cost
        self.current_year = current_year

    def __str__(self):
        return "{} ({}) : {}".format(self.name, self.year, self.cost)

    def get_age(self):
        """
        Returns the age of the guitar.
        """
        return self.current_year - self.year

    def is_vintage(self):
        """Returns whether or not the guitar is over 50 years old."""
        return self.get_age() > 50
