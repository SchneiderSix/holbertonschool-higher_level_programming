#!/usr/bin/python3
"""Class Square."""


class Square:
    """Square
    Attributes:
        __size (int): size of square's side
        __position (tuple): position of square
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the square
        Args:
            size (int): size of square's side
            position (tuple): position of square
        Returns:
            None
        """
        self.__size = size
        self.__position = position

    def area(self):
        """Size squared
        Returns:
            The area of the square
        """
        return self.__size ** 2

    @setter
    def size(self, value):
        """Setter
        Args:
            value (int): size of square's side
        Returns:
            None
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @setter_position
        def position(self, value):
            """Setter position
            Args:
                value (tuple): tuple for position
            Returns:
                None
            """
            if len(value) != 2 or type(value) is not tuple or type(value[0]) is not int or type(value[1] is not int or value[0] < 0 or value[1] < 0:
                raise TypeError("position must be a tuple of 2 positive integers")
            else:
                self.__position = value


    @retrieve_size
    def size(self):
        """Getter
        Returns: Size
        """
        return self.__size
        
    @retrieve_position
    def position(self):
        """Getter position
        Returns: Position
        """
        return self.__position

    def my_print(self):
        """Prints square
        Returns: None
        """
        if self.__size == 0:
            print()
            return None
        else:
            for i in range(1, self.area() + 1):
                for j in range(1, self.area() + 1):
                    print("#", end="")
