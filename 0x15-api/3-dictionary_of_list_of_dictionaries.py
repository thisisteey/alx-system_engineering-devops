#!/usr/bin/python3
"""Python Script that gathers employee data from using RESTAPI"""
from json import dump
from requests import get


RESTAPI_URL = "https://jsonplaceholder.typicode.com"
"""The RESTAPI's URL"""


if __name__ == "__main__":
    emp_resp = get(f"{RESTAPI_URL}/users").json()
    tsk_resp = get(f"{RESTAPI_URL}/todos").json()
    emps_data = {}
    for emp in emp_resp:
        emp_id = emp.get("id")
        emp_name = emp.get("username")
        tsks = list(filter(lambda x: x.get("userId") == emp_id, tsk_resp))
        emp_data = list(
                map(lambda x: {"username": emp_name,
                               "task": x.get("title"),
                               "completed": x.get("completed")}, tsks)
        )
        emps_data[f"{emp_id}"] = emp_data
    with open("todo_all_employees.json", "w") as fl:
        dump(emps_data, fl)
