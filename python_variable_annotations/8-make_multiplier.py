#!/usr/bin/env python3
"""
Module: A file that runs functions under Python3.
typing: a module used to define arguments types for type-annotated functions.
Callable: a module used to call arguments in a function.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """A type-annotated function to_kv that takes a string k and an int OR
    float v as arguments and returns a tuple. The first element of the tuple
    is the string k."""
    def multiplier_func(x: float) -> float:
        return x * multiplier
    return (multiplier)

