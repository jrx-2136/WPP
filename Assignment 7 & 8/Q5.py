import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement area method")
    
    def perimeter(self):
        raise NotImplementedError("Subclasses must implement perimeter method")

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius

# Example usage:
if __name__ == "__main__":
    rect = Rectangle(10, 5)
    circle = Circle(7)
    
    print("Rectangle Area:", rect.area())
    print("Rectangle Perimeter:", rect.perimeter())
    print("Circle Area:", circle.area())
    print("Circle Perimeter:", circle.perimeter())
