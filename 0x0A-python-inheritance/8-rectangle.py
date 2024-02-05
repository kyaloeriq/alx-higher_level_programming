#!/usr/bin/python3
"""Module for class Rectangle that inherits from BaseGeometry"""


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
        self.width = width
        self.height = height

    def __str__(self):
        return f"<{self.__class__.__name__} ({self.width})/{self.height}>"

    def area(self):
        return self.__width * self.__height


if __name__ == "__main__":
    r = Rectangle(3, 5)

    print(r)
    print(dir(r))

    try:
        print("Rectangle: {} - {}".format(r.width, r.height))
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        r2 = Rectangle(4, True)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
