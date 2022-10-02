#!/usr/bin/python3
"""Module Rectangle"""
from .base import Base


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
    def width_setter(self, value):
        """Setter for width"""

        self.__width = value

    @property
    def width_getter(self):
        """Getter for width"""

        return self.__width

    @height.setter
    def height_setter(self, value):
        """Setter for height"""

        self.__height = value

    @property
    def height_getter(self):
        """Getter for height"""

        return self.__height

    @x.setter
    def x_setter(self, value):
        """Setter for x"""

        self.__x = value

    @property
    def x_getter(self):
        """Getter for x"""

        return self.__x

    @y.setter
    def y_setter(self, value):
        """Setter for y"""

        self.__y = value

    @property
    def y_getter(self):
        """Getter for y"""

        return self.__y
