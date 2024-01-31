#!/usr/bin/python3
"""returns a new Rectangle instance with width == height == size"""


class Rectangle:
    """class Rectangle that defines a rectangle"""

    """A class variable, counting the number of rectangles"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Instantiation with optional width and height"""
        self.__width = width
        self.__height = height
        self.print_symbol = Rectangle.print_symbol  # Initialize print_symbol
        Rectangle.number_of_instances += 1  # Incremented during instantiation

    @property
    def width(self):
        """Retrieve the value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the value of width with validation"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the value of height with validation"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width + self.__height) * 2

    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """returns a new Rectangle instance with width == height == size"""
        return cls(size, size)

    def my_print(self):
        """prints in stdout the rectangle with character at print_symbol"""
        if self.__width == 0 or self.__height == 0:
            print()
        else:
            for _ in range(self.__height):
                print(self.print_symbol * self.__width)

    def __str__(self):
        """String representation of the rectangle"""
        self.my_print()
        return ""

    def __repr__(self):
        """Official string representation of the rectangle"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """instance is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1  # instance deletion


if __name__ == "__main__":
    my_square = Rectangle.square(5)
    print("Area: {} - Perimeter: {}".format(
        my_square.area(), my_square.perimeter()))
    print(my_square)
