#!/usr/bin/python3
"""Module that makes an API request and exports data to CSV"""
import requests
import csv
import sys

user_id = sys.argv[1]


def export_employee_todo_to_csv(user_id):
    api_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"

    """Make an API request to get user data"""
    user_response = requests.get(api_url)
    user_data = user_response.json()
    employee_name = user_data.get('username')

    """Make an API request to get user's TODOs"""
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    csv_filename = f"{user_id}.csv"

    """Open CSV file and write data"""
    with open(csv_filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)

        for todo in todos_data:
            if todo["completed"]:
                task_completed_status = "True"
            else:
                task_completed_status = "False"
            csv_writer.writerow([user_id,
                                 employee_name,
                                 task_completed_status,
                                 todo["title"]])


export_employee_todo_to_csv(user_id)
