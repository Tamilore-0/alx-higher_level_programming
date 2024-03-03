#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]

    payload = {"q": q}
    response = requests.post("http://0.0.0.0:5000/search_user", data=payload)

    try:
        json_data = response.json()
        if not json_data:
            print("No result")
        else:
            id = json_data['id']
            name = json_data['name']
            print(f"[{id}] {name}")
    except Exception as e:
        print("Not a valid JSON")
