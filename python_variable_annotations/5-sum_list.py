#!/usr/bin/env python3
"""
Module: A type-annotated function sum_list which takes a list
input_list of floats as argument and returns their sum as a float
typing: This module is used to annotate in a list
"""
import typing


def sum_list(input_list: typing.List[float]) -> float:
    """
    A type-annotated function sum_list which takes a list
    input_list of floats as argument and returns their sum as a float
    """
    return sum(input_list)
