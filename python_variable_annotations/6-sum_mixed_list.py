#!/usr/bin/env python3
import typing
"""
Module: all Python modules
typing: a module used to define arguments types for type-annotated functions.
"""


def sum_mixed_list(mxd_lst: typing.List[typing.Union[int, float]]) -> float:
    """A type-annotated function sum_mixed_list which takes a list mxd_lst of
    integers and floats and returns their sum as a float."""
    sum = 0.0
    for i in mxd_lst:
        sum += i
    return (sum)
