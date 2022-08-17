#!/usr/bin/env python3
""" 12-logs-stats """
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collect = client.logs.nginx

    n_logs = nginx_collect.count_documents()
    n_get_logs = nginx_collect.count_documents({'methods': "GET"})
    n_post_logs = nginx_collect.count_documents({'methods': "POST"})
    n_put_logs = nginx_collect.count_documents({'methods': "PUT"})
    n_patch_logs = nginx_collect.count_documents({'methods': "PATCH"})
    n_delete_logs = nginx_collect.count_documents({'methods': "DELETE"})
    n_status_logs = nginx_collect.count_documents({'methods': "GET", "path": "/status"})

    print("{} logs".format(n_logs))
    print("methods:\n\tmethod GET: {}".format(n_get_logs))
    print("\tmethod POST: {}".format(n_post_logs))
    print("\tmethod PUT: {}".format(n_put_logs))
    print("\tmethod PATCH: {}".format(n_patch_logs))
    print("\tmethod DELETE: {}".format(n_delete_logs))
    print("{} status check".format(n_status_logs))
