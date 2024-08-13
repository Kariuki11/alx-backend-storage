#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon July 17 16:00:00 2023

@Author: Nicanor Kyamba
"""
from pymongo import MongoClient


if __name__ == "__main__":
    """
    Prints the total number of logs and the number
    of logs for each method
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_collection = client.logs.nginx

    """Get the total number of logs"""
    total_logs = logs_collection.count_documents({})
    print(f"{total_logs} logs")

    """Get the number of logs for each method"""
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = logs_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    """Get the number of logs with method=GET and path=/status"""
    count_status_check = logs_collection.count_documents(
            {"method": "GET",
             "path": "/status"
             })
    print(f"{count_status_check} status check")
