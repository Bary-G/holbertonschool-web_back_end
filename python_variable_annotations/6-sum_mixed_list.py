#!/usr/bin/env python3
"""
Module: A type-annotated function sum_mixed_list which takes a list
mxd_lst of floats as argument and returns their sum as a float
typing: This module is used to annotate in a list
"""
import typing


def sum_mixed_list(mxd_lst: typing.List[typing.Union[float]]) -> float:
    """
    A type-annotated function sum_mixed_list which takes a list
    mxd_lst of floats as argument and returns their sum as a float
    """
    return sum(mxd_lst)
