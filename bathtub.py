import typing as tp


class Bathtub:
    """Class representing a bathtub object"""

    def __init__(self, colour: str, brand: str) -> None:
        self.colour = colour
        self.brand = brand

    @property
    def colour(self) -> str:
        return self._colour

    @colour.setter
    def colour(self, value: tp.Any) -> None:
        if not isinstance(value, str):
            raise ValueError
        self._colour = value

    @property
    def brand(self) -> str:
        return self._brand

    @brand.setter
    def brand(self, value: tp.Any) -> None:
        if not isinstance(value, str):
            raise ValueError
        self._brand = value
