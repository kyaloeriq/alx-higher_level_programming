#!/usr/bin/python3
class Square:
    """
    Defines a square
    """
    def __init__(self, size):
        """
        Initializes a new instance of a Square class
        Parameters:size (int): The size of the square
        """
        self.__size = size


if __name__ == "__main__":
    my_square = Square(3)
    print(type(my_square))
    print(my_square.__dict__)

    try:
        print(my_square.size)
    except Exception as e:
        print(e)

    try:    
        print(my_square.__size)
    except Exception as e:
        print(e)
