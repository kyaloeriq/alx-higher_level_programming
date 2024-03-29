#!/usr/bin/python3
"""Instances module"""


class Rectangle:
    """class Rectangle that defines a rectangle"""

    """A class variable, counting the number of rectangles"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Instantiation with optional width and height"""
        self.__width = width
        self.__height = height
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

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__width == 0 or self.__height == 0:
            print()
        else:
            for _ in range(self.__height):
                print("#" * self.__width)

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
    my_rectangle_1 = Rectangle(2, 4)
    my_rectangle_2 = Rectangle(2, 4)
    print("{:d} instances of Rectangle".format(
        Rectangle.number_of_instances))
    del my_rectangle_1
    print("{:d} instances of Rectangle".format(
        Rectangle.number_of_instances))
    del my_rectangle_2
    print("{:d} instances of Rectangle".format(
        Rectangle.number_of_instances))
