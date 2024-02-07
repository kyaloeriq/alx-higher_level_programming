#!/usr/bin/python3
"""dictionary description for JSON serialization of an object module"""


""" My class module
"""


class MyClass:
    """ My class
    """

    def __init__(self, name):
        self.name = name
        self.number = 0

    def __str__(self):
        return "[MyClass] {} - {:d}".format(self.name, self.number)

    @staticmethod
    def class_to_json(obj):
        """
        returns the dictionary description with simple data structure,
        (list, dict, string, integer, boolean)for JSON serialization of obj
        obj is an instance of a Class
        attributes of the obj Class are serializable
        """
        serialized = "{"
        serialized += '"name": "{}", '.format(obj.name)
        serialized += '"number": {:d}'.format(obj.number)
        serialized += "}"
        return serialized


if __name__ == "__main__":
    m = MyClass("John")
    m.number = 89
    print(type(m))
    print(m)

    mj = MyClass.class_to_json(m)
    print(type(mj))
    print(mj)
