#!/usr/bin/env python3
"""
Module: A type-annotated function element_length that takes an iterable
sequence as argument and returns a tuple
"""
import typing


def element_length(lst: typing.Iterable[typing.Sequence]) -> typing.List[typing.Tuple[typing.Sequence, int]]:
    """
    A type-annotated function element_length that takes an iterable
    sequence as argument and returns a tuple
    """
    return [(i, len(i)) for i in lst]
