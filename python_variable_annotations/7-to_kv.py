#!/usr/bin/env python3
"""
Module: A file that runs functions under Python3.
typing: a module used to define arguments types for type-annotated functions.
"""
import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    """A type-annotated function to_kv that takes a string k and an int OR
    float v as arguments and returns a tuple. The first element of the tuple
    is the string k."""
    v = v * v
    AssembledTuple = (k, v)
    return (AssembledTuple)
