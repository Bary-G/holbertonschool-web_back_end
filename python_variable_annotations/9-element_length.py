#!/usr/bin/env python3
"""
Module: A file that runs functions under Python3.
typing: a module used to define arguments types for type-annotated functions.
Callable: a module used to call arguments in a function.
"""
import typing


def element_length(lst: typing.Iterable[typing.Sequence]) -> typing.List[typing.Tuple[typing.Sequence, int]]:
    """A type-annotated function element_length that takes a sequence lst
    as arguments and returns each elements and a float that represents their
    length into a tuple."""
    return [(i, len(i)) for i in lst]
