#!/usr/bin/python3

"""Defines the inherited class."""


def inherits_from(obj, a_class):
    """Checks if an object is the exaxt inherited instance of a class.

    Args:
        obj (any): The object to be checked out.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is an inherited instance of a_class - True.
        Otherwise - False.
    """
    
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
