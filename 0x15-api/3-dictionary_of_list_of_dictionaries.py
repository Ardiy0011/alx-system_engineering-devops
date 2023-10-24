#!/usr/bin/python3
"""Module that makes an API request and exports data in JSON format"""
import requests
import json

def export_employee_todo_to_json():
    api_url = f"https://jsonplaceholder.typicode.com/users"
    todos_url = f"https://jsonplaceholder.typicode.com/todos"


    """Make an API request to get user dat"""
    user_response = requests.get(api_url)
    user_data = user_response.json()

    """Make an API request to get all TODOs"""
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    json_filename = "todo_all_employees.json"
    all_user_tasks = {}

    for user in user_data:
        user_id = user["id"]
        employee_username = user["username"]
        user_tasks = []

        for todo in todos_data:
            if todo["userId"] == user_id:
                task_completed_status = todo["completed"]
                task_title = todo["title"]

                user_tasks.append({
                    "username": employee_username,
                    "task": task_title,
                    "completed": task_completed_status
                })

        all_user_tasks[user_id] = user_tasks

    with open(json_filename, mode='w') as json_file:
        json.dump(all_user_tasks, json_file, indent=4)

    print(f"Data exported to {json_filename}")


export_employee_todo_to_json()
