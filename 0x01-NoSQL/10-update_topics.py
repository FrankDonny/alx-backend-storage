#!/usr/bin/env python3
"""module containing update_topics function"""


def update_topics(mongo_collection, name, topics):
    """function that changes all topics of a school document"""
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
