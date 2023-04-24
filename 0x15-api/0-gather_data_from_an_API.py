#!/usr/bin/python3
import requests
import sys

"""
This script uses the requests module to get the employee's TODO list progress from a REST API.

Usage: python3 todo.py EMPLOYEE_ID
"""

def main():
    """
    Main function that gets the employee's TODO list progress from a REST API.
    """
    if len(sys.argv) != 2:
        print("Usage: {} EMPLOYEE_ID".format(sys.argv[0]))
        sys.exit(1)

    employee_id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(employee_id)
    response = requests.get(url)

    if response.status_code != 200:
        print("Error: Employee ID not found")
        sys.exit(1)

    todos = response.json()
    employee_name = todos[0]['name']
    total_tasks = len(todos)
    done_tasks = len([todo for todo in todos if todo.get('completed')])

    print("Employee {} is done with tasks({}/{}):".format(employee_name, done_tasks, total_tasks))

    for todo in todos:
        if todo.get('completed'):
            print("\t {}".format(todo['title']))

if __name__ == '__main__':
    main()
