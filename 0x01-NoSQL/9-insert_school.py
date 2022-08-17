#!/usr/bin/env python3
"""insert function
"""


def insert_school(mongo_collection, **kwargs):
    """mongodb insert command
    """
    one_doc = mongo_collection.insert_one(kwargs)
    return one_doc.inserted_id
