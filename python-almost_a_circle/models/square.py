#!/usr/bin/python3
"""Module Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return Class represent str"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Dictionary key/value to attributes"""
        if args:
            if args[0]:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
    def to_dictionary(self):
        """Dictionary representation"""
        return {'id': self.id, 'width': self.width, 'height': self.height
        , 'x': self.x, 'y': self.y}
