#!/usr/bin/env python3
"""list function
"""


def list_all(mongo_collection):
    """list all documents in mongodb collection
    """
    result = mongo_collection.find()
    return result
