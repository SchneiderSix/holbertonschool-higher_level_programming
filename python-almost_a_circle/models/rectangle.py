#!/usr/bin/python3
"""Module Rectangle"""
from models.base import Base


class Rectangle(Base):
    """Class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor"""

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @width.setter
    def width_setter(self, width):
        """Setter for width"""

        self.__width = width

    @property
    def width_getter(self):
        """Getter for width"""

        return self.__width

    @height.setter
    def height_setter(self, height):
        """Setter for height"""

        self.__height = height

    @property
    def height_getter(self):
        """Getter for height"""

        return self.__height

    @x.setter
    def x_setter(self, x):
        """Setter for x"""

        self.__x = x

    @property
    def x_getter(self):
        """Getter for x"""

        return self.__x

    @y.setter
    def y_setter(self, y):
        """Setter for y"""

        self.__y = y

    @property
    def y_getter(self):
        """Getter for y"""

        return self.__y
