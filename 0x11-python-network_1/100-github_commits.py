#!/usr/bin/python3
"""
"""
import requests
import sys

if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]

    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    response = requests.get(url)
    json_data = response.json()
    i = 0

    while i < 10:
        commit_id = f"{json_data[i].get('sha', '')}"
        committer = f"{json_data[i]['commit']['author']['name']}"
        print(f"{commit_id}: {committer}")
        i = i + 1
