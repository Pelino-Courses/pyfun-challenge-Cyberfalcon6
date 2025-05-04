from abc import ABC, abstractmethod
import math

class Shape(ABC):
    def __init__(self, name):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name must be a non-empty string.")
        self.name = name

    @abstractmethod
    def area(self):
        pass

    def __str__(self):
        return f"Shape: {self.name}"


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        if not isinstance(radius, (int, float)) or radius <= 0:
            raise ValueError("Radius must be a positive number.")
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"{super().__str__()}, Radius: {self.radius}, Area: {self.area():.2f}"


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("Rectangle")
        if not all(isinstance(dim, (int, float)) and dim > 0 for dim in (width, height)):
            raise ValueError("Width and height must be positive numbers.")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __str__(self):
        return f"{super().__str__()}, Width: {self.width}, Height: {self.height}, Area: {self.area():.2f}"


class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__("Triangle")
        if not all(isinstance(dim, (int, float)) and dim > 0 for dim in (base, height)):
            raise ValueError("Base and height must be positive numbers.")
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def __str__(self):
        return f"{super().__str__()}, Base: {self.base}, Height: {self.height}, Area: {self.area():.2f}"


if __name__ == "__main__":
    try:
        shapes = [
            Circle(5),
            Rectangle(4, 6),
            Triangle(3, 7)
        ]
        for shape in shapes:
            print(shape)
    except Exception as e:
        print(f"Error: {e}")