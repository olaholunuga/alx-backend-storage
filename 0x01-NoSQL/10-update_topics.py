#!/usr/bin/env python3
"""update function
"""


def update_topics(mongo_collection, name, topics):
    """mongo command to update document
    """
    mongo_collection.update_many({"name": name}, {"topics": topics})
