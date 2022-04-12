#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''Module 1-export_to_CSV
Exports data got from API to CSV'''


import requests
from sys import argv
import json


def main():
    """this is main funtion to get run 
    """

    user = \
        requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])).json()
    todo = \
        requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'.format(argv[1])).json()

    final = {}
    list_inner = []

    for x in todo:
        inner_todo = {}
        inner_todo['task'] = x['title']
        inner_todo['completed'] = x['completed']
        inner_todo['username'] = user['username']
        list_inner.append(inner_todo)

    final[str(user['id'])] = list_inner

    with open('USER_ID.json', 'w') as file:
        json.dump(final, file, indent=2)


if __name__ == '__main__':
    main()
