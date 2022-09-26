#!/usr/bin/python3
# 1-my_list.py
# Adamu Clement <adamuclementjatau@gmail.com>
"""Defines an inherited list class Mylist."""

class Mylist(list):
    """Implement sorted printing for the buil-in list class."""

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))
