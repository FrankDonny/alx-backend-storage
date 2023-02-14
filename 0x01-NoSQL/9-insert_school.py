#!/usr/bin/env python3
"""module containing insert_school function"""


def insert_school(mongo_collection, **kwargs):
    """function to insert document to a collection"""
    theID = mongo_collection.insert_one(kwargs).inserted_id
    return theID
