#!/usr/bin/python3
"""Square that inherits from Rectangle module"""


class BaseGeometry:
    """
    class BaseGeometry with public instance methods def area(self)
    """
    def area(self):
        """public instance method that raises an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        you can assume name is always a string
        public instance method that validates value
        if value is not an integer, TypeError exception is raised
        if value is less/equal to 0, ValueError exception is raised
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """class Rectangle that inherits BaseGeometry"""
    def __init__(self, width, height):
        """Instantiation with width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        return f"[Rectangle] <{self.__width}/{self.__height}>"

    def area(self):
        return self.__width * self.__height


class Square(Rectangle):
    """class Square that inherits Rectangle"""
    def __init__(self, size):
        """Instantiation with size"""
        super().__init__(size, size) # Call parent constructor 
        self.__size = size

    def __str__(self):
        return f"[Square] <{self.__size}/{self.__size}>"

    def area(self):
        return self.__size * self.__size


if __name__ == "__main__":
    s = Square(13)

    print(s)
    print(s.area())
