#!/usr/bin/python3
"""Module Rectangle"""


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
        self.__width = width

    @property
    def width_ret(self):
        return self.__width

    @height.setter
    def height_setter(self, height):
        self.__height = height

    @property
    def height_ret(self):
        return self.__height

    @x.setter
    def x_setter(self, x):
        self.__x = x

    @property
    def x_ret(self):
        return self.__x

    @y.setter
    def y_setter(self, y):
        self.__y = y

    @property
    def y_ret(self):
        return self.__y
