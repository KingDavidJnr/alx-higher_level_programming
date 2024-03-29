#!/usr/bin/python3

"""Define the class Rectangle that inherits from a Base Geometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents the rectangle with Base Geometry."""

    def __init__(self, width, height):
        """Craetes a new Rectangle.

        Args:
            width (int): width of the new Rectangle.
            height (int): height of the new Rectangle.
        """

        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns the area value of a rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the print() and str() representation of a Rectangle."""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
