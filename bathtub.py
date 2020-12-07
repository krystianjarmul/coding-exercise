import typing as tp


class Bathtub:
    """Class representing a bathtub object"""

    def __init__(self, colour: str, brand: str, material: str,
                 weight: int) -> None:
        self.colour = colour
        self.brand = brand
        self.material = material
        self.weight = weight

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
