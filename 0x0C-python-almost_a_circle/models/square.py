#!/usr/bin/python3
"""The Square Module"""
from rectangle import Rectangle


class Square(Rectangle):
    """class Square that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes the square with a specified size"""
        super().__init__(size, size, x, y, id)  # Base handles id assignment

    @property
    def size(self):
        """Provides a getter and setter method for the size"""
        return self.width

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        """provides custom string representation of square object"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
    def update(self, *args, **kwargs):
        """assigns a key/value argument to attributes"""
        if args:
            if len(args) >= 1:
                self.set_id(args[0])  # Set ID if provided
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    self.set_id(value)
                elif key == 'size':
                    self.size = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value


if __name__ == "__main__":

    s1 = Square(5)
    print(s1)

    s1.update(10)
    print(s1)

    s1.update(1, 2)
    print(s1)

    s1.update(1, 2, 3)
    print(s1)

    s1.update(1, 2, 3, 4)
    print(s1)

    s1.update(x=12)
    print(s1)

    s1.update(size=7, y=1)
    print(s1)

    s1.update(size=7, id=89, y=1)
    print(s1)
