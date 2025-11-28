#!/usr/bin/env python3
"""
Module: A type-annotated function element_length that takes an iterable
sequence as argument and returns a tuple
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    A type-annotated function element_length that takes an iterable
    sequence as argument and returns a tuple
    """
    return [(i, len(i)) for i in lst]
