#!/usr/bin/env python3
"""module containing top_students function"""


def top_students(mongo_collection):
    """function that returns all students sorted by average score"""
    students = mongo_collection.find({})
    for student in students:
        sum = 0
        for topic in student['topics']:
            sum += topic['score']
        mongo_collection.update_one({"name": student['name']}, {
                                    "$set": {"averageScore":
                                             sum/len(student['topics'])}})
    return mongo_collection.find({}).sort("averageScore", -1)
