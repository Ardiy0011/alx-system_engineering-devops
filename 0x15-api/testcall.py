#!/usr/bin/python3
"""module that makes an API request"""
import requests
import sys



def call_id():
    """make an API request to user and todo endpoints"""
    api_url = f"https://jsonplaceholder.typicode.com/users"
    tdurl = f"https://jsonplaceholder.typicode.com/todos"

    response = requests.get(api_url)
    data = response.json()
    print(f"first insance of data:{data}")
    """further filter by name"""
    print('==================================================================')
    print('==================================================================')
    for user in data:
        e_name = user['name']
        
        print(f"all names: {e_name}")

    todos_response = requests.get(tdurl)
    todos_data = todos_response.json()
    total = len(todos_data)
    """iterate through toda and increment by 1 if completed"""
    done = sum(1 for todo in todos_data if todo["completed"] is True)

    print(f'Employee {e_name} is done with tasks ({done}/{total}):')
    for todo in todos_data:
        if todo["completed"] is True:
            print(f"\t{todo['title']}")


call_id()
