#!/usr/bin/env python3
""" 11-school """

def schools_by_topic(mongo_collection, topic):
    """list schools by topic
    """
    return mongo_collection.find({'topics': {'$in': [topic]}})