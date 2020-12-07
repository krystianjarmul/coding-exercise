import typing as tp


class BathtubError(Exception):
    """A Exception raised when bathtub operation is invalid"""
    pass


class Bathtub:
    """Class representing a bathtub object"""

    def __init__(self, colour: str, brand: str, material: str, weight: int,
                 length: int, width: int, height: int, capacity: int) -> None:
        self.colour = colour
        self.brand = brand
        self.material = material
        self.weight = weight
        self.length = length
        self.width = width
        self.height = height
        self.capacity = capacity
        self.has_stopper_in = False

    def put_stopper(self):
        """Put stopper to the bathtub"""
        if self.has_stopper_in:
            raise BathtubError('Stopper is already in.')
        self.has_stopper_in = True

    @property
    def colour(self) -> str:
        return self._colour

    @colour.setter
    def colour(self, value: tp.Any) -> None:
        if not isinstance(value, str):
            raise ValueError('Invalid value of colour. String required.')
        self._colour = value

    @property
    def brand(self) -> str:
        return self._brand

    @brand.setter
    def brand(self, value: tp.Any) -> None:
        if not isinstance(value, str):
            raise ValueError('Invalid value of brand. String required.')
        self._brand = value

    @property
    def material(self) -> str:
        return self._material

    @material.setter
    def material(self, value: tp.Any) -> None:
        if not isinstance(value, str):
            raise ValueError('Invalid value of material. String required.')
        self._material = value

    @property
    def weight(self) -> int:
        return self._weight

    @weight.setter
    def weight(self, value: tp.Any) -> None:
        if not isinstance(value, int) or value <= 0:
            raise ValueError(
                'Invalid value of weight. Positive integer required.')
        self._weight = value

    @property
    def length(self) -> int:
        return self._length

    @length.setter
    def length(self, value: tp.Any) -> None:
        if not isinstance(value, int) or value <= 0:
            raise ValueError(
                'Invalid value of length. Positive integer required.')
        self._length = value

    @property
    def width(self) -> int:
        return self._width

    @width.setter
    def width(self, value: tp.Any) -> None:
        if not isinstance(value, int) or value <= 0:
            raise ValueError(
                'Invalid value of width. Positive integer required.')
        self._width = value

    @property
    def height(self) -> int:
        return self._height

    @height.setter
    def height(self, value: tp.Any) -> None:
        if not isinstance(value, int) or value <= 0:
            raise ValueError(
                'Invalid value of height. Positive integer required.')
        self._height = value

    @property
    def capacity(self) -> int:
        return self._capacity

    @capacity.setter
    def capacity(self, value: tp.Any) -> None:
        if not isinstance(value, int) or value <= 0:
            raise ValueError(
                'Invalid value of capacity. Positive integer required.')
        self._capacity = value
