#!/usr/bin/python3
"""accesses and updates private attribute"""


class Square:
    """instance attribute"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """retrieves value of size"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets value of size with validation"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns the current square area"""
        return self.__size**2


if __name__ == "__main__":
    my_square = Square(89)
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))

    my_square.size = 3
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))

    try:
        my_square.size = "5 feet"
        print("Area: {} for size: {}".format(my_square.area(), my_square.size))
    except Exception as e:
        print(e)
