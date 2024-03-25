#!/usr/bin/python3
"""Python Script that gathers employee data from using RESTAPI"""
from json import dump
from re import fullmatch
from requests import get
from sys import argv


RESTAPI_URL = "https://jsonplaceholder.typicode.com"
"""The RESTAPI's URL"""


if __name__ == "__main__":
    if len(argv) > 1:
        if fullmatch(r"\d+", argv[1]):
            emp_id = int(argv[1])
            emp_resp = get(f"{RESTAPI_URL}/users/{emp_id}").json()
            tsk_resp = get(f"{RESTAPI_URL}/todos").json()
            emp_name = emp_resp.get("username")
            tsks = list(filter(lambda x: x.get("userId") == emp_id, tsk_resp))
            with open(f"{emp_id}.json", "w") as fl:
                emp_data = list(
                        map(lambda x: {"task": x.get("title"),
                                       "completed": x.get("completed"),
                                       "username": emp_name}, tsks)
                )
                emps_data = {f"{emp_id}": emp_data}
                dump(emps_data, fl)
