#!/usr/bin/python3
"""getting data from an api
    """

import requests
from sys import argv


def main():
    """this tis the main function"""

    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(
        argv[1])).json()
    todo = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}/todos".format(
            argv[1])).json()

    final = ""
    for x in todo:
        final = final + "\"{}\",\"{}\",\"{}\"\n".format(
            x["userId"], x["completed"], x["title"])

    with open(str(user["id"]) + ".csv", "w") as f:
        f.write(final)


if __name__ == "__main__":
    main()
