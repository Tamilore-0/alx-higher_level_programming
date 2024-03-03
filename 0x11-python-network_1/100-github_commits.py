#!/usr/bin/python3
"""
Script that gets the last 10 commits of a specified user
"""
import requests
import sys

if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"
    response = requests.get(url)

    try:
        json_data = response.json()

        for i in range(10):
            commit_id = json_data[i].get('sha')
            committer = json_data[i].get('commit').get('author').get('name')
            print(f"{commit_id}: {committer}")
    except Exception as e:
        pass
