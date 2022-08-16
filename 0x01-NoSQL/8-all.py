#!/usr/bin/env python3
def list_all(mongo_collection):
    """list all documents in mongodb collection
    """
    if mongo_collection is not None:
        return mongo_collection.find()
    return []