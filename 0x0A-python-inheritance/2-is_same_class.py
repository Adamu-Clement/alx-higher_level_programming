#!/usr/bin/python3
# 2-is_same_class.py
#  Adamu Clement  <adamuclementjatau@gmail.com>
"""Defines a class-checking function."""

def is_same_class(obj, a_class):
    """Cehck if an object is exactly an instance of a given class.

    Args:
        obj (any): The objects to check. 
        a_class (type): The class to match the type of the obj to.
    Returns:
        if obj is exactly an instance of a_class - True. 
        otherwise - False.
    """
    if type(obj) == a_class:
        return True 
    return False 

