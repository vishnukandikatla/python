class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

# Create objects
r1 = Rectangle(10, 5)
r2 = Rectangle(7, 3)

# Show results
print("Rectangle 1 -> Area:", r1.area(), ", Perimeter:", r1.perimeter())
print("Rectangle 2 -> Area:", r2.area(), ", Perimeter:", r2.perimeter())
