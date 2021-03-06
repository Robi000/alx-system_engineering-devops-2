#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""getting data from an api
"""

import json
import requests

user = requests.get('https://jsonplaceholder.typicode.com/users').json()

final = {}  # TODO: final [str(user[id])] = list_inner

list_inner = []  # TODO: list_inner.append(todo_dict)

todo_dict = {}

   # TODO: todo_dict["username"], todo_dict["task"], todo_dict["completed"]

for x in user:
    list_inner = []
    todo = \
        requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'.format(x['id'
                     ])).json()
    for y in todo:
        todo_dict = {}
        todo_dict['username'] = x['username']
        todo_dict['task'] = y['title']
        todo_dict['completed'] = y['completed']
        list_inner.append(todo_dict)
    final[str(x['id'])] = list_inner

with open('todo_all_employees.json', 'w') as file:
    json.dump(final, file, indent=2)
