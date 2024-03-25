#!/usr/bin/python3
"""Python Script that gathers employee data from using RESTAPI"""
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
            emp_name = emp_resp.get("name")
            tsks = list(filter(lambda x: x.get("userId") == emp_id, tsk_resp))
            comp_tsks = list(filter(lambda x: x.get("completed"), tsks))
            print(
                    f"Employee {emp_name} is done with "
                    f"tasks({len(comp_tsks)}/{len(tsks)}):"
            )
            for comp_tsk in comp_tsks:
                print(f"\t {comp_tsk.get('title')}")
