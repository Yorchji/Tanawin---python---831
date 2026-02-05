class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # Method to get the area
    def get_area(self):
        return self.length * self.width

    # Method to get the perimeter
    def get_perimeter(self):
        perimeter = self.length + self.width * 2
        return perimeter


rect = Rectangle(10, 5)
print(rect.get_area())       # Should print 50
print(rect.get_perimeter())  # Should print 30
