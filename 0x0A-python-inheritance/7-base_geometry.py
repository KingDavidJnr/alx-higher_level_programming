#!/usr/bin/python3

"""Defines the base geometry class."""


class BaseGeometry:
    """Represents the base geometry."""

    def area(self):
        """Not yet implemented for class."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validating the parameter as an integer.

        Args:
            name (str): name of the parameter.
            value (int): parameter to be validated.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
