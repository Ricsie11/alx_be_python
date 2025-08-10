import math

# Base class
class Shape:
    def area(self):
        """Method to be overridden by subclasses."""
        raise NotImplementedError("Subclasses must override area() method")


# Derived class for Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """Calculate area of rectangle."""
        return self.length * self.width


# Derived class for Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Calculate area of circle."""
        return math.pi * (self.radius ** 2)
