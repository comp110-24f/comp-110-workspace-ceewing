"""File to define Fish class."""


class Fish:
    """Fish class."""

    age: int

    def __init__(self):
        """Init for fish."""
        self.age = 0
        return None

    def one_day(self):
        """One day for fish."""
        self.age = +1
        return None
