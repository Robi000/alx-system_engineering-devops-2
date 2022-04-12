#!/usr/bin/python3
"""getting data from an api
"""

import requests
from sys import argv

user = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(
    argv[1])).json()
todo = requests.get(
    "https://jsonplaceholder.typicode.com/users/{}/todos".format(
        argv[1])).json()

final = ""
for x in todo:
    final = final + "\"{}\",\"{}\",\"{}\"\n".format(x["userId"],
                                                    x["completed"], x["title"])

with open("USER_ID.csv", "w") as f:
    f.write(final)
