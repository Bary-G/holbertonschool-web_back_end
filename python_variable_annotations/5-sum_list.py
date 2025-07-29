#!/usr/bin/env python3
import typing
"""
Module: all Python modules
typing: a module used to define arguments types for type-annotated functions.
"""


def sum_list(input_list: typing.List[float]) -> float:
    """A type-annotated function sum_list which takes a list input_list of
    floats as argument and returns their sum as a float."""
    sum = 0.0
    for i in input_list:
        sum += i
    return (sum)
