import math 

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius


# Example usage
if __name__ == "__main__":
    circle = Circle(5)
    print(f"Radius: {circle.radius}")
    print(f"Area: {circle.area()}")
    print(f"Perimeter: {circle.perimeter()}")