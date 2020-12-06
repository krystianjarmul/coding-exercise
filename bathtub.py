class Bathtub:
    """Class representing a bathtub object"""

    def __init__(self, colour: str) -> None:
        self.colour = colour

    @property
    def colour(self):
        return self._colour

    @colour.setter
    def colour(self, value):
        if not isinstance(value, str):
            raise ValueError
        self._colour = value
