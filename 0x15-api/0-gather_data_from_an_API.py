#!/usr/bin/python3
""" script that, using this REST API, for a given employee ID, returns information about his/her TODO list progress. """


import requests
import sys

if __name__ == "__main__":

# Base URL for the JSONPlaceholder API
g       url = f"https://jsonplaceholder.typicode.com/todos"

# Employee information
        employee_id = sys.argv[1]
        user = requests.get(url + "users/{}".format(employee_id)).json()

# The to-do list for the employee
        params = {"userld": employee_id}
        todos = requests.get(url + "todos", params).json()
# Compeleted tasks and count them
        completed = [task.get("title") for task in todos if task.get("completed") is True]

        print("Employee {} is done with tasks({}/{}):".format(user.get("name"), len(completed), len(todos)))
        [print("\t {}".format(complete)) for complete in completed]
