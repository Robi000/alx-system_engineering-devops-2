#!/usr/bin/python3
"""getting data from an api
"""

import requests
from sys import argv

if __name__ == '__main__':
    endpoint = "https://jsonplaceholder.typicode.com/users"
    userId = argv[1]
    user = requests.get(endpoint)
    todo = requests.get(endpoint)
    print(user)
