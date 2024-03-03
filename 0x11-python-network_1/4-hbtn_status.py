#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
"""
import requests

url = "https://alx-intranet.hbtn.io/status"
r = requests.get(url)

print("Body response:")
print(f"\t- type: {type(r.text)}\n\t- content: {r.text}")
