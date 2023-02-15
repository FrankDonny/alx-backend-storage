#!/usr/bin/env python3
"""module containing top_students function"""


def top_students(mongo_collection):
    """function that returns all students sorted by average score"""
    students = mongo_collection.find({})
    # print("\nstart\n")
    # print([student["topics"] for student in students])
    # print("\nend\n")
    # return [student for student in students]
    studentDetail = []
    for student in students:
        sum = 0
        for topic in student['topics']:
            sum += topic['score']
        studentDetail.append(
            {"name": student['name'], "avg": sum/len(student['topics'])})
    studentDetail.sort(key=lambda x: x["avg"])
    return [studentDetail]
    # return [student for student in students]
