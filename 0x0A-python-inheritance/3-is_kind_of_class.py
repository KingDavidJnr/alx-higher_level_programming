#!/usr/bin/python3

"""Defines the class and inherited class functions."""


def is_kind_of_class(obj, a_class):
    """Check if the object is an instance or inherited instance of  particular class.

    Args:
        obj (any): The object to be checked.
        a_class (type): The class that must match the type of obj to.
    Returns:
        If obj is an instance or inherited instance of a_class - True.
        Otherwise - False.
    """
    
    if isinstance(obj, a_class):
        return True
    return False
