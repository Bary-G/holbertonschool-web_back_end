#!/usr/bin/env python3
"""
Module:
A file that runs functions under Python3.
"""


def to_str(n: float) -> str:
    """A  type-annotated function to_str that takes a float n as argument and
    returns the string representation of the float."""
    if n >= 0:
        return int(n)
    elif n == int(n):
        return int(n) - 1
    else:
        return int(n) - 0
