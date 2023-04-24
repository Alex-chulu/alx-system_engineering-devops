#!/usr/bin/python3
import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        exit(1)

    employee_id = sys.argv[1]
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id)
    todo_url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(employee_id)

    user_response = requests.get(user_url)
    todo_response = requests.get(todo_url)

    try:
        user_dict = user_response
