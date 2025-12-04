#!/usr/bin/env python3
"""
Module file with test functions
"""


def insert_school(mongo_collection, **kwargs):
    """Insert a new document in a collection based on kwargs"""
    if mongo_collection is None:
        return []
    if kwargs is None:
        return mongo_collection
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
