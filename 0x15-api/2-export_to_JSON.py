#!/usr/bin/python3
"""Module that makes an API request and exports data in JSON format"""
import requests
import json
import sys

user_id = sys.argv[1]


def export_employee_todo_to_json(user_id):
    """export todo to json format"""
    api_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"

    """Make an API request to get user data"""
    user_response = requests.get(api_url)
    user_data = user_response.json()
    employee_name = user_data.get('username')

    """Make an API request to get user's TODOs"""
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    json_filename = f"{user_id}.json"
    user_tasks = []

    for todo in todos_data:
        task_completed_status = todo["completed"]
        task_title = todo["title"]

        user_tasks.append({
            "task": task_title,
            "completed": task_completed_status,
            "username": employee_name
        })

    with open(json_filename, mode='w') as json_file:
        json.dump({user_id: user_tasks}, json_file)


export_employee_todo_to_json(user_id)
