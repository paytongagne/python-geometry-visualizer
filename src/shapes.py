from __future__ import annotations

from dataclasses import dataclass
from math import pi, sqrt


def require_positive(value: float, name: str) -> None:
    if value <= 0:
        raise ValueError(f"{name} must be positive")


@dataclass(frozen=True)
class Rectangle:
    width: float
    height: float

    def __post_init__(self) -> None:
        require_positive(self.width, "width")
        require_positive(self.height, "height")

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)


@dataclass(frozen=True)
class Circle:
    radius: float

    def __post_init__(self) -> None:
        require_positive(self.radius, "radius")

    def area(self) -> float:
        return pi * self.radius ** 2

    def perimeter(self) -> float:
        return 2 * pi * self.radius


@dataclass(frozen=True)
class Triangle:
    side_a: float
    side_b: float
    side_c: float

    def __post_init__(self) -> None:
        require_positive(self.side_a, "side_a")
        require_positive(self.side_b, "side_b")
        require_positive(self.side_c, "side_c")
        if self.side_a + self.side_b <= self.side_c or self.side_a + self.side_c <= self.side_b or self.side_b + self.side_c <= self.side_a:
            raise ValueError("triangle sides do not satisfy triangle inequality")

    def perimeter(self) -> float:
        return self.side_a + self.side_b + self.side_c

    def area(self) -> float:
        semi_perimeter = self.perimeter() / 2
        return sqrt(
            semi_perimeter
            * (semi_perimeter - self.side_a)
            * (semi_perimeter - self.side_b)
            * (semi_perimeter - self.side_c)
        )
