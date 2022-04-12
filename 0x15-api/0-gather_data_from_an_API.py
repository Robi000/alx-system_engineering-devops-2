#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
from sys import argv

"""this wis well documentd file 
    """

user = \
    requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])).json()  # this is where we find user interface
todo = \
    requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'.format(argv[1])).json()  # this is where we find to do list

countx = 0
for y in todo:  # this is where we itrate to do list
    if y['completed'] == True:
        countx += 1

# this is where we print the user thing

print ('Employee {} is done with tasks({}/{}):'.format(user['name'],
        countx, len(todo)))
for y in todo:
    if y['completed'] == True:
        print ('\t ', y['title'])
