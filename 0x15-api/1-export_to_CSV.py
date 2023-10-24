#!/usr/bin/python3
"""Module that makes an API request and exports data to CSV"""


import csv
import json
import requests
import sys


if __name__ == "__main__":

    sessionReq = requests.Session()

    idEmp = sys.argv[1]
    idURL = f'https://jsonplaceholder.typicode.com/users/{idEmp}/todos'
    nameURL = f'https://jsonplaceholder.typicode.com/users/{idEmp}'

    employee = sessionReq.get(idURL)
    employeeName = sessionReq.get(nameURL)

    json_req = employee.json()
    usr = employeeName.json()['username']

    totalTasks = 0

    for done_tasks in json_req:
        if done_tasks['completed']:
            totalTasks += 1

    fileCSV = idEmp + '.csv'

    with open(fileCSV, "w", newline='') as csvfile:
        write = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
        for i in json_req:
            write.writerow([idEmp, usr, i.get('completed'), i.get('title')])
