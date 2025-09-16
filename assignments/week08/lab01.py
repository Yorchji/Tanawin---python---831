class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def get_area(self):
        return self.__length * self.__width
    
    def get_perimeter(self):
        perimeter = self.__length + self.__width * 2
        return perimeter
    
    def isSquare(self):
        return self.__length == self.__width
    
rect = Rectangle(50,80)
print(rect.get_area())
print(rect.get_perimeter())
print(rect.isSquare())
        

