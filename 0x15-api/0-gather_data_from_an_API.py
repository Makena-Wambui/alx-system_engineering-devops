#!/usr/bin/python3

"""
Write a Python script that, using this REST API,
for a given employee ID, returns information about his/her TODO list progress.

You must use urllib or requests module
The script must accept an integer as a parameter, which is the employee ID
The script must display on the standard output the
employee TODO list progress in this exact format:
    First line: Employee EMPLOYEE_NAME is done with
        tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
    EMPLOYEE_NAME: name of the employee
    NUMBER_OF_DONE_TASKS: number of completed tasks
    TOTAL_NUMBER_OF_TASKS: total number of tasks,
        which is the sum of completed and non-completed tasks
    Second and N next lines display the title of completed tasks:
        TASK_TITLE (with 1 tabulation and 1 space before the TASK_TITLE)
"""

import sys
import requests

base_url = 'https://jsonplaceholder.typicode.com/'


def do_request():
    """
    Func: do_request

    This function performs request.
    """

    if len(sys.argv) < 2:
        return print('USAGE:', __file__, '<employee id>')
    eid = sys.argv[1]
    try:
        _eid = int(sys.argv[1])
    except ValueError:
        return print('Employee id must be an integer')

    response = requests.get(base_url + 'users/' + eid)
    if response.status_code == 404:
        return print('User id not found')
    elif response.status_code != 200:
        return print('Error: status_code:', response.status_code)
    user = response.json()

    response = requests.get(base_url + 'todos/')
    if response.status_code != 200:
        return print('Error: status_code:', response.status_code)
    todos = response.json()

    user_todos = [todo for todo in todos
                  if todo.get('userId') == user.get('id')]
    completed = [todo for todo in user_todos if todo.get('completed')]
    print('Employee', user.get('name'),
          'is done with tasks({}/{}):'.
          format(len(completed), len(user_todos)))
    [print('\t', todo.get('title')) for todo in completed]


if __name__ == '__main__':
    do_request()
