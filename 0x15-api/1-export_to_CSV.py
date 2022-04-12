#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""getting data from an api
    Records all tasks that are owned by this employee
    Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
    File name must be: USER_ID.csv
    """

import requests
from sys import argv


def main():
    """this tis the main function"""

    user = \
        requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])).json()
    todo = \
        requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'.format(argv[1])).json()

    final = ''
    for x in todo:
        final = final + '"{}","{}","{}"\n'.format(x['userId'],
                x['completed'], x['title'])

    with open('USER_ID.csv', 'w') as f:
        f.write(final)


if __name__ == '__main__':
    main()
