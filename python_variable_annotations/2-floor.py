#!/usr/bin/env python3
"""
Module:
A file that runs functions under Python3.
"""


def floor(n: float) -> int:
    """A type-annotated function floor which takes a float n as argument and
    returns the floor of the float."""
    if n >= 0:
        return int(n)
    elif n == int(n):
        return int(n) - 1
    else:
        return int(n) - 0
