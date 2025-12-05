#!/usr/bin/env python3
"""
Module file with test functions
"""


def update_topics(mongo_collection, name, topics):
    """Change all topics of a school document based on the name"""
    if mongo_collection is None:
        return []
    if not name or not topics:
        return mongo_collection
    result = mongo_collection.update_many(
        {"name": name}, {"$set": {"topics": topics}}
    )
    return result
