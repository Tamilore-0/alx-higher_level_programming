#!/usr/bin/python3
"""
Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id
"""
import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    data = {"name": username}
    headers = {"Authorization": f"Bearer {password}"}
    url = "https://api.github.com/user"
    response = requests.get(url, data=data, headers=headers)

    try:
        json_data = response.json()
        print(f"{json_data.get('id', 'None')}")
    except Exception as e:
        print("JSON decoding failed")
