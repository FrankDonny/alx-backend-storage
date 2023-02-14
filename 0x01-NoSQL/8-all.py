#!/usr/bin/env python3
"""module containing list_all function"""


def list_all(mongo_collection):
    """return a list of all documents in a collection"""
    if mongo_collection.count_documents == 0:
        return []
    return list(mongo_collection.find())
