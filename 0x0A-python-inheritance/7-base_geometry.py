#!/usr/bin/python3
"""Geometry module with public instance methods def area(self)"""


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


if __name__ == "__main__":
    bg = BaseGeometry()

    bg.integer_validator("my_int", 12)
    bg.integer_validator("width", 89)

    try:
        bg.integer_validator("name", "John")
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        bg.integer_validator("age", 0)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        bg.integer_validator("distance", -4)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
