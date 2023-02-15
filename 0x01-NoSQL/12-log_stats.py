#!/usr/bin/env python3
"""script that provides some stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx
    totalCount = []
    statsCheck = 0
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        count = collection.count_documents({"method": f"{method}"})
        totalCount.append(f"method {method}: {count}")
        if method == "GET":
            statsCheck = collection.count_documents(
                {"method": f"{method}", "path": "/status"})
    print(f"{collection.count_documents({})} logs")
    print(
        f"Methods:\n"
        f"{totalCount[0]}\n\t"
        f"{totalCount[1]}\n\t{totalCount[2]}\n\t"
        f"{totalCount[3]}\n\t{totalCount[4]}")
    print(f"{statsCheck} status check")
