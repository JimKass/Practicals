
class Guitar():
    """
    Represents a guitar object.
    """

    def __init__(self, name, year, cost):
        """
        Initialize Guitar class.
        """
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{} ({}) : {}".format(self.name, self.year, self.cost)
