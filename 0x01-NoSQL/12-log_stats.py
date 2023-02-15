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
    print("Methods:")
    print(f"\t{totalCount[0]}")
    print(f"\t{totalCount[1]}")
    print(f"\t{totalCount[2]}")
    print(f"\t{totalCount[3]}")
    print(f"\t{totalCount[4]}")
    print(f"{statsCheck} status check")
