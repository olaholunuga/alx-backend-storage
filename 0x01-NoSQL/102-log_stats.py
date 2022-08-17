#!/usr/bin/env python3
""" 102-log_stats """
from pymongo import MongoClient

def log_stats(mongo_collection):
    """function to print nginx logs
    """
    print("{} logs".format(mongo_collection.count_documents()))
    print("methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        doc_count = mongo_collection.count_documents({"methods": method})
        print("\tmethod {}: {}".format(method, doc_count))
    status_count = mongo_collection.count_documents({"methods": "GET", "path": "/status"})
    print("{} status check".format(status_count))

def ip_aggregate(mongo_collection):
    """function to list ip aggregate
    """
    ip_list = mongo_collection.aggregate(
        [
            {
                "$group": {"_id": "$ip", "total": {"$sum":1}}
            },
            {
                "$limit":10
            },
            {
                "$sort":-1
            }
        ]
    )

def run():
    """ main function
    """
    client = MongoClient("mongodb://127.0.0.1:27017")
    nginx_collection = client.logs.nginx
    log_stats(nginx_collection)