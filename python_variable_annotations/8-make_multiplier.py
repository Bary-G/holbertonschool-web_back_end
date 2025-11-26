#!/usr/bin/env python3
"""
Module: A type-annotated function make_multiplier that takes a float
multiplier as argument and returns a function that multiplies
a float by multiplier
"""
import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """
    A type-annotated function make_multiplier that takes a float
    multiplier as argument and returns a function that multiplies
    a float by multiplier
    """
    def multiply(x: float) -> float:
        return x * multiplier
    return multiply
