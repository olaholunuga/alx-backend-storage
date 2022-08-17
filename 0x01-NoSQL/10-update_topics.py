#!/usr/bin/env python3
def update_topics(mongo_collection, name, topics):
    """mongo command to update document
    """
    result = mongo_collection.update_one({'name': name}, {'topics': topics})
    return