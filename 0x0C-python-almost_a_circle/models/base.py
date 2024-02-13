#!/usr/bin/python3
"""The base Module"""


class Base:
    """The Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Instantiation with id"""
        if id is not None:
            self.__id = id
        else:
            Base.__nb_objects += 1
            self.__id = Base.__nb_objects

    @property
    def id(self):
        return self.__id

    def set_id(self, new_id):
        """Method to set the id"""
        self.__id = new_id


if __name__ == "__main__":
    b1 = Base()
    print(b1.id)

    b2 = Base()
    print(b2.id)

    b3 = Base()
    print(b3.id)

    b4 = Base(12)
    print(b4.id)

    b5 = Base()
    print(b5.id)
