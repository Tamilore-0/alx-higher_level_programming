#!/usr/bin/python3
"""
Script that gets the last 10 commits of a specified user
"""
import requests
import sys

if __name__ == "__main__":
    repository_name = sys.argv[1]
    owner_name = sys.argv[2]

    url = f"https://api.github.com/repos/{owner_name}/{repository_name}/commits"
    response = requests.get(url)
    json_data = response.json()

    for(i = 0; i < 10; i++):
        if type(json_data[i]) is dict:
            commit_id = json_data[i]['sha']
            committer = json_data[i]['commit']['author']['name']
            print(f"{commit_id}: {committer}")
