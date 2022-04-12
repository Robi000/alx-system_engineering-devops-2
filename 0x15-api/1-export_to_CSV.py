#!/usr/bin/python3
"""this wis well documentd file 
    """

import requests
from sys import argv

user = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(
    argv[1])).json()
todo = requests.get(
    "https://jsonplaceholder.typicode.com/users/{}/todos".format(
        argv[1])).json()

countx = 0
for y in todo:
    if y["completed"] == True:
        countx += 1

print("Employee {} is done with tasks({}/{}):".format(user["name"], countx,
                                                      len(todo)))
for y in todo:
    if y["completed"] == True:
        print("\t ", y["title"])
